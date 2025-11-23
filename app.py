#To do list in python

Tasks = []

#define a function

def output():
    print("To do list \n")
    print("1.add task")
    print("2.Remove a task that you already did")
    print("3.display all the tasks")
    print("4.exit")
    options = input("enter a number 1,2,3,or 4: ")
    return options

options = "xxxxxx"
while options != "4":
    options = output(Tasks)
    if options == "1":
        task = input("add your item here: ")
        Tasks.append(task)
        print(f'task added: \n,{task}' )
    elif options == "2":
        task = input("tick off the task you did: ")
        if task in Tasks:
         Tasks.remove(task)
         print(f'task removed: ,{task}')
        else:
             print("task not found")
       
    elif options == "3":
        if len(Tasks) != 0:
         for task in Tasks:
          print("please view your tasks:,{task}")
        else:
            print("task not found")
    elif options == "4":
        print("bye")
    else:
        print("please enter 1,2,3,or 4")
    

    
                





    
