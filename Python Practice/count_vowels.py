sentence=input("Enter the sentence : ").lower()
vowels="aeiou"
count=0
for char in sentence:
    if char in vowels:
        count += 1       
print(f"Number of vowels in {sentence} is {count}")
