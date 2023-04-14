
# Your task is to complete the validate_triangle and the validate_rectangle functions for the classes. 
# Hint for validating is given in the comments of the code. Also you will have to fill the following after validation in respective functions:

# Invalid triangle: If the triangle sum property of sides is not valid (more hints in the comments of the code)
# Valid Triangle: If the triangle sum property of sides is valid
# Valid rectangle: If 2 side pairs are same and they are input in correct order like l,b,l,b
# Invalid rectangle: If Not Valid rectangle as stated above

# Input format
# The side length of the triangle followed by for rectangle in the next line in order

# Output format:
# Since objects are created in order, so first validate info about triangle will come and then rectangle

# Sample input:0
# 3 4 5
# 2 4 2 4

# Sample Output:0
# Valid Triangle
# Valid Rectangle



class Triangle():
    def __init__(self,lst):
        self.lst=lst
    def validate_triangle(self,l):
        if len(l)==3 and (l[0]+l[1])>l[2]:
            return "Valid Triangle"         
        else:
            return "Invalid Triangle"
s=list(map(int,input().split()))
class Rectangle():
    def __init__(self,lst):
        self.lst=lst
    def validate_rectangle(self,l):
        if len(l)==4 and  (l[0]==l[2]) and (l[1]==l[3]):
            return "Valid Rectangle"         
        else:
            return "Invalid Rectangle"
# s=list(map(int,input().split()))
t=list(map(int,input().split()))
A=Triangle(s)       
print(A.validate_triangle(s))
B=Rectangle(t)
print(B.validate_rectangle(t))