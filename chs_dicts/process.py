from cqkm import cqkm
import re

with open('chs_dicts/base.dict.yaml.orig', 'r', encoding='utf-8-sig') as rf:
    with open('chs_dicts/base.dict.yaml', 'w', encoding='utf-8') as wf:
        header = False
        for l in rf.readlines():
            if l == '---\n':
                header = True
            if l == '...\n':
                header = False
                wf.write(l)
                continue
            if header or l.startswith('#'):
                wf.write(l)
                continue
            l = l.rstrip('\n')
            kanji, codes, weight = l.split('\t')
            codes = codes.split(' ')
            if '|' in codes[len(codes)-1]:
                codes[len(codes)-1] = re.sub(r'\|.*', '', codes[len(codes)-1])
            if kanji[len(kanji)-1] in cqkm.keys():
                codes[len(codes)-1] += '|' + cqkm[kanji[len(kanji)-1]][0]
            if kanji[0] in cqkm.keys():
                codes[0] += '|' + cqkm[kanji[0]][0]
            wf.write(kanji + '\t' + ' '.join(codes) + '\t' + weight + '\n')
