alpha_values = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}
o = 0
for w in open("1.input", "r"):
    idxs_front = {}
    idxs_back = {}
    # find word number indices front
    for key in alpha_values:
        i = w.find(key)
        if i >= 0:
            idxs_front[i] = key
    # find word number indices back
    for key in alpha_values:
        i = w.rfind(key)
        if i >= 0:
            idxs_back[i] = key
    # first digit
    for c in range(len(w)):
        if w[c].isnumeric():
            idxs_front[c] = w[c]
            break
    # last digit
    rev = w[::-1]
    for c in range(len(rev)):
        if rev[c].isnumeric():
            idxs_back[len(w)-c-1] = rev[c]
            break
    # fetch first
    first:str = idxs_front[min(list(idxs_front.keys()))]
    if not first.isnumeric():
        first = alpha_values[first]
    # fetch last
    last:str = idxs_back[max(list(idxs_back.keys()))]
    if not last.isnumeric():
        last = alpha_values[last]
    # concat
    o += int(first + last)
print(o)
