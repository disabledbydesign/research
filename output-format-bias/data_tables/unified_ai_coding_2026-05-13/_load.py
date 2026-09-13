import json, os
from collections import defaultdict

BASE = '/Users/june/Documents/GitHub/research/output-format-bias/data/raw_outputs'

FILES = {
    'binary-narrow-both':   'test_unified_binary_narrow_both_FULL_CORPUS_gemma12b_2026-05-13_0234.json',
    'binary-narrow-single': 'test_unified_binary_narrow_single_FULL_CORPUS_gemma12b_2026-05-13_0312.json',
    'binary-narrow-neither':'test_unified_binary_narrow_neither_FULL_CORPUS_gemma12b_2026-05-13_0349.json',
    'binary-broad-both':    'test_unified_binary_broad_both_FULL_CORPUS_gemma12b_2026-05-13_0424.json',
    'binary-broad-single':  'test_unified_binary_broad_single_FULL_CORPUS_gemma12b_2026-05-13_0458.json',
    'binary-broad-neither': 'test_unified_binary_broad_neither_FULL_CORPUS_gemma12b_2026-05-13_0532.json',
    '4axis-both':           'test_unified_4axis_both_FULL_CORPUS_gemma12b_2026-05-13_0604.json',
    '4axis-single':         'test_unified_4axis_single_FULL_CORPUS_gemma12b_2026-05-13_0636.json',
    '4axis-neither':        'test_unified_4axis_neither_FULL_CORPUS_gemma12b_2026-05-13_0707.json',
    'genob-both':           'test_unified_genob_both_FULL_CORPUS_gemma12b_2026-05-13_0739.json',
    'genob-single':         'test_unified_genob_single_FULL_CORPUS_gemma12b_2026-05-13_0822.json',
    'genob-neither':        'test_unified_genob_neither_FULL_CORPUS_gemma12b_2026-05-13_0905.json',
}

data = {}
for v, fn in FILES.items():
    d = json.load(open(os.path.join(BASE, fn)))
    rec = {r['student_id']: r for r in d['results'] if r.get('run')==1}
    data[v] = rec

OUT = '/Users/june/Documents/GitHub/research/output-format-bias/data_tables/unified_ai_coding_2026-05-13'
with open(os.path.join(OUT, '_all_data.json'),'w') as f:
    json.dump({'variants': list(FILES.keys()), 'data': data}, f)

print('Loaded variants:', len(data))
print('All student IDs:', sorted(data['binary-narrow-both'].keys()))
