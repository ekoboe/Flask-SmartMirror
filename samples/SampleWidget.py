from newsapi.articles import Articles
from .abstract.Widget import Widget

'''
** This is a sample template for modular widget implementation **
Steps for implementation:
1) add this widget into /scripts/widgets/ folder
2) add the definition to the CommandHandler "commands" dictionary with object
3) After creating the widget backend, create the JavaScript side to parse information
'''

class SampleWidget(Widget):

	# Abstract functions inherited
	def get(self):  # Return
		json = None
		return json

	def get_script(self):
		script = ""
		return script


if __name__ == '__main__':
	pass