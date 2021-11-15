# Functions go here

# Puts series of symbols at start and end of text
def statement_generator(text, decoration):
     decor = decoration * 5
     print(decor,text,decor)


# displays instructions / information
def instructions():
    statement_generator("Instructions / Information", "=")
    print()
    print("Please input a factor (image / text / integer)")
    print()
    print("This program assumes something")
    print()
    print("Completye as many calculations as necessary, pressing <enter> at the end of each calculation ot any key to quit")
    print()
    return ""


# checks input is a number more than a given value
def num_check(question):
    valid = False

    while not valid: 

        error = "Please enter a number more than "
        "(or equal to) {}".format(low)

        try:


# gets factors, returns a sorted list


# main routine goes here

# heading
statement_generator("Factors Calculator", "-")

# Display instructions if user has not used the program before
first_time = input("Press <enter> to see the instructions or any key to continue")

if first_time == "":
    instructions()

# Loop to allow multiple per session
keep_going = ""
while keep_going == "":

    comment = ""

    # ask user for number to be factored...
    var_to_factor = num_check("Number? ")

    if var_to_factor != 1:
        factor_list = get_factors(var_to_factor)
        comment = "One is UNITY! It only has one factor. Itself :)"

    # Comments for squares / primes
    if len(factor_list) == 2:
        comment = "{} is a prime number.".format(var_to_factor)
    elif len(factor_list) % 2 ==1:
        comment = "{} is a perfect square".format(var_to_factor)

    # output factors and comment

    # Generate heading
    if var_to_factor == 1:
        heading = "One is special..."

    else:
        heading = "Factors of {}".format(var_to_factor)

    # Output factors and comment
    statement_generator(heading, "*")
    print()
    print(factor_list)
    print(comment)

    print()
    keep_going = input("Press <enter> to continue or any key to quit ")
    print()

print()
print("Thank you for using the factors calculator")
print()


