# Вычислить число Пи c заданной точностью d
# Пример: при d = 0.001,  c= 3.141


def Pi(precision: float) -> float:
    pi = 3.0
    i = 2
    while True:
        pi += (-1 if i % 4 == 0 else 1) * 4 / (i * (i + 1) * (i + 2))
        k = abs(4 / (i * (i + 1) * (i + 2)) - 4 / (i + 2 * (i + 3) * (i + 4)))
        if k < precision:
            return pi
        i += 2


print(Pi(0.001))