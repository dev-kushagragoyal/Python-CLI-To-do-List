# Terminal-Based To-Do List Application 📝

A simple, interactive, terminal-based CLI (Command Line Interface) application built in Python to manage daily tasks efficiently. 

## 🚀 Features

* **Add New Tasks:** Dynamically build up your task list.
* **Display Active Tasks:** View all pending tasks directly formatted as a list.
* **Mark Tasks Completed:** Remove completed tasks from your list by choosing their index number.
* **Track Total Tasks:** Instantly check the total number of tasks remaining.
* **Bulk Delete:** Safely wipe the slate clean with an optional confirmation prompt to delete all tasks.

---

## 🛠️ How It Works

The program runs inside a continuous loop (`while True`) until manually stopped, serving an easy-to-use menu system:

1. **Add a new task** — Prompts for a string description and appends it to your records.
2. **Display all tasks** — Outputs your current tasks.
3. **Enter a completed task** — Allows you to pop off completed items by selecting a range from 0 to 10.
4. **View total number of tasks** — Prints the dynamic count tracker.
5. **Delete all tasks** — Features a safety prompt (`Yes`/`No`) before purging active entries.

---

## 💻 Code Structure Overview

The application relies on fundamental Python concepts, making it highly customizable:

* **Lists:** Used for data storage (`all_task`) to keep track of individual items.
* **Control Flow:** Utilizes `if-elif-else` blocks to properly route user inputs to their respective operations.
* **Dynamic Range Checking:** Includes safety boundaries to ensure users don't accidently try to complete elements outside the boundaries of the list size.
