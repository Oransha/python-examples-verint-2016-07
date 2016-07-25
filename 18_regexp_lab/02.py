
import re

def camelCase(text):
    res = re.search(r'(\w+)_(\w+)', text)
    if res == None: 
        print text, "not have _"   
    else:
        upper = re.sub((r'_(\w)') ,
        lambda m: m.group(0).upper()
        , text)
        camel_case_word = re.sub('_' , '', upper)
        return camel_case_word

print camelCase('hi_there_hoe_r_u')

def underline(text1):
    res1 = re.search(r'([a-z])([A-Z])', text1)
    if res1 == None:
        print text1, "not have big letter"
    else:
        lower = re.sub('([A-Z])',
        lambda m: '_' + m.group(0).lower()
        , text1) 
        return lower



print underline('hiThereHowAre')