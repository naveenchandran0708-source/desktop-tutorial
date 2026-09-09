# Open first file in read mode
with open("file1.txt", "r") as f1:
    data1 = f1.read()
# Open second file in read mode
with open("file2.txt", "r") as f2:
    data2 = f2.read()
# Open third file in write mode and merge
with open("merged.txt", "w") as f3:
    f3.write(data1)
    f3.write("\n") # optional: add a newline between files
    f3.write(data2)
print("Files merged successfully into merged.txt")