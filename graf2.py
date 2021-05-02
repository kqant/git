def comp_sv():

    def dfs(v):
        used.append(v)
        for u in g[v]:
            if u not in used:
                dfs(u)

    n = 0
    for v in g:
        if v not in used:
            dfs(v)
            n += 1
    print(n)


V = int(input())  # Кол-во вершин
used = []
g = []
gtemp = {i: set() for i in range(V)}
for i in range(V):
    g.append(list(map(int, input().split())))
for i in range(V):
    for j in range(V):
        if g[i][j]:
            gtemp[i].add(j)
g = gtemp
comp_sv()
        
