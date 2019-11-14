test_cases = int(input())
for t in range(test_cases):
    n = int(input())
    arr = [int(i) for i in input().split()]
    num_dict = {}
    majorityElement = ""
    for num in arr:
        if num in num_dict:
            num_dict[num] = num_dict[num] + 1
        else:
            num_dict[num] = 1
    for k,v in num_dict.items():
        if v > n/2:
            majorityElement = k
    if(not majorityElement == ""):
        print(majorityElement)
    else:
        print("-1")