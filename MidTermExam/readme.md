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














