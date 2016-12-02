from grammar_corrections import corrector
from ngram import ngrammer

cc = corrector()
cc.check("I think its a cup.")
cc.check("Is that you're cup")
