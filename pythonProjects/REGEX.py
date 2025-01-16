import re

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa

MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )

coreyms.com

321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234

Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T

cat
mat
pat
bat
'''

sentence = 'Start a sentence and then bring it to an end'
# pattern = re.compile(r"\s")
# pattern = re.compile(r"\S")
# pattern = re.compile(r"\bHa")
# pattern = re.compile(r"\BHa")
# pattern = re.compile(r"^Start")
# pattern = re.compile(r"end$")
# pattern = re.compile(r"\d\d\d.\d\d\d.\d\d\d\d")
# pattern = re.compile(r"\d\d\d[-.]\d\d\d[-.]\d\d\d\d")
# pattern = re.compile(r"[89]00[-.]\d\d\d[-.]\d\d\d\d")
# pattern = re.compile(r"[0-4]")
# pattern = re.compile(r"[a-zA-Z]") #"[ ]" square brackets mean a char set
# pattern = re.compile(r"[^a-zA-Z]") #caret in this case negates the set
# pattern = re.compile(r"[^b]at")
# pattern = re.compile(r"\d{3}.\d{3}.\d{4}") #the best case scenario using this
# pattern = re.compile(r"Mr.?\s[A-Z]\w*")
# pattern = re.compile(r"(Mr|Ms|Mrs).?\s[A-Z]\w*")
pattern = re.compile(r"(Mr|Ms|Mrs).?\s[A-Z]\w*")
# pattern=re.compile(r"Start")
# pattern=re.compile(r"and")
# pattern=re.compile(r"start",re.I) #"I" stands for IGNORECASE


matches = pattern.finditer(text_to_search)
# matches = pattern.finditer(sentence)
# matches = pattern.findall(text_to_search) #return a data with no extra info
# matches = pattern.match(sentence) #a match method doesn't return a span and matches only from the start
# matches = pattern.search(sentence) #matches all and returns a span
# print(matches)

for match in matches:
    print(match)


# with open("REGEX_data.txt","r") as f:
#     contents=f.read()
#     matches = pattern.finditer(contents)
#     for match in matches:
#         print(match)