import datetime

def calculate_age(birth_date_str):
    """Calculates the age based on the birth date and current date.

    Args:
        birth_date (str): The birth date in the format "dd-mm-yyyy".

    Returns:
        int: The calculated age.
    """
# make a function called calculate_age, with user input (birth_date_str)
def calculate_age(birth_date_str):

# datetime.datetime fixed         
    birth_date = datetime.datetime.strptime(birth_date_str, "%d-%m-%Y")
    today = datetime.date.today()

#                                             date today       BEFORE <         actual birthday 
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))

# calculation
    return age

# Get user input for birth date
birth_date_input = input("Birth Date (dd-mm-yyyy): ")

# Calculate and print the age and call the function (calculate_age)
age = calculate_age(birth_date_input)

# displays calculation 
print("Your age is:", age)
