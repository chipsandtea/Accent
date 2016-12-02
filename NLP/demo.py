from grammar_corrections import corrector
import sys

cc = corrector()
if int(sys.argv[1]) == 1:
	cc.check("Is that you're cup?")
elif int(sys.argv[1]) == 2:
	cc.check("Whos is that, is it Albert's?")