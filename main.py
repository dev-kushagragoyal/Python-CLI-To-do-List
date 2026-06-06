print("TO DO LIST")
print()

print("You can add up to 11 tasks only")
print()

print("Choose from the options given below")
print()


all_task = []
all_tasks_no = 0
comp = "complete"

while True:

    print('''
        1 == Add a new task
        2 == Display all tasks
        3 == Enter a completed task
        4 == View total number of tasks
        5 == Delete all tasks
        6 == Exit
    ''')
    print()


    choice = int(input("Enter your choice : "))
    print()


    if choice  == 1:

        task = input("Enter your new task : ")
        print()

        all_tasks_no = all_tasks_no + 1
        all_task.append(task)

    elif choice == 2:

        if all_tasks_no == 0:

            print("You do not have any pending task")

        else:
            print("Here are all your tasks -->")
            print()

            print(all_task)
            print()

    elif choice == 3:

        if all_tasks_no == 0:
            print("You do not have any pending task")
            print()

        else:

            print("Here are all your tasks -->")
            print()

            print(all_task)
            print()

            length = len(all_task)

            completed_task = int(input("Enter the task number you have completed starting from 0,1,2,3... : "))
            print()            

            if completed_task >= length or completed_task < 0:
                
                print("You do not have enough task to delete")
                print()
                
            elif completed_task == 0:

                all_task.pop(0)
                all_tasks_no = all_tasks_no - 1

                if all_tasks_no == 0:
                    print("Now you do not have any pending task")
                    print()

                else:
                    print("Here are the remaining tasks -->")
                    print()

                    print(all_task)
                    print()
                
            elif completed_task == 1:

                all_task.pop(1)
                all_tasks_no = all_tasks_no - 1

                if all_tasks_no == 0:
                    print("Now you do not have any pending task")
                    print()

                else:
                    print("Here are the remaining tasks -->")
                    print()

                    print(all_task)
                    print()

            elif completed_task == 2:

                all_task.pop(2)
                all_tasks_no = all_tasks_no - 1

                if all_tasks_no == 0:
                    print("Now you do not have any pending task")
                    print()

                else:
                    print("Here are the remaining tasks -->")
                    print()

                    print(all_task)
                    print()

            elif completed_task == 3:

                all_task.pop(3)
                all_tasks_no = all_tasks_no - 1

                if all_tasks_no == 0:
                    print("Now you do not have any pending task")
                    print()

                else:
                    print("Here are the remaining tasks -->")
                    print()

                    print(all_task)
                    print()

            elif completed_task == 4:

                all_task.pop(4)
                all_tasks_no = all_tasks_no - 1

                if all_tasks_no == 0:
                    print("Now you do not have any pending task")
                    print()

                else:
                    print("Here are the remaining tasks -->")
                    print()

                    print(all_task)
                    print()   

            elif completed_task == 5:

                all_task.pop(5)
                all_tasks_no = all_tasks_no - 1

                if all_tasks_no == 0:
                    print("Now you do not have any pending task")
                    print()

                else:
                    print("Here are the remaining tasks -->")
                    print()

                    print(all_task)
                    print()

            elif completed_task == 6:

                all_task.pop(6)
                all_tasks_no = all_tasks_no - 1

                if all_tasks_no == 0:
                    print("Now you do not have any pending task")
                    print()

                else:
                    print("Here are the remaining tasks -->")
                    print()

                    print(all_task)
                    print()

            elif completed_task == 7:

                all_task.pop(7)
                all_tasks_no = all_tasks_no - 1

                if all_tasks_no == 0:
                    print("Now you do not have any pending task")
                    print()

                else:
                    print("Here are the remaining tasks -->")
                    print()

                    print(all_task)
                    print()

            elif completed_task == 8:

                all_task.pop(8)
                all_tasks_no = all_tasks_no - 1

                if all_tasks_no == 0:
                    print("Now you do not have any pending task")
                    print()

                else:
                    print("Here are the remaining tasks -->")
                    print()

                    print(all_task)
                    print()

            elif completed_task == 9:

                all_task.pop(9)
                all_tasks_no = all_tasks_no - 1

                if all_tasks_no == 0:
                    print("Now you do not have any pending task")
                    print()

                else:
                    print("Here are the remaining tasks -->")
                    print()

                    print(all_task)
                    print()

            elif completed_task == 10:

                all_task.pop(10)
                all_tasks_no = all_tasks_no - 1

                if all_tasks_no == 0:
                    print("Now you do not have any pending task")
                    print()

                else:
                    print("Here are the remaining tasks -->")
                    print()

                    print(all_task)
                    print()

    elif choice == 4:

        print("Your total number of tasks is  : ",all_tasks_no)
        print()

    elif choice == 5:


        if all_tasks_no == 0:

            print("You do not have any task to delete")
            print()

        elif all_tasks_no > 0:

            print("Do you want to delete all the tasks")
            print()

            del_choice = int(input("Enter your choice 1.Yes  2.No : "))
            print()

            if del_choice == 1:

                print("Deleting all the tasks")
                print()

                print("All tasks have been deleted")
                print()

                all_tasks_no = 0
                all_task = []

            elif del_choice == 2:

                print("Cancelling the tasks to delete")
                print()

                print("Not any task deleted")
                print()

            else:
                
                print("Invalid option selected")
                print()

    elif choice == 6:

        print("Thanks for using our To Do List")
        print()
        break

    else:

        print("Invalid option selected")
        print()
