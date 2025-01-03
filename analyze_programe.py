import subprocess
import sys
import os
import pylint

def analyze_file(file_path):
    try:
        result = subprocess.run(['pylint', file_path], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return e.output
    except FileNotFoundError:
        return "Error: Pylint is not installed or not found in the system path."
    except Exception as e:
        return f"An unexpected error occurred: {e}"

if __name__ == '__main__':
    file_to_analyze = input('Enter the path to the Python program: ')  # Prompt user for file path

    if not file_to_analyze.endswith('.py'):
        print("Error: The file must be a Python (.py) file.")
        sys.exit(1)

    try:
        with open(file_to_analyze, 'r') as f:
            pass
    except FileNotFoundError:
        print(f"Error: The file '{file_to_analyze}' does not exist.")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred while accessing the file: {e}")
        sys.exit(1)

    analysis_result = analyze_file(file_to_analyze)

    print(f"Analysis results for {file_to_analyze}:")
    print(analysis_result)