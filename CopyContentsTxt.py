#Write a python program to read a file and write the contents to another file
with open("file1.txt", "r") as input:
	with open("file2.txt", "w") as output:
		for line in input:
			output.write(line)
print ("file1.txt has been written onto new file named file2.txt")