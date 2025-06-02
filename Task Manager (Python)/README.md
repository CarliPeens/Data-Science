# 📝 Task Manager Application

This is a simple terminal-based Task Manager written in Python. It allows users to log in, assign tasks, view their own or all tasks, mark tasks as completed, and generate reports. It also includes role-based access (admin vs regular user) and validates date inputs.

---

## 🚀 Features

- User login system with credential validation
- Admin and regular user roles
- Add tasks with due dates
- View all tasks or only your own
- Mark tasks as complete or edit them
- Delete tasks
- View completed tasks
- Generate and view detailed task reports
- Input validation (including due date format)
- Dynamic admin role management via `user.txt`

---

## 🧾 File Structure

```
├── task_manager.py       # Main application file
├── user.txt              # Stores usernames, passwords, and admin status
├── tasks.txt             # Stores all assigned tasks
├── task_overview.txt     # Automatically generated task summary
├── user_overview.txt     # Automatically generated user summary
```

---

## 📥 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/task-manager.git
cd task-manager
```

### 2. Prepare Initial Files
Create a `user.txt` file with default credentials. For example:
```
admin, adm1n, True
user1, password1, False
```

Create an empty `tasks.txt` file:
```
touch tasks.txt
```

### 3. Run the Program
```bash
python task_manager.py
```

---

## 👤 User Roles

- **Admin users** can:
  - Register new users
  - Delete tasks
  - Generate reports
  - View statistics
  - Do everything regular users can do

- **Regular users** can:
  - Add tasks
  - View all tasks
  - View and edit their own tasks
  - Exit the program

---

## 🗃️ Example Input

```
Enter username: admin
Enter password: adm1n
Login successful! Welcome, admin.

Select one of the following options:
r - register a user
a - add task
va - view all tasks
...
```

---

## ✅ Due Date Format

All due dates must be entered in the format:  
`DD Mon YYYY` (e.g., `25 Oct 2025`)

Invalid formats are rejected automatically.

---

## 📊 Reports

When the admin selects **"generate reports"**, two files are created:
- `task_overview.txt`: Stats on tasks (complete, incomplete, overdue)
- `user_overview.txt`: Stats per user (assigned, completed, overdue)

These can be viewed from the **"display statistics"** menu.

---

## 🛠 Future Improvements (Optional Ideas)

- Password encryption
- Task filtering by status or due date
- Export tasks as CSV
- GUI interface using Tkinter or PyQt

---

## 📄 License

This project is open-source and available under the MIT License.
