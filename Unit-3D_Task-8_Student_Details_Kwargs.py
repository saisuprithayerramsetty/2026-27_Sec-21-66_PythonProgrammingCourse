def student_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
student_details(name="Sai",maths=100,science=96)