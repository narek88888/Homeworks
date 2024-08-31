# 14-4 File Splitting:
# Develop a Python Function that reads a large text file (input.txt) and splits it
# into smaller files, each containing a specified number of lines. Function paramis
# ter the number of lines per file. Generate multiple output files (output1.txt,
# output2.txt, etc.).



with open('file.for.14-4.txt', 'r') as f_1 :
    
     x = f_1.read()
     y = x.split()
    

with open('new.file.for.14-4.txt', 'w') as f_2:
     for i in y:
         if len(i) > 2:
          f_2.write(i)
            






