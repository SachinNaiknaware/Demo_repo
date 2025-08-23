#Regular expressions (RegEx) are used to match patterns in strings. 
#In Python, they are handled using the built-in re module.

# Function	Description
# re.match()	Matches pattern only at the beginning of the string
# re.search()	Searches pattern anywhere in the string
# re.findall()	Returns all matches as a list
# re.finditer()	Returns iterators over matches
# re.sub()	Replaces matches with a string
# re.split()	Splits string by pattern

# Patterns
# Patterns are rules you define to match specific formats:

# Pattern	Meaning
# 'abc'	Exact characters
# '\d'	Digit (0–9)
# '\D'	Not a digit
# '\w'	Word character
# '\W'	Non-word character
# '\s'	Whitespace
# '.'	Any character
# '^'	Start of string
# '$'	End of string

# Meta Characters
# Meta characters have special meaning in regular expressions:

# Meta Char	Meaning
# .	Any character
# ^	Start of string
# $	End of string
# []	Matches any one char
# `	`
# ()	Grouping
# \	Escape character

#  Character Classes
# Character classes define sets of characters to match.

# Class	Description
# [abc]	Matches a, b, or c
# [a-z]	Matches lowercase a to z
# [A-Z]	Matches uppercase A to Z
# [0-9]	Matches any digit
#[^abc]	Matches any char except a, b, c

# import re
# python="Python is Fun. Python3 is Powerfull"
# #print(re.search('Python',python))     #<re.Match object; span=(0, 6), match='Python'>
# print(re.match("is",python))