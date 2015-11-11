import sys
x = len(sys.argv)
if x == 2:
    print(sys.argv[1])
else: 
    print("usage: python3 solution.py PARAM")
