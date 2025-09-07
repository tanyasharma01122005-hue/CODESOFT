# make a list for storing the task that which task you have to perform according to your requirement
work=[]
# define a function which contains tasks  what you can do
def tasks():
  print(" 1. Add Task ")
  print(" 2. Remove Task ")
  print(" 3. View Task ")
# Herw using while loop because the no. of steps are decided according to the need of user 
while True:
  # call the function tasks
  tasks()
  # time to select which option a user prefer to do 
  select_choice=input("Enter the option from (1 to 3):")
  # using if-elif-else statements 
  if select_choice == "1":
        if len(work) == 0:
            print("No tasks in the list.")
        else:
            print("Your Tasks:")
            for i, works in enumerate(work , start=1):
                print(f"{i}. {works}")

    elif select_choice == "2":
        works = input("Enter a new task: ")
        work.append(works)
        print(f"Task '{works}' added successfully!")

    elif select_choice == "3":
        if len(Work) == 0:
            print("No tasks to remove.")
        else:
            print("Your Tasks:")
            for i, works in enumerate(work, start=1):
                print(f"{i}. {works}")
            try:
                work_number = int(input("Enter task number to remove: "))
                removed_work = work.pop(work_number - 1)
                print(f"Task '{removed_work}' removed successfully!")
            except (ValueError):
                print("Invalid task number.")

    elif select_choice == "4":
        print("Exiting... Goodbye!")
        break

    else:
        print("Invalid choice! Please try again.")
  

