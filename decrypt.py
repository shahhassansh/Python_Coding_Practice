"""

An Example of word encryption

To encrypt the word “crime”

Decrypted message:	c	r	i	m	e
Step 1:	            99	114	105	109	101
Step 2:	            100	214	319	428	529
Step 3:	            100	110	111	116	113
Encrypted message:	d	n	o	t	q

"""

## The below code takes a decrypted word as input and returns encrypted word as output.
## 
## Input:
## 
## "dnotq" 
## 
## Output:
##
## "crime"
   
def decrypt(word):
    out = []
    prev_s1 = 1
    for i in range(0,len(word)):
        asc = ord(word[i])
        s2 = asc - prev_s1
        prev_s1 = asc
        while s2 < 97:
            s2+=26
        out.append(chr(s2))
    return ''.join(out)

print(decrypt("dnotq"))