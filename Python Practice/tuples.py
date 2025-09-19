#Creating a Tuple
empty_tuple = ()
# or using the tuple constructor
empty_tuple = tuple()
print(empty_tuple)
#Tuple with initial values
tpl = ('item1', 'item2','item3')
fruits = ('banana', 'orange', 'mango', 'lemon')
# Tuple length
tpl = ('item1', 'item2', 'item3')
len(tpl)
print(tpl)
print(fruits)
#Accessing Tuple Items
tpl = ('item1', 'item2', 'item3')
first_item = tpl[0]
second_item = tpl[1]
print(first_item)
print(second_item)
fruits = ('banana', 'orange', 'mango', 'lemon')
first_fruit = fruits[0]
second_fruit = fruits[1]
print(fruits)
print(first_fruit)
print(second_fruit)
last_index =len(fruits) - 1
last_fruit = fruits[last_index]
print(last_fruit)
# Negative indexing
tpl = ('item1', 'item2', 'item3','item4')
first_item = tpl[-4]
second_item = tpl[-3]
print(first_item)
print(second_item)

fruits = ('banana', 'orange', 'mango', 'lemon')
first_fruit = fruits[-4]
second_fruit = fruits[-3]
last_fruit = fruits[-1]
print(first_fruit)
print(second_fruit)
print(last_fruit)
#Range of Positive Indexes
tpl = ('item1', 'item2', 'item3','item4')
all_items = tpl[0:4]         # all items
all_items = tpl[0:]         # all items
middle_two_items = tpl[1:3]  # does not include item at index 3
print(tpl)
print(all_items)
print(middle_two_items)
fruits = ('banana', 'orange', 'mango', 'lemon')
all_fruits = fruits[0:4]    # all items
all_fruits= fruits[0:]      # all items
orange_mango = fruits[1:3]  # doesn't include item at index 3
orange_to_the_rest = fruits[1:]
print(fruits)
print(all_fruits)
print(orange_mango)
print(orange_to_the_rest)
#Range of Negative Indexes
# Syntax
tpl = ('item1', 'item2', 'item3','item4')
all_items = tpl[-4:]         # all items
middle_two_items = tpl[-3:-1]  # does not include item at index 3 (-1)
print(tpl)
print(all_items)
print(middle_two_items)
fruits = ('banana', 'orange', 'mango', 'lemon')
all_fruits = fruits[-4:]    # all items
orange_mango = fruits[-3:-1]  # doesn't include item at index 3
orange_to_the_rest = fruits[-3:]
print(fruits)
print(all_fruits)
print(orange_mango)
print(orange_to_the_rest)
# Changing Tuples to Lists
# Syntax
tpl = ('item1', 'item2', 'item3','item4')
lst = list(tpl)
print(tpl)
print(lst)
fruits = ('banana', 'orange', 'mango', 'lemon')
fruits = list(fruits)
fruits[0] = 'apple'
print(fruits)     # ['apple', 'orange', 'mango', 'lemon']
fruits = tuple(fruits)
print(fruits)     # ('apple', 'orange', 'mango', 'lemon')
# Checking an Item in a Tuple
# Syntax
tpl = ('item1', 'item2', 'item3','item4')
'item2' in tpl # True
print(tpl)
fruits = ('banana', 'orange', 'mango', 'lemon')
print('orange' in fruits) # True
print('apple' in fruits) # False
#fruits[0] = 'apple' # TypeError: 'tuple' object does not support item assignment
#Joining Tuples
fruits = ('banana', 'orange', 'mango', 'lemon')
vegetables = ('Tomato', 'Potato', 'Cabbage','Onion', 'Carrot')
fruits_and_vegetables = fruits + vegetables
print(fruits)
print(vegetables)
print(fruits_and_vegetables)
#Deleting Tuples
fruits = ('banana', 'orange', 'mango', 'lemon')
del fruits
print(fruits)