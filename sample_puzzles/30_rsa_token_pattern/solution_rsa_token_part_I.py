# RSA tokens produce a sequence of pseudorandom six-digit numbers
#     that update every 60 seconds. 
# The six-digit numbers are used to help authenticate users that
#     log into systems, typically by requiring the user to supply
#     both a PIN and the six-digit number.
# On the screen, the numbers are broken into two groups of three
#     and might look something like the following:
#     * 247 456
#     * 765 294
#     * 232 543

# Interestingly, the six-digit numbers occasionally have patterns
#     such as the following:
#     * 123 321     - a palindrome if you consider all six numbers
#     * 121 454     - two mini palindromes, one in each group of three
#                     (they do not need to be identical)
#     * 123 679     - rising numbers (each subsequent number is equal to 
#                     or larger than the previous number)
#     * 654 321     - falling numbers (each subsequent number is
#                     equal to or smaller than the previous number)

# For example, given the following, we can categorize each six-digit number
#     and count the number of occurrences...

#     * 123 321     palindrome
#     * 247 456     no category
#     * 765 294     no category
#     * 123 679     rising
#     * 345 543     palindrome

# the largest count is 2 (palindrome) and smallest count is 1 (rising), 
#     ignore the no category samples.

# Given the values in the file rsa_token_values_I.txt:
# Count how many times each pattern occurs and identify the smallest and 
# largest counts (ignore the count of items that don't match any category).
# 

# ============================================================================
# Put your code here:

def cleaner(token):
    return token.replace(' ', '')

def ispalindromic(token):
    token = cleaner(token)
    if token == token[::-1]:
        return True
    return False

def isminipalindromic(token):
    token = cleaner(token)
    first_half = token[:3]
    last_half = token[3:]
    if (first_half == first_half[::-1] and
        last_half == last_half[::-1]):
        return True
    return False
    
def isrising(token):
    token = cleaner(token)
    current = token[0]
    for digit in token[1:]:
        if digit < current:
            return False
        current = digit    
    return True

def isfalling(token):
    token = cleaner(token)
    reverse_token = token[::-1]
    return isrising(reverse_token)


counter = {}
for item in ['pal', 'mini', 'rising', 'falling']:
    counter[item] = 0
    

with open ('rsa_token_values_I.txt') as fin:
    for line in fin:
        token = line.strip()
        if ispalindromic(token):
            counter['pal'] += 1
            print('pal:', token)
        if isminipalindromic(token):
            counter['mini'] += 1
            print('min:', token)
        if isrising(token):
            counter['rising'] += 1
            print('ris:', token)
        if isfalling(token):
            counter['falling'] += 1
            print('fal:', token)            
print(counter)
        
        