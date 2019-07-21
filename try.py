t = int(input())
for x in range(t):
    a, b = map(int, input().split())
    m = []
    print("--")
    for i in range(a):
        m.append(list(map(int, input().rstrip().split())))
#   maxN = max([max(j) for j in matrix])
    e = []
    for r in m:
        e.append(max(r))
    p = e.index(max(e))
    print(p)
    q = m[p].index(max(m[p]))
    print(q)
    # print(max(0,p-int(a/2)+q-int(b/2)))
    print(abs(p-int(a/2))+abs(q-int(b/2)))
