import sys
x = len(sys.argv)
if x > 1:
    print(int(sys.argv[1]) - int(sys.argv[2]))
else:
    print("usage: python3 solution.py OP1 OP2")
