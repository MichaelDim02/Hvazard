from __future__ import print_function
import argparse

def banner():
	print("Dictionary Modifier")
	print("By MichaelDim02\n")

def help():
	print("-d --dict    The dictionary to modify")
	print("-o --out     Output file name (default is out.txt)")
	print("-s --short   Remove lines with length shorter/equal to number specified")
	print("-m --multi   Remove duplicate lines of the dictionary")
	print("-l --lower   Turn all upper-case letters to lower-case")
	print("-u --upper   Turn all lower-case letters into upper-case")
	print("-j --join    Join two dictionaries into one")
	print("-e --exp     Arguments, options, examples & explaination")
	print("-a --arg     Options & arguments (help)\n")
	print("Usage: python dm.py -d [FILENAME] [OPERATION]")

def explain():
	print("Manual & explaination")
	print("\n-d --dict \n Specifies the file you want to modify. This is the only parameter / argument that is not optional.\n")
	print("-o --out \n The output filename (optional). Default is out.txt.\n\n")
	print("-s --short \n This operation removes the lines with length shorter/equal to the specified number. Example:")
	print("	python dm.py -d dictionary.txt -s 5	<- This removes all lines with 5 or less characters of the file dictionary.txt\n\n")
	print("-d --dupli \n This operation removes duplicate lines. If a line appears more than once, it gets removed.\n This is done so no password is tried more than once, since it is a waste of time. Example:")
	print("	python dm.py -d wordlist -d\n\n")
	print("-l --lower \n This operation turns all upper-case letters to lower-case. Lower-case letters remain that way. Example:")
	print("	python dm.py --lower -d dictionary\n\n")
	print("-u --upper \n This operation turns all lower-case letters to upper-case. upper-case letters remain that way. Example:")
	print("	python dm.py -u -d file.txt\n\n")
	print("-j --join \n This operation joins two files together to great one larger file. Example:")
	print("	python dm.py -d wd1.txt -j wd2.txt	<- The result is saved on the second wordlist (wd2.txt)\n\n")
	print("-e --exp \n This option shows this message. \n\n")
	print("-a --arg \n This option shows the arguments & options. \n\n")

def file_len(filename):
	i = 0
	with open(filename) as f:
		for i, l in enumerate(f):
			pass
	return i + 1

def remove_short_lines(file1, short, output):
	count = 0;
	short = int(short)
	short = short + 1
	print("Source:", file1)
	filelength = file_len(file1)
	print("Lines:",filelength)
	print("Removing lines with length shorter than", short, "character\n")
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
parser = argparse.ArgumentParser()
parser.add_argument("-d", "--dict", help="The dictionary")
parser.add_argument("-o", "--out", help="Output file name (default is out.txt)")
parser.add_argument("-s","--short", help="Remove lines with length shorter or equal to number specified")
parser.add_argument("-m","--multi", action="store_true", help="Remove duplicate lines of the dictionary")
parser.add_argument("-l","--lower", action="store_true", help="Turn all upper-case letters to lower-case")
parser.add_argument("-j","--join", help="Join two dictionaries into one")
parser.add_argument("-u","--upper", action="store_true", help="Turn all lower-case letters into upper-case")
parser.add_argument("-e","--exp", action="store_true", help="Arguments, options, exampls & explaination")
parser.add_argument("-a","--arg", action="store_true", help="Options & arguments (help)")
args = parser.parse_args()

exp = args.exp
filename = args.dict
out = args.out
arg = args.arg
upper = args.upper
lower = args.lower
multi = args.multi
join = args.join
output = "out.txt"
banner()
if out:
	output = out;
short = args.short
if short:
	remove_short_lines(filename, short, output)
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
elif multi:
	multi_remove(filename, output)
elif arg:
	help()
elif exp:
	explain()
else:
	print("Please use -a / --arg for help")




