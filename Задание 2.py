import math

def binomial_probability(n, k, p):
    """
    Рассчитывает вероятность получения k успехов в n испытаниях
    с вероятностью успеха p.
    """
    return math.comb(n, k) * (p**k) * ((1-p)**(n-k))

def information_content(p):
    """
    Рассчитывает количество информации в сообщении с вероятностью p.
    """
    return -math.log2(p)

N = 128  # количество генерируемых фотонов
M = 12   # количество зарегистрированных фотонов
p_scatter = 0.3  # вероятность рассеивания фотона
p_register = 0.4  # вероятность регистрации фотона

# Рассчитываем вероятность зарегистрировать M фотонов
probability_registered = sum(binomial_probability(N, m, p_scatter) * binomial_probability(M, m, p_register) for m in range(M+1))

# Рассчитываем количество информации в сообщении
information = information_content(probability_registered)

print("Количество информации в сообщении:", information, "бит")
