data=[ ['Harry Potter','JK Rowling',12,'$2'],
        ['Start With Why','Simon Sinek',10,'$1.5'],
        ['Programming With Python','John Smith',30,'$1.5'],
        ['Piyush','piyush',3,'$2']]
btitle= str(input('Enter the title of the book:')).title()    
bamount=int(input('Enter the amount of books you want to buy max 2:'))

for i in data:
    if i[0] == btitle:
        if 0 < bamount <= i[2]:
            current_stock= i[2]-bamount
            print(current_stock)
            
