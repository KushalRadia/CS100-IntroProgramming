# for LOOP....................................................................
# range(start , stop , step)
# If starting value is not given ; range function by default takes starting value as 0.
for  i in range(1,11):
    print("Hello , World!!")

for a  in range(10):
    print(a,"Hello , World!!")
    
for _ in range(1,11,2):
    print(i,"Hello , World!!")

fruits = ["Apples" , "Mango" , "Kiwi" , "Banana" , "Pineapple"] 
list1 = [1,78,348,22,89,354]
for i in fruits:
    print(i)
for j in list1:
    print(j)       
print("EVEN NUMBERS TILL 100 ARE : ")
for i in range(2,101,2):
    print(i)    

# while LOOP....................................................................
# It runs until the condition is true.
i = 2
while i <101 : # can also be written as i <= 100
    print(i)
    i += 2     

# PROGRAM TO FIND A NUMBER THAT IS DIVISIBLE BY 3 OR BUT NOT BY 15 
num = int(input("ENTER A NUMBER : "))
if num % 15 == 0:
    print("NUMBER",num,"IS DIVISIBLE BY 15.")
else:
    if num % 3==0 or num % 5 == 0:
        print("NUMBER" ,num,"IS DIVIBLE BY 3 OR 5 BUT NOT WITH 15.")
    else:
        print("NUMBER",num,"IS NOT DIVISIBLE BY 3 , 5, 15.")    
     