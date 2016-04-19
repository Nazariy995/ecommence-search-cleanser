import json
import nltk
import re
from match_data import all_brands,all_merchants
from nltk import Tree
'''
Directions:
from cleanser import cleanser
trial = cleanser("slim jeans from zappos for around 50 dollars")
trial.start_parse()
Get the data:
trial.prices
trial.brands
trial.merchants
'''
class cleanser(object):
    def __init__(self, search_string):
        self.prices = []
        self.merchants = []
        self.brands = []
        self.price_comparative = None
        self.temp_price = ()
        self.temp_brand = None
        self.temp_merchant = None
        self.temp_price_comparative = None
        self.temp_gender = None
        self.gender = None
        self.search_query = ""
        self.all_brands = all_brands
        self.all_merchants = all_merchants
        self.grammar = r"""
                PP: {<IN>+<(?!IN).*>*<NN.*|CD|PP>+}
                NP: {<JJ|NN.*>+}
        """
        self.search_string = self.clean_from_non_alphanumeric(search_string)
        self.tokenized_string = self.tokenize_sentence_and_chunk_it()
        self.search = self.tree2dict(self.tokenized_string)
    
    #Cleaning the whole sentence from anything that is not a word
    def clean_from_non_alphanumeric(self,search_string):
        cleaned_string = re.sub(r'((?! )\W+)','',search_string)
        cleaned_string = re.sub(r'(dollar[s]*)','',search_string)
        return cleaned_string
    
    #tokenize the search strng into its parts of speech
    def tokenize_sentence_and_chunk_it(self):
        tokenized_string = nltk.word_tokenize(self.search_string)
        tokenized_string = nltk.pos_tag(tokenized_string)#('50','CD') ('value','part of speech')
        cp = nltk.RegexpParser(self.grammar,loop=2)
        return cp.parse(tokenized_string)
    
    #convert tree to a dictionary
    def tree2dict(self,tree):
        return {tree.label(): [self.tree2dict(t)  if isinstance(t, Tree) else t for t in tree]}
    
    #called when parsing the string
    def start_parse(self):
        self.parse(self.search)
    
    #go through each tuple and save the appropriate data
    def parse(self, search):
        for key, sentence in search.iteritems():
            print sentence
            for word in sentence:
                if isinstance(word, tuple):
                    part_of_speech = re.compile('[JJ|NN|CD|VBD]+')
                    if part_of_speech.match(word[1]):
                        if self.price_match(word):
                            print "Price matched"
                            self.prices.append(self.temp_price)
                            self.temp_price = None
                        elif self.merchant_match(word):
                            print "Merchant Matched"
                            self.merchants.append(self.temp_merchant)
                            self.temp_merchant=None
                        elif self.brand_match(word):
                            print "Brand Matched"
                            self.brands.append(self.temp_brand)
                            self.temp_brand = None
                        elif self.gender_match(word):
                            print "Gender Matched"
                            self.gender = self.temp_gender
                        elif key != "PP":
                            self.search_query += " " + word[0] # actual value
                elif isinstance(word,dict):
                    self.parse(word)
    
    #get the price from tuple
    def price_match(self, word):
        if word[1] == "CD":
            self.temp_price = word[0]
            return True
        else:
            return False
    
    #get the merchant from tuple
    def merchant_match(self,word):
        if word[0].lower() in self.all_merchants:
            self.temp_merchant = word[0]
            return True
        else:
            return False

    #get the brand from tuple
    def brand_match(self,word):
        if word[0].lower() in self.all_brands:
            self.temp_brand = word[0]
            return True
        else:
            return False
    
    #match the gender from the stirng
    def gender_match(self,word):
        male_match = re.compile('male|(boy[s]?)|(m[ea]n[s]?)')
        female_match = re.compile('female|(girl[s]?)|(wom[ea]n[s]?)')
        if male_match.match(word[0]):
            self.temp_gender = "M"
            return True
        elif female_match.match(word[0]):
            self.temp_gender = "F"
            return True
        else:
            return False
        