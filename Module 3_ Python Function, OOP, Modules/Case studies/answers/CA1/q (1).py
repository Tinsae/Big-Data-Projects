# 1
import math
# origin
x1 = 0
y1 = 0
# directions
up = 5
down = 3
right = 2
left = 3
# get destination coordinates
x2 = right - left
y2 = up - down 

dist = math.hypot(x2-x1, y2-y1)
print(f"distance from ({x1},{y1}) to ({x2},{y2}) is {dist}")