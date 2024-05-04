import math

# Вероятности символов
probabilities = [0.3, 0.4, 0.2, 0.1]

# Расчет энтропии
entropy = -sum(p * math.log2(p) for p in probabilities if p != 0)

# Расчет избыточности
redundancy = 1 - entropy / math.log2(len(probabilities))

print("Энтропия источника сообщений:", entropy)
print("Избыточность источника сообщений:", redundancy)
