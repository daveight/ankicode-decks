import json

f = open('do_terminated_lists_overlap.tsv', 'r')
f2 = open('do_terminated_lists_overlap.tsv.new', 'w')
lines = f.readlines()
f2.write(lines[0])
for line in lines[1:]:
    split = line.split('\t')
    list0 = json.loads(split[0])
    list1 = json.loads(split[1])
    result = json.loads(split[2])
    list0 = list0 + result
    list1 = list1 + result

    s = json.dumps(list0) + '\t' + json.dumps(list1) + '\t' + json.dumps(result) + '\n'
    f2.write(s)


