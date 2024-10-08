class Solution(object):
   def romanToInt(s):
    # Map of Roman numerals and their corresponding integer values
    roman_map = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    total = 0  # To store the final result

    # Loop through the string
    for i in range(len(s)):
        current_val = roman_map[s[i]]  # Value of current Roman numeral
        next_val = roman_map[s[i + 1]] if i + 1 < len(s) else 0  # Value of the next Roman numeral

        # If the current value is less than the next value, subtract it
        if current_val < next_val:
            total -= current_val
        # Otherwise, add it
        else:
            total += current_val

    return total
