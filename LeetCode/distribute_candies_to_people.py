class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        result = [0] * num_people
        i = 0
        j = 0
        while candies > 0:
            if j == num_people:
                j = 0
            result[j] += min(candies, i+1)
            candies = candies - i - 1
            j+=1
            i+=1
        return result
