import time

my_time = int(input("Süre Giriniz: "))

for x in range(my_time,0,-1):
    print(x)
    time.sleep(1)

print("Süre Doldu!")