add= lambda x,y: x+y
a=add(3,10)
print(a)


"Nested Lambda"

add=lambda x=10 : (lambda y : x+y)
a=add()
print(a(100))

"passing lambda func to another func"


def show(a):
    print(a(10))


show(lambda x : x)    


"returning lambda func from a func"
def show():
    y=10
    return(lambda x :x+y)
a=show()
print(a(10))





numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)  # Output: [1, 4, 9, 16, 25]



numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # Output: [2, 4, 6, 8, 10]





from functools import reduce

numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)
print(product)  # Output: 120



from functools import reduce

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Step 1: Square each number
squared = map(lambda x: x ** 2, numbers)

# Step 2: Filter out odd squares
even_squares = filter(lambda x: x % 2 == 0, squared)

# Step 3: Sum the remaining squares
sum_of_even_squares = reduce(lambda x, y: x + y, even_squares)

print(sum_of_even_squares)  # Output: 220 (4 + 16 + 36 + 64 + 100)

