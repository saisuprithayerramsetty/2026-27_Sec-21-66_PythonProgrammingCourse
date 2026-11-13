counter = 0

def increment():
    global counter
    counter = counter + 1
    print("Inside counter, counter=",counter)

print("Before:", counter)
increment()
print("After:", counter)




counter = 0

def increment():
    global counter
    counter = counter + 1
    print("Inside function, counter =", counter)

print("Before:", counter)
increment()
print("After:", counter)