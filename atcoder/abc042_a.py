from collections import defaultdict
strings = raw_input().split()
cand = {
    '5': 2,
    '7': 1
}
source = defaultdict(int)
for i in range(len(strings)):
    if strings[i] == '5':
        if source[strings[i]]:
            source[strings[i]] += 1
        else:
            source[strings[i]] = 1
    elif strings[i] == '7':
        if source[strings[i]]:
            source[strings[i]] += 1
        else:
            source[strings[i]] = 1
if source == cand:
    print "YES"
else:
    print "NO"
