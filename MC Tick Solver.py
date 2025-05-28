import time
import os
print("1. Ticks to Seconds")
print("2. Seconds to Ticks")
while True:
 try:
  x = int(input())
  break
 except:
  print("That's not a valid Input!")

import os
os.system('cls')
if x == 1:
  print("Insert Minecraft Ticks:")
  y = input()
  result = (int(y) * 5) / 100
  os.system('cls')
  print(str(result) + " Seconds")
elif x == 2:
  print("Insert Seconds:")
  y = input()
  result = int((int(y) * 100) / 5)
  os.system('cls')
  print(str(result) + " Game Ticks")
else:
 print("That's not a valid Input!")
k = input()