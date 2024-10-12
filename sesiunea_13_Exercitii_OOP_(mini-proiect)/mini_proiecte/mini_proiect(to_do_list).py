class TodoList:
    # todo: -The to_do attribute is a dictionary that will store tasks and their descriptions
    to_do = {}

    # Method to add a task to the to-do list
    def add_task(self, name, description):
        self.to_do[name] = description
        print(f"Task '{name}' has been successfully added.")

    # Method to mark (delete) a task from the to-do list as completed
    def complete_task(self, name):
        if name in self.to_do:
            del self.to_do[name]
            print(f"Task '{name}' has been completed and removed.")
        else:
            print(f"Task '{name}' does not exist in the to-do list.")

    # Method to display only the task names (keys from the dictionary)
    def show_todo_list(self):
        if self.to_do:
            print("To-Do List:")
            for task_name in self.to_do:
                print(f"- {task_name}")
        else:
            print("No tasks in the to-do list.")

    # Method to display additional details for a task
    def show_task_details(self, task_name):
        if task_name in self.to_do:
            print(f"Details for task '{task_name}': {self.to_do[task_name]}")
        else:
            print(f"Task '{task_name}' does not exist in the to-do list.")
            add = input("Do you want to add this task? (yes/no): ").strip().lower()
            if add == 'yes':
                description = input("Enter the description for the new task: ")
                self.add_task(task_name, description)
            else:
                print("Task was not added.")

# Example usage
# Create a TodoList object


todolist = TodoList()

# Add some tasks
todolist.add_task("Wash dishes", "Wash the dishes after dinner.")
todolist.add_task("Grocery shopping", "Buy fruits and vegetables.")

# Display the to-do list
todolist.show_todo_list()

# Show additional details for a task
todolist.show_task_details("Grocery shopping")

# Try to display details for a task that doesn't exist
todolist.show_task_details("Walk the dog")

# Complete a task
todolist.complete_task("Wash dishes")

# Display the to-do list after completing a task
todolist.show_todo_list()
