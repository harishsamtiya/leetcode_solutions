class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        
        def count_even_odd(num):
            even = num//2
            odd = num - even
            return (even, odd)
        
        f_even, f_odd = count_even_odd(n)
        s_even, s_odd = count_even_odd(m)

        return f_even*s_odd + f_odd*s_even
        