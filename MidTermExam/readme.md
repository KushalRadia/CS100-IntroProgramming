This page discusses the questions on the midterm examination.

__Section A__

__Q1.__ You have to write a code to print your name in the centre of a rectangular box made of #.

__Solution:__ The solution consists of the following steps:

Step 1: First, we have to count the number of characters in your name. For example, if your name is "Sitaram Sharma", it has 14 characters.

Step 2: Planning the dimensions of the rectangular box. For symmetry, lets add 4 characters to the left and right. The boundary of the box is made of one character.
Thus, the total number of characters is 14+2x4+2 = 24 characters.

Step 3: Printing line by line. 

  Line 1: Print 24 # symbols using a for loop.

  Line 2: # is printed only on columns 1 and 24. Remaining columns we will print a whitespace ' '. 
  
  Line 3: Name is printed here. # is printed only on columns 1 and 24. Next 4 columns we will print a whitespace ' '. Next we will print the name. Next 4 columns we will print a whitespace ' '
  
  Line 4: # is printed only on columns 1 and 24. Remaining columns we will print a whitespace ' '. 
  
  Line 5: Print 24 # symbols using a for loop.

Notice that Line 1 and 5 have similar pattern. Line 2 and 4 also have similar pattern.
Thus, we can use nested loops to solve this problem.

__More practice:__
* BQ1.1: Write a code to print an isoceles triangle made of * where the base has (2*n+1) characters where n is an input given by the user.
* BQ1.2: Write a code to print a right angled triangle made of * where the base has n characters where n is an input given by the user.
* BQ1.3: Write a code to print an english alphabet like A, B, C made of * on a 5x5 grid of LEDs.


__Q2:__ Print all numbers below 1000 whose sum of digits is 7.

__Solution:__ The solution consists of the following steps:

**Planning:** We first recognize that we have to repeatedly compute the sum of digits in of a given number. It would be good to implement this as a function. It is also clear that this function has to be called 999 times with every number below 1000. We can reduce the number of calls by optimizing. For example, any number having a 8 or 9 can never have sum of its digits as 7.

How to compute sum of digits of a number?
Initialize the sum to 0. Keep incrementing sum by the digit in unit's place by remainder operator, num divided with 10. Divide the number by 10 so that the unit digit is removed. Continue till the number becomes 0.

def sum_digit(num):
Step 1: sum = 0
Step 2: While the number is greater than 0,
Step 3: sum = sum + num%10   
Step 4: num = num //10
Step 5: return sum

for i in range(1,1000):
  print sum_digit(i)

The above problem can also be solved by converting the number to a string and iterating on its characters and adding their integer value to the sum.

__More practice:__
* BQ2.1: Write a code to print all numbers below 1000, whose product of digits is 8.
* BQ2.2: Write a code to print all numbers made of following set of digits {1, 4, 5, 8} where each digit appears at least once and at most 3 times.
* BQ2.3: Write a code to print all numbers made of following set of digits {1, 3, 5, 8} where sum of digits is 14.
* 





















