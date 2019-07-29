from __future__ import print_function
import argparse


def banner():
	print(" ")
	print("""\ \ \  \ /=\ /=/ /=\ /=\ =\ 
|=| |==| |=|  /  |=| |=/ | |
\ \  \/  / / /=/ / / | \ =/""")
	print("\nDictionary Modifier v5.0")
	print("By MichaelDim02\n")

def info():
	print("Thessaloniki // Greece // 2019")
	print("Licensed under the MCD's Penetration testing software License (mcd_pt_1.0)\n")
	print("Do not use for illegal purposes. The author is not responsible for any damage caused")

def help():
	print("-d --dict    The dictionary to modify")
	print("-o --out     Output file name (default is out.txt)")
	print("-s --short   Remove lines with length shorter/equal to number specified")
	print("-b --big     Remove lines with length greater/equal to number specified")
	print("-m --multi   Remove duplicate lines of the dictionary")
	print("-l --lower   Turn all upper-case letters to lower-case")
	print("-u --upper   Turn all lower-case letters into upper-case")
	print("-j --join    Join two dictionaries into one")
	print("-c --cut     Remove all passwords before a specified line")
	print("-q --leet    Add/replace with leet mod (0=add, 1=replace)")
	print("-e --exp     Arguments, options, examples & explaination")
	print("-a --arg     Options & arguments (help)")
	print("-i --info    Info, copyright & license")
	print("-g --gen     Generator. Provide all characters you want to use")
	print("             in a string without commas or spaces.")
	print("   --min     Minimum number of digits")
	print("   --max     Maximum number of digits\n")

	print("Usage: python dm.py -d [FILENAME] [OPERATION] -o [OUTPUT-FILENAME]")

def explain():
	print("Manual & explaination")
	print("\n-d --dict \n Specifies the file you want to modify. This is the only parameter / argument that is not optional.\n")
	print("-o --out \n The output filename (optional). Default is out.txt.\n\n")
	print("-s --short \n This operation removes the lines with length shorter/equal to the specified number. Example:")
	print("	python dm.py -d dictionary.txt -s 5	<- This removes all lines with 5 or less characters of the file dictionary.txt\n\n")
        print("-s --short \n This operation removes the lines with length greater/equal to the specified number. Example:")
        print(" python dm.py -d dictionary.txt -b 7     <- This removes all lines with 7 or more characters of the file dictionary.txt\n\n")
	print("-d --dupli \n This operation removes duplicate lines. If a line appears more than once, it gets removed.\n This is done so no password is tried more than once, since it is a waste of time. Example:")
	print("	python dm.py -d wordlist -d\n\n")
	print("-l --lower \n This operation turns all upper-case letters to lower-case. Lower-case letters remain that way. Example:")
	print("	python dm.py --lower -d dictionary\n\n")
	print("-u --upper \n This operation turns all lower-case letters to upper-case. upper-case letters remain that way. Example:")
	print("	python dm.py -u -d file.txt\n\n")
	print("-j --join \n This operation joins two files together to great one larger file. Example:")
	print("	python dm.py -d wd1.txt -j wd2.txt	<- The result is saved on the second wordlist (wd2.txt)\n\n")
	print("-c --cut \n This operation removes all lines before the line number you specify. Useful if you have already used a large part of the wordlist and do not want to go through the same process. Example:")
	print("	python dm.py --cut rockyou.txt -o cutrocku.txt\n\n")
	print("-q --leet \n This operation enables leet mode. (a=4,e=3,i=1,o=0). With mode 0, you add the new modified lines and with option 1 you replace them\n\n")
	print("-g --gen \n This operation generates a wordlist with a characters of the string to use as a value to it.")
	print(" The passwords have a minimum length of --min and a maximum length with --max.")
	print("\n\npython dm.py --gen abcd123 --min 2 --max 3	<- This creates a wordlist with the combinations of abcd123 with min and max lengths 2 and 3.")
	print("\n\n-e --exp \n This option shows this message. \n\n")
	print("-a --arg \n This option shows the arguments & options. \n\n")

def split(word):
	word = str(word)
	return [char for char in word]

def file_len(filename):
	i = 0
	with open(filename) as f:
		for line in f:
			i = i + 1
	return i

def turn_leet(filename, output, mode):
	print("Source: ", filename)
	filelength = file_len(filename)
	if mode == "0":
		print("Lines:",filelength)
	print("Leet mode", mode)
	with open(filename) as f:
		with open(output, "w+") as f1:
			for line in f:
				if "a" in line or "e" in line or "o" in line or "1" in line:
					if mode == "0":
						f1.write(line)
					new_line = line.replace("a","4").replace("e","3").replace("o","0").replace("i","1")
					f1.write(new_line)
				else:
					f1.write(line)
	print("\n")
	if mode == "0":
		newfilelength = file_len(output)
		print("Lines:",newfilelength)
	print("Output:",output)

def remove_short_lines(file1, short, output):
	count = 0;
	short = int(short)
	short = short + 1
	print("Source:", file1)
	filelength = file_len(file1)
	print("Lines:",filelength)
	print("Removing lines with length shorter than", short, "digits\n")
	with open(file1) as f:
		with open(output, "w+") as f1:
			for line in f:
				length = len(line.strip())
				if length > short:
					f1.write(line)
				else:
					count = count + 1
	print("Removed", count, "lines")
	print("Lines:", file_len(output))
	print("Output:", output)

def remove_long_lines(file1, long, output):
	count = 0
	long = int(long)
	print("Source:", file1)
	filelength = file_len(file1)
        print("Lines:",filelength)
        print("Removing lines with length greater than", long, "digits\n")
        with open(file1) as f:
                with open(output, "w+") as f1:
                        for line in f:
                                length = len(line.strip())
                                if length < long:
                                        f1.write(line)
                                else:
                                        count = count + 1
        print("Removed", count, "lines")
        print("Lines:", file_len(output))
        print("Output:", output)


def multi_remove(filename, output):
	length = file_len(filename)
	print("Source:", filename)
	print("Lines: ", length)
	print("Removing duplicate lines of",filename,"\n")
	with open(filename, 'r') as f:
		unique_lines = set(f.readlines())
	with open(output, 'w') as f:
		f.writelines(unique_lines)
	print("Lines:", file_len(output))
	print("Output:",output)

def generator(charset, min_, max_, output):
	f = open(output, "w+")
	min_ = int(min_)
	max_ = int(max_)
	list_charset = split(charset)
	if min_ <= 1:
		for digit in list_charset:
			text = digit+"\n"
			f.write(text)
	if min_ <= 2 and max_ >= 2:
		for digit in list_charset:
			for digit2 in list_charset:
				text = digit+digit2+"\n"
				f.write(text)
	if min_ <= 3 and max_ >= 3:
		for digit in list_charset:
			for digit2 in list_charset:
				for digit3 in list_charset:
					text = digit+digit2+digit3+"\n"
					f.write(text)
	if min_ <= 4 and max_ >= 4:
		for digit in list_charset:
			for digit2 in list_charset:
				for digit3 in list_charset:
					for digit4 in list_charset:
						text = digit+digit2+digit3+digit4+"\n"
						f.write(text)
	if min_ <= 5 and max_ >= 5:
		for digit in list_charset:
			for digit2 in list_charset:
				for digit3 in list_charset:
					for digit4 in list_charset:
						for digit5 in list_charset:
							text = digit+digit2+digit3+digit4+digit5+"\n"
							f.write(text)
	if min_ <= 6 and max_ >= 6:
		for digit in list_charset:
			for digit2 in list_charset:
				for digit3 in list_charset:
					for digit4 in list_charset:
						for digit5 in list_charset:
							for digit6 in list_charset:
								text = digit+digit2+digit3+digit4+digit5+digit6+"\n"
								f.write(text)
	if min_ <= 7 and max_ >= 7:
		for digit in list_charset:
			for digit2 in list_charset:
				for digit3 in list_charset:
					for digit4 in list_charset:
						for digit5 in list_charset:
							for digit6 in list_charset:
								for digit7 in list_charset:
									text = digit+digit2+digit3+digit4+digit5+digit6+digit7+"\n"
									f.write(text)
	if min_ <= 8 and max_ >= 8:
		for digit in list_charset:
			for digit2 in list_charset:
				for digit3 in list_charset:
					for digit4 in list_charset:
						for digit5 in list_charset:
							for digit6 in list_charset:
								for digit7 in list_charset:
									for digit8 in list_charset:
										text = digit+digit2+digit3+digit4+digit5+digit6+digit7+digit8+"\n"
										f.write(text)
	if min_ <= 9 and max_ >= 9:
		for digit in list_charset:
			for digit2 in list_charset:
				for digit3 in list_charset:
					for digit4 in list_charset:
						for digit5 in list_charset:
							for digit6 in list_charset:
								for digit7 in list_charset:
									for digit8 in list_charset:
										for digit9 in list_charset:
											text = digit+digit2+digit3+digit4+digit5+digit6+digit7+digit8+digit9+"\n"
											f.write(text)
	if min_ <= 10 and max_ >= 10:
		for digit in list_charset:
			for digit2 in list_charset:
				for digit3 in list_charset:
					for digit4 in list_charset:
						for digit5 in list_charset:
							for digit6 in list_charset:
								for digit7 in list_charset:
									for digit8 in list_charset:
										for digit9 in list_charset:
											for digit10 in list_charset:
												text = digit+digit2+digit3+digit4+digit5+digit6+digit7+digit8+digit9+digit10+"\n"
												f.write(text)
	print("Output: "+output)
	print("Generated ",file_len(output)," lines")
parser = argparse.ArgumentParser()
parser.add_argument("-d", "--dict", help="The dictionary")
parser.add_argument("-o", "--out", help="Output file name (default is out.txt)")
parser.add_argument("-s","--short", help="Remove lines with length shorter or equal to number specified")
parser.add_argument("-b","--big", help="Remove lines with length grater or equal to number specified")
parser.add_argument("-m","--multi", action="store_true", help="Remove duplicate lines of the dictionary")
parser.add_argument("-l","--lower", action="store_true", help="Turn all upper-case letters to lower-case")
parser.add_argument("-j","--join", help="Join two dictionaries into one")
parser.add_argument("-c","--cut", help="Remove all passwords before a specified line")
parser.add_argument("-q","--leet", help="Add/replace with leet mod (0=add, 1=replace)")
parser.add_argument("-u","--upper", action="store_true", help="Turn all lower-case letters into upper-case")
parser.add_argument("-g","--gen", help="Generator. Provide all characters you want to use in a string without commas or spaces.")
parser.add_argument("--min", help="Minimum number of digits")
parser.add_argument("--max", help="Maximum number of digits")
parser.add_argument("-e","--exp", action="store_true", help="Arguments, options, exampls & explaination")
parser.add_argument("-a","--arg", action="store_true", help="Options & arguments (help)")
parser.add_argument("-i","--info", action="store_true", help="Info, copyright & license")
args = parser.parse_args()

exp = args.exp
filename = args.dict
out = args.out
arg = args.arg
cut = args.cut
inf = args.info
leet = args.leet
upper = args.upper
lower = args.lower
multi = args.multi
join = args.join
gen = args.gen
min_ = args.min
max_ = args.max
output = "out.txt"
short = args.short
big = args.big

banner()

if out:
	output = out;

if gen:
	print("Generator mode\nCharset: ",gen)
	if min_:
		print("Minimum number of digits: ",min_)
		if max_:
			print("Maximum number of digits: ",max_)
			generator(gen, min_, max_, output)
		else:
			print("You need to provide min and max when using the generator.")
	else:
		print("You need to provide min and max when using the generator.")
	exit(0)
try:
	if short:
		remove_short_lines(filename, short, output)
	elif big:
		remove_long_lines(filename, big, output)

	elif lower:
		print("Source:", filename)
		print("Upper case to lower case\n")
		with open(filename) as f:
			with open(output, "w+") as f1:
				for line in f:
					line = line.lower()
					f1.write(line)

		print("Output:",output)
	elif upper:
		print("Source:", filename)
		print("Lower case to upper case\n")
		with open(filename) as f:
			with open(output, "w+") as f1:
				for line in f:
					length = len(line.strip())
					line = line.upper()
					f1.write(line)

		print("Output:",output)
	elif join:
		print("Joining",filename, "and", join, "\n")
		with open(filename) as f:
			with open(join, "a") as f1:
				for line in f:
					f1.write(line)
		print("Output:", join)
	elif cut:
		print("Remove lines of",filename,"before line",cut)
		count = 0
		with open(filename) as f:
			with open(output, "w+") as f1:
				for line in f:
					count = count + 1
					if count >= int(cut):
						f1.write(line)
		print("Output:", output)
	elif leet:
		turn_leet(filename,output,leet)
	elif multi:
		multi_remove(filename, output)
	elif arg:
		help()
	elif exp:
		explain()
	elif inf:
		info()
	else:
		print("Please use -a / --arg for help")
except:
	print("There was an error. Please check if the filepath and other values are correct.")
	print("If you are certain that your command was correct, please contact me on Github.")
	print("If you believe there is an error in the code, or a bug, please start a new issue")
	print("thread and describe your problem and your suspicion. I will try to resolve it.")
	print("Thanks :)")
