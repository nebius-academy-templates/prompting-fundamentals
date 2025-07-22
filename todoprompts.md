## Advanced Todo App Prompt Patterns

### Pattern 1: The Step-by-Step
```
Add task search functionality to the todo app in 3 steps:
1. First, add a search entry widget to the GUI with live filtering
2. Then, implement search methods in TodoDatabase for title/description matching
3. Finally, integrate search with existing filter system (pending/completed)

Show me each step separately so I can test before proceeding.
```

### Pattern 2: The Alternative Options
```
I need to implement task reminders for my todo app. Please suggest 3 different approaches:
1. Simple popup notifications using tkinter messagebox
2. System notifications using plyer library


For each approach, explain:
- Integration complexity with current codebase
- Dependencies required
- User experience implications
- Implementation in gui.py and database.py
```

### Pattern 3: The Teaching Prompt
```
Implement task import/export functionality for my todo app and explain:
1. Why JSON format is better than CSV for our task structure
2. How to handle data validation during import
3. Best practices for file handling in tkinter applications
4. Error recovery strategies when import fails

Current task structure from database.py:
- id, title, description, completed, created_at, updated_at

I want to understand the design decisions, not just copy code.
```