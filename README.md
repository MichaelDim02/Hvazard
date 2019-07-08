# DirectoryModifier
Remove short passwords &amp; duplicates, change lowercase to uppercase &amp; reverse, combine wordlists!

### Manual & explaination

-d --dict 
 Specifies the file you want to modify. This is the only parameter / argument that is not optional.

-o --out 
 The output filename (optional). Default is out.txt.


-s --short 
 This operation removes the lines with length shorter/equal to the specified number. Example:
	python dm.py -d dictionary.txt -s 5	<- This removes all lines with 5 or less characters of the file dictionary.txt


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


-e --exp 
 This option shows this message. 


-a --arg 
 This option shows the arguments & options. 
