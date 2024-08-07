try:
    with open("ansh.txt","r") as file:
        print(file.read())
except FileNotFoundError:
        print("Error: The file 'ansh.txt' was not found. Please check the file name and try again.")
        