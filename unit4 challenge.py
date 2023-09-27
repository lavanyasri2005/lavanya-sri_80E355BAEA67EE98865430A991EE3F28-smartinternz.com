# define punctuation


punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''


my_str = "Hello!!!, he said ---and went."


# To take input from the user


# my_str = input("Enter a string: ")


# remove punctuation from the string


no_punct = ""


for char in my_str:


   if char not in punctuations:


       no_punct = no_punct + char


# display the unpunctuated string


print(no_punct)
from datetime import datetime


my_date_string = "Mar 11 2011 11:31AM"


datetime_object = datetime.strptime(my_date_string, '%b %d %Y %I:%M%p')


print(type(datetime_object))
print(datetime_object) 