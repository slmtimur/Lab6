n = 0
graph = {}
print("Введите номер вершины неориентированного графа и номера её соседей через пробел\nЧтобы завершить, введите -1")
while True:
    arr = list(map(int, input("Ввод: ").split()))
    if arr == [-1]:
        break
    if arr[0] not in graph.keys():
        graph[arr[0]] = arr[1:]
    else:
        graph[arr[0]] += arr[1:]

    for i in arr[1:]:
        if i not in graph.keys():
            graph[i] = [arr[0]]
        else:
            graph[i].append(arr[0])
    n = max(n, *arr)

def dfs(k, p):
    colors[k] = 1
    for i in graph[k]:
        if i in p and p[-1] != i:
            print("В графе есть цикл!")
            quit()
        if i not in p:
            p.append(k)
            dfs(i, p)
    if p != []:
        p.pop()
    colors[k] = 2

colors = [0 for i in range(n + 1)]

for i in range(1, n + 1):
    if colors[i] == 0:
        dfs(i, [])
print("В графе нет цикла!")