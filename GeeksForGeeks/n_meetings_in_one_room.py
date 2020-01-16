#code
num = int(input())
for tests in range(num):
    size = int(input())
    index_array = list(range(1,size+1))
    start = [int(i) for i in input().split()]
    end = [int(i) for i in input().split()]
    index_array = [x for y, x in sorted(zip(end, index_array))]
    start = [x for y, x in sorted(zip(end, start))]
    end = sorted(end)
    print(index_array[0], end=" ")
    for i in range(1,len(index_array)):
        if(start[i]>=end[i-1]):
            print(index_array[i], end=" ")
        else:
            end[i] = end[i-1]
    print()