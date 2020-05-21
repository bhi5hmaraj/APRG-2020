n, d, r = map(int, input().split())
mor = list(map(int, input().split()))
noon = list(map(int, input().split()))
mor.sort()
noon.sort(reverse = True)
ans =0
for i in range(n):
    if mor[i] + noon[i] > d:
        ans += (mor[i] + noon[i] - d)*r
print(ans)