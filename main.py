from math_utils import add, mul

print("math_utils test:")
print(f"add(5, 3) = {add(5, 3)}")
print(f"mul(5, 3) = {mul(5, 3)}")
print()

from shapes.circle import area_circle
from shapes.square import area_square

print("shapes test:")
print(f"area_circle(radius=3) = {area_circle(3):.2f}")
print(f"area_square(length of side=4) = {area_square(4)}")
print()