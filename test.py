 #Group Name: [DAN/EXT 12]
#Group Members:
              #Sandeep Prasai - [S396604]
              #Avinash Babu Chalise - [S396603]
              #Rahul Kandel - [S396567]
              #Harlen Rajith Christopher Jansz - [S358415]

#  PART A: Triangle Checker 
print("== Triangle Side Length Checker ==")
a = int(input("User input 1: "))
b = int(input("User input 2: "))
c = int(input("User input 3: "))

if a + b > c and a + c > b and b + c > a:
    print("Yes, these three lengths can form a triangle.")
else:
    print("NO, these three lengths CANNOT form a triangle.")



# PART B:  Drawing Square based on the user input.
print("Drawing a Square")
size = int(input("Enter the size of the square: "))
 
for i in range(size):
    print("* " * size)
