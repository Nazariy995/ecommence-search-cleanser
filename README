E-commerce Search Cleanser
=========================

Using Python NLTK we can extract the following data from a sentence:

 - Brands
 - Merchants
 - Price
 - General Search Query

Run
---
    	>>> from cleanser import cleanser
	>>> trial = cleanser("slim jeans from zappos for around 50 dollars")
	>>> trial.start_parse()
	{u'S': [{u'NP': [('slim', 'NN'), ('jeans', 'NNS')]}, {u'PP': [('from', 'IN'), ('zappos', 'NNS')]}, {u'PP': [('for', 'IN'), ('around', 'IN'), ('50', 'CD')]}]}
	{u'NP': [('slim', 'NN'), ('jeans', 'NNS')]}
	{u'NP': [('slim', 'NN'), ('jeans', 'NNS')]}
	('slim', 'NN')
	('jeans', 'NNS')
	{u'PP': [('from', 'IN'), ('zappos', 'NNS')]}
	{u'PP': [('from', 'IN'), ('zappos', 'NNS')]}
	('from', 'IN')
	('zappos', 'NNS')
	{u'PP': [('for', 'IN'), ('around', 'IN'), ('50', 'CD')]}
	{u'PP': [('for', 'IN'), ('around', 'IN'), ('50', 'CD')]}
	('for', 'IN')
	('around', 'IN')
	('50', 'CD')
	>>> trial.prices
	['50']
	>>> trial.merchants
	['zappos']
	>>> trial.search_query
	' slim jeans'
