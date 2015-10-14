def Content():
	"""content() will hold the logic behind the custom built search bar """
	TOPIC_DICT = {"Basics": [["Introduction to Python", "/introduction-to-python/"], 
													 ["Print functions", "/python-print-function/"],
													 ["Math basics with Python 3", "/math-basics-python-3/"
													 ]],
								"Web Dev": []} #Web dev is now the second topic
								#Introduction to Python
	#will be the title and the link to that is immediately after. Each inner array will be a specific sub section of the basics
	#section

	return TOPIC_DICT