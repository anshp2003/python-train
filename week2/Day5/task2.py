# def fab(n):
#     a,b = 0,1
#     for _ in range(n):
#         yield a
#         a,b=b,a+b

# # num=10
# f1=fab(10)
# for fib in f1:
#     print(fib)        


# def list1(n):
#     x=[]
#     for i in range(0,100):
#         yield n+i
#         x.append(i)
    
# l=list1(1)
# for num in l:
#     print(num)


def even_numbers_generator(limit):
    num = 0
    while num < limit:
        yield num
        num += 2

# Example usage
for even in even_numbers_generator(10):
    print(even)
