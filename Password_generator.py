import random

letter_list = ['a', 'B', 'c', 'F', 'x', 'Y', 'u', 'R', 'r', 'L', 'm', 'N', 'J', 'h', 'g', 'w', 'Q', 's', 'p', 'i']
num_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
char_list = ['!', '?', '$', '£', '(', '&', '^', '%', '@', '#']

# ask the user how many letters, number and symbols they would like in their password
nr_letters = int(input('How many letters would you like?'))
nr_nums = int(input('How many numbers would you like?'))
nr_symbols = int(input('How many symbols would you like?'))

# create an empty password list to store its random elements
password = []

for letter in range(1, nr_letters + 1): # +1 needed as last element from range list is not included
    random_letter = random.choice(letter_list)
    password.append(random_letter)


for num in range(1, nr_nums + 1):
    random_num = random.choice(num_list)
    password.append(random_num)

for symbol in range(1, nr_symbols + 1):
    random_symbol = random.choice(char_list)
    password.append(random_symbol)

# shuffle the password list to randomise all its elements
random.shuffle(password)
final_password = ''
for elm in password:
    final_password += elm

print('Your password is: ' + final_password)


