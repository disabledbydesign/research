import json, os, sys
OUT = '/Users/june/Documents/GitHub/research/output-format-bias/data_tables/unified_ai_coding_2026-05-13'
all_data = json.load(open(os.path.join(OUT, '_all_data.json')))
data = all_data['data']
variants = all_data['variants']

def show(sid, variant_filter=None):
    print(f"\n========== {sid} ==========")
    for v in variants:
        if variant_filter and not any(f in v for f in variant_filter):
            continue
        r = data[v][sid]
        verdict = r.get('verdict') or r.get('axis') or 'GENOB'
        conf = r.get('confidence')
        sig = (r.get('signal') or '').strip()
        reas = (r.get('reasoning') or '').strip()
        obs = (r.get('observation') or '').strip()
        print(f"--- {v} | verdict={verdict} | conf={conf}")
        if sig: print(f"  signal: {sig}")
        if reas: print(f"  reasoning: {reas}")
        if obs: print(f"  observation: {obs}")

if __name__ == '__main__':
    sids = sys.argv[1:] if len(sys.argv) > 1 else []
    for s in sids:
        show(s)
