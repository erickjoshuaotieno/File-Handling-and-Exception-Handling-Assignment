# try block checks for the file name
try:
    fileName=input("Enter file name: ")
    file=open(fileName,'r')
    print(file.read())

#except block returns an error when file is not found
except:
    print("Error! File not found!!!")

#always executed, closes the file
finally:
    file.close()
