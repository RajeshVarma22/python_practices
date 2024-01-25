#this is to open file location of the python

# import sys
# locate_python = sys.exec_prefix
# print(locate_python)

#This is to show the paths set 
import sys
for path in sys.path:
    print(path)