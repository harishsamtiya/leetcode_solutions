class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        n = len(words)
    
        def form_array(word):
            array = [0]*26
            for ch in word:
                ind = ord(ch) - ord('a')
                array[ind]  += 1
            return array

        def same_array(arr1, arr2):
            for i in range(26):
                if arr1[i] != arr2[i]:
                    return False
            return True


        result = []
        prev_word_array = form_array(words[-1])
        prev_word = words[-1]
        for i in range(n-2, -1, -1):
            curr_array = form_array(words[i])

            if not same_array(prev_word_array, curr_array):
                result.append(prev_word)
                prev_word_array = curr_array
            prev_word = words[i]

        result.append(words[0])
        return result[::-1]
                