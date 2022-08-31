import os
n = raw_input("Enter file name:   ")
c = raw_input("Delete file?:  ")
if c == "yes":
    os.remove(n)
    print("File succesfully deleted!")
elif c=="No":
    print("File not deleted")
else:
    print("Invalid command!")
    

