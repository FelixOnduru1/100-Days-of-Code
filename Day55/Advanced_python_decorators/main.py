# This section covers how you can pass arguments into decorator's wrapper function using args and kwargs

# Consider this class

class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False


# What if we want to create a decorator
# that can be used to decorate any function in our website
# that requires user to be logged in.
# This is where the advanced decorator comes in.

# Here we create a decorator passing in args and kwargs into the wrapper
# then using the position of the argument in the function being wrapped
# i.e. create_blog_post(user),
# user has a position of 0 hence args[0],
# anytime we call args[0] = user.
# With this method we are able to pass in arguments into the decorator


def is_authenticated_decorator(function):
    def wrapper(*args, **kwargs):
        if args[0].is_logged_in:
            function(args[0])
    return wrapper

# Now consider this function that takes an instance of the class User.
# It then uses this instance to tap into the name by user.name and print the statement


@is_authenticated_decorator
def create_blog_post(user):
    print(f"This is {user.name}'s new blog post")


new_user = User("Felix")
new_user.is_logged_in = True
create_blog_post(new_user)


