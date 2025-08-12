#Input with parameters

import sys
print("Jenkins build using parameters !")
X_VALUE = int(sys.argv[1])
Y_VALUE = int(sys.argv[2])
print("Multiply= ", (X_VALUE * Y_VALUE))