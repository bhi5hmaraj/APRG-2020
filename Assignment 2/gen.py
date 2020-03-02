import random, collections, rbtree

MAX = 10**6

def generate(n):
	return [[random.randint(1, MAX)] if random.randint(1, 2) == 1 else sorted([random.randint(1, MAX), random.randint(1, MAX)]) for _ in range(n)]


def solveBrute(tc):
	ans = []
	ds = set()
	
	for test in tc:

		if len(test) == 1:
			ds.add(test[0])
		else:
			cnt = 0
			# print("ds ", ds)
			# for e in ds:
			# 	if(e >= test[0] and e <= test[1]) :
			# 		print(e, "in range")

			# 	cnt += 1 if (e >= test[0] and e <= test[1]) else 0

			ans.append(sum(map(lambda x : 1 if (x >= test[0] and x <= test[1]) else 0, ds)))
			# print("==")
			# ans.append(cnt)


	return ans


def solveTree(tc):
	ans = []
	tree = rbtree.RedBlackTree()
	for test in tc:

		if len(test) == 1:
			tree.insert(test[0])
		else:
			ans.append(tree.get_count_in_range(*test))

	return ans



def stresstest():

	RUNS = 100
	QUERIES = 10

	for _ in range(RUNS):

		testcases = generate(QUERIES)
		ansB = solveBrute(testcases)
		ansT = solveTree(testcases)

		if ansB != ansT:
			print("wrong at", testcases)
			print("Correct ", ansB)
			print("tree ", ansT)
			# print("Wrong at ", "%d \n %s" % (QUERIES, '\n'.join(map(lambda x : ' '.join(x), testcases))))
		else:
			print("Correct till now !")



# testcases = [[4], [2], [1, 7], [10], [10, 10], [3, 7], [9], [3], [2], [1, 5]]
# solveTree(testcases)

stresstest()

# g = generate(10**5)

# print('\n'.join(map(lambda a : ' '.join(map(str, a)), g)))
