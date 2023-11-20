class LMS:
    
    def options(self):
        print('**********LIBRARY MANAGEMENT SYSTEM**********')
        print('LIBRARY \n 1. AVALIABLE BOOKS \n 2. ADD A BOOK \n 3. BUY BOOK \n 4. EXIT ')
        try :
            view = int(input('Enter your option from 1 to 4:'))
        
            if view == 1:
                return self.readfile()

            elif view == 2:
                return self.addabook()

            elif view == 3:
                return self.buyabook()
        
            elif view == 4:
                sure=str(input('Are you sure you want to exit? y or n.'))
                if sure == 'y':
                    print('Bye!')

                elif sure == 'n':
                    print(book.options())

                else:
                    print(f'Enter a valid value. {book.options()}')
        
            else:
                print('Please enter a valid number!')
                print(book.options())
                

        except ValueError as e:
            print(f'Invalid input! {e}')
            print(book.options())
            
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
                f.write(f'\n{title},{author},{stock},${price}')
                f.close
            print('The book has been added to the library.') 
            con=str(input('Do you wish to continue? type \'y\' for yes and \'n\' for no.')).capitalize()
            if con == 'Y':
                print(book.options())
                
            elif con == 'N':
                print('Thank you for your time.')

            else: 
                print('Invalid input, try again.')
                print(book.options())

        except Exception as e:
            print(f'Invalid input. {e}')
            print(book.options())

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
