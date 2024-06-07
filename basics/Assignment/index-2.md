# Project Assignment: A todo list

## Project Brief

In this project assignment, you will create a simple command-line todo list application using Python. The application will allow users to add, view, and remove tasks from a list. You will implement the core functionality of the todo list and test it with various scenarios.

Todos are stored as a JSON and readed from a file. The file is created if it does not exist.

## Project Requirements

To complete this project, you will need to implement the following features:

1. **Add a Task**: Users can add a new task to the todo list. Each task should have a unique ID, a title, and a description. The ID should be automatically generated based on the existing tasks.
2. **View Tasks**: Users can view all tasks in the todo list. Each task should be displayed with its ID, title, and description.
3. **Remove a Task**: Users can remove a task from the todo list by providing the task ID.
4. **Save and Load Tasks**: The todo list should be saved to a JSON file when the application exits and loaded from the file when the application starts. This ensures that tasks are persisted across different sessions.

## Project Implementation

To implement the todo list application, you can follow these steps:

1. Similar to the previous session (S6), this time you must implement a "Database" monad that receives a path to a JSON as input, and implement the following functions
- `get(key: str) -> Any`: returns the value associated with the key, or None if the key doesn't exist
- `set(key: str, value: Any) -> None`: sets the value associated with the key. Note that this information must be written to the db json immediately
- `delete(key: str) -> None`: deletes the key from the database. Note that this must be deleted in the db json immediately
- `keys() -> List[str]`: returns a list of all the keys in the database
- `values() -> List[Any]`: returns a list of all the values in the database

The monad will be useful for this:

1. We'll make a simple program that receives a sql'ish statement from the user:

```sql
> get 1;
None
> set 1 "Buy milk"; set 2 "Buy bread";
> delete 1;
> get 1; get 2;
Buy milk    Buy bread
> delete 1; delete 2;
> get 1; get 2;
None    None
```

This should compile to the following usage of the monad
```python
db = Database("todos.json")
print(db.get("1"))
db.set("1", "Buy milk").set("2", "Buy bread")
print(db.get("1"), db.get("2"))
db.delete("1").delete("2")
print(db.get("1"), db.get("2"))
```

Make sure to handle exceptions (e.g., the key does not exist when deleting) and to write the changes to the JSON file immediately after every operation. Also, all operations should be asynchronous as well.

## Project Submission

To submit your project, please create a GitHub repository and upload your `todo.py` script along with any other necessary files. You can also include a README file with instructions on how to run the application and use its features.

## Need help?

You can ask me for help, I'll answer any question you might have!

