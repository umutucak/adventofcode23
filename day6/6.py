from math import prod
f = [open("6.input", "r").read().split("\n")[i].split()[1:] for i in [0,1]]
# print(prod([e*2 if e%2==0 else (e*2)-1 for e in [sum([1 for j in range(1, (int(t)//2)+1) if j*(int(t)-j) > int(f[1][i])]) for i, t in enumerate(f[0])]]))
# print([])
# print(f)
# ts = [(int(t)-j)-j+1 for i, t in enumerate(f[0]) for j in range(1, (int(t)//2)+1) if j*(int(t)-j) > int(f[1][i])]
ts = []
for i, t in enumerate(f[0]):
    for j in range(1, (int(t)//2)+1):
        if j*(int(t)-j) > int(f[1][i]):
            ts.append((int(t)-j) - j + 1)
            break
print(ts)