from collections import Counter
from collections import defaultdict
from collections import namedtuple

myList = [1, 1, 1, 2, 2, 3, 3, 3, 3]
print(Counter(myList))
print(Counter("aaabbbffgggg"))
sentence = "find repeated word by word"
print(Counter(sentence.lower().split()))
# print(Counter(sentence))
# default dictionary

d = defaultdict(lambda: 0)
print(d["one"])
d["two"] = 1
print(d["two"])
print(d)


# NAME TUPLE
mytuple = (1, 2, 3, 4, 5, 6, 7)
Dog = namedtuple("DogDetails", ["age", "breed", "name"])

sam = Dog(age=2, breed="Lab", name="Sammy")

frank = Dog(age=2, breed="Shepard", name="Frankie")
print(sam, "         ", frank)
print(sam.name)
