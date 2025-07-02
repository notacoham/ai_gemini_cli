# AI CLI Python

A command-line interface for interacting with AI models (currently supporting Google's Gemini) directly from your terminal. This tool allows you to have conversations with AI, manipulate files, and execute Python code through natural language commands.

## ⚠️ Warning

**This is a toy/experimental implementation** of an AI CLI tool, similar to but not as sophisticated as official Claude or Gemini CLI tools. It should be used with caution and is not intended for production use. The tool has limited safety checks and may have unexpected behaviors.

## Features

- Interactive conversations with AI models
- File content reading and manipulation
- Python code execution through natural language
- Basic calculator functionality
- File system navigation within working directory

## Available Functions

The CLI has access to several core functions for file and directory manipulation within its working directory:

### File Operations
- **Read File Content**: Can read and return the contents of any text file (with character limit protection of 10,000)
- **Write File**: Can create new files and write content to them (prevents overwriting existing files)
- **Execute Python Files**: Can run Python files and capture their output (with a 30-second timeout)

### Directory Operations
- **List Directory Contents**: Can list files and directories, including their sizes and types
- **Working Directory Protection**: All operations are restricted to the working directory for safety
- **Path Resolution**: Handles both relative and absolute paths within the working directory

### Safety Features
- Prevents access to files outside the working directory
- File size limits for reading operations
- Execution timeouts for Python files
- Basic error handling and reporting

## Getting Started

1. Install the required dependencies:
```bash
pip install -r requirements.txt
```

2. Set up your environment variables (you'll need a Google API key for Gemini)

## Example Commands

Here are some commands you can try:

```bash
# Start a basic conversation
python main.py "What is the current weather?"

# Ask it to create a Python function
python main.py "Create a function that calculates the fibonacci sequence"

# Read and analyze a file
python main.py "What does the content of functions/get_file_content.py do?"

# Use the calculator
python main.py "Calculate 15 * 45 + 123"

# Create or modify files
python main.py "Create a new Python file that implements a binary search tree"
```

## Limitations

- Limited error handling
- No persistent memory between conversations
- Basic file system safety checks
- No support for complex programming tasks
- Limited to text-based interactions