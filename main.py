Hobbies = ["I love programming in Python!", "I enjoy hiking in the mountains.", "Reading science fiction novels is a passion of mine."]

file_path = "C:\\Users\\dhara\\OneDrive\\Desktop\\example.txt"

try:
    with open(file_path,"a") as file:
       for hobby in Hobbies:
        file.write(hobby + "\n")
        print(f"The text has been written to '{file_path}' successfully.")

except FileExistsError:
    print(f"The file '{file_path}' already exists. Please choose a different name or delete the existing file.")