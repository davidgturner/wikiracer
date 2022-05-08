from difflib import SequenceMatcher
import Tokenizer

s1 = "/wiki/Jacquard_loom"
s2 = "/wiki/Richard_Soley"

sm = SequenceMatcher(a=s1, b=s2)
r = sm.ratio()

print(r)
print(1.0 - r)
