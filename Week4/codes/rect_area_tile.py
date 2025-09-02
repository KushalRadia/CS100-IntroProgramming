#  Find the area of the rectangle
import math

l = float(input("input length"))
b = float(input("input breath"))
s = float(input("input s")) 

while (l < 0):
    print("length can't be negative")
    l = float(input("length"))
    print("length is: ", l)
    
while(b <0):
    print("breath cant be negative")
    b = float(input("breath"))
    print("breath is: ", b)
    
rect_area = l * b
print("area of the rectangle is: ", rect_area)
               
# compute the number of titles
while (s <0):
    print("s can't be negative")
    s = float(input("number of tiles"))

tile_area = s * s
print("Area of the tile is: ", tile_area)

# how many tiles needed ?

num_tile = math.ceil(rect_area / tile_area)

print("Number of tile is: ", num_tile)

# find max value

int_l = int(l)
int_b = int(b)
int_s = int(s)

# while the gcd of the l and b to be done

def gcd_with_factors(a, b):
    """
    Create a function to find the GCD of two numbers.
    """
    # create empty lists to hold the factors
    factors_a = []
    factors_b = []

    # find factors of a
    for i in range(1, a + 1):
        if a % i == 0:      # if i divides a without remainder
            factors_a.append(i)

    # find factors of b
    for j in range(1, b + 1):
        if b % j == 0:      # if j divides b without remainder
            factors_b.append(j)

    # now check common factors
    common_factors = []
    for f in factors_a:
        if f in factors_b:
            common_factors.append(f)

    # gcd is the largest common factor
    gcd_val = 1
    for c in common_factors:
        if c > gcd_val:     # keep updating if we find a bigger common factor
            gcd_val = c

    # return everything so we can see
    return gcd_val, factors_a, factors_b, common_factors
        

int_l, int_b = int(l), int(b)

gcd_val, fa, fb, fc = gcd_with_factors(int_l, int_b)

print("Factors of", l, ":", fa)
print("Factors of", b, ":", fb)
print("Common factors:", fc)
print("GCD is:", gcd_val)


            
        
        
        
        
        
    

    