# A n*n
# - собств знач
# - умножение матриц

import numpy as np

matr1 = np.random.rand(2,2)
matr2 = np.random.rand(2,2)

print("xz  ",np.linalg.eig(matr1))
print("eig ",np.linalg.eigvals(matr1))
print("eig ",np.linalg.eigvalsh(matr1))
print("ymn ",matr1@matr2)
print("ymn ",matr1*np.random.rand(2))
print("shp ",(matr1*np.random.rand(2)).shape)


