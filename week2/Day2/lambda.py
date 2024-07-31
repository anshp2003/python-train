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