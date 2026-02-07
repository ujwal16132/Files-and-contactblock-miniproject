task = {
    "week":{
        "monday".lower(): [],
        "tuesday".lower():[],
        "wednesday".lower():[],
        "thursday".lower():[],
        "friday".lower():[],
        "saturday".lower():[],
        "sunday".lower():[]
        }
}
while True:
    print("1.add task" ,end =" ")
    print("2.view tasks",end =" ")
    print("3.delete tasks",end =" ")
    print("4.Mark tasks",end =" ")
    print("5.Quit to do list",end =" ")
    try:
        click = int(input("click ="))
    except ValueError:
        print("only you want enter numbers")
        break
    if click ==1:
        days = input("Enter the day :").lower().strip().split()
        task_1 = input("Enter the tasks \nTasks will be one day or multiple days:").lower().split(",")
        for  day in days:
            if day not in task["week"]:
                print("day was invalid")
                break
        for tsk in task_1:
            if tsk in task["week"]:
                print("You entered days in tasks also\nYou want take tasks only")
                break
            elif day in task["week"]:
                task["week"][day].append(tsk.strip())
    elif click == 2 :
        days = input("Enter the same day that you entered in add task:").lower().strip().split()
        for day in days:
            #for tasks in task["week"].values():
                if day in task["week"]:
                    view_task = task["week"][day]
                    print(day,":" ,view_task)
                elif day not in task["week"]:
                    print("You did not entered the tasks in add tasks section")
                    print("To view tasks Please enter tasks in add tasks section")
                    break
                else:
                    print(day ,": not valid")
                    break     
    elif click == 3:
        days = input("Enter the same day that you entered in add task:").lower().strip().split()
        task_1 = input("Enter the  same tasks that you entered in add tasks:").lower().split(",")
        for day in days:
            #for tasks in task["week"][day].values():
            #if len(days)==0 and len(task_1) == 0:
            if day not in task["week"]:
                print("You did not entered the day correctly")
                print(day,":", "is invalid")
                break
        for tsk in task_1:
            if tsk not in  task["week"][day]:
                print(" the entered task is invalid ")
                print("To delete tasks Please enter tasks in add tasks section")
                break
            elif tsk in task["week"][day]:
                    task["week"][day].remove(tsk.strip())
                    print(f"{day}:{tsk} task is deleted sucessfully")
    elif click == 4:
        days = input("Enter the day :").lower().strip().split()
        task_1 = input("Enter the same task that you entered the add task section:")
        for day in days:
            if task_1 in task["week"][day]:
                print(day,":",task_1,":","your task is marked")
            elif task_1 not in task["week"][day]:
                print("if you want to Mark task\nYou want to enter the same task that added in add task section")
    elif click == 5:
        print("thanks for using to do list")
        for day,tsk in task["week"].items():
            if len(tsk) ==0:
                print(day,":","No tasks are added")
            else:
                print(day,":",tsk)