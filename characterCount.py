import pprint
message = "It was a bright cold day in April, and the clock were striking thirteen."
count = {}

for character in message.lower():
    count.setdefault(character, 0)
    count[character] = count[character] + 1

pprint.pprint(count)
# if you want it as a string use pprint.pformat(count)
