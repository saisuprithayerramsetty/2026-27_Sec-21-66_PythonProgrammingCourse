angle_1_degrees = int(input("enter a first angle in degrees:"))
angle_2_degrees = int(input("enter a second angle in degrees:"))
angle_3_degrees = int(input("enter a third angle in degrees:"))
if angle_1_degrees > 0 and angle_2_degrees > 0 and angle_3_degrees > 0 and angle_1_degrees+angle_2_degrees+angle_3_degrees == 180:
    print(f"valid triangle, (sum of angles = {angle_1_degrees+angle_2_degrees+angle_3_degrees})")
else:    
    print(f"not a valid triangle (sum of angles = {angle_1_degrees+angle_2_degrees+angle_3_degrees})")