test_cases = int(input())
for t in range(test_cases):
    n = int(input())
    arr = [int(i) for i in input().split()]
    num_dict = {}
    for num in arr:
        if num in num_dict:
            num_dict[num] = num_dict[num] + 1
        else:
            num_dict[num] = 1
    sortedList = []

    for i in range(3):
        if i in num_dict:
            valList = [i] * num_dict[i]
            sortedList.extend(valList)


    print(*sortedList, sep=" ")