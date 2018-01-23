import base64
base64.b64encode(b'binarystring')

print(base64.b64encode(b'binarystring1'))
print(base64.b64encode(b'binarystring11'))
print(base64.urlsafe_b64encode(b'binarystring11'))

def safe_base64_decode(s):
    s=s+b'='*(4-(len(s)%4))
    return base64.b64decode(s)
print(safe_base64_decode(b'YWJjZA'))

assert b'abcd' == safe_base64_decode(b'YWJjZA=='), safe_base64_decode('YWJjZA==')
assert b'abcd' == safe_base64_decode(b'YWJjZA'), safe_base64_decode('YWJjZA')
print('Pass')

s='YWJjZA'+'s'
print(s)
