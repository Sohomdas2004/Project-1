import random
import pandas as pd

def otp_generator():
    num1=random.choice([0,1,2,3,4,5,6,7,8,9])
    num2=random.choice([0,1,2,3,4,5,6,7,8,9])
    num3=random.choice([0,1,2,3,4,5,6,7,8,9])
    num4=random.choice([0,1,2,3,4,5,6,7,8,9])
    num5=random.choice([0,1,2,3,4,5,6,7,8,9])
    num6=random.choice([0,1,2,3,4,5,6,7,8,9])
    otp=str(num1)+str(num2)+str(num3)+str(num4)+str(num5)+str(num6)
    return int(otp)

def add_task(task_list, time_list, task, time):
    task_list.append(task)  
    time_list.append(time)  

def delete_task(task_list, time_list, task):
    if task in task_list:
        n = task_list.index(task)  
        task_list.pop(n)  
        time_list.pop(n)  

def show(task, time):
    
    data = {
        "Task": task,
        "Time": time
    }
    df = pd.DataFrame(data)
    print(df)


s = otp_generator()
print(f"The OTP is {s}")
print("Enter the OTP:")
s1 = int(input())
if s == s1:
    
    task_list = []
    time_list = []

    while True:
        print("\nMain Menu\n1. Add Task\n2. Delete Task\n3. Show Task\n4. Exit\n")
        print("Enter your choice:")
        choice = int(input())
        
        match choice:
            case 1:
                print("Enter the task:")
                task = input()  
                print("Enter the time you want to spend for the task (in minutes):")
                time = int(input())  
                add_task(task_list, time_list, task, time)
            
            case 2:
                print("Enter the task you want to delete:")
                task = input()  
                delete_task(task_list, time_list, task)
            
            case 3:
                show(task_list, time_list)
            
            case 4:
                print("Exiting...")
                break
            
            case _:
                print("Please enter a valid choice")
else:
    print("OTP doesn't match")
