import sys

print(f"The name of this file is: {sys.argv[0]}")

print(f"Sys.argv has {len(sys.argv) - 1} arguments")

for i in range (1, len(sys.argv)):
    
    print(f"Argument {i} is {sys.argv[i]}")
    i += 1