"""
Решето Эратосфена
"""
import cProfile


def prime(n):
    sieve = []
    i = 2
    cnt = 0
    while True:
        #  for i in range(2, n + 1):
        #  Ищем делитель среди простых чисел не превышающих делимое
        for j in sieve:
            if i % j == 0:
                break
        else:
            sieve.append(i)
            cnt += 1
        if cnt == n:
            break
        i += 1
    return sieve[n - 1]


# "task_2.prime(50)"
# 100 loops, best of 5: 69.5 usec per loop
# "task_2.prime(100)"
# 100 loops, best of 5: 240 usec per loop
# "task_2.prime(200)"
# 100 loops, best of 5: 853 usec per loop
# "task_2.prime(400)"
# 100 loops, best of 5: 3.71 msec per loop
# "task_2.prime(800)"
# 100 loops, best of 5: 14.1 msec per loop
# "task_2.prime(1600)"
# 100 loops, best of 5: 56.6 msec per loop

# cProfile.run('prime(800)')
# 804 function calls in 0.022 seconds
# 1    0.022    0.022    0.022    0.022 task_2.py:7(prime)
# 800    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
# cProfile.run('prime(1600)')
# 1604 function calls in 0.054 seconds
# 1    0.054    0.054    0.054    0.054 task_2.py:7(prime)
# 1600    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}


def prime_number_resheto(n):
    def primes_resheto(_n):
        primes = [i for i in range(_n)]
        primes[1] = 0

        for i in range(2, _n):
            if primes[i] != 0:
                j = i * 2

                while j < _n:
                    primes[j] = 0
                    j += i
        return [i for i in primes if i != 0]

    # Пробуем найти простое число с номером n в последовательности из n чисел
    k = n
    my_primes = primes_resheto(k)
    # Если не нашли, то увеличиваем количество последовательности чисел до n*2 и пробуем снова. И так пока не найдем.
    while len(my_primes) < n:
        k *= 2
        my_primes = primes_resheto(k)
    return my_primes[n - 1]

# "task_2.prime_number_resheto(50)"
# 100 loops, best of 5: 147 usec per loop
# "task_2.prime_number_resheto(100)"
# 100 loops, best of 5: 324 usec per loop
# "task_2.prime_number_resheto(200)"
# 100 loops, best of 5: 674 usec per loop
# "task_2.prime_number_resheto(400)"
# 100 loops, best of 5: 1.41 msec per loop
# "task_2.prime_number_resheto(800)"
# 100 loops, best of 5: 3.02 msec per loop
# "task_2.prime_number_resheto(1600)"
# 100 loops, best of 5: 13.8 msec per loop
# "task_2.prime_number_resheto(3200)"
# 100 loops, best of 5: 28.1 msec per loop

# cProfile.run('prime_number_resheto(800)')
# 20 function calls in 0.003 seconds
# 1    0.000    0.000    0.003    0.003 task_2.py:49(prime_number_resheto)
# cProfile.run('prime_number_resheto(1600)')
# 24 function calls in 0.016 seconds
# 1    0.000    0.000    0.016    0.016 task_2.py:49(prime_number_resheto)


# print(prime(10))
# print(prime_number_resheto(10))

# Выводы. Самым оптимальным алгоритмом конечно же является решето Эратосфена. Сложность алгоритма Эратосфена O(n).
# Сложность алгоритма prime O(n^2).
