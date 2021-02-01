# This is just an example of a simple function.
def greet():
    print("Hello.")
    print("How are you doing?")
    print("My name is Felix's A.I.")


greet()

# Now let's create a function with an input


def greet_with_name(username):
    print(f"Hello {username}.")
    print(f"How are you doing, {username}?")
    print("My name is Felix's A.I.")


username_entry = input("What is your name?\n")
greet_with_name(username_entry)

# Now, we look at a function with more than one parameter


def greet_with(username, activity):
    print(f"Hello {username}.")
    print(f"How are you doing, {username}?")
    print("My name is Felix's A.I.")
    print(f"Let's {activity}, {username}.")


username_entry = input("What is your name?\n")
activity_entry = input("What do you want us to do together?\n").lower()
greet_with(username_entry, activity_entry)


# Functions with keyword arguments

def greet_with(username, activity):
    print(f"Hello {username}.")
    print(f"How are you doing, {username}?")
    print("My name is Felix's A.I.")
    print(f"Let's {activity}, {username}.")


username_entry = input("What is your name?\n")
activity_entry = input("What do you want us to do together?\n").lower()
greet_with(activity=activity_entry, username=username_entry)