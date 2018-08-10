import re
with open('/home/sam/Downloads/regularexp', 'r') as f:
    cont=f.read()
text = '''
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
'''
email='''
CoreyMSchafer@gmail.com
corey.schafer@university.edu
corey-321-schafer@my-work.net
sameer.apsdk@gmail.com
'''
urls = '''
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
'''

sentence = 'start a sentence and then bring it to an end'
#print(cont)
# manually writing every character
pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d')
#using Quantifiers
patternQ = re.compile(r'\d{3}.\d{3}.\d{4}')
#pattern for extracting on names
patternN=re.compile(r'M(r|s|rs)\.?\s[A-Z]\w+')
#pattern for mail
patternM=re.compile(r'[a-zA-Z0-9.-]+@[a-zA-Z-]+\.(com|net|edu)')
#pattern for url
patternU=re.compile(r'(https?)+://(www\.)?(\w+)(\.\w+)')

matchN=patternN.finditer(text)
matches = pattern.finditer(cont)
matchsQ = patternQ.finditer(cont)
matchM = patternM.finditer(email)
matchU= patternU.finditer(urls)
#printing phone numbers fromt the text file
# for match in matches:
#     print(match)
#
# for match in matchsQ:
#     print("using Quantifiers")
#     print(match)

# for match in matchN:
#     print(match)

# for match in matchM:
#     print(match)

#subbed url
sub_url = patternU.sub(r'\3\4',urls)
print(sub_url)

for match in matchU:
    print(match)
    print('group')
    print(match.group(2))



