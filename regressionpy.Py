#  (555)-555-5555
#  r"(\d{3})-\d{3}-\d{4}"

import numbers
from os import times
import re
from string import whitespace
from unicodedata import digit, numeric

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

print("groups ----------------------------------------")

phone_pattern = re.compile(r'(\d{4})-(\d{3})-(\d{3})')
results = re.search(phone_pattern, text)

print(results.group())
print(results.group(1))
print(results.group(2))
print(results.group(3))


# patterns

# cat|dog  return if either cat or dog is present
# .at      return like hat, tat, sat, mat etc
# ^\d      return if sentence starts with numeric
# \d$      returns if sentence ends with numeric
# [^\d]+   returns string excluding the numbers

print("pattern ----------------------------------------")

print(re.search(r'cat|dog', "we have a dog").group())

print(re.findall(r'.at', "he hit the man who sat on the hat"))

print(re.findall(r'^\d', "2 starting"))

print(re.findall(r'\d$', "ending 2"))

print(re.findall(r'[^\d]+', "exclude 3 5 number 7 in 4 7sentence"))

print("".join(re.findall(
    r'[^.,?!]+', "Remove. the punctions ! in the sentence, will you?")))

print(re.findall(r"[\w]+-[\w]+",
      "find the hyphen-words in the hyphen-sentence"))
