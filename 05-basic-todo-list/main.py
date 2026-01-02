"""
Basic To-Do List - Python Project 05
====================================
A simple command-line to-do list manager with file persistence.

🎯 LEARNING OBJECTIVES:
- Work with lists (add, remove, display)
- Store data in text files (file I/O)
- Handle file operations (read, write, append)
- Create a persistent data application
- Implement CRUD operations (Create, Read, Update, Delete)

📚 CONCEPTS COVERED:
- File handling (open, read, write, close)
- List operations (append, remove, enumerate)
- String methods (strip, split, join)
- Exception handling (FileNotFoundError)
- Data persistence across program runs
"""

import os

# File to store tasks
TASKS_FILE = "tasks.txt"

def load_tasks():
    """
    Load tasks from file into a list.
    
    Returns:
        list: List of task strings
    
    LEARNING: Reading from files, handling missing files
    """
    if not os.path.exists(TASKS_FILE):
        return []  # Return empty list if file doesn't exist
    
    try:
        with open(TASKS_FILE, 'r') as file:
            # Read lines and remove newline characters
            tasks = [line.strip() for line in file.readlines()]
            return [task for task in tasks if task]  # Remove empty lines
    except Exception as e:
        print(f"⚠️ Error loading tasks: {e}")
        return []

def save_tasks(tasks):
    """
    Save tasks list to file.
    
    Args:
        tasks (list): List of task strings
    
    LEARNING: Writing to files, overwriting existing content
    """
    try:
        with open(TASKS_FILE, 'w') as file:
            for task in tasks:
                file.write(task + '\n')
        return True
    except Exception as e:
        print(f"⚠️ Error saving tasks: {e}")
        return False

def display_tasks(tasks):
    """
    Display all tasks with numbers.
    
    LEARNING: Using enumerate() to get index and value
    """
    if not tasks:
        print("\n📭 No tasks yet! Add some to get started.")
        return
    
    print("\n" + "="*60)
    print("📝 YOUR TO-DO LIST")
    print("="*60)
    
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")
    
    print("="*60)
    print(f"Total tasks: {len(tasks)}")

def add_task(tasks):
    """
    Add a new task to the list.
    
    LEARNING: Getting user input and appending to lists
    """
    task = input("\nEnter new task: ").strip()
    
    if not task:
        print("❌ Task cannot be empty!")
        return tasks
    
    tasks.append(task)
    print(f"✅ Added: '{task}'")
    
    return tasks

def remove_task(tasks):
    """
    Remove a task by its number.
    
    LEARNING: Removing items from lists by index
    """
    if not tasks:
        print("\n📭 No tasks to remove!")
        return tasks
    
    display_tasks(tasks)
    
    try:
        task_num = int(input("\nEnter task number to remove: "))
        
        if 1 <= task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)  # Convert to 0-based index
            print(f"✅ Removed: '{removed_task}'")
        else:
            print(f"❌ Invalid task number! Choose 1-{len(tasks)}")
    
    except ValueError:
        print("❌ Please enter a valid number!")
    
    return tasks

def clear_all_tasks(tasks):
    """
    Remove all tasks after confirmation.
    
    LEARNING: User confirmation for destructive operations
    """
    if not tasks:
        print("\n📭 No tasks to clear!")
        return tasks
    
    confirm = input(f"\n⚠️ Are you sure you want to clear all {len(tasks)} tasks? (y/n): ").lower()
    
    if confirm == 'y':
        tasks.clear()
        print("✅ All tasks cleared!")
    else:
        print("❌ Cancelled")
    
    return tasks

def mark_task_done(tasks):
    """
    Mark a task as done by adding [DONE] prefix.
    
    LEARNING: Modifying list items
    """
    if not tasks:
        print("\n📭 No tasks to mark!")
        return tasks
    
    display_tasks(tasks)
    
    try:
        task_num = int(input("\nEnter task number to mark as done: "))
        
        if 1 <= task_num <= len(tasks):
            # Check if already marked
            if tasks[task_num - 1].startswith("✓ "):
                print("ℹ️ Task already marked as done!")
            else:
                tasks[task_num - 1] = "✓ " + tasks[task_num - 1]
                print("✅ Task marked as done!")
        else:
            print(f"❌ Invalid task number! Choose 1-{len(tasks)}")
    
    except ValueError:
        print("❌ Please enter a valid number!")
    
    return tasks

def display_menu():
    """
    Display main menu options.
    """
    print("\n" + "="*60)
    print("📝 TO-DO LIST MENU")
    print("="*60)
    print("1. View all tasks")
    print("2. Add new task")
    print("3. Remove task")
    print("4. Mark task as done")
    print("5. Clear all tasks")
    print("6. Save and exit")
    print("="*60)

def main():
    """
    Main program loop.
    
    LEARNING: 
    - Program lifecycle (load → operate → save)
    - Menu-driven applications
    - Data persistence
    """
    print("\n🎯 Welcome to Your To-Do List Manager!")
    print("📂 Loading tasks...")
    
    # Load existing tasks from file
    tasks = load_tasks()
    print(f"✅ Loaded {len(tasks)} task(s)")
    
    # Main loop
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-6): ").strip()
        
        if choice == '1':
            # View tasks
            display_tasks(tasks)
        
        elif choice == '2':
            # Add task
            tasks = add_task(tasks)
        
        elif choice == '3':
            # Remove task
            tasks = remove_task(tasks)
        
        elif choice == '4':
            # Mark as done
            tasks = mark_task_done(tasks)
        
        elif choice == '5':
            # Clear all
            tasks = clear_all_tasks(tasks)
        
        elif choice == '6':
            # Save and exit
            print("\n💾 Saving tasks...")
            if save_tasks(tasks):
                print("✅ Tasks saved successfully!")
                print(f"📁 Saved to: {TASKS_FILE}")
                print("\n👋 Goodbye! Your tasks will be here next time.")
                break
            else:
                print("⚠️ Error saving tasks!")
                retry = input("Try again? (y/n): ").lower()
                if retry != 'y':
                    break
        
        else:
            print("❌ Invalid choice! Please select 1-6.")

if __name__ == "__main__":
    main()

# ============================================================================
# FILE I/O CONCEPTS EXPLAINED:
# ============================================================================
# 'r' mode: Read (file must exist)
# 'w' mode: Write (creates new or overwrites existing)
# 'a' mode: Append (adds to end of file)
# 'with' statement: Automatically closes file (best practice)
#
# file.read() - reads entire file as string
# file.readlines() - reads file as list of lines
# file.write(text) - writes text to file
# file.writelines(list) - writes list of strings to file

