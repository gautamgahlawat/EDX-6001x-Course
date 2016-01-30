count = 0
vowel = ('a','e','i','o','u')
for chr in s:
    if chr in vowel:
        count += 1
print "Number of vowels: "+str(count)