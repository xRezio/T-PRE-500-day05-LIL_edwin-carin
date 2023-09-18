import time
import random
startingTime = time.time()
liste = [
    random.randint(1,1000000)
    for _ in range (1000000)]

sorted_list = sorted(liste)

print (sorted_list)
duration = time.time() - startingTime
print(duration)
