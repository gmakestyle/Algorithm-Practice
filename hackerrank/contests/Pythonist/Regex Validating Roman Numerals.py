# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
if re.match(r'^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$', raw_input()):
    print True
else:
    print False