# HVAZARD Dictionary Modifier
Remove short passwords &amp; duplicates, change lowercase to uppercase &amp; reverse, combine wordlists and more!

### Disclaimer
**This is free software and comes with _no warranty!_ Licensed under the MCD Penetration Testing Software License. Do not use for illegal purposes.**

### Manual & explaination

-d --dict 
 Specifies the file you want to modify. This is the only parameter / argument that is not optional.

-o --out 
 The output filename (optional). Default is out.txt.


-s --short 
 This operation removes the lines with length shorter/equal to the specified number. Example:
	python dm.py -d dictionary.txt -s 5	<- This removes all lines with 5 or less characters of the file dictionary.txt


-s --short 
 This operation removes the lines with length greater/equal to the specified number. Example:
 python dm.py -d dictionary.txt -b 7     <- This removes all lines with 7 or more characters of the file dictionary.txt


-d --dupli 
 This operation removes duplicate lines. If a line appears more than once, it gets removed.
 This is done so no password is tried more than once, since it is a waste of time. Example:
	python dm.py -d wordlist -d


-l --lower 
 This operation turns all upper-case letters to lower-case. Lower-case letters remain that way. Example:
	python dm.py --lower -d dictionary


-u --upper 
 This operation turns all lower-case letters to upper-case. upper-case letters remain that way. Example:
	python dm.py -u -d file.txt


-j --join 
 This operation joins two files together to great one larger file. Example:
	python dm.py -d wd1.txt -j wd2.txt	<- The result is saved on the second wordlist (wd2.txt)


-c --cut 
 This operation removes all lines before the line number you specify. Useful if you have already used a large part of the wordlist and do not want to go through the same process. Example:
	python dm.py --cut rockyou.txt -o cutrocku.txt


-q --leet 
 This operation enables leet mode. (a=4,e=3,i=1,o=0). With mode 0, you add the new modified lines and with option 1 you replace them


-g --gen 
 This operation generates a wordlist with a characters of the string to use as a value to it.
 The passwords have a minimum length of --min and a maximum length with --max.


python dm.py --gen abcd123 --min 2 --max 3	<- This creates a wordlist with the combinations of abcd123 with min and max lengths 2 and 3.


-e --exp 
 This option shows this message. 


-a --arg 
 This option shows the arguments & options. 
