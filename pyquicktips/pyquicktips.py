# Print a string n times
print("This is a separator","-"*50)
print('\n')

# Change string case
print('Change string case','-'*20)
my_string = "sTrangECaSE"
print('Standard:',my_string)
my_string_lower = my_string.lower()
print('Lower:',my_string_lower)
my_string_upper = my_string.upper()
print('Upper:',my_string_upper)
my_string_title = my_string.title()
print('Title:',my_string_title)
print('\n')

# Split a string and join it back
print('Split a string and join it back','-'*20)
my_string = "This is a string"
print("Original string:",my_string)
my_string_list = my_string.split()
my_string_list = [el.title() for el in my_string_list]
my_string = " ".join(my_string_list)
print("Modified String:",my_string)
print('\n')

# List flattening
print('List flattening','-'*20)
list_of_lists = [["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"]]
print('Input:',list_of_lists)
flattened_list = [item for sublist in list_of_lists for item in sublist]
print('Output:',flattened_list)
print('\n')

# Get unique elements from list
print('Get unique elements from list','-'*20)
list_duplicates = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'a', 'a', 'c', 'd', 'e', 'l', 'g', 'z', 'i']
print('Duplicates:',list_duplicates)
unique_list = list(set(list_duplicates))
print('Uniques:',unique_list)
# If you need to sort the list
print('Sorted Uniques:',sorted(unique_list))
print('\n')

# Merge two list into a dictionary
print('Merge two list into a dictionary','-'*20)
list_a = ['a', 'b', 'c']
list_b = [1, 2, 3]
out_dict = dict(zip(list_a, list_b))
print(out_dict)
print('\n')

# Sort a list of dictionaries by a key
print('Sort a list of dictionaries by a key','-'*20)
people = [
    {'name': 'John', 'height': 90},
    {'name': 'Mary', 'height': 160},
    {'name': 'Isla', 'height': 80},
    {'name': 'Sam', 'height': 75},
]
print("Original List:",people)
sorted_people = sorted(people, key=lambda k: k['height'])
print("Sorted List:",sorted_people)
print('\n')

# Sort a list based on another list
print('Sort a list based on another list','-'*20)
list_a = ['a', 'b', 'c']
list_b = [2, 0, 1]
print('Original List:',list_a)
ordered_list_a = [list_a[i] for i in list_b]
print('Ordered List:',ordered_list_a)
print('\n')

# Get most frequent value from a list
print('Get most frequent value from a list','-'*20)
list_a = ['a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'b', 'a', 'b', 'c', 'b', 'b', 'c', 'a', 'b', 'c']
print(list_a)
print('Most frequent value:', max(set(list_a), key=list_a.count))
print('\n')

# Palindrome
palindrome_string = "racecar"
is_palindrome = palindrome_string == palindrome_string[::-1]
print("Is a palindrome:",is_palindrome)
print('\n')