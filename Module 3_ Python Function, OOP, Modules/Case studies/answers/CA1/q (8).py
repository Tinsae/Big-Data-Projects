# 8
import math
C = 50
H = 30

D = input().split(",")
calc = lambda d: int(math.sqrt((2 * C * int(d)) / H))
Q  = [str(calc(d)) for d in D]
print(",".join(Q ))