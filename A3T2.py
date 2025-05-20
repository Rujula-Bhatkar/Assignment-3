import math
num=int(input("Enter a number:"))
def compute(a):
    sqroot=math.sqrt(a)
    print("Square root:", sqroot)
    logarithm=math.log(a)
    print("Logarithm:",logarithm)
    sine=math.sin(a)
    print("Sine:",sine)
compute(num)

