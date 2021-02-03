def format_name(f_name, l_name):
    """Takes the first and last name and formats it
    to return the title case version of the name."""
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    return f"{formatted_f_name} {formatted_l_name}"


formatted_string = format_name(f_name="felix", l_name="OMONDI")
print(formatted_string)
