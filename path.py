import os

# Print the current working directory
print("Current working directory:", os.getcwd())

# List files and directories in the current directory
print("Files and directories in the current directory:")
for item in os.listdir():
    print(item)
