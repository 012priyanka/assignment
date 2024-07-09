def longest_path(graph: list) -> int:
  topo_order = topological_sort(graph)
  if not topo_order:  
    raise ValueError("Graph contains a cycle!")
  return calculate_longest_path(graph, topo_order)


def topological_sort(graph):

  n = len(graph)
  in_degree = {i: 0 for i in range(n)}
  for i in range(len(graph)):
    for neighbor, _ in graph[i]:
      in_degree[neighbor] += 1

  queue = [i for i in range(n) if in_degree[i] == 0]
  topological_order = []
  while queue:
    u = queue.pop(0)
    topological_order.append(u)
    for neighbor, _ in graph[u]:
      in_degree[neighbor] -= 1
      if in_degree[neighbor] == 0:
        queue.append(neighbor)

  if len(topological_order) != len(graph):
    return []  

  return topological_order


def calculate_longest_path(graph, topo_order):
  n = len(graph)
  dist = [-float('inf')] * n
  for node in topo_order:
    if dist[node] == -float('inf'):
      dist[node] = 0
    for neighbor, weight in graph[node]:
      if dist[neighbor] < dist[node] + weight:
        dist[neighbor] = dist[node] + weight
  return max(dist)
