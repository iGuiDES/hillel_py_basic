text = """
    Любіть Україну, як сонце, любіть,
    як вітер, і трави, і води…
    В годину щасливу і в радості мить,
    любіть у годину негоди.
    Любіть Україну у сні й наяву,
    вишневу свою Україну,
    красу її, вічно живу і нову,
    і мову її соловʼїну.
    Між братніх народів, мов садом рясним,
    сіяє вона над віками…
    Любіть Україну всім серцем своїм
    і всіми своїми ділами.
    Для нас вона в світі єдина, одна
    в просторів солодкому чарі…
    Вона у зірках, і у вербах вона,
    і в кожному серця ударі,
    у квітці, в пташині, в електровогнях,
    у пісні у кожній, у думі,
    в дитячий усмішці, в дівочих очах
    і в стягів багряному шумі…
"""

cleaned_text = []
for ch in text:
    if ch.isalnum() or ch.isspace():
        cleaned_text.append(ch.lower())
    else:
        cleaned_text.append(' ')
cleaned_text = ''.join(cleaned_text)

words = cleaned_text.split()

word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1

most_common_word = None
least_common_word = None

for word, count in word_count.items():
    if most_common_word is None or count > word_count[most_common_word]:
        most_common_word = word
    if least_common_word is None or count < word_count[least_common_word]:
        least_common_word = word

print(f"Найбільше зустрічається слово '{most_common_word}' - {word_count[most_common_word]} разів.")
print(f"Найменше зустрічається слово '{least_common_word}' - {word_count[least_common_word]} раз.")
