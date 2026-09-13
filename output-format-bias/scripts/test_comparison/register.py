"""Safe registry editor for scripts/test_comparison/registry.json.

Avoids hand-editing JSON (and the syntax errors that come with it). All edits
read-validate-write so the registry never ends up in a broken state.

Commands:
    list                       — print all configs / comparisons / observations
    add-file <config> <path>   — append a new run JSON to an existing config's files list
    add-config                 — add a new test config (binary_concern / 4axis / manual_codes)
    add-observation            — add a gen-ob observation entry
    add-comparison             — add a new comparison
    rename-config <old> <new>  — rename a config (and emit a one-time localStorage migration snippet)
    validate                   — load registry, run sanity checks

Run:
    python -m scripts.test_comparison.register <command> [args]
"""
import argparse
import json
import sys
from pathlib import Path

REGISTRY_PATH = Path(__file__).parent / "registry.json"


def _load() -> dict:
    if not REGISTRY_PATH.exists():
        return {"test_configs": [], "genob_observations": [], "comparisons": []}
    with open(REGISTRY_PATH) as fh:
        return json.load(fh)


def _save(reg: dict) -> None:
    # validate before writing
    validate(reg, raise_on_error=True)
    with open(REGISTRY_PATH, "w") as fh:
        json.dump(reg, fh, indent=2)
        fh.write("\n")
    print(f"Wrote {REGISTRY_PATH}")


def validate(reg: dict, raise_on_error: bool = False) -> list:
    """Sanity-check the registry. Returns list of error strings."""
    errors = []
    config_ids = set()
    for c in reg.get("test_configs", []):
        cid = c.get("id")
        if not cid:
            errors.append("test_configs entry missing 'id'")
            continue
        if cid in config_ids:
            errors.append(f"duplicate config id: {cid!r}")
        config_ids.add(cid)
        if c.get("schema") not in ("binary_concern", "4axis", "observation", "manual_codes", "unified"):
            errors.append(f"config {cid!r}: schema {c.get('schema')!r} not recognized")
        files = c.get("files") or []
        if not files:
            errors.append(f"config {cid!r}: empty files list")
        for f in files:
            # Path is relative to repo root (output-format-bias/)
            full = Path(__file__).parent.parent.parent / f
            if not full.exists():
                errors.append(f"config {cid!r}: file does not exist: {f}")

    obs_ids = set()
    for o in reg.get("genob_observations", []):
        oid = o.get("id")
        if not oid:
            errors.append("genob_observations entry missing 'id'")
            continue
        if oid in obs_ids:
            errors.append(f"duplicate observation id: {oid!r}")
        obs_ids.add(oid)
        for f in o.get("files", []):
            full = Path(__file__).parent.parent.parent / f
            if not full.exists():
                errors.append(f"observation {oid!r}: file does not exist: {f}")

    comp_ids = set()
    for c in reg.get("comparisons", []):
        cid = c.get("id")
        if not cid:
            errors.append("comparisons entry missing 'id'")
            continue
        if cid in comp_ids:
            errors.append(f"duplicate comparison id: {cid!r}")
        comp_ids.add(cid)
        for cf_id in c.get("configs", []):
            if cf_id not in config_ids:
                errors.append(f"comparison {cid!r}: references unknown config {cf_id!r}")
        if not c.get("output"):
            errors.append(f"comparison {cid!r}: missing output path")

    if raise_on_error and errors:
        raise ValueError("Registry validation failed:\n  - " + "\n  - ".join(errors))
    return errors


def cmd_list(args):
    reg = _load()
    print("test_configs:")
    for c in reg.get("test_configs", []):
        n_files = len(c.get("files", []))
        print(f"  - {c['id']:<55} [{c.get('schema')}] {n_files} file(s)")
    print("\ngenob_observations:")
    for o in reg.get("genob_observations", []):
        print(f"  - {o['id']:<55} {len(o.get('files', []))} file(s)")
    print("\ncomparisons:")
    for c in reg.get("comparisons", []):
        print(f"  - {c['id']:<55} configs={c.get('configs')}")
        print(f"    output: {c.get('output')}")


def cmd_add_file(args):
    reg = _load()
    for c in reg.get("test_configs", []):
        if c["id"] == args.config:
            if args.file in c["files"]:
                print(f"File already registered to {args.config!r}: {args.file}")
                return
            c["files"].append(args.file)
            _save(reg)
            print(f"Appended {args.file} to {args.config!r} (now {len(c['files'])} files)")
            return
    print(f"ERROR: no test_config with id {args.config!r}", file=sys.stderr)
    sys.exit(1)


def cmd_add_config(args):
    reg = _load()
    if any(c["id"] == args.id for c in reg.get("test_configs", [])):
        print(f"ERROR: config id {args.id!r} already exists", file=sys.stderr)
        sys.exit(1)
    new = {
        "id": args.id,
        "label": args.label or args.id,
        "schema": args.schema,
        "files": list(args.files),
    }
    reg.setdefault("test_configs", []).append(new)
    _save(reg)


def cmd_add_observation(args):
    reg = _load()
    if any(o["id"] == args.id for o in reg.get("genob_observations", [])):
        print(f"ERROR: observation id {args.id!r} already exists", file=sys.stderr)
        sys.exit(1)
    new = {"id": args.id, "label": args.label or args.id, "files": list(args.files)}
    reg.setdefault("genob_observations", []).append(new)
    _save(reg)


def cmd_add_comparison(args):
    reg = _load()
    if any(c["id"] == args.id for c in reg.get("comparisons", [])):
        print(f"ERROR: comparison id {args.id!r} already exists", file=sys.stderr)
        sys.exit(1)
    new = {
        "id": args.id,
        "label": args.label or args.id,
        "configs": list(args.configs),
        "output": args.output,
        "flag_threshold": args.flag_threshold,
    }
    reg.setdefault("comparisons", []).append(new)
    _save(reg)


def cmd_rename_config(args):
    reg = _load()
    found = False
    for c in reg.get("test_configs", []):
        if c["id"] == args.old:
            c["id"] = args.new
            found = True
            break
    if not found:
        print(f"ERROR: no config with id {args.old!r}", file=sys.stderr)
        sys.exit(1)
    # update comparison references
    for cmp in reg.get("comparisons", []):
        cmp["configs"] = [args.new if x == args.old else x for x in cmp.get("configs", [])]
    _save(reg)
    print(f"\n--- LocalStorage migration snippet ---")
    print(f"Paste this into your browser's dev console while viewing the comparison HTML:")
    print(f"""
(function () {{
  var oldId = {args.old!r}, newId = {args.new!r}, migrated = 0;
  for (var i = 0; i < localStorage.length; i++) {{
    var k = localStorage.key(i);
    if (k && k.indexOf("::" + oldId + "::") !== -1) {{
      var nk = k.replace("::" + oldId + "::", "::" + newId + "::");
      localStorage.setItem(nk, localStorage.getItem(k));
      localStorage.removeItem(k);
      migrated++;
    }}
  }}
  console.log("Migrated " + migrated + " note(s) from " + oldId + " to " + newId);
}})();
""")


def cmd_relabel_config(args):
    reg = _load()
    for c in reg.get("test_configs", []):
        if c["id"] == args.id:
            if args.display_label is not None:
                if args.display_label == "":
                    c.pop("display_label", None)
                else:
                    c["display_label"] = args.display_label
            if args.label is not None:
                c["label"] = args.label
            _save(reg)
            print(f"Updated {args.id}: display_label={c.get('display_label')!r}, label={c.get('label')!r}")
            return
    print(f"ERROR: no config with id {args.id!r}", file=sys.stderr)
    sys.exit(1)


def cmd_validate(args):
    reg = _load()
    errors = validate(reg, raise_on_error=False)
    if not errors:
        print("Registry is valid.")
        return
    print("Errors:")
    for e in errors:
        print(f"  - {e}")
    sys.exit(1)


def main(argv=None):
    p = argparse.ArgumentParser(description="Safe registry editor for test_comparison.")
    sub = p.add_subparsers(dest="cmd", required=True)

    sub.add_parser("list").set_defaults(func=cmd_list)
    sub.add_parser("validate").set_defaults(func=cmd_validate)

    af = sub.add_parser("add-file", help="append a JSON file to an existing config")
    af.add_argument("config")
    af.add_argument("file")
    af.set_defaults(func=cmd_add_file)

    ac = sub.add_parser("add-config")
    ac.add_argument("--id", required=True)
    ac.add_argument("--label")
    ac.add_argument("--schema", required=True, choices=["binary_concern", "4axis", "manual_codes"])
    ac.add_argument("--files", nargs="+", required=True)
    ac.set_defaults(func=cmd_add_config)

    ao = sub.add_parser("add-observation")
    ao.add_argument("--id", required=True)
    ao.add_argument("--label")
    ao.add_argument("--files", nargs="+", required=True)
    ao.set_defaults(func=cmd_add_observation)

    acmp = sub.add_parser("add-comparison")
    acmp.add_argument("--id", required=True)
    acmp.add_argument("--label")
    acmp.add_argument("--configs", nargs="+", required=True)
    acmp.add_argument("--output", required=True)
    acmp.add_argument("--flag-threshold", dest="flag_threshold", type=float, default=0.5)
    acmp.set_defaults(func=cmd_add_comparison)

    rc = sub.add_parser("rename-config")
    rc.add_argument("old")
    rc.add_argument("new")
    rc.set_defaults(func=cmd_rename_config)

    rl = sub.add_parser("relabel-config", help="set the display_label (short) or label (full) for a test config")
    rl.add_argument("id")
    rl.add_argument("--display-label", help="short label shown in column header / toggle buttons")
    rl.add_argument("--label", help="full label shown in tooltips")
    rl.set_defaults(func=cmd_relabel_config)

    args = p.parse_args(argv)
    args.func(args)


if __name__ == "__main__":
    main()
