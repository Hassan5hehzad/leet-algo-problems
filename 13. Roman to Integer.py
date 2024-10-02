class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_int = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
      
        prev_number = roman_to_int[s[-1]]
      
        total = prev_number
      
        for i in range(len(s) - 2, -1, -1):
            curr_number = roman_to_int[s[i]]
          
            if curr_number < prev_number:
                total -= curr_number
            else:
                total += curr_number
          
            prev_number = curr_number
      
        return total