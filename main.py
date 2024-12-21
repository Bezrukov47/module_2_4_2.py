numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for num in numbers: # Проверяем/перебираем очередной номер в numbers
    is_prime = True # Считаем, что число простое
    if num < 2: # Пропускаем 1
        is_prime = False
    for i in range(2, num): # Проверяем делители от 2 до num-1
        if num % i == 0:  # Если число делится на i без остатка
            is_prime = False  # То это не простое число
            break  # Выходим из цикла, если делитель найден
    if is_prime: # Добавляем число в соответствующий список
        primes.append(num)
    else:
        not_primes.append(num)
print("Простые числа:", primes)
print("Непростые числа:", not_primes)




