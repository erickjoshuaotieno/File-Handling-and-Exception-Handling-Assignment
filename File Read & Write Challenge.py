#Reading the details file
file=open('Details.txt','r')
print(file.read())

#Writing the data from Details to details_modified
file1=open('Details_modified.txt','w')
for data in file:
    file1.write(data)
file1=open('Details_modified.txt','r')
print(file1.read())