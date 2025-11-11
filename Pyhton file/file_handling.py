#with open('nebulaa.txt', 'a') as w:
#     w.write('\nNebulaa is Startup Compnay')



# Operation	Function / Method
# Open file	   open("file.txt", "r")
# Read file	   .read(), .readline(), .readlines()
# Write file	.write(), .writelines()
# Append file	"a" mode
# Close file	.close()
# Auto-close	 with open(...) as f:
# Work with JSON	json.load(), json.dump()
# Work with CSV	 csv.reader(), csv.writer()
# Excel	         pandas.read_excel()



# Mode	Description
# 'r'	    Read-only (default)
# 'w'	    Write (overwrites)
# 'a'	    Append
# 'r+'	Read and write
# 'b'	    Binary
# 't'	    Text (default)

# f = open("example.txt", "w")
# f.write("Hello, world!")  # Overwrites content
# f.close()

# Appending
# f = open("example.txt", "a")
# f.write("\nNew line")
# f.close()

# Edit file line-by-line
# with open("example.txt", "r") as f:
#     lines = f.readlines()

# lines[1] = "Updated line\n"

# with open("example.txt", "w") as f:
#     f.writelines(lines)\
    
#Working with Different File Extensions
#a) .txt (Text File)
# with open("example.txt", "r") as f:
#     print(f.read())

#b) .csv

# import csv
# with open("data.csv", newline='') as f:
#     reader = csv.reader(f)
#     for row in reader:
#         print(row)

#c) .json
# import json
# with open("data.json") as f:
#     data = json.load(f)
#     print(data)

#d) .xlsx
# import pandas as pd
# df = pd.read_excel("data.xlsx")
# print(df.head())


