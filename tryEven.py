t = int(input())
for x in range(t):
    a, b = map(int, input().split())
    m = []
    # print("--")

    for i in range(a):
        m.append(list(map(int, input().rstrip().split())))
#   maxN = max([max(j) for j in matrix])
    e = []
    for r in m:
        e.append(max(r))
    p = e.index(max(e))
    #print(p)
    q = m[p].index(max(m[p]))
    #print(q)
    u=p-int(a/2)
    v=q-int(b/2)

    # print(max(0,p-int(a/2)+q-int(b/2)))
    if a%2==0:
        if u<0:
         x=max(u,u+1)
        else:
         x=min(u,u+1)
    else:
        x=u
    x=abs(x)
    if b%2==0:
        if v<0:
         y=max(v,v+1)
        else:
         y=min(v,v+1)
    else:
        y=v
    y=abs(y)
    print(x+y)
    
