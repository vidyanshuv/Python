def leap_year(year):
    """
    This function checks if year entered is a Leap Year or not.
    :param year: Year to be checked for Leap
    :type year: int
    :return: True or False
    """
    year = int(year)
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

print(leap_year(3000))

