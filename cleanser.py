import json
import nltk
import re

class cleanser():
    def __init__(self, search_string):
        self.search_string = self.clean_from_non_alphanumeric(search_string)
        self.tokenized_string = self.tokenize_sentence()
        self.price = self.get_price()
#        self.brand = self.get_brand()
#        self.merchant = self.get_merchant()
        print self.price
    
    #Cleaning the whole sentence from anything that is not a word
    def clean_from_non_alphanumeric(self,search_string):
        cleaned_string = re.sub(r'((?! )\W+)','',search_string)
        return cleaned_string
        
    #tokenize the search strng into its parts of speech
    def tokenize_sentence(self):
        tokenized_string = nltk.word_tokenize(self.search_string)
        return nltk.pos_tag(tokenized_string)

    def get_price(self):
        prices = []
        for index,word in enumerate(self.tokenized_string):
            if word[1] == "CD":
                prices.append(word[0])

        return prices

