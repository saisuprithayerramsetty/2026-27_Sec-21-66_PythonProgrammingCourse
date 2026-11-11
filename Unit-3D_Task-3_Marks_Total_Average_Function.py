def total_average(s1,s2,s3):
    total = s1+s2+s3
    average = total/3
    return total,average
s1 = int(input("Enter the marks of subject 1:"))
s2 = int(input("Enter the marks of subject 2:"))
s3 = int(input("Enter the marks of subject 3:"))
total,average = total_average(s1,s2,s3)
print("Total:",total)
print("Average:",average)