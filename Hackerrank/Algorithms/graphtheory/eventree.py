from collections import defaultdict
n, m = map(int, raw_input().split())

class Graph:
	def __init__(self, countnodes, countedges):
		self.graph = defaultdict(list)
		self.countnodes = countnodes
		self.countedges = countedges

	def add_edge(self, node1, node2):
		self.graph[node2].append(node1)

	def returnvalues(self, node):
		return self.graph[node]


graph = Graph(n, m)
for i in range(m):
	node1, node2 = map(int, raw_input().split())
	graph.add_edge(node1, node2)

childrennodescount = [1] * (n+1)
for i in range(n, 0, -1):
	temp = graph.returnvalues(i)
	childrennodescount[i] = len(temp) + 1

ans = 0
maxm = max(childrennodescount)
for i in childrennodescount:
	if i % 2 != 0 and i != 1 and i != maxm:
		ans += 1
print ans
