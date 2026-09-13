import json, os
from collections import defaultdict

OUT = '/Users/june/Documents/GitHub/research/output-format-bias/data_tables/unified_ai_coding_2026-05-13'
all_data = json.load(open(os.path.join(OUT, '_all_data.json')))
data = all_data['data']
variants = all_data['variants']

BINARY = [v for v in variants if v.startswith('binary')]
AXIS = [v for v in variants if v.startswith('4axis')]
GENOB = [v for v in variants if v.startswith('genob')]

# Build matrix
students = sorted(data[variants[0]].keys())

def verdict_of(rec, variant):
    if variant.startswith('binary'):
        return rec.get('verdict')
    if variant.startswith('4axis'):
        return rec.get('axis')
    if variant.startswith('genob'):
        return 'GENOB'  # always free text
    return None

# Print compact matrix
print('=== VERDICT MATRIX (binary + 4axis) ===')
header = f"{'SID':<5} | " + ' | '.join(f"{v[:18]:<18}" for v in BINARY+AXIS)
print(header)
for sid in students:
    row = [sid]
    for v in BINARY+AXIS:
        rec = data[v][sid]
        verd = verdict_of(rec, v)
        row.append(f"{(verd or '?')[:18]:<18}")
    print(row[0].ljust(5) + ' | ' + ' | '.join(row[1:]))
