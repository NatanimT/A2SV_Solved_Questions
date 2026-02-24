class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        l,r= 0, len(skill) -1
        skill.sort()
        ans = []
        while l < r:
            if skill[l] + skill[r] == skill[l+1] + skill[r - 1]:
                ans.append(skill[l] * skill[r])
                l += 1
                r -= 1
            else:
                return -1   

        return sum(ans)
  