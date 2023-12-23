class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        myhash = dict()
        result = []
        ind = 0
        for st in strs:
            l = []
            for ch in st:
                l.append(ch)
            l.sort()
            s = ''.join(l)

            if s in myhash:
                result[myhash[s]].append(st)
            else:
                myhash[s] = ind
                ind += 1
                result.append([st])

        return result