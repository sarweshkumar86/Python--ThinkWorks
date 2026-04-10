# Append to an existing file called John Doe.txt 
# It should add data about John Doe's Hometown

f = open("John Doe.txt", "a")

string = '''
John Doe initially lived in Phoenix, Arizona. He is a very nice guy
'''
f.write(string)

f.close()

# w = overwirte (replace the old data with new content)
# a= add new data with existing content