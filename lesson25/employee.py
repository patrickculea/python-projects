class employee:
    def __init__(self):
        print("Employee created.")
    def __del__(self):
        print("Destructor called")

def create_obj():
    print("Making Object")
    employee_object = employee()
    import time
    time.sleep(3)
    print("The function has ended.")
    return employee_object

print("Calling create_obj() function")
obj = create_obj()
print("The program has ended.")

