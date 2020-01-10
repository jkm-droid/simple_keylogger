import matplotlib.pyplot as plt

log_file = open("logs.txt", 'r+')

chars = 0
lines = 0
letters = []
counted = {}
new_dict = {}

for lf in log_file.read():
	if lf == '\n':
		lines += 1
	chars += 1
	letters.append(lf)

key_string = "".join(letters)
word_string = key_string.replace('\n', "")
final_keywords_list = word_string.split()

with open("words.txt", 'w') as f:
	for word in final_keywords_list:
		f.write("%s\n" % word)

for letter in final_keywords_list:
	let = str(letter)
	if let in counted:
		counted[let] += 1
	else:
		counted[let] = 1

for item in counted:
	if counted[str(item)] >= 3:
		new_dict[str(item)] = counted[str(item)]


print(lines, "Lines", "||", chars, "Characters", " || ", len(final_keywords_list), "words")
print('\n')


plt.title("Keylog Analysis", fontsize = 20)
plt.bar(range(len(new_dict)), list(new_dict.values()))
plt.xticks(range(len(new_dict)), list(new_dict.keys()))

plt.show()