from collections import Counter
s1 = input()
s2 = input()
total = 0
good = 0
t = s1.count("+") - s1.count("-")
def backtrack(i, res):
    global total, good
    if i == len(s1):
        total += 1
        if res == t:
            good += 1  
        return
    if s2[i] == "+":
        backtrack(i +1, res + 1)
    elif s2[i] == "-":
        backtrack(i +1, res - 1)
    else:
        backtrack(i +1, res + 1)
        backtrack(i +1, res - 1)
backtrack(0,0)
print(good/total)