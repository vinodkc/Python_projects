# 05 - Basic To-Do List

## 🚀 Project Overview

A command-line to-do list manager with persistent storage. Add, view, remove, and mark tasks as complete. All tasks are saved to a file and automatically loaded when you restart the program.

## 🎯 Learning Objectives

By completing this project, you will:
- Read and write files in Python
- Work with lists (CRUD operations)
- Understand data persistence
- Handle file exceptions (missing files, permissions)
- Use the `with` statement for safe file handling
- Implement menu-driven applications
- Manage program state across sessions

## 📚 What You'll Learn

### **Core Concepts:**
- **File I/O**: Reading from and writing to files
- **Data Persistence**: Saving data between program runs
- **Lists**: Dynamic data structures
- **CRUD Operations**: Create, Read, Update, Delete
- **Context Managers**: `with` statement for resource management
- **Exception Handling**: Dealing with file errors

### **Python Skills:**
- `open()`, `read()`, `write()`, `close()`
- `with` statement (context manager)
- List methods: `append()`, `pop()`, `clear()`
- `enumerate()` for indexed iteration
- String methods: `strip()`, `startswith()`
- `os.path.exists()` for file checking

## 🔧 Implementation Explanation

**Architecture:**
1. **Load Phase**: Read tasks from `tasks.txt` on startup
2. **Operation Phase**: User adds/removes/marks tasks
3. **Save Phase**: Write all tasks back to file on exit

**Key Features:**
- ✅ Add unlimited tasks
- ✅ Remove tasks by number
- ✅ Mark tasks as done (✓ prefix)
- ✅ Clear all tasks with confirmation
- ✅ Auto-save on exit
- ✅ Persistent storage (survives program restart)

## ⚙️ How to Run

```bash
cd Python_projects/05-basic-todo-list
python main.py
```

**Files Created:**
- `tasks.txt` - Stores your tasks (created automatically)

## 📖 Further Learning - W3Schools

- [Python File Handling](https://www.w3schools.com/python/python_file_handling.asp)
- [Python File Open](https://www.w3schools.com/python/python_file_open.asp)
- [Python File Write](https://www.w3schools.com/python/python_file_write.asp)
- [Python Lists](https://www.w3schools.com/python/python_lists.asp)
- [Python Try Except](https://www.w3schools.com/python/python_try_except.asp)

---

**Difficulty**: 🟢 Beginner  
**Estimated Time**: 60 minutes  
**Key Concepts**: File I/O, Lists, Data Persistence

