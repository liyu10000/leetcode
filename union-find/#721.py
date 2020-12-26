# use dfs
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        def dfs(i, n, res):
            if visited[i]:
                return res
            visited[i] = 1
            # print(i, visited)
            for j in range(n):
                if not visited[j] and same[i][j]:
                    res.append(j)
                    dfs(j, n, res)
            return res
        
        amap = defaultdict(list)
        for account in accounts:
            name, emails = account[0], account[1:]
            amap[name].append(set(emails))
        merged = []
        for name, email_list in amap.items():
            # build connectivity map
            n = len(email_list)
            same = [[0 for j in range(n)] for i in range(n)]
            for i in range(n):
                for j in range(i+1, n):
                    if email_list[i].intersection(email_list[j]):
                        same[i][j] = 1
                        same[j][i] = 1
            # print(same)
            # dfs to find all unions
            visited = [0] * n
            for i in range(n):
                if not visited[i]:
                    emails = email_list[i]
                    res = dfs(i, n, [])
                    for j in res:
                        emails = emails.union(email_list[j])
                    emails = list(emails)
                    emails.sort()
                    merged.append([name] + emails)
        return merged