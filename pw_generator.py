import random
import sys
from enum import Enum, auto, unique

# all lower-case alphabet letters
ALPHABET_LETTERS_LOWER_CASE = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
                               'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# all upper-case alphabet letters
ALPHABET_LETTERS_UPPER_CASE = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
                               'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

# special characters
SPECIAL_CHARACTERS = ['!', '$', '%', '&', '@', '_', '-', '.', ':', ',', ';', '=', '?']

# digits
DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# unique constants defining a respective password element
@unique
class PwElement(Enum):
    LOWER_CASE_LETTER = auto()
    UPPER_CASE_LETTER = auto()
    SPECIAL_CHAR = auto()
    DIGIT = auto()

def compute_password(pw_length, nb_lower_case, nb_upper_case, nb_special_chars, nb_digits):
    """
    Returns a randomly generated password which satisfies following conditions:
    - Total password length is equal to 'pw_length'
    - Number of lower case letters is equal to 'nb_lower_case'
    - Number of upper case letters is equal to 'nb_upper_case'
    - Number of special characters is equal to 'nb_special_chars'
    - Number of digits is equal to 'nb_digits'
    """
    # number of occurrences of the respective element in the current password
    cur_nb_of_pw_elements = {PwElement.LOWER_CASE_LETTER : 0, PwElement.UPPER_CASE_LETTER: 0,
                             PwElement.SPECIAL_CHAR : 0, PwElement.DIGIT : 0}

    computed_pw = ''

    while True:
        # choose next pw element randomly
        pw_element = random.choice(list(PwElement))

        if pw_element == PwElement.LOWER_CASE_LETTER:
            # check if total number of lower case letters is already reached
            if cur_nb_of_pw_elements[PwElement.LOWER_CASE_LETTER] < nb_lower_case:
                cur_nb_of_pw_elements[PwElement.LOWER_CASE_LETTER] += 1
                computed_pw += random.choice(ALPHABET_LETTERS_LOWER_CASE)

        elif pw_element == PwElement.UPPER_CASE_LETTER:
            # check if total number of upper case letters is already reached
            if cur_nb_of_pw_elements[PwElement.UPPER_CASE_LETTER] < nb_upper_case:
                cur_nb_of_pw_elements[PwElement.UPPER_CASE_LETTER] += 1
                computed_pw += random.choice(ALPHABET_LETTERS_UPPER_CASE)

        elif pw_element == PwElement.SPECIAL_CHAR:
            # check if total number of special characters is already reached
            if cur_nb_of_pw_elements[PwElement.SPECIAL_CHAR] < nb_special_chars:
                cur_nb_of_pw_elements[PwElement.SPECIAL_CHAR] += 1
                computed_pw += random.choice(SPECIAL_CHARACTERS)

        elif pw_element == PwElement.DIGIT:
            # check if total number of digits is already reached
            if cur_nb_of_pw_elements[PwElement.DIGIT] < nb_digits:
                cur_nb_of_pw_elements[PwElement.DIGIT] += 1
                computed_pw += random.choice(DIGITS)

        # stop loop if password was fully generated
        if len(computed_pw) == pw_length:
            break

    return computed_pw

def print_help():
    print("Usage: pw_generator <len> <#low> <#up> <#spec> <#dig>")
    print("--- <len>: total password length")
    print("--- <#low>: number of lower case letters")
    print("--- <#up>: number of upper case letters")
    print("--- <#spec>: number of special characters")
    print("--- <#dig>: number of digits")


if __name__ == '__main__':
    if (len(sys.argv) != 6): # 6 because [0] is script name
        print("Error: Number of given input parameters ({}) does not match expected one (6)".format(len(sys.argv)))
        print_help()
        sys.exit(1)

    pw_length = int(sys.argv[1])
    nb_lower_case = int(sys.argv[2])
    nb_upper_case = int(sys.argv[3])
    nb_special_chars = int(sys.argv[4])
    nb_digits = int(sys.argv[5])

    # length check
    sum_pw_elements = nb_lower_case + nb_upper_case + nb_special_chars + nb_digits
    if pw_length != sum_pw_elements:
        print("Error: Total number of password elements ({}) do not match expected password length ({})!".format(sum_pw_elements, pw_length)) 
        print_help()
        sys.exit(1)
    
    print("===================================================")
    print("Generating a password under following conditions:")
    print("- Total length: {}".format(pw_length))
    print("- Number lower case letters: {}".format(nb_lower_case))
    print("- Number lower upper letters: {}".format(nb_upper_case))
    print("- Number special characters: {}".format(nb_special_chars))
    print("- Number of digits: {}".format(nb_digits))
    print("===================================================")

    computed_password = compute_password(pw_length, nb_lower_case, nb_upper_case, nb_special_chars, nb_digits)

    print("Computed password: {}".format(computed_password))
