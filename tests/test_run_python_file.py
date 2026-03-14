from functions.run_python_file import run_python_file

print(run_python_file("calculator", "main.py"))

print(run_python_file("calculator", "main.py", ["3 + 5"]))

print(run_python_file("calculator", "tests.py"))

print(run_python_file("calculator", "../main.py")) # Should Return Error

print(run_python_file("calculator", "nonexistent.py")) # Should Return Error

print(run_python_file("calculator", "lorem.txt")) # Should Return Error