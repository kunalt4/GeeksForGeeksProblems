test_cases = int(input())
for t in range(test_cases):
    n, sumArr = input().split()
    n = int(n)
    sumArr = int(sumArr)

    arr = [int(i) for i in input().split()]
    start = 0
    end = 1
    while(sum(arr[start:end])!=sumArr) & (end <= n):
        if(sum(arr[start:end])>sumArr):
            start = start + 1
        else:
            end = end + 1
    if(sum(arr[start:end])==sumArr):
        print(str(start+1)+" "+str(end))    
    else:
        print(-1)