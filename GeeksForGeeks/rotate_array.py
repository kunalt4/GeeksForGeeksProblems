#code
test_cases = int(input())
for t in range(test_cases):
    n, d = [int(i) for i in input().split()]
    arr = [int(i) for i in input().split()]
    arr[:d] = arr[:d][::-1]
    arr[d:] = arr[d:][::-1]
    arr = arr[::-1]
    print(*arr, sep=" ")
