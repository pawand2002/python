my_numbers = {1, 2, 3, 2, 4, 1, 5}
print(f"Original set: {my_numbers}")  # Duplicates removed

my_numbers.add(6)
my_numbers.remove(2)

print(f"Updated set: {my_numbers}")

# Membership test
if 3 in my_numbers:
    print("3 is in the set")
else:
    print("3 is not in the set")
