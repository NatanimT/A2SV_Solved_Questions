class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        "9001 discuss.leetcode.com"
        count = defaultdict(int)
        for cp in cpdomains:
            num, domain = cp.split(" ")
            num = int(num)
            parts = domain.split(".")
            for i in range(len(parts)):
                count[".".join(parts[i:])] += num
        return [f"{cnt} {dom}" for dom, cnt in count.items()]

