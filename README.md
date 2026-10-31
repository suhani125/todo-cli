# Todo CLI

A simple command-line to-do list manager written in Python. Tasks are saved in a local `tasks.json` file.

## Features

- Add, list, complete, and delete tasks
- Persistent storage using JSON
- No external dependencies (pytest only for tests)

## Requirements

- Python 3.8+

## Usage

```bash
python todo.py add "Buy groceries"
python todo.py add "Finish homework"
python todo.py list
python todo.py done 1
python todo.py delete 2
python todo.py clear
```

Example output:

```
[x] 1. Buy groceries
[ ] 2. Finish homework
```

## Run tests

```bash
pip install -r requirements.txt
pytest
```

## License

MIT
