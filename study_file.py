
hello_file = open("requirements.txt", "r")
print(hello_file.read())

write_hello_file = open("hello.txt", "w")
for i in range(5):
    write_hello_file.write("hello\n")
