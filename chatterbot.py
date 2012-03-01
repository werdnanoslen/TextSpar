#!/usr/bin/python

import aiml
import sys
import getopt

def main(argv=None):
	# in case we want to implement arguments later
    if argv is None:
        argv = sys.argv
        
	# The Kernel object is the public interface to the AIML interpreter.
	k = aiml.Kernel()
	
	# Use the 'learn' method to load the contents of an AIML file into the Kernel.
	#k.learn("std-startup.xml")
	k.learn("spar.aiml")
	
	# Use the 'respond' method to compute the response to a user's input string.  
	# Here we're just  using it to load a bunch of other AIML files
	print ""
	print k.respond("load aiml b")
	print ""
	
	# Loop forever, reading user input from the command line and printing responses.
	# (except if the user types "quit", in which case we quit) 
	while True: 
		s = raw_input("> ")
		if s == "quit": return 0
		print k.respond(s)

if __name__ == "__main__":
    sys.exit(main())
