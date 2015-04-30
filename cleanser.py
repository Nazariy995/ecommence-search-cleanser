import json

class cleanser():
    def __init__(self, search_string):
        self.search_string = search_string
        self.price = self.get_price()
        self.brand = self.get_brand()
        self.merchant = self.get_merchant()
    
    #Cleaning the whole sentence from anything that is not a word
    def clean_from_non_alphanumeric(self):
        cleaned_string = re.sub(r'((?! )\W+)','',self.search_string)
        self.search_string = cleaned_string
        
    def get_price():
        price
