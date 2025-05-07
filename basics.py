
print("+ P1. save this to numbers, print the 3rd item in the list [10, 20, 30, 40]")
numbers = [10,20,30,40]
print(numbers)

print("+ P2. what happens in this?")
# x= 5
# x= x + 2
# y = 2
# print(x+y)
x=5
x=x+2
y=2
print(x+y)

print("+ P3. print all the `numbers` using `for`.")
for sans in numbers:
  print(sans)
  

print("+ P4. create a code to do this")
# 1 square is 1
# 2 square is 4
# 3 square is 9
# 4 square is 16

numbers=[1,2,3,4]
for jojo in numbers:
  print(f"{jojo} square is {jojo*jojo}")



print("+ P5. print a list of words [“apple”, “banana”, “orange”]")
A= ["superhero","powerranger","ninja"]
for jojo in A:
    print(jojo)


# -- Level 2

print("+ P6. print the price of each item with tax.")
# P6. You have a list of items prices [100, 200, 300]. You need to pay 18% GST. print the price of each item with tax.
price=[100,200,300]
for pp in price:
    x=pp+0.18*pp
    print(x)

## Learn conditions

x=10 # assignment
if x == 10: # condition
    print("x is great")

# conditions
# == is equals
# > greater than
# < less than
# != not equals

# -- Level 3

print("+ P7. write code to print numbers from 1 to 10 but skip 5.")
A=[1,2,3,4,5,6,7,8,9,10]
for S in A:
  if S == 5:
    continue # skips below logic
  
  print(S)


print("++ some more examples")
A= ["superhero","powerranger","ninja"]
for jojo in A:
    if jojo == "superhero":
       print("jumps a lot")
    print(jojo)

print("+ Learn. functions")

def f(x):
  print(x)
  return x

f(x)

# function for f(x) = x+1
# def name(parameters):
#    logic
#    return output

# purpose, increase the input value by 1
def f1(x):
  # logic
  # x = x + 1
  # x = x * x - 2 * x + 1
  # for i in [1, 2, 3, 4]:
  #   x = x + i
  x=x+1
  return x

output = f1(9)
print(output)

# f(x,y) = x2 + 5y
def sama(x,y):
  # let us assume a = x2, b = 5y
  a = x*x
  b = 5*y
  return a+b

print(sama(1,2))
