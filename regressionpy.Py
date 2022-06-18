#  (555)-555-5555
#  r"(\d{3})-\d{3}-\d{4}"

from os import times
import re
from string import whitespace
from unicodedata import digit

text = "The phone number of this person is 7092-789-422. Change the phone number"
pattern = "phone"

match = re.search(pattern, text)

print(match)
print(match.span())

matches = re.findall(pattern, text)

print(matches)

for m in re.finditer(pattern, text):
    print(match.group(), match.span())

# \d digit
# \w alphanumeric
# \s whitespace
# \D non digit
# \W non-alphanumeric
# \S non whitespace

#  +     one or more time
#  {3}   occurs 3 time for exact
#  {2,5} range of occurances 2 to 5
#  {4,}  occurs 4 or more times
#  *     occurs zero or more times
#  ?     one or none

phone = re.search(r"\d{4}-\d{3}-\d{3}", text)
print(phone.group())

# groups

phone_pattern = re.compile(r'(\d{4})-(\d{3})-(\d{3})')
results = re.search(phone_pattern, text)

print(results.group())
print(results.group(1))
print(results.group(2))
print(results.group(3))
