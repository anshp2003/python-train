
def test_sequence():
    num = 0
    while num < 10:
        yield num
        num += 1
for i in test_sequence():
       print(i, end=",")

def data_source():
    for i in range(100):
        yield i

def filter_even_numbers(data):
    for number in data:
        if number % 2 == 0:
            yield number

def square_numbers(data):
    for number in range(10):
        yield number * number

pipeline = square_numbers([])
for result in pipeline:
    print(result)


def countdown(start):
    while start > 0:
        yield start
        start += 1

for number in countdown(5):
    print(number)