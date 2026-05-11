class Solution(object):
    def reverse(self, x):
        int_min,int_max = -2**31, 2**31 - 1
        
        sign = -1 if x < 0 else 1
        x = abs(x)
        
        reversed_x = int(str(x)[::-1])
        result = sign * reversed_x
        
        if result < int_min or result > int_max:
            return 0
        return result
       

















        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        
        sign = -1 if x < 0 else 1
        x = abs(x)
        
        reversed_x = int(str(x)[::-1])
        result = sign * reversed_x
        
        if result < INT_MIN or result > INT_MAX:
            return 0
        return result
