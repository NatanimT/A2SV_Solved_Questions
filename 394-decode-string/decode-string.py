class Solution:
    def decodeString(self, s: str) -> str:
        stacknum = []
        stack = []
        ans = []
        num = 0

        for i in s:
            if i.isdigit():
                num = num * 10 + int(i)
                continue

            if i == '[':
                stacknum.append(num)
                num = 0

            elif i == ']':
                c = ""
                while stack and stack[-1] != "[":
                    c = stack.pop() + c

                stack.pop()
                n = stacknum.pop()
                stack.append(c * n)
                continue

            stack.append(i)

        for i in stack:
            ans.append(i)

        return "".join(ans)
