#!usr/bin/env python3
# Created by: Ishami Sebgoya
# Created on: October 2023
# This program checks if user guessed random number
import random
num = random.randint(0, 9)
print(num)
if num == 5:
    print("You have guessed correct")
    print("Congratulations")
else:
    print("Sorry, you have guessed incorrect.")
