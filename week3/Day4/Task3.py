class resource:
    def __enter__(self):
        print("locking the resource")

    def __exit__(self,exc_type, exc_val, exc_tb):
        print('releasing the resource')

with resource():
    print('resource is in use')            