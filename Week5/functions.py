# FUNCTIONS ARE BLOCKS OF REUSABLE CODE THAT PERFORMS A SPECIFIC TASK.....................

# FUNCTION THAT TAKES TWO NUMBERS AS INPUT AND RETURN THEIR SUM .
def add(n1 = 0 , n2 = 1 ):
    print(" n1 : " , n1)
    print(" n2 : " , n2)
    sum = n1 +n2 
    return sum 
# POSITINAL ARGUMENT 
print("The sum of numbers is : " , add( 5 ,9 ))
#  KEYWORD ARGUMENT 
print("The sum of numbers is : " , add(n2 = 6 , n1 = 4))
# DEFAULT ARGUMENT 
print("The sum of numbers is : " , add(2))
print("The sum of numbers is : " , add())
# ARBITRARY ARGUMENTS(VARIABLE LENGTH ARGUMENTS - *args AND **kwargs(keyworded argument / key-value pairs argument) WHERE *args IS A TUPLE AND **kwargs IS A DICTIONARY WHERE WE STORE LIKE name = "AAHANA".)
def add_all_num(*args):
    sum = 0
    for i in args : 
        sum += i
    return sum 
print("The sum of given numbes is : " , add_all_num(2,4,65,3,6,6,3,46,5,5,56))    
def student_info(**kwargs) :
    for i,j in kwargs.items() :
        print( i ,"is" , j)
student_info(name ="Light Yagami" , profession = "Theif" , age = 20)
student_info(name ="Monkey D. Luffy" , profession = "Robber" , age = 12)     

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
# NESTED FUNCTIONS...........................................................................
def outer_function():
    x = 1 # VARIABLE IN THE OUTER FUNCTION
    def inner_function():
        y = 2 
        result = x + y
        return result
    return inner_function()
output = outer_function()
print(output)

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
# GOLBAL - LOCAL VARIABLE....................................................................

# PASS BY VALUE - HERE WE PASS IMMUTABLE OBJECTS (LIKE STRINGS , TUPLES , INTEGERS , FLOATS). WHEN PASSED TO FUNCTION , A COPY OF THE OBJECT IS CREATED  AND ASSIGNED TO A LOCAL VARIABLE IN A FUNCTION(ANY CHANGE MADE TO THEM INSIDE FUNCTION , DO NOT AFFECT THE ORIGINAL OBJECT OUTSIDE FUNCTION).
def add_one(x):
    x = x + 1 
    print("Inside function value of x is : " , x) # LOCAL VARIABLE
x = 5 # GLOBAL VARIABLE 
add_one(x)
print("Outside function value of x is : " , x)  

# PASS BY REFERENCE - HERE WE PASS MUTABLE OBJECTS (LIKE LIST , DICTIONARIES). A REFERENCE TO ACTUAL OBJECT IS PASSED TO FUNCTION . CHANGES INSIDE THE FUNCTION WILL AFFECT THE ORIGINAL OBJECT.
def modify_list(lst):
    lst.append(4)
    print("The inside function list is :" , lst) # LOCAL VARIABLE
lst = [1,32,5,7,2] # GLOBAL VARIABLE
modify_list(lst)
print("The outside function list is :" , lst) 
# ------------------------------------------------------------
def modify_list(lst):
    lst.append(4)
    lst = [7,8,9,3,2] # LOCAL VARIABLE
    print("The inside function list is :" , lst) 
lst = [1,32,5,7,2] # GOBAL VARAIBLE
modify_list(lst)
print("The outside function list is :" , lst) 

# QUESTION : WRITE A PYTHON FUNCTION TO CALCULATE THE FACTORIAL OF A NUMBER( A NON NEGATIVE INTEGER ). THE FUNCTION ACCEPTS THE NUMBER AS AN ARGUMENT.
def fact(num1):
    if num1 > 0 :
        num = 1
        for i in range(1 , num1 + 1):
            num = num * i 
        print("Factorial of a number is : " , num)
    elif num1 == 0 :
        print("Factorial of zero is : 1")   
    else : 
        print("Factorial of negative number does not exist")         
num1 = int(input("Enter a integer number : "))       
fact(num1) 