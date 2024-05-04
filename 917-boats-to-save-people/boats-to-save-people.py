class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l, r = 0, len(people)-1

        no_of_boats = 0

        while l <= r:
            weight = people[r]
            r -= 1

            if l <= r:
                if people[r] + weight <= limit:
                    r -= 1
                elif people[l] + weight <= limit:
                    l += 1
            
            no_of_boats += 1

        return no_of_boats