''' # Version 1
import time

for second in range(1, 5+1):
    print(f"{second} Mississippi")
    time.sleep(1)

print("Ready or not, here I come!")

'''

# Version 2
from time import sleep

for second in range(1, 5+1):
    print(f"{second} Mississippi")
    sleep(1)

print("Ready or not, here I come!")
