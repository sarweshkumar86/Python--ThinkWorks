
f = open("harry.txt", "r")  # Open the file 'harry.txt' in read mode ("r")

content = f.read()    # Read the entire content of the file and store it in variable 'content'

print(content)   # Print the content of the file on the screen

f.close()  # Close the file (important to free memory/resources)



# "r" = read mode
# f = file object