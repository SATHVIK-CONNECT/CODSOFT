def add_task(task_list, task):
  task_list.append(task)
  print("Task added!")

def view_tasks(task_list):
  if not task_list:
    print("No tasks found.")
  else:
    for index, task in enumerate(task_list, start=1):
      print(f"{index}. {task}")
  
  return task_list

def remove_task(task_list, task_index):
  try:
    del task_list[task_index - 1]
    print("Task removed!")
  except IndexError:
    print("Invalid task index.")

def update_task(task_list, task_index, new_task):
  try:
    task_list[task_index - 1] = new_task
    print("Task updated!")
  except IndexError:
    print("Invalid task index.")

def main():
  task_list = []

  while True:
    print("\nTo-Do List App")
    print("1. Add task")
    print("2. View tasks")
    print("3. Remove task")
    print("4. Update")
    print("5. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
      task = input("Enter task: ")
      if task:
          add_task(task_list, task)
      else:
          print('Task should not be blank! ')
    elif choice == "2":
      view_tasks(task_list)
    elif choice == "3":
      list = view_tasks(task_list)
      if list:
          task_index = int(input("Enter task index to remove: "))
          if task_index != 0:
              remove_task(task_list, task_index)
          else:
              print('There is no task with index 0.')
    elif choice == "4":
        list = view_tasks(task_list)
        if list:
            task_index = int(input("Enter task index to update: "))
            if task_index != 0 and task_index < len(list) + 1:
               new_task = input("Enter new task: ")
               update_task(task_list, task_index, new_task)
            else:
                print('Invalid Index')
    elif choice == "5":
      break
    else:
      print("Invalid choice.")

if __name__ == "__main__":
  main()
