def validate_args(func):
    def wrapper(*args):
        if len(args) < 1:
            return "Not enough arguments"
        elif len(args) > 1:
            return "Too many arguments"

        arg = args[0]

        if not isinstance(arg, int):
            return "Wrong types"

        if arg < 0:
            return "Negative argument"

        return func(*args)

    return wrapper

@validate_args
def example_function(x):
    return x

# Примеры использования:

result_1 = example_function(42)
print(result_1)  

result_2 = example_function()  
print(result_2)  

result_3 = example_function(1, 2) 
print(result_3)  

result_4 = example_function("abc")  
print(result_4) 

result_5 = example_function(-5)  
print(result_5)
