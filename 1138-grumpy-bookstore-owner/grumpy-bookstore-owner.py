class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n = len(customers)

        satisfiedCustomers = 0
        maxTechniqueBenefit = 0

        techniqueOnInd = 0
        techniqueBenefit = 0

        for i in range(n):
            if grumpy[i] == 0:
                satisfiedCustomers += customers[i]
            else:
                if i >= techniqueOnInd + minutes:
                    maxTechniqueBenefit = max(maxTechniqueBenefit, techniqueBenefit)
                    
                    while i >= techniqueOnInd + minutes :
                        if grumpy[techniqueOnInd] == 1:
                            techniqueBenefit -= customers[techniqueOnInd]
                        techniqueOnInd += 1
                
                techniqueBenefit += customers[i]


        maxTechniqueBenefit = max(maxTechniqueBenefit, techniqueBenefit)
        return satisfiedCustomers + maxTechniqueBenefit
