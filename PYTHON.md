# HashSet

[Tutorial](https://www.w3schools.com/python/python_sets.asp)

```python
# Init
newSet = set()

# add
newSet.add('yo')

# check if contains
print( 'yo' in newSet )

# remove will throw error, discard won't
newSet.remove('yo')
newSet.discard('yo2')
```

# Char and Int Conversion

```python
char = chr(97)
integer = ord('a')
```

# String Manipulation

```python
"WAT".isupper() #true
'wat'.islower() #true
"WAT".lower() #wat
"wat".upper() # WAT

# filter space and other things
''.join(e for e in string if e.isalnum())
# filter anything but alphabet
''.join(e for e in string if e.isalpha())
```

