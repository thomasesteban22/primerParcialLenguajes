import time

sum = 0
start = time.time()
for i in range(1, 10000001):
    sum += i
end = time.time()

time_taken = end - start
print(f"Suma: {sum}")
print(f"Tiempo tomado: {time_taken} segundos")
