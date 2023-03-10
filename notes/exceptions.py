# try means smt that might cause exception
try:
    file = open('file1.txt')
    # lists = [1]
    # print(lists[2])
# do this if there was an exception
# dont use except by itself, it'll ignore all errors
except FileNotFoundError:  # can add as alias_name after the error name to get the error message
    print("We did not find the file")
except IndexError:
    print("Invalid index accessed")
# do this if no exceptions
else:
    print(file.read())
    file.close()
# do this no matter what
finally:
    print("Finished reading file")

# Raising own exceptions
