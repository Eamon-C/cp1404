"""
CP1404, prac, week 3
randoms.py
"""

"""
Questions:
1.  Ran line 1 three times. Results: 20, 5, 17.
    The lowest number possible would be 5, and the largest would be 20.

2.  Ran line 2 three times. Results: 7, 7, 9.
    The lowest number possible would be 3, and the largest would be 9.
    line 2 cannot produce a 4, as it only produces ODD numbers (every second number, starting from 3).

3.  Ran line 3 three times. Results: 3.295931601339505, 2.761110119609922, 4.606238046755772.
    The smallest number possible would be 2.5, and the largest would be 2.1.
"""

import random

print(random.randint(1, 100))
