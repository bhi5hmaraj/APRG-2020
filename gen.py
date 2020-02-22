import random, collections 

MAX = 10**1

def generate(n):
	tc = []
	for _ in range(n):
		tc.append([random.randint(1, MAX)] if random.randint(1, 2) == 1 else sorted([random.randint(1, MAX), random.randint(1, MAX)]))

	return tc


def solve(tc):
	ans = []
	ds = collections.defaultdict(int)
	
	for test in tc:
		if len(test) == 1:
			ds[test[0]] += 1
		else:
			ans.append(sum(map(lambda pair: pair[1] if pair[0] >= test[0] and pair[0] <= test[1] else 0, ds.items())))

	return ans


testcases = generate(10)
print("testcases", testcases)
print("ans ", solve(testcases))


