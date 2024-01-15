class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        mylist = [-1]*(10**5+1)

        for winner, losser in matches:
            if mylist[losser] == -1:
                mylist[losser] = 1
            else:
                mylist[losser] += 1

            if mylist[winner] == -1:
                mylist[winner] = 0
            
        answers = [[], []]
        for i in range(10**5+1):
            if mylist[i] == 0:
                answers[0].append(i)
            elif mylist[i] == 1:
                answers[1].append(i)


        return answers