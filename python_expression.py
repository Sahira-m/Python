import re

text = "please find my phone number and phone color"
pattern = "phone"
match = re.search(pattern, text)
print("result is", match)
print("start and end index is", match.span())
print("start index is", match.start())
print("End index is", match.end())
matches = re.findall("phone", text)
print("find all will return all elements ", matches)
print("length ", len(matches))

for item in re.finditer("phone", text):
    print("1:", item.span())
print("2:", item.group())
## orginal use of regular expression
text = "My telephone number is 408-555-1234"
phone = re.search(r"\d\d\d-\d\d\d-\d\d\d\d", text)
print(" group is", phone.group())
phones = re.search(r"\d{3}-\d{3}-\d{4}", text)
print("2: group is", phones.group())
email = input("Enter your Email id?")
check = re.compile(r"([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})")


if re.fullmatch(check, email):
    print("The given mail is valid")
else:
    print("The given mail is invalid")
# OR operator
print(re.search(r"cat|dog|cow", "do yo see dog cow a cow?"))  # OR
print(re.findall(r"..at", "do yo see a hat,cat rat and mat ?"))  # wild operator
