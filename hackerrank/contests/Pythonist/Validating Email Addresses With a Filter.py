# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

def validate_at_sign(splitAddress):
    return len(splitAddress) == 2

def validate_user_name(userName):
    return re.match(r'[\w-]+$', userName)

def validate_address(address):
    website = address.split('.')
    if len(website) != 2:
        return False
    if len(website[1]) == 0 or len(website[1]) > 3:
        return False
    alphanumeric = re.match(r'^[a-zA-Z0-9]+$', website[0])
    alpha = re.match(r'^[a-zA-Z]+$', website[1])
    return alphanumeric and alpha

def validate_email(email):
    splitAddress = email.split('@')
    if not validate_at_sign(splitAddress):
        return False
    if not validate_user_name(splitAddress[0]):
        return False
    return validate_address(splitAddress[1])

numTestCases = int(raw_input())
emails = []
for i in xrange(numTestCases):
    emails.append(raw_input())
print sorted(list(filter(lambda x: validate_email(x), emails)))