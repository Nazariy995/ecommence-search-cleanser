import json
import nltk
import re
from nltk import Tree

class cleanser():
    def __init__(self, search_string):
        self.prices = []
        self.merchants = []
        self.brands = []
        self.temp_price = None
        self.temp_brand = None
        self.temp_merchant = None
        self.search_query = ""
        self.grammar = r"""
                PP: {<IN>+<(?!IN).*>*<NN.*|CD>+}
                NP: {<JJ|NN.*>+}
        """
        self.search_string = self.clean_from_non_alphanumeric(search_string)
        self.tokenized_string = self.tokenize_sentence_and_chunk_it()
        self.search = self.tree2dict(self.tokenized_string)
        self.get_all_names()

    def get_all_names(self):
        with open("brands.json","r") as infile:
            self.all_brands = json.load(infile)
        with open("merchants.json") as infile:
            self.all_merchants = json.load(infile)
    
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

    def tree2dict(self,tree):
        return {tree.label(): [self.tree2dict(t)  if isinstance(t, Tree) else t for t in tree]}

    def start_parse(self):
        self.parse(self.search)

    def parse(self,search):
        for key, sentence in search.iteritems():
            for word in sentence:
                if isinstance(word,tuple):
                    part_of_speech = re.compile('[JJ|NN|CD]+')
                    if part_of_speech.match(word[1]):
                        if self.price_match(word):
                            self.prices.append(self.temp_price)
                            self.temp_price = None
                        elif self.merchant_match(word):
                            self.merchants.append(self.temp_merchant)
                            self.temp_merchant=None
                        elif self.brand_match(word):
                            self.brands.append(self.temp_brand)
                            self.temp_brand = None
                        elif key != "PP":
                            self.search_query+= " "+word[0]#actual value
                elif isinstance(word,dict):
                    self.parse(word)

    def price_match(self,word):
        if word[1] == "CD":
            self.temp_price = word[0]
            return True
        else:
            return False

    def merchant_match(self,word):
        if word[0] in self.all_merchants:
            self.temp_merchant = word[0]
            return True
        else:
            return False

    def brand_match(self,word):
        if word[0] in self.all_brands:
            self.temp_brand = word[0]
            return True
        else:
            return False


