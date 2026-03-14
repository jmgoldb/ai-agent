import os
from subprocess import run

def run_python_file(working_directory, file_path, args=None):
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_path = os.path.normpath(os.path.join(working_dir_abs, file_path))

        is_valid_target_path = os.path.commonpath([working_dir_abs, target_path]) == working_dir_abs

        if not is_valid_target_path:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(target_path):
            return f'Error: "{file_path}" does not exist or is not a regular file'
        if not file_path.endswith('.py'):
            return f'Error: "{file_path}" is not a Python file'
        
        command = ["python", target_path]
        if args:
            command.extend(args)

        process = run(command, capture_output=True, text=True, timeout=30)

        output = ""

        if process.returncode:
            output += f"Process exited with code {process.returncode}\n"
        
        if not process.stdout and not process.stderr:
            output += "No output produced"
        else:
            output += f"STDOUT: {process.stdout}\nSTDERR: {process.stderr}"

        return output


    
    
    except Exception as e:
        return f"Error: executing Python file: {e}"