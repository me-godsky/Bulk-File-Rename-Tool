import os
import re
import shutil
from past.builtins import xrange
from datetime import datetime

def func(i):
	print("\n {} Files modified successfully \n".format(i))


def main(): 
	try:
		
		j = int(input('''What do you want to change :

	1. Filenames
	2. Extension
	3. Both filenames and extensions

Advanced options : 

	4. Using range				6. Size of the file
	5. Time of file creation		7. About
	
	: '''))

		i = 0
		if j == 1 :
			p = str(input("   Enter the path to the files : "))
			c = str(input("	  Enter the starting name of the files : "))				
			for filename in os.listdir(p): 
				dst = c + str(i) + "." + filename.split(".")[-1]
				src = p + filename 
				dst = p + dst 
				shutil.move(src, dst) 
				i += 1
			func(i)

		elif j == 2 :
			p = str(input("   Enter the path to the files : "))
			x = str(input("   Enter the new extension of the files : "))
			x = x.split(".")[-1]
			for filename in os.listdir(p): 
				dst = filename.split(".")[0] +'.' + x
				src = p + filename 
				dst = p + dst 
				shutil.move(src, dst)
				i +=1 
			func(i)

		elif j ==3 :
			p = str(input("   Enter the path to the files : "))
			c = str(input("	  Enter the starting name of the files  : "))
			x = str(input("   Enter the new extension of the files : "))
			x = x.split(".")[-1]
			for filename in os.listdir(p): 
				dst = c + str(i) + '.' + x
				src = p + filename 
				dst = p + dst 
				shutil.move(src, dst) 
				i += 1
			func(i)

		elif j==4 : 
			p = str(input("	  Enter the path to the files : "))
			c = str(input("   Enter the range upto which the filenames are to be changed [a-z] : "))
			x = str(input("   Enter the starting names of the files : "))
			e = str(input("   Enter the extension of the files : "))
			e = e.split(".")[-1]
			a,b = c[0].lower(),c[2].lower() 
			for filename in os.listdir(p) :
				if ord(filename[0].lower()) in range(ord(a), ord(b)+1):
					dst = x + str(i) + '.' + e
					src = p + filename 
					dst = p + dst 
					shutil.move(src, dst) 
					i += 1
			func(i)
		
		elif j==5 :
			p = str(input("   Enter the path to the files : "))
			c = str(input("   Enter the date  [YYYY-mm-dd] : "))
			x = str(input("   Enter the time  [HH-mm-ss] : "))
			q = str(input("   You want to change the files created before this time or after this time [b or a] : ")).lower()
			a = str(input("   Enter the starting names of the files : "))
			b = str(input("   Enter the extension of the files : "))
			b = b.split(".")[-1]
			d = int(c.split('-')[0] + c.split('-')[1] + c.split('-')[2])
			t = float(x.split('-')[0] + x.split('-')[1] + x.split('-')[2])
			for filename in os.listdir(p) :
				created = os.stat(p + filename).st_ctime
				c = datetime.fromtimestamp(created)
				print(c)
				c,x = str(c).split(' ')
				c = int(c.split('-')[0] + c.split('-')[1] + c.split('-')[2])
				x = float(x.split(':')[0] + x.split(':')[1] + x.split(':')[2])
				if q == 'b':			
					if c < d :
						dst = a + str(i) + '.' + b
						src = p + filename 
						dst = p + dst 
						shutil.move(src, dst) 
						i += 1

					elif c == d and x < t :
						dst = a + str(i) + '.' + b
						src = p + filename 
						dst = p + dst 
						shutil.move(src, dst) 
						i += 1
					
				elif q== 'a':
					if c > d :
						dst = a + str(i) + '.' + b
						src = p + filename 
						dst = p + dst 
						shutil.move(src, dst) 
						i += 1

					elif c == d and x > t :
						dst = a + str(i) + '.' + b
						src = p + filename 
						dst = p + dst 
						shutil.move(src, dst) 
						i += 1
				else :
					print("Wrong input")
							
			func(i)
			
		elif j==6 :
			p = str(input("   Enter the path to the files : "))
			c = float(input("   Enter the size  [in mb] : "))
			q = str(input("	  You want to change the filenames smaller than this size or bigger(or equal) than this size [s or b] : ")) 
			a = str(input("   Enter the starting names of the files : "))
			b = str(input("   Enter the extension of the files : "))
			b = b.split(".")[-1]
			for filename in os.listdir(p) :
				if q == 's':
					if float((os.stat(p + filename).st_size)/1024) < c :
						dst = a + str(i) + '.' + b
						src = p + filename 
						dst = p + dst 
						shutil.move(src, dst) 
						i += 1
				elif q == 'b':
					if float((os.stat(p + filename).st_size)/1024) >= c :
						dst = a + str(i) + '.' + b
						src = p + filename 
						dst = p + dst 
						shutil.move(src, dst) 
						i += 1
				else :
					print("Wrong input")
			func(i)

		elif j==7 :
			print('''
*************************************************************************************

	This tool comes in quite handy when one wants to change filenames in 
	bulk according to user defined criteria of how the filenames should
	be renamed.

	-> There are standard ways of changing the filenames/extensions and
	   there are some other ways too that are case sensitive and could 
	   lead to specific results as required by the user.
	
	[+] Filenames :
	    This option will change all of the filenames in the given path.

	[+] Extension : 
	    You can change extensions of files too using this option.

	[+] Both filenames and extension :
	    If you want to change both the filenames and extension of the 
	    files then this option should be selected.

	[+] Providing range of files : 
	    If you provide range of the files like starting name of files 
	    that comes in specific range, then providing range of files 
	    would lead to change in only those filenames to be changed.
	    
	[+] Time of file creation :
	    If you want to change the filenames to changed if they are 
	    created before that specific time then this option comes in 
	    handy.

	[+] Size of file :
	    If you want to change some files with smaller or greater than
	    a specified size then this option is useful.

*************************************************************************************
''')

		else : 
			print("Wrong input! ")


	except:
		print("An unexpected error occured while processing!")
		pass 


if __name__ == '__main__' :
	main()
