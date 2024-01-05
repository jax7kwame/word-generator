from itertools import permutations
import enchant

d = enchant.Dict("en_US")
op = set()

inp = input("Enter letters: ")
letter = [x.lower() for x in inp]

for n in range(3, len(inp)):
	for y in list(permutations(letter, n)):
		z = "".join(y)

		if d.check(z):  
			op.add(z)

print(op)