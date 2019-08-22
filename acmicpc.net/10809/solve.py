NONE = '-1'

_input = input()
indexer = [NONE] * 26

counter = 0
for char in _input:
    if indexer[ord(char) - 0x61] is NONE:
        indexer[ord(char) - 0x61] = str(counter)
    counter += 1

print(" ".join(indexer))