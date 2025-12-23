# fastapi-demo

Bigger Applications - Multiple Files

Python 3.10+

file structure
```
.
├── app
│   ├── __init__.py
│   ├── main.py
│   ├── dependencies.py
│   └── routers
│   │   ├── __init__.py
│   │   ├── items.py
│   │   └── users.py
│   └── internal
│       ├── __init__.py
│       └── admin.py
```

how to run
```
pip install fastapi,uvicorn
uvicorn app.main:app
```
