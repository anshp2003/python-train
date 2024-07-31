def read_large_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line.strip()  # Use strip() to remove any trailing newline characters

# Example usage
file_path = 'C:\\Users\\hp\\Desktop\\ansh\\python training\\week2\\Day5\\ansh.txt'  # Replace with the path to your large file

for line in read_large_file(file_path):
    print(line)  # Process each line as needed
