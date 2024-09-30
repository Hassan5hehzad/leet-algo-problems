class Solution:
  def isPalindrome(self, x: int) -> bool:
    if x < 0:
      return False

    rev_half = 0
    y = x

    while y:
      rev_half = rev_half * 10 + y % 10
      y //= 10

    return rev_half == x