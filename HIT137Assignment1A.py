#Group Name: [DAN/EXT 12]
#Group Members:
              #Sandeep Prasai - [S396604]
              #Avinash Babu Chalise - [S396603]
              #Rahul Kandel - [S396567]
              #Harlen Rajith Christopher Jansz - [S358415]
 
#  PART A: Checking Triangle Checker
print("Triangle Side Length Checker")
a = int(input("User input 1: "))
b = int(input("User input 2: "))
c = int(input("User input 3: "))
 
#Checking if the triangle can be formed.
if a + b > c and a + c > b and b + c > a:
    print("Yes, these three lengths can form a triangle.")
else:
    print("No, these three lengths cannot form a triangle.")