class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        n = len(energy)
        maxEnergy = energy[-1]

        for i in range(0, k):
            energyGain = 0
            for j in range(i, n, k):
                if energyGain < 0:
                    energyGain = energy[j]
                else:
                    energyGain += energy[j]
            maxEnergy = max(maxEnergy, energyGain)
        return maxEnergy