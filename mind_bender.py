#!/usr/bin/env python3
"""Visual quine that prints its own source code as ASCII art.
Run the output as Python and it will do the same.
"""
q = r'''#                 ________
#                /        \
#   ________    |  ()  ()  |
#  /        \   |    /\    |
# |  O    O  |   \  /  \  /
# |    --    |    \/____\/
# |  \____/  |
#  \________/
q = {q!r}
print(q.format(q=q))
'''
print(q.format(q=q))
