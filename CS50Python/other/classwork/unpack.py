#*args is positional, variable length of arguments.  **kwargs are keyword args with key value
def f(*args, **kwargs):
    print("Positional:", kwargs)

f(first= "yeet", second= "yoot" )
