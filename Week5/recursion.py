# RECURSION FUNCTION CALLS ITSELF SO THAT IT CAN DIVIDE A PROBLEM INTO IT'S SUBPROBLEM OR SOLVE A PROBLEM THROUGH IT'S SUBPROBLEM.
# RECURSION IS DONE IN MEMORY USING THE PROCESS CALLED CALL STACK.

# QUESTION : WRITE A PYTHON PROGRAM  TO CALCULATE THE FACTORIAL OF A NUMBER( A NON NEGATIVE INTEGER ) USING RECURSIVE FUNCTION.
def fact(n):
    # BASE CASE , TELLS THE FUNCTION WHERE TO STOP.
    if n == 0:   
        return 1 
    # RECURSIVE CASE , WHERE FUNCTION CALLS ITSELF.
    answer = n * fact(n-1) 
    return answer 
n = int(input("Enter a positive integer : "))
print("The value of factorial is : ",fact(n))

# QUESTION : WRITE A PROGRAM TO PRINT NUMBERS FROM n TO 1 .
# INPUT : n = 5
# OUTPUT : 
'''
5
4
3
2
1
'''
def prnt(n):
    # BASE CASE 
    if n == 0:
        return None
    print(n)
    # RECURSIVE CASE 
    prnt(n-1)
n = int(input("Enter a number : "))
prnt(n)

# QUESTION PRINT SUM 1 TO N USING RECURSION.
# INPUT : n = 5 
# OUTPUT : SUM : 15
def sum(n):
    if n == 1:
        return 1 
    answer = n  + sum(n-1)
    return answer
n = int(input("Enter a positive number : "))
print("The sum of numbers till " , n , "is : " ,sum(n))

# QUESTION : MAKE A FUNCTION WHICH CALCULATES "a" RAISED TO THE POWER "b" USING RECURSION.
# INPUT : a = 2 , b = 3
# OUTPUT : a RAISED TO POWER b : 8 
b = int(input("Enter power : "))
a = int(input("Enter base :  "))
def pow(a,b):
    if b == 0 :
        return 1 
    answer = a * pow(a , b-1)
    return answer
answer = pow(a,b)
print(a ,"RAISED TO THE POWER", b, "IS :", answer)

# QUESTION :WRITE A PROGRAM WHICH CALCULATES FIBONACCI SEQUENCE USING RECURSION.
# INPUT : n = 7 
# OUTPUT : 0 1 1 2 3 5 8 
def fibonacci(n):
    if n == 1 :  # BASE CASE 
        return 0 
    elif n == 2 :  # BASE CASE 
        return 1
    else:   
        return (fibonacci(n-1) + fibonacci(n-2)) # RECURSIVE CASE 
    
n = int(input("Enter a number : "))
for i in range(1, n+1):
    print(fibonacci(i) , end = " ")
 