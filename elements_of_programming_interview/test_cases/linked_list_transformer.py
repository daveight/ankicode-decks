import json
import os

for name in os.listdir('.'):
    file = open(name, 'r')
    lines = file.readlines()
    header = lines[0]
    header_items = header.split('\t')
    linked_list_idx = []
    for i, item in enumerate(header_items):
        if item.startswith('linked_list'):
            linked_list_idx.append(i)
    if len(linked_list_idx) > 0:
        result = open(name + '.new', 'w')
        result.write(header)
        for line in lines[1:]:
            split = line.split('\t')
            s = []
            for idx, element in enumerate(split):
                if idx in linked_list_idx and idx != len(split) - 1:
                    arr = json.loads(split[idx])
                    i = 1
                    linked_list_arr = []
                    for j, item in enumerate(arr):
                        linked_list_arr.append(item)
                        if j != len(arr) - 1:
                            linked_list_arr.append(i)
                        i += 1
                    s.append(json.dumps(linked_list_arr))
                else:
                    s.append(element)
            s = '\t'.join(s)
            if not s.endswith('\n'):
                s += '\n'
            result.write(s)
        result.close()

# result = open('./even_odd_list_merge_v1.tsv', 'w')
# lines = file.readlines()
# header_processed = False
# linked_list_idx = []
