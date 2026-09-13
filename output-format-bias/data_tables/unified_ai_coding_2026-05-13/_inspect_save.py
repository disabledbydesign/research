import json, os, sys
OUT = '/Users/june/Documents/GitHub/research/output-format-bias/data_tables/unified_ai_coding_2026-05-13'
all_data = json.load(open(os.path.join(OUT, '_all_data.json')))
data = all_data['data']
variants = all_data['variants']

def render(sid):
    lines = [f"\n========== {sid} =========="]
    for v in variants:
        r = data[v][sid]
        verdict = r.get('verdict') or r.get('axis') or 'GENOB'
        conf = r.get('confidence')
        sig = (r.get('signal') or '').strip()
        reas = (r.get('reasoning') or '').strip()
        obs = (r.get('observation') or '').strip()
        lines.append(f"--- {v} | verdict={verdict} | conf={conf}")
        if sig: lines.append(f"  signal: {sig}")
        if reas: lines.append(f"  reasoning: {reas}")
        if obs: lines.append(f"  observation: {obs}")
    return "\n".join(lines)

target = sys.argv[1]  # output filename
sids = sys.argv[2:]
with open(os.path.join(OUT, target), 'w') as f:
    for s in sids:
        f.write(render(s))
        f.write("\n")
print(f"Wrote {target} with {len(sids)} students")
