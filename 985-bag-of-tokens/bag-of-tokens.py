class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        n = len(tokens)
        tokens.sort()
        l,r = 0, n-1
        score = 0

        while l <=r:
            while l <= r and tokens[l] <= power:
                score += 1
                power -= tokens[l]
                l += 1
            
            if l+1< r and score > 0:
                score -= 1
                power += tokens[r]
                r-=1
            else:
                break 
        return score