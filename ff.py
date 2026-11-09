def count_vowels(text):
    count = 0

    for ch in text:
        if ch.lower() in "aeiou":
            count += 1

    print("Number of vowels:", count)


text = input("Enter a string: ")

count_vowels(text)
