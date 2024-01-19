class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)

        myhash = dict()
        need = 0
        for ch in t:
            if ch in myhash:
                myhash[ch][1] += 1
            else:
                myhash[ch] = [0, 1]
                need += 1

        have = 0
        l = 0
        result = [0, n+1]

        for i in range(n):
            if s[i] in myhash:
                array = myhash[s[i]]
                array[0] += 1
                if array[0] == array[1]:
                    have += 1

            if have == need:
                if i -l < result[1] - result[0]:
                    result = [l, i]

                while l <= i and have == need:
                    if i - l < result[1] - result[0]:
                        result = [l, i ]

                    if s[l] in myhash:
                        array = myhash[s[l]]
                        if array[1] == array[0]:
                            have -= 1
                        array[0] -= 1

                    l += 1

        if result[1] == n+1:
            return ""
        return s[result[0]: result[1]+1]
            