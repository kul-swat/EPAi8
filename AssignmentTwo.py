def fibonacci():
    """This function returns a closure, which is calculating the fibonacci series"""
    a,b = 0,1
    counter = 0
    def fib():
        """This function returns the next fibonacci number"""
        nonlocal counter
        nonlocal a,b
        if counter == 0:
            return_value = 0 
        elif counter ==1:
            return_value = 1
        else:
            c = a+b
            a,b = b,c
            return_value = c
        counter += 1
        return return_value
    return fib

if __name__ == "__main__":
    fibonacci_value = fibonacci()
    fibonacci_value()
