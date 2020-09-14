def check_docstr():
    """This function returns a closure to calculate the length of docstring"""
    free_variable = 50
    def inner(func):
        """This function calculate the number of character present in a docstring of a function"""
        doc_chr = func.__doc__ 
        if doc_chr == None:
            return "oops!! You didnot mention docstring"
        else:
            if len(func.__doc__) > free_variable:
                return "Yes, The docstring has more than 50 Character"
            else:
                return "The docstring does not have more than 50 Character"
    return inner

if __name__==if __name__ == "__main__":
    checking_docstring = check_docstr()
    def my_func():
        """This function is created to calculate the number of characters are used to the function or number of characters are used in docstring"""
        return 0
    checking_docstring(my_func)