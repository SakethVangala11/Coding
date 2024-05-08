class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        answer = []
        for i in range(len(score)):
            answer.append(score[i])
        score.sort(reverse= True)
        d = {}
        for i in range(len(score)):
            if i == 0:
                d[score[i]] = "Gold Medal"
            elif i == 1:
                d[score[i]] = "Silver Medal"
            elif i == 2:
                d[score[i]] =  "Bronze Medal"
            else:
                d[score[i]] = str(i+1)
        
        for i in range(len(answer)):
            answer[i] = d[answer[i]]
        return answer

        



        