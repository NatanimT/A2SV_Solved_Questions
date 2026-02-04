class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        star = "*"
        forward_slash = "/"
        res = []
        in_block = False
        cur = ""
        for i in source:
            j = 0
            while j < len(i):
                if j + 1 < len(i) and i[j] == forward_slash and i[j + 1] == star and not in_block:
                    in_block = True
                    j += 2
                    continue
                if j + 1 < len(i) and i[j] == star and i[j + 1] == forward_slash and in_block:
                    in_block = False
                    j += 2
                    continue
                elif j + 1 < len(i) and i[j] == forward_slash and i[j + 1] == forward_slash and not in_block:

                    break
                if not in_block:
                    cur += i[j]
                j += 1
            if cur and not in_block:
                res.append(cur)
                cur = ""
        return res               