import time

print("Student Result Evaluation")
start =int(input("press 1 to go next:"))

while start == 1:
    name = input("Enter the student name: ")
    time.sleep(2)
    english_mark = float(input("Enter the English subject Mark:"))
    
    tamil_mark = float(input("enter the tamil subject mark: "))
    
    maths_mark = float(input("enter the maths subject mark:"))
    
    biology_mark = float(input("enter the Biology subject mark:"))
    
    social_mark = float(input("enter the social subject mark:"))
    
    physics_mark = float(input("enter the physics subject mark:"))

    print(f"The total Mark of {name}:{english_mark + tamil_mark + maths_mark + biology_mark + social_mark + physics_mark}/600")

    start = int(input("press 1 calculate next one or press 2 to exit:"))

    if start == 2:
        print("Thank you")
        break