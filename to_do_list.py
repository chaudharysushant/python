#define
to_do_list = [] 

#append
def add_task(task):
    to_do_list.append(task)
    print(f"Task '{task}' added to the to-do list." )

#view
def view_tasks():
    if not to_do_list:
        print("Empty List.")
    else:
        print("Your to-do list is:")
        for index, task in enumerate(to_do_list, 1):
            print(f"{index}. {task}")

#function to mark task completion

def mark_completed(task):
    if task in to_do_list:
        to_do_list.remove(task)
        print(f"Task '{task}' mark completed.")
    else:
        print(f"Task '{task} not found in to-do list.")

#function to remove task in to-do list

def remove_task(task):
    if task in to_do_list:
        to_do_list.remove(task)
        print(f"Task '{task}' removed from to-do list")
    else:
        print(f"Task '{task}' not found in to do list.")

#main function to run the program
def main():
    while True:
        print("\nWhat would you like to do?")
        print("1. Add a task")
        print("2. View Tasks")
        print("3. Mark a task as completed")
        print("4. Remove a task")
        print("5. Exit")

        choice = input("Enter your choice:")
        if choice == "1":
            task = input("Enter the task you want to add:")
            add_task(task)
        
        elif choice == "2":
            view_tasks()

        elif choice == "3":
            task = input("Enter the task you want to mark as completed:")
            mark_completed(task)
        
        elif choice == "4":
            task = input("Enter thye task you want to remove:")
            remove_task(task)
        
        elif choice == "5":
            print("Exiting the program.")
            break
    
        else:
            print("Invalid request")
 
if __name__ == "__main__":
    main()


    