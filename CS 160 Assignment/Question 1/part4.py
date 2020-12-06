import numpy as np
ndarray = np.ones((5,5))
print("Required Array")
ndarray[1:-1,1:-1] = 0
print(ndarray)