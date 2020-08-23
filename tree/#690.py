class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        ep_map = {ep.id:ep for ep in employees}
        stack = [id]
        res = 0
        while stack:
            id = stack.pop()
            res += ep_map[id].importance
            for subid in ep_map[id].subordinates:
                stack.append(subid)
        return res