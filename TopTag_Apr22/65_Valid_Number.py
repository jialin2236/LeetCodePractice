"""
65. Valid Number (H, 49)
"""

# determine if input string is a valid number
# definition
# decimal or integer
# could have 'e'/'E' followed by integer
# decimal
#   could have a sign
#   - 1+ digits followed by '.'
#   - 1+ digits, followed by '.', followed by 1+ digits
#   - '.' followed by 1+ digits

# exceptions
# if encounter anything other than digits, '.', 'e', 'E', '+', '-'
# '+'/'-' if already seen '+', '-', unless right after 'e'/'E'
# '.' if already seen '.', 'e'/'E' if already seen 'e'/'E' or never saw digit
# no digit if seen 'e'/'E'

# variables to indicate the signals we've seen

class Solution:
    def is_num(self, s: str) -> bool:
        e = dot = digits = sign = False
        for c in s:
            if c.isdigit():
                digits = True
            elif c in ['+', '-']:
                if digits or sign or dot:
                    # encounter '+'/'-' after anything
                    return False
                sign = True
            elif c == '.':
                if dot or e:
                    return False
                dot = True
            elif c.lower == 'e':
                if e or not digits:
                    return False
                e = True
                # reset digits (for +/-)
                digits = False
                sign = False
                dot = False
            else:
                return False
        return digits
