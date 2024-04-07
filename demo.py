# import the spell check module
from spellcheck import SpellCheck
from tabulate import tabulate
# choose data file
spell_check = SpellCheck('meddata.csv')

# set the string
string_to_be_checked = "Montair LC"
spell_check.check(string_to_be_checked)
# Get suggestions
query_result = spell_check.suggestions()
print(tabulate(query_result, headers=['Name','Salt','Match %']))