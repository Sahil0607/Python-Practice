childerParty = ['Paki', 'Sahil', 'Akshar', 'Akshit']

# This is how we can access perticular member of list
print(childerParty[2])

# Give us 3rd member of list
i = 3
print(childerParty[i])

# Print Each member of our list. Our list is childerparty
for x in childerParty:
    print('Hey this is ' + x)

# Print each index of our list. Our list is childerparty
for eachMember in range(len(childerParty)):
    print('This is index of member ', eachMember)

# While loop
i = 1
while i < 3:
    print(childerParty[i])
    i = i + 1

# Shortcut of for loop. Or Short hand syntex of for loop
[print(x) for x in childerParty]


# For loop with if statment
for x in childerParty:
    print('Hey i am outside if. I am ', x)

    if x == 'Paki':
        print('Hey i am ', x)

    print('I am after if. I am ', x)