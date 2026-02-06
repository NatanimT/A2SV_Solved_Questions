class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        
        c = defaultdict(list)
        for path in paths:
            path = path.split(" ")
            folder = path[0]
            for i in path[1:]:
                i = i.split(".txt")
                name = i[0]
                content = i[1]
                c[content].append((folder, name))
        ans = []
        for k, v in c.items():
            if len(v) > 1:
                temp = []
                for path, name in v:
                    temp.append(path+"/"+name+".txt")
                ans.append(temp)
        return ans
