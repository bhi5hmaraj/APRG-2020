from collections import defaultdict


alphabet = [chr(65 + i) for i in range(26)] 
adj = tempMarked = globalMarked = inDegree = source = None

def checkDAG():
	global tempMarked, globalMarked
	tempMarked = set()
	globalMarked = set()
	for ch in alphabet:
		if ch not in globalMarked and dfs(ch):
			return False

	return True

def dfs(ch):
	global tempMarked, globalMarked

	tempMarked.add(ch)
	for v in adj[ch]:
		if v not in globalMarked:
			if v in tempMarked or dfs(v):
				return True
	# tempMarked.remove(ch)
	globalMarked.add(ch)

	return False

def topoSort(buffer):
	global source, inDegree

	if len(source) == 0:
		return [' '.join(buffer)]
	else:
		ret = []
		for ch in alphabet:
			if ch in source:
				source.remove(ch)
				for v in adj[ch]:
					inDegree[v] -= 1
					if inDegree[v] == 0:
						source.add(v)

				buffer.append(ch)
				ret += topoSort(buffer)

				buffer.pop()
				source.add(ch)
				for v in adj[ch]:
					if inDegree[v] == 0:
						source.remove(v)
					inDegree[v] += 1

		return ret

def solve(line1, line2):
	vertices = line1.split()
	edges = map(lambda x : x.split('<'), line2.split())

	global adj, inDegree, source

	adj = defaultdict(list)
	inDegree = defaultdict(int)
	source = set()

	for e in edges:
		adj[e[0]].append(e[1])
		inDegree[e[1]] += 1


	if not checkDAG():
		return ["NO"]
	else:
		for ch in alphabet:
			if ch in vertices and inDegree[ch] == 0:
				source.add(ch)

		return topoSort([])




def uva_solver():
	n = int(input())
	for _ in range(n):
		input()
		solve(input(), input())
		print()



TOTAL = 60
for i in range(TOTAL):
	fin = open('./input/input%02d.txt' % i, 'r')
	lines = fin.readlines()
	fout = open('./output/output%02d.txt' % i, 'w')
	print('\n'.join(solve(lines[0], lines[1])), file=fout)
	fout.close()

