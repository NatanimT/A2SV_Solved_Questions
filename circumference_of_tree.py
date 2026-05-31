n = int(input())
if n == 1:
    print(0)
    exit()
g = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    u, v = map(int, input().split())
    g[u].append(v)
    g[v].append(u)
def bfs(s):
    dist = [-1] * (n + 1)
    q = [s]
    dist[s] = 0
    i = 0
    while i < len(q):
        v = q[i]
        i += 1
        for to in g[v]:
            if dist[to] == -1:
                dist[to] = dist[v] + 1
                q.append(to)
    mx = 0
    node = s
    for i in range(1, n + 1):
        if dist[i] > mx:
            mx = dist[i]
            node = i
    return node, mx
u, _ = bfs(1)
v, d = bfs(u)
print(3 * d)
