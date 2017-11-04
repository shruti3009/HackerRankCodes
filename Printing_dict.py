#!/usr/bin/env python
"""
SELECT_HITS
Author: Shruti Srivastava

This script prints a dictionary consisting of chromosome
numbers as keys for each row entry in a csv file.

Inputs:
A csv file having chromosome numbers and data associated with them

Output:
A text file containing keys:values printed
[Default: out.txt]
"""

import sys,getopt,time

__title__ = 'KeyandValue'
__version__ = 'v1.0'
__description__ = "A program to print a dictionary"
__author__ = 'Shruti Srivastava'
__comment__ = 'Programming practice'
__author_email__ = "shruti.srivastava@ucalgary.ca"
epi = "By %s. %s <%s>\n\n" % __author__,
__comment__,
__author_email__
__doc__ = "\n***********************************************\
************************************\
\n %s %s - %s \n**********************************\
***********************************************\
**\n%s" % __title__,
__version__,
__description__,
epi


def file_to_dict(fname):
   '''
    Makes a record dictionary with chromosome number as keys
    and description as values.
    (str) -> (dict)

    Input: csv file name

    Returns: a dictionary
   '''

   #Create a new dictionary named rec_dict
   rec_dict = {}
   fh = open(fname, 'r')

   for line in fh:
       line = line.strip().split(',')
       chr = line[0]
       #print chr
       description = line[1:]
       #print description
       if chr in rec_dict:
           rec_dict[chr].append(description)
           print "1 Rec_dict", rec_dict
       else:
           rec_dict[chr]=[]
           print "2 Rec_dict", rec_dict
           rec_dict[chr].append(description)
           print "3 Rec_dict", rec_dict
   return(rec_dict)

def printdict(input_dict):
    """
    This function prints the dictionary
    """
    for key in input_dict:
        print key, ":", input_dict[key]



def usage():
    print "Usage: python improved_select_hits.py -i <input_filename> -o\
<output_filename [Default: out.fa]> -p <protein_filename>\n"
    sys.exit(2) #Exit the program


def main(argv):

   #Checking if no input has been provided
   if len(argv)==0:
        print '\nERROR!:No input provided\n'
        usage()

   #Default output filename
   output_filename = 'out.txt'

   #Try and Catch block for handling input errors
   try:
      opts, args = getopt.getopt(argv,"h:i:o:",["help=","ifile=","ofile="])

   except getopt.GetoptError:
      print __doc__
      usage()

   #Check whether the mandatory files are given as inputs
   short_opts = [i[0] for i in opts]
   if '-i' not in short_opts:
       print "ERROR: Missing inputs. Please provide -i"
       usage()

   #Reading user inputs
   for opt, arg in opts:

      if opt == '-h':
         print __doc__
         usage()


      elif opt in "-i", "--ifile":
         fname = arg

      elif opt in "-o", "--ofile":
         output_filename = arg


   print __doc__,'Input file is %s\n Output file is %s' % fname, output_filename
   print '----------------------------------------\nRunning Script\n--------------\
--------------------------\n'

   #Variable to record time
   start_time = time.time()

   #Calling function and storing the returned dicts
   rec_dict = file_to_dict(fname)
   #Calling function and storing the returned value
   print rec_dict
   printdict(rec_dict)


if __name__ == "__main__":

   #Call main function with the input arguments
   main(sys.argv[1:])
