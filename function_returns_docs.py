def returning_doc():
	'''
This function returns its own docstring.
	'''
	message = 'Code exits'
	return '{}'.format(message) + '\n' + returning_doc.__doc__



print(returning_doc())