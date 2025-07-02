import os
from google.genai import types

def write_file(working_directory, file_path, content):
  abs_working_dir = os.path.abspath(working_directory)
  abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))
  if not abs_file_path.startswith(abs_working_dir):
      return f'Error: Cannot write "{file_path}" as it is outside the permitted working directory'
  if os.path.exists(abs_file_path):
    return f'Error: File already exists: "{file_path}"'
  try:
    with open(abs_file_path, "w") as f:
      f.write(content)
      return f'Successfully write to "{file_path}" ({len(content)} characters written)'
  except Exception as e:
        return f'Error writing file "{file_path}": {e}'
  
schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes content to a file within the working directory. Creates the file if it doesn't exist.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the file to write, relative to the working directory.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="Content to write to the file",
            ),
        },
        required=["file_path", "content"],
    ),
)