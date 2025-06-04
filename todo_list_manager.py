"""
Todo List Manager

This script implements a simple command-line Todo List Manager.
It allows users to add, remove, and display tasks in a todo list.

Usage:
1. Create an instance of TodoList.
2. Use add_task to add a new task.
3. Use remove_task to remove a task by its index.
4. Use display_tasks to show all current tasks.
"""

class TodoList:
    def __init__(self):
        """
        Initializes the TodoList instance.
        Creates a list to hold tasks.
        """
        self.tasks = []  # List to store todo tasks

    def add_task(self, task):
        """
        Adds a new task to the todo list.

        Args:
            task (str): The task description to be added.
        """
        self.tasks.append(task)  # Append task to the tasks list

    def remove_task(self, index):
        """
        Removes a task from the todo list by its index.

        Args:
            index (int): The index of the task to be removed. Zero-based.

        Returns:
            bool: True if the task was successfully removed, False if index is invalid.
        """
        if 0 <= index < len(self.tasks):  # Check if the index is valid
            self.tasks.pop(index)  # Remove task at the specified index
            return True  # Task removed successfully
        return False  # Invalid index, no task removed

    def display_tasks(self):
        """
        Displays all tasks in the todo list.

        Returns:
            str: A string representation of all tasks, or a message if empty.
        """
        if not self.tasks:
            return "No tasks in the todo list."  # Check if tasks list is empty
        return '\n'.join([f'{i+1}. {task}' for i, task in enumerate(self.tasks)])  # Format tasks for display

# Example usage (this part would usually be excluded):
# if __name__ == '__main__':
#     todo = TodoList()
#     todo.add_task('Buy groceries')
#     todo.add_task('Read a book')
#     print(todo.display_tasks())
#     todo.remove_task(0)
#     print(todo.display_tasks())