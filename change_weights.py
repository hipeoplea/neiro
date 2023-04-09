import numpy as np

x = np.array([[1, 1, 0.3], [1, 0.4, 0.5], [1, 0.7, 0.8]])
y = np.array([1, 1, 0])
w = np.array([0, 0, 0])
for i in range(len(x)):
  p = int(w.T @ x[i] > 0)
  if p != y[i]:
    w = w - x[i] if p else w + x[i]
print(*w.round(2), sep=',')