from functions.get_file_content import get_file_content

def test():
    # Test reading a regular file
    result = get_file_content("calculator", "main.py")
    print("Result for main.py:")
    print(result)
    print("")

    # Test reading a file in a subdirectory
    result = get_file_content("calculator", "pkg/calculator.py")
    print("Result for pkg/calculator.py:")
    print(result)
    print("")

    # Test reading a file outside working directory
    result = get_file_content("calculator", "/bin/cat")
    print("Result for /bin/cat:")
    print(result)
    print("")

if __name__ == "__main__":
    test()