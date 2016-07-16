def my_words(number, *words):
    for word in words:
        if len(word) > number:
            print word

my_words(3, 'hit', 'me', 'baby', 'one', 'more', 'time')