# pylint: disable=missing-module-docstring
# pylint: disable=invalid-name

text = """Python is good language to learn 
          and in same time we like to tell 
          that it is cool expereance for us
       """

letter_count = {}

for letter in text:
    if letter in letter_count:
        letter_count[letter] += 1
    else:
        letter_count[letter] = 1

print(letter_count)
