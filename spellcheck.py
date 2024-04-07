# import the fuzzywuzzy module
from tesstmodule.modlib import strmatcher
import csv

# spellcheck main class


class SpellCheck:

    # initialization method
    def __init__(self, word_dict_file=None):
        # open the dictionary file
        data = []
        salt = []
        self.file = open(word_dict_file, 'r')
        with open(word_dict_file, 'r') as self.csvfile:
            csvreader = csv.reader(self.csvfile)
            for i in csvreader:
                data.append(i[0])
                salt.append(i[2])

        # store all the words into a class variable dictionary
        self.dictionary = data
        self.saltdict = salt

    # string setter method
    def check(self, string_to_check):
        # store the string to be checked in a class variable
        self.string_to_check = string_to_check

    # this method returns the possible suggestions of the correct words
    def suggestions(self):
        # store the words of the string to be checked 
        string_words = self.string_to_check

        # a list to store all the possible suggestions
        suggestions = []
        salt_suggestions = []
        match = []
        
        # loop over words in the dictionary
        for name in range(len(self.dictionary)):
            # Calculating match Value
            temp_match_value = strmatcher.WRatio(string_words.lower(), self.dictionary[name].lower())
            # if matched value greater than 84
            if temp_match_value >= 87:
                # append the dict word to the suggestion list
                suggestions.append(self.dictionary[name])
                salt_suggestions.append(self.saltdict[name])
                match.append(temp_match_value)
        # return the suggestions list
        rlist=[]
        for i in range(len(suggestions)):
            rlist.append([suggestions[i],salt_suggestions[i],match[i]])
        rlist.sort(key=lambda x : x[2],reverse=True)
        return rlist
    
        