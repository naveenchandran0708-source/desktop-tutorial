src = open("source.txt", "r")
# Open destination file in write mode
dest = open("destination.txt", "w")
# Copying character by character
while True:
    ch = src.read(1) # read one character at a time
    if not ch: # if nothing left, break
        break
dest.write(ch) # write character to destination
# Close both files
src.close()
dest.close()
print("File copied successfully!")