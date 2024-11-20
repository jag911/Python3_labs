#! /usr/bin/python
# Exercise 6, string formatting and regular expressions.
import re

infile = open(r'/Users/thomas/python/Python3_labs/labs/postcodes.txt', 'r')

# Variables for counting valid and invalid codes (part b)
valid = 0
invalid = 0

for postcode in infile:
    # The variable 'postcode' contain the line read from the file.
    
    # Ignore empty lines.
    if postcode.isspace(): continue
    
    # TODO (a): Remove newlines, tabs and spaces.
    postcode = re.sub(r"[ \t\n\f]","",postcode)
    
    # TODO (a): Convert to uppercase.
    postcode = postcode.upper()

    # TODO (a): Insert a space before the final digit and 2 letters.
    postcode = re.sub(r"([0-9][A-Z][A-Z])$",r" \1", postcode)
    
    # Print the reformatted postcode.
    #print (postcode)

    # TODO (b) Validate the postcode, returning a match object 'm'.
    m = re.match(r"^[A-Z]{1,2}[0-9]{1,2}[A-Z]? [0-9][A-Z][A-Z]",postcode)   # TODO (b) Replace this line with a call to re.match().
    
    if m:
        valid += 1
        print(f"Valid: {postcode}")
    else:
        invalid += 1
        print(f"ERROR: {postcode}")
        

infile.close()

# TODO (b) Print the valid and invalid totals.

print(f"Valid = {valid} : Invalid = {invalid}")