from collections import deque

def bfs(graph, start):
    visited = set()  # 用于记录已经访问过的节点
    queue = deque([start])  # 使用队列保存待访问的节点

    while queue:
        node = queue.popleft()  # 从队列中取出一个节点
        print(node)  # 可根据需要进行处理，这里只是简单地打印节点值

        if node not in visited:
            visited.add(node)  # 将节点标记为已访问

            # 将当前节点的未访问邻居节点加入队列
            queue.extend(neighbor for neighbor in graph[node] if neighbor not in visited)

# 示例用法
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

print("广度优先搜索结果:")
bfs(graph, 'A')
