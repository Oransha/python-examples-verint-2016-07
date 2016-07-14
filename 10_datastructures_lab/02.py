import sys
file1 = sys.argv[1]
word_dict = {}

with open(file1, 'r') as fin:
    for word in fin:
        word = word.strip('\n')
        key = sorted(word)
        key_str = ''.join(key)
        word_dict.setdefault(key_str, [])
        if key_str in word_dict:
            word_dict[key_str].append(word)
    for key_str in word_dict:
        print word_dict[key_str]