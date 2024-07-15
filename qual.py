l = eval(input())

ans = list(range(1, len(l) + 1))

for i in range(1, len(l) + 1):
    if i in l and i in ans:
        ans.pop(ans.index(i))
        
print(ans)