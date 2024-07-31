class stringRepeater:

    def __init__(self,string):
        self.string=string

    def __mul__(self,times):
        return self.string*times 

    # def __str__(self):
    #     return self.string   
    
obj=stringRepeater(10)
print(obj*3)