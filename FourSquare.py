import os.path
import sys
import getopt
from sys import argv, stdout

#---------------------------------------------------------------------#

table1=[['a','b','c','d','e'],['f','g','h','i','j'],['k','l','m','n','o'],['p','r','s','t','u'],['v','w','x','y','z']]


#---------------------------------------------------------------------#

#Function: usage
#Purpose: to provide a mini help to the users for usage of the code
#Parameter:
#Return:

def usage(script):
	"to provide a mini help to the users regarding the code"
	print ("\n \n %s [-i] [-o] [-f] [-l]" %script)
	print ("\n this is how the user is supposed to")
	print (" enter data in the command line")
	print ("\n -i [--in]  : input file to be analyzed")
	print ("\n -o [--out] : stores the output of the analyzed file")
	print ("\n -f [--key_f] : first key to be used for analyzing")
	print ("\n -l [--key_l] : last key to be used for analyzing")
	print ("\n \n ")


#----------------------------------------------------------------------#

#Function : log
#purpose : to store the output in a different file
#parameters :
#return :


def log( message, sink) :
	sink.write(message)
pass

#----------------------------------------------------------------------#

#Function: table_creation
#Purpose: the table formed is used for analyzing the file given by the user
#Parameter: key
#Return: 

def table_creation(key):
	"a 5x5 matrix is created using the key given"
	table = [[0] * 5 for row in range(5)]
	alph="abcdefghijklmnoprstuvwxyz"
	key=key.replace(" ","")
	key.lower()
	for i in range(0,5):
		for j in range(0,5):
			if len(key):
				table[i][j]=key[0]
				alph=alph.replace(key[0],'')
				key=key.replace(key[0],'')
			else:
				table[i][j]=alph[0]
				alph=alph[1:]
	return table

#---------------------------------------------------------------------#

#Function: encrypt
#Purpose: to encrypt the file
#Parameter:
#Return:

def encrypt(infile,L,R, sink):
	"this will form the cipher text of the input file given by the user"
	ctext=""
	for i in range(0,len(infile),2):
	#	i=i.lower()
		dig=infile[i:i+2]
#		print dig
		for m in range(5):
			for n in range(5):
				if L[m][n]==dig[0]:
#					print dig[0]

					tmp1,tmp2=m,n

		for m1 in range(5):
			for n1 in range(5):
				if R[m1][n1]==dig[1]:
#					print dig[1]
					tmp3,tmp4=m1,n1
		
		ctext=ctext+table1[tmp1][tmp4]+table1[tmp3][tmp2]
#	print ctext

	log(ctext, sink)

#---------------------------------------------------------------------#

#Function: decrypt
#Purpose: to decrypt the file which had been encrypted before
#Parameter:
#Return:

def decrypt(infile,L,R,sink):
	"this will decrypt the cipher text to the original plain text"
	ptext=""
        for i in range(0,len(infile),2):
	#	i=i.lower()
                dig=infile[i:i+2]
#               print dig
                for m in range(5):
                        for n in range(5):
                                if table1[m][n]==dig[0]:
#                                       print dig[0]

                                        tmp1,tmp2=m,n

                for m1 in range(5):
                        for n1 in range(5):
                                if table1[m1][n1]==dig[1]:
#                                       print dig[1]
                                        tmp3,tmp4=m1,n1

                ptext=ptext+L[tmp1][tmp4]+R[tmp3][tmp2]
#        print ptext

	log(ptext,sink)


#---------------------------------------------------------------------#

#Function: main
#Purpose: taking inputs from the user via command line
#Parameter: argv
#Return:

def main(argv):
	"To take inputs from the user via command line"
	
	in_file = ""
	out_file = ""
	key1 = ""
	key2 = ""
	this_script = argv[0]
	sink = stdout

	if len(argv) < 5:
		usage(this_script)
		sys.exit(3)

	pass

	try:
		opts, args = getopt.getopt(argv[1:], "i:o:f:l:",["in=","out=","key_i=","key_l="])

	except getopt.GetoptError:
		usage(this_script)
		sys.exit(3)

	pass

	for opt, arg in opts:
		
		if opt in ("-i", "--in"):
			in_file = arg
		
		elif opt in ("-o", "--out"):
			out_file = arg

		elif opt in ("-f", "--key_f"):
			key1 = arg

		elif opt in ("-l", "--key_l"):
			key2 = arg

		pass
	
	pass
	
	if ( out_file != ""):
		sink = open(out_file,"w")

	pass

	if ( in_file == ""):
		print ("\n proper filename has to be given")	
		return(-3)

	pass
	
	if ( key1 == ""):
		print ("\n proper initial key has to be given")
		return(-3)

	pass

	if ( key2 == ""):
		print ("\n proper final key has to be given")
		return (-3)

	pass


	L,R=table_creation(key1), table_creation(key2)

	#for i in open(in_file,"r").read().replace(" ","").replace("q","i"):
	#	i=i.lower()
	#	in_file=in_file+i
	#print in_file

	infile=open(in_file,"r").read().replace(" ","").replace("q","i")
	# print infile
	
	user_choice=raw_input("what do you want to perform? E for encryption/ D for decryption")
	
	if user_choice=="E":
		encrypt(infile,L,R,sink)
	elif user_choice=="D":
		decrypt(infile,L,R,sink)

	else:
		sys.exit

#----------------------------------------------------------------------#

if __name__=="__main__":
	main(sys.argv[0:])

