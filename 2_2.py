n = 0
graph = {}
print("Введите через пробел номер вершины, откуда идёт ребро, и номер вершины, в которую оно приходит\nЧтобы завершить, введите -1")
while True:
    arr = list(map(int, input("Ввод: ").split()))
    if arr == [-1]:
        break
    if arr[0] not in graph.keys():
        graph[arr[0]] = [arr[1]]
    else:
        graph[arr[0]].append(arr[1])

    n = max(n, arr[0], arr[1])

n1, n2 = list(map(int, input("Введите начальную и конечную вершину через пробел: ").split()))

def bfs(graph, k, rast, bef):
    for i in graph[k]:
        if i not in bef:
            if rast[i] != 0:
                rast[i] = min(rast[i], rast[k] + 1)
                continue
            else:
                rast[i] = rast[k] + 1
            bef.append(i)
            bfs(graph, i, rast, bef)
    bef.pop()
    return rast
    
rast = [0 for i in range(n + 1)]

ans = bfs(graph, n1, rast, [n1])
print("Расстояние от вершины " + str(n1) + " до вершины " + str(n2) + " равно: " + str(ans[n2]))