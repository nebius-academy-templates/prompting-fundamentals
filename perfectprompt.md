**Perfect Prompt**:

I'm enhancing my Python todo application that currently handles basic task management with tkinter GUI and SQLite database.

Current structure:

- Tasks table: id, title, description, completed, created_at, updated_at
- GUI: Task list, add/edit forms, filter buttons
- Database operations: CRUD operations through TodoDatabase class

Requirements:

1. Add due date field to tasks with date picker widget
2. Add priority levels (Low, Medium, High, Critical) with colour coding
3. Sort tasks by priority and due date
4. Add overdue task highlighting in red
5. Add priority filter dropdown alongside existing status filters
6. Add task statistics (total, completed, overdue, by priority)

Technical constraints:

- Keep existing Python/tkinter/SQLite stack
- Maintain current TodoDatabase class structure
- Use existing GUI layout patterns from gui.py
- Follow NZ date format (DD/MM/YYYY)
- Keep database operations in separate methods
- Maintain backward compatibility with existing data

Please provide:

1. Updated database schema with migration script
2. Modified TodoDatabase class methods
3. GUI components for date picker and priority selection
4. Updated task display logic with colour coding
5. Error handling for date validation

Files to modify:

- database.py: Add new columns and methods
- gui.py: Add new widgets and update display logic
- main.py: Any initialization changes needed

Ask clarifying questions if anything is unclear about the current implementation. 