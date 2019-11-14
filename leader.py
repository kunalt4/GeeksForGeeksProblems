test_cases = int(input())
for t in range(test_cases):
    n = int(input())
    arr = [int(i) for i in input().split()]
    maxList = []
    max_curr = arr[-1]
    arr.reverse()
    for m in arr:
        if m >= max_curr:
            max_curr = m
            maxList.append(max_curr)
    
    maxList.reverse()
    print(*maxList, sep=" ")