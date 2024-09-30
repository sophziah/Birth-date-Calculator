import datetime

def calculate_age(birth_date):
    """Calculates the age based on the birth date and current date.

    Args:
        birth_date (str): The birth date in the format "dd-mm-yyyy".

    Returns:
        int: The calculated age.
    """

    birth_date = datetime.datetime.strptime(birth_date, "%m-%d-%Y")
    today = datetime.datetime.now()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age

if __name__ == "__main__":
    birth_date = input("Birth Date (mm-dd-yyyy): ")
    age = calculate_age(birth_date)
    print("Your age is", age)