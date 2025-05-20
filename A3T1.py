
num = int(input("Enter a number:"))
fac=1
#Factorial using while loop
def factorial(a):
    while(a>0):
        global fac
        fac *= a
        a-=1
    return fac
ans=factorial(num)
print("Factorial of",num,"is:",ans,"(Using while loop)")

#Factorial using recursion
def fact(b):
    if b<2:
        return 1
    else:
        return b*fact(b-1)
ans=fact(num)
print("Factorial of",num,"is:",ans,"(Using recursion)")




