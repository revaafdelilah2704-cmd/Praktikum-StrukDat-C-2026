thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)

  fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)
