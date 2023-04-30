# Mark Bulmer - CIS 115 - 7-26-2021

# Final Project - A Ten and Thirteen Digit ISBN

# Main function.
def main():
    display()

# Display the menu.
def display():
    print('Python ISBN Conversion Menu')
    print('1. Verify the check digit of an ISBN-10')
    print('2. Verify the check digit of an ISBN-13')
    print('3. Convert an ISBN-10 to an ISBN-13')
    print('4. Convert an ISBN-13 to an ISBN-10')
    print('5. Exit')
    
    # Obtain user selection in the menu.
    selection = input('Please enter your selection:')
    # Ten digit inputs.
    if selection == '1' or selection == '3':
	    number = input('Enter a 10 digit number with no dashes:')
	    while len(number) != 10:
		    print('Invalid entry, please try again.')
		    number = input('Enter a 10 digit number with no dashes:')
		    print(format(number))

	    if selection == '1':
		    print(isbn_10_check(number))
	    else:
		    print(conversion_13(number))
		    
    # Thirteen digit inputs.
    elif selection == '2' or selection == '4':
		
	    number = input('Enter a 13 digit number with no dashes:')
	    while len(format(number)) != 13:
		    print('Invalid entry, please try again.')
		    number = input('Enter a 13 digit number with no dashes:')
		
	    if selection == '2':
		    print(isbn_13_check(number))
	    else:
		    print(conversion_10(number))
		    
    # Exit
    elif  selection == '5':
	    return
	
    # Redisplay menu.
    display()
    
# Take ISBN number from user input and add them together to find remainder and determine if the entry is valid.
def isbn_10_check(number):
    check = 0
    for y in range(len(number)):
	    x = number[y]
	    z = int(x)
	    check += (y+1) * z
	    c = check % 11
	
    print('This ISBN has a remainder of', str(c))
    if c == 0:
	    print('The check digit of this ISBN is valid.')
    else: 
	    print('The check digit of this is invalid.')

# Convert a ten digit ISBN into a thirteen digit ISBN.
def conversion_13(number):
    isbn13 = '978' + number[:-1]
    x = str(isbn13)
    check = 0
    for y in range(len(x)):
	    if y % 2 == 0:
		    check += int(x[y])
	    else:
		    check += int(x[y]) * 3
    check = check % 10

    converted = str(isbn13) + str(check)
    print('Your converted ISBN number is', converted)

# Determine the remainder to find validity of check digit.
def isbn_13_check(number):
    x = str(number)
    check = 0
    for y in range(len(x)):
	    if y % 2 == 0:
		    check += int(x[y])
	    else:
		    check += int(x[y]) * 3
    check = check % 10

    print('This ISBN has a remainder of', check)
    if check == 0:
	    print('The check digit of this ISBN is valid.')
    else: 
	    print('The check digit of this ISBN is invalid.')

# Convert a thirteen digit ISBN into a ten digit ISBN.
def conversion_10(number):
    if number[:3] == '978':
	    x = str(number[3:-1])
    else :
	    raise 'ISBN cannot be converted.'
		
    check = 0
    for y in range(len(x)):
	    if y % 2 == 0:
		    check += int(x[y])
	    else:
		    check += int(x[y]) * 3
    check = 10 - (check % 10)	
	
    converted = str(x) + str(check)
    print('Your converted ISBN number is', converted)

main()
