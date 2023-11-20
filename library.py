class LMS:
    
    def options(self):
        print('LIBRARY \n 1. AVALIABLE BOOKS \n 2. BUY BOOKS \n 3. BORROW BOOKS \n 4. EXIT ')
        view = int(input('Enter your option from 1 to 4:'))
        if view == 1:
            return self.readfile()

        elif view == 2:
            return self.addabook()

        elif view == 3:
            return self.buyabook()

        else:
            print('b')
            
    def readfile(self):
        with open ('data.txt', 'r') as f:
          for line in f:
              print(line.strip())
        f.close()
            
    def addabook(self):
        print('Add the required info for the book to be added in the library.')
        title=str(input('Enter the title of the book:'))
        author=str(input('Enter the author of the book:'))
        stock=int(input('Enter the stock of the book:'))
        price=int(input('Enter the price of the book:'))
        with open ('data.txt','a') as f:
            f.write(f'{title},{author},{stock},{price}')
            f.close

    def buyabook(self):
        print("Enter the details of the book you want to buy")
        btitle=str(input('Enter the title of the book:'))
        bamount=int(input('Enter the amount of books you want to buy limited to 3 person:'))
        with open ('data.txt','r+') as f:
            lines=f.readlines()

            for line in lines:
                bdetails= line.strip().split(',')

                if btitle==bdetails[0]:
                    bdetails[2]=str(int(bdetails[2])-bamount)
                    f.seek(0)
                    line = ','.join(bdetails) + '\n'

                f.write(line)

    def borrowbooks(self):
        pass

book=LMS()
book.options()
