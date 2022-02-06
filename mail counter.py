#get the file and read it 
name = input("Enter file name: ") 
text = open(name, "r") 

#store all emails and how many times are sent 
mails = dict() 

for line in text: 
    x = line.split()
    
    if line.startswith("From"): 
        mail = x[1] 
        mails[mail] = mails.get(mail, 0) + 1 

#find the most sent email 
big_count = None 
big_mail = None 

for key, value in mails.items(): 
    if big_count is None or value > big_count: 
        big_count = value
        big_mail = key 

#print the result 
print(big_mail, big_count)