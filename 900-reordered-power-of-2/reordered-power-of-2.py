class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        temp_n = n

        def count_digits(temp_n):
            no_of_digits = 0
            array = [0]*10
            while temp_n > 0:
                no_of_digits += 1
                digit = temp_n%10
                temp_n //= 10
                array[digit] += 1
            return no_of_digits, '.'.join(map(str, array))
        
        target_digit_count, target_str = count_digits(n)
        
        temp = 1

        while True:
            count, st = count_digits(temp)
            temp <<= 1
            if target_digit_count < count:
                break
            elif target_digit_count == count:
                if st == target_str:
                    return True
            else:
                continue
            
        
        return False