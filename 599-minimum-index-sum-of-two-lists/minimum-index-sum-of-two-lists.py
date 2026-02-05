class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        min_sum = float('inf')
        ans = []
    
        for i in range(len(list1)):
            for j in range(len(list2)):
                if list1[i] == list2[j]:
                    s = i + j 
                    if s < min_sum:
                        min_sum = s
                        ans = [list1[i]]
                    elif s == min_sum:
                        ans.append(list1[i])           
        return ans
