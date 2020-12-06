
import numpy as np
ndarray  = np.random.randint(1, 27, size=(3, 3, 3))
print(ndarray )

print("Sum of all elements : \n",np.sum(ndarray))
print("Sum of each column: \n",np.sum(ndarray, axis=1))
print("Sum of each row: \n",np.sum(ndarray, axis=2))
