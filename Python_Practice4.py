#WHILE LOOP
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

#WHILE ELSE
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")

#FOR LOOPS
for x in range(6):
  print(x)
else:
  print("Finally finished!")

#NESTED FOR
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)