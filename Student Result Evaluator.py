import time

print("Student Result Evaluation")
start =int(input("press 1 to go next:"))

while start == 1:
    name = input("Enter the student name: ")
    time.sleep(1)
    english_mark = float(input("Enter the English subject Mark:"))
    
    tamil_mark = float(input("enter the tamil subject mark: "))
    
    maths_mark = float(input("enter the maths subject mark:"))
    
    biology_mark = float(input("enter the Biology subject mark:"))
    
    social_mark = float(input("enter the social subject mark:"))
    
    physics_mark = float(input("enter the physics subject mark:"))

    total_mark = ((english_mark + tamil_mark + maths_mark + biology_mark + social_mark + physics_mark)/600)*100
    print(f"The total Mark of {name}:{total_mark} out of 600")

    if total_mark >= 0 and total_mark <= 34:
        print(f"Grad of the {name}: f")

    elif total_mark >=35 and total_mark <= 59:
        print(f"Grad of the {name}: d")

    elif total_mark >=  60 and total_mark <= 70:
        print(f"Grad of the {name}: C")

    elif total_mark >= 71 and total_mark <= 89:
        print(f"Grad of the {name}: b")

    elif total_mark >= 90 and total_mark <= 100:
        print(f"Grad of the {name}: A")
    

    start = int(input("press 1 calculate next one or press 2 to exit:"))

    if start == 2:
        print("Thank you")
        break