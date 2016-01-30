start = 0
count = 0
sub ='bob'
while True:
    start = s.find(sub,start)+1
    if start>0:
        count+=1
    else:
        print count
        break
