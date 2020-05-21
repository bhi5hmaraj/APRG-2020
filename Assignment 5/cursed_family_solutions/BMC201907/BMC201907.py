num_fam = int(input())
inp = []
for i in range(num_fam - 1):
    inp.append(list(map(int, input().split())))

    
adj_list = [[] for i in range(num_fam)]
for i in range(len(inp)):
    adj_list[inp[i][0] - 1].append(inp[i][1])

grandchildren = [[] for i in range(num_fam)]
for i in range(num_fam):
    for j in adj_list[i]:
        grandchildren[i].extend(adj_list[j - 1])

dp_dict = {}

def find_max(i):
    if i in dp_dict.keys():
        return(dp_dict[i])
    elif (adj_list[i - 1] == []):
        dp_dict[i] = 1
        return(1)
    else:
        dp_dict[i] = max(sum(map(find_max, adj_list[i - 1])), 1 + sum(map(find_max, grandchildren[i - 1])))
        return(dp_dict[i])

root_list = [0 for i in range(num_fam)]
for i in range(num_fam):
    for j in adj_list[i]:
        root_list[j - 1] = 1
root = root_list.index(0) + 1
find_max(root)
    
print(max(dp_dict.values()))