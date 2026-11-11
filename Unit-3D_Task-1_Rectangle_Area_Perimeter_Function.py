def rectangle(breadth,length):
    perimeter =  2*(length+breadth)
    area = length * breadth
    return area,perimeter
user_input1 = int(input("Enter  the length of a rectangle:"))
user_input2 = int(input("Enter the breadth of a rectangle:"))
area,perimeter = rectangle(user_input1,user_input2)
print("area:",area)
print("perimeter:",perimeter)