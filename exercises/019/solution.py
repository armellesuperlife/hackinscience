import sys
x = len(sys.argv)
a = sys.argv[2]
b = sys.argv[3]
if x > 2:
    print int(a) + int(b)
else:
    print("usage: python3 solution.py OP1 OP2")
