import random

horror_message = random.randint(3, 20)
print(horror_message)

horror_message = int(input("введите число с левых ворот "))  # программа на Вашем смартфоне начинается отсюда
parole = []
for i in range(1, horror_message):
    for j in range(1, horror_message):
        if horror_message % (i + j) == 0:
            if i > j:
                continue
            parole = [i, j]

            print(parole)
