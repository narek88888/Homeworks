# 3. Write a python program that will raise an exception (Invalid
# File) if text file contents first symbol is starting with number

with open("file.for.16-3.txt", "r") as f :
    x = f.read()
    if x[0].isdigit() :
        raise "Expection"
    
