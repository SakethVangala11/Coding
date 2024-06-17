class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        Eid = logs[0][0]
        time = logs[0][1]
        for i in range(1, len(logs)):
            diff = logs[i][1] - logs[i-1][1]
            if diff>time:
                Eid = logs[i][0]
                time = diff
            elif diff == time:
                Eid = min(Eid, logs[i][0])
        return Eid

        