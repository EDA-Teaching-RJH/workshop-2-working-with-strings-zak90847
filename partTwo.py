import math  

def main():
 side_a = int(input("Enter length of side A: "))
 side_b = int(input("Enter length of side B" )) 
 result = pythag(side_a,side_b)
 print("The hypotenuse is " ,result )

def pythag(A,B):
 sum_of_squares = A**2 + B**2

 C = math.sqrt(sum_of_squares)
 return C 
main()
