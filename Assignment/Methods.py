S='python tutorial'

print(S.casefold())
'''
Return a version of the string suitable for caseless comparisons
'''

print(S.encode())
'''
Encode the string using the codec registered for encoding.

encoding
The encoding in which to encode the string.
errors
The error handling scheme to use for encoding errors. The default is 'strict' meaning that encoding errors raise a UnicodeEncodeError.
Other possible values are 'ignore', 'replace' and 'xmlcharrefreplace' as well as any other name registered with codecs.register_error
that can handle UnicodeEncodeErrors.
'''

print(S.find('u')) 
'''
Return the lowest index in S where substring sub is found,
such that sub is contained within S[start:end]. Optional arguments start and end are interpreted as in slice notation.
'''

print(S.index('p'))
'''
Return the lowest index in S where substring sub is found,
such that sub is contained within S[start:end]. Optional arguments start and end are interpreted as in slice notation.

Raises ValueError when the substring is not found.
'''

print(S.isascii())
'''
Return True if all characters in the string are ASCII, False otherwise.

ASCII characters have code points in the range U+0000-U+007F. Empty string is ASCII too.
'''
print(S.isidentifier())
'''
Return True if the string is a valid Python identifier, False otherwise.

Call keyword.iskeyword(s) to test whether string s is a reserved identifier, such as "def" or "class".
'''

print(S.isprintable())
'''
Return True if the string is printable, False otherwise.

A string is printable if all of its characters are considered printable in repr() or if it is empty.
'''

print(S.isupper())
if S.isupper()==False:
    print('Not in Upper case')
else:
    print('Good to go')
'''
Return True if the string is an uppercase string, False otherwise.

A string is uppercase if all cased characters in the string are uppercase and there is at least one cased character in the string.
'''

print(S.lower())
'''
Return a copy of the string converted to lowercase.
'''

print(S.partition('n'))
'''
Partition the string into three parts using the given separator.

This will search for the separator in the string. If the separator is found, 
returns a 3-tuple containing the part before the separator, the separator itself, and the part after it.

If the separator is not found, returns a 3-tuple containing the original string and two empty strings.
'''

print(S.replace('tutorial','class'))
print(S)
'''
Return a copy with all occurrences of substring old replaced by new.

count
Maximum number of occurrences to replace. -1 (the default value) means replace all occurrences.

If the optional argument count is given, only the first count occurrences are replaced.
'''

print(S.rjust(1))
'''
Return a right-justified string of length width.

Padding is done using the specified fill character (default is a space).
'''

print(S.rstrip())
'''
Return a copy of the string with trailing whitespace removed.

If chars is given and not None, remove characters in chars instead.
'''

print(S.startswith('Linar'))
if S.startswith('Linar')==False:
    print('Pls start with Linar')
else:
    print('Lets go')
'''
S.startswith(prefix[, start[, end]]) -> bool

Return True if S starts with the specified prefix, False otherwise. 
With optional start, test S beginning at that position. 
With optional end, stop comparing S at that position. prefix can also be a tuple of strings to try.
'''

print(S.title())
'''
Return a version of the string where each word is titlecased.

More specifically, words start with uppercased characters and all remaining cased characters have lower case.
'''

print(S.zfill(3))
'''
Pad a numeric string with zeros on the left, to fill a field of the given width.

The string is never truncated.
'''