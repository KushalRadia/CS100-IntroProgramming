# PROGRAM TO CALCULATE THE SUM OF TWO NUMBERS..............................
num1 = float(input("Enter first number : "))
num2 = float(input("Enter second number : "))
sum = num1 + num2
print("The sum of given numbers is  : " , sum)

# ARITHMETIC OPERATORS.....................................................
number1 = 4 
number2 = 3
print(number1 + number2) # ADDITION - 7
print(number1 - number2) # SUBTRACTION - 1
print(number1 * number2) # MULTIPLICATION - 12 
print(number1 / number2) # DIVISION - 1.3333333333333333
print(number1 % number2) # MODULUS - 1(gives remainder)
print(number1 // number2) # FLOOR DIVISION - 1(gives nearest whole number)
print(number1 ** number2) # EXPONENTIAL - 64
print(18//10)

# LOGICAL OPERATORS........................................................
exp1 = 3>4
exp2 = 5>4
print("exp1 and exp2 : ", exp1 and exp2)
print("exp1 or exp2 : ", exp1 or exp2)
print("not exp1 : ",  not(exp1))

# IDENTITY OPERATORS.......................................................
# is - returns True if both variables are the same objects.
# is not - returns True if both the objects are not the same objects.
x = 3
y = 3
print("If x is y : ", x is y)
print("If x is not y : ", x is not y)

# MEMBERSHIP OPERATORS.....................................................
fruits = ["banana" , "apple", "mango","pineapple"]
print("If mango is in fruits : ", "mango" in fruits)
print("If kiwi not in fruits : ", "kiwi"  not in fruits)

# BITWISE OPERATORS........................................................
# LOGICAL AND - &
# LOGICAL OR - |
# XOR OPERATOR - ^(give false when both bits are same)
# NOr OPERATOR - ~
# LEFT SHIFT - <<(like 10110 << 1 is  01100 as leftside one is removed and at rightside one is added)
# RIGHT SHIFT OPERATORS - >>(like 10110 >> 1 is 01011 as rightside zero is removed and at leftside zero is added)
a = 5 
b = 3
print("a and b : ", a & b)
print("a or b : ", a | b)
print("a xor b : ", a ^ b)
print("nor of b : ", ~b)
print("leftshift of b: ",b<<1)#(shift b binary form 1 places)
print("rightshift of b: ",b>>2)#(shift b binary form 2 places)

# OPERATORS PRECEDENCE......................................................
# () then ** then then / , // , %  then * then + , - then bitwise shift operators(>> , <<) then bitwise operators(& , ^ , |) then comparison operators(== , != , < , >) then logical operators(or , and , not)

