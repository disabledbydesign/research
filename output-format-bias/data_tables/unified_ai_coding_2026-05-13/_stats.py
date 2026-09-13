import json, os
from collections import Counter, defaultdict
OUT = '/Users/june/Documents/GitHub/research/output-format-bias/data_tables/unified_ai_coding_2026-05-13'
all_data = json.load(open(os.path.join(OUT, '_all_data.json')))
data = all_data['data']
variants = all_data['variants']

# Axis distribution across 4axis variants
print("=== 4-AXIS DISTRIBUTION ===")
for v in [x for x in variants if '4axis' in x]:
    c = Counter(data[v][s]['axis'] for s in data[v])
    print(f"{v}: {dict(c)}")

# Binary distribution
print("\n=== BINARY VERDICT COUNTS ===")
for v in [x for x in variants if 'binary' in x]:
    c = Counter(data[v][s]['verdict'] for s in data[v])
    print(f"{v}: {dict(c)}")

# Find self-contradictions: where reasoning text has 'CLEAR' or 'no indication'-type language but verdict==CONCERN, etc.
print("\n=== POTENTIAL SELF-CONTRADICTIONS IN BINARY ===")
contra_patterns = [
    ('CONCERN', ['no indication of present-tense', 'no indication of the student\'s own current', 'this aligns with the CLEAR']),
    ('CLEAR', ['warrants attention', 'this indicates a present-tense', 'current crisis', 'crisis-level']),
]
for v in [x for x in variants if 'binary' in x]:
    for sid, rec in data[v].items():
        verd = rec['verdict']
        reas = (rec.get('reasoning') or '').lower()
        sig = (rec.get('signal') or '').lower()
        text = reas + ' ' + sig
        for target_verd, patterns in contra_patterns:
            if verd == target_verd:
                for p in patterns:
                    if p.lower() in text:
                        print(f"{v} | {sid} | verdict={verd} | pattern='{p}' found in text")
                        break

# Where binary flips between supersedes states for same scope
print("\n=== SUPERSEDES FLIPS (binary-narrow) ===")
for sid in sorted(data['binary-narrow-both'].keys()):
    a = data['binary-narrow-both'][sid]['verdict']
    b = data['binary-narrow-single'][sid]['verdict']
    c = data['binary-narrow-neither'][sid]['verdict']
    if not (a == b == c):
        print(f"  {sid}: both={a} | single={b} | neither={c}")

print("\n=== SUPERSEDES FLIPS (binary-broad) ===")
for sid in sorted(data['binary-broad-both'].keys()):
    a = data['binary-broad-both'][sid]['verdict']
    b = data['binary-broad-single'][sid]['verdict']
    c = data['binary-broad-neither'][sid]['verdict']
    if not (a == b == c):
        print(f"  {sid}: both={a} | single={b} | neither={c}")

print("\n=== SUPERSEDES FLIPS (4axis) ===")
for sid in sorted(data['4axis-both'].keys()):
    a = data['4axis-both'][sid]['axis']
    b = data['4axis-single'][sid]['axis']
    c = data['4axis-neither'][sid]['axis']
    if not (a == b == c):
        print(f"  {sid}: both={a} | single={b} | neither={c}")

# Confidence distribution
print("\n=== CONFIDENCE DISTRIBUTION ===")
for v in variants:
    confs = [data[v][s].get('confidence', 0) for s in data[v]]
    print(f"{v}: min={min(confs)} max={max(confs)} avg={sum(confs)/len(confs):.3f} n_at_0.95={sum(1 for c in confs if c==0.95)}/{len(confs)}")

# Cross-format flip count: scope-narrow vs 4axis
print("\n=== BINARY-NARROW-BOTH vs 4AXIS-BOTH FLIPS ===")
for sid in sorted(data['binary-narrow-both'].keys()):
    bv = data['binary-narrow-both'][sid]['verdict']
    ax = data['4axis-both'][sid]['axis']
    # CONCERN -> non-CRISIS/BURNOUT or CLEAR -> CRISIS/BURNOUT is a flip
    bv_concern = (bv == 'CONCERN')
    ax_concern = ax in ('CRISIS', 'BURNOUT', 'DISENGAGED')
    if bv_concern != ax_concern:
        print(f"  {sid}: binary-narrow-both={bv} | 4axis-both={ax}")
