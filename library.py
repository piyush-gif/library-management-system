class LMS:
    
    def options(self):
        print('LIBRARY \n 1. AVALIABLE BOOKS \n 3. ADD A BOOK \n 3. BUY BOOK \n 4. EXIT ')
        try :
            view = int(input('Enter your option from 1 to 4:'))
        
            if view == 1:
                return self.readfile()

            elif view == 2:
                return self.addabook()

            elif view == 3:
                return self.buyabook()
        
            elif view == 4:
                return 0
        
            else:
                print('Please enter a valid number!')

        except ValueError as e:
            print(f'Invalid input! {e}')   
            
    def readfile(self):
        with open ('data.txt', 'r') as f:
          for line in f:
              print(line.strip())
        f.close()
            
    def addabook(self):
        print('Add the required info for the book to be added in the library.')
        try:
            title=str(input('Enter the title of the book:')).title()
            author=str(input('Enter the author of the book:'))
            stock=int(input('Enter the stock of the book:'))
            price=int(input('Enter the price of the book:'))
            with open ('data.txt','a') as f:
                f.write(f'{title},{author},{stock},{price}')
                f.close
        except Exception as e:
            print(f'Invalid input. {e}')

    def buyabook(self):
        print("Enter the details of the book you want to buy")
        try :
    
            btitle=str(input('Enter the title of the book:')).title()
            bamount=int(input('Enter the amount of books you want to buy limited to 3 person:'))
            with open ('data.txt', 'r') as f:
                lines=f.readlines()

            with open ('data.txt', 'w') as f:
                for line in lines:
                    bdetails= line.strip().split(',')

                    if btitle==bdetails[0]:
                        bdetails[2]=str(int(bdetails[2]) - bamount)
                        f.write(','.join(bdetails)+'\n')
                        
                    else:
                        f.write(line)      
                
        except Exception as e:
            print(f'Enter a Valid Input!{e}')


book=LMS()
book.options()
