#FILE HANDLING
#Reading in a text file
file = open('test.txt', 'r')
for each in file:
    print (each)


file = open("file.txt", "r")
print (file.read(5))

#Writing in a File
file = open('test.txt','w')
file.write("This is the write command")
file.write("It allows us to write in a particular file")
file.close()

#Append mode
file = open('geek.txt', 'a')
file.write("This will add this line")
file.close()