from sympy import symbols, solve

# Объявляем символьные переменные
k, r = symbols('k r')
N = 128
t = 2

# Формула для количества информационных символов (k)
k_formula = N - 2*t

# Формула для количества проверочных символов (r)
r_formula = t

# Решаем уравнения
k_value = solve(k_formula - k, k)[0]
r_value = solve(r_formula - r, r)[0]

print("Количество информационных символов (k):", k_value)
print("Количество проверочных символов (r):", r_value)

