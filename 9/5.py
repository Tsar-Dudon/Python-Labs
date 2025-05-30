import numpy as np
from scipy.stats import multivariate_normal
import time

np.random.seed(42)
D = 3  
N = 10000 
m = np.array([1.0, 2.0, 3.0])  
C = np.array([[2.0, 0.5, 0.3],  
              [0.5, 1.5, 0.2],
              [0.3, 0.2, 2.5]])

X = np.random.randn(N, D)
start_time = time.time()
diff = X - m

inv_C = np.linalg.inv(C)
det_C = np.linalg.det(C)


log_const = -0.5 * D * np.log(2 * np.pi) - 0.5 * np.log(det_C)

quad_form = np.sum(diff @ inv_C * diff, axis=1)

our_logpdf = log_const - 0.5 * quad_form

our_time = time.time() - start_time


start_time = time.time()
scipy_dist = multivariate_normal(m, C)
scipy_logpdf = scipy_dist.logpdf(X)
scipy_time = time.time() - start_time

abs_diff = np.abs(our_logpdf - scipy_logpdf)
max_diff = np.max(abs_diff)
mean_diff = np.mean(abs_diff)

print("Результаты вычислений:")
print(f"Наша реализация заняла: {our_time:.6f} сек")
print(f"SciPy реализация заняла: {scipy_time:.6f} сек")
print("\nСравнение точности:")
print(f"Максимальное расхождение: {max_diff:.5e}")
print(f"Среднее расхождение: {mean_diff:.5e}")
print("\nПервые 5 значений логарифма плотности:")
print("Наши значения:", our_logpdf[:5])
print("SciPy значения:", scipy_logpdf[:5])