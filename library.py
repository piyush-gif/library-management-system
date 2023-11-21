class LMS:
    
    def options(self):
        print('**********LIBRARY MANAGEMENT SYSTEM**********')
        print('LIBRARY \n 1. AVALIABLE BOOKS \n 2. ADD A BOOK \n 3. BUY BOOK \n 4. EXIT ')
        try :
            view = int(input('Enter your option from 1 to 4:'))
        
            if view == 1:
                self.readfile()

            elif view == 2:
                self.addabook()

            elif view == 3:
                self.buyabook()
        
            elif view == 4:
                self.exit_program()
        
            else:
                print('Please enter a valid number!')
                self.options()
                
        except ValueError as e:
            print(f'Invalid input! {e}')
            print(book.options())
            
    def readfile(self):
        with open ('data.txt', 'r') as f:
          print('Here are the list of books in the library.')
          for line in f:
              print(line.strip())
          self.continue_program()
            
    def addabook(self):
        print('Add the required info for the book to be added in the library.')
        try:
            title = str(input('Enter the title of the book:')).title()
            author = str(input('Enter the author of the book:'))
            stock = int(input('Enter the stock of the book:'))
            price = int(input('Enter the price of the book:'))
            with open ('data.txt','a') as f:
                f.write(f'\n{title},{author},{stock},${price}')
                f.close()
            print('The book has been added to the library.') 
            self.continue_program()

        except Exception as e:
            print(f'Invalid input. {e}')
            print(book.options())

    def buyabook(self):
        print("Enter the details of the book you want to buy.")
        
        try :
    
            btitle = str(input('Enter the title of the book:')).title()
            book_found = False
            with open ('data.txt', 'r') as f:
                lines = f.readlines()
            updated_lines = []

            for line in lines:
                bdetails = line.strip().split(',')

                if btitle == bdetails[0]:
                    book_found = False
                    bamount = int(input('Enter the amount of books you want to buy limited to 3 person:'))
                    current_stock=int(bdetails[2])
                    if 0 < bamount <=3 and current_stock >= bamount:
                        bdetails[2] = str(current_stock - bamount)
                        updated_lines.append(','.join(bdetails) + '\n')
                    else :
                        print('Invalid input! Either the amount is invalid or out of stock.')
                else:
                        updated_lines.append(lines)
            with open ('data.txt', 'w') as f:
                f.writelines(updated_lines)
                            
            if not book_found:
                    print('There is no such book in the database.')

            self.continue_program()
                
        except Exception as e:
            print(f'Enter a Valid Input!{e}')
            self.options()

    def exit_program(self):
        sure = str(input('Are you sure you want to exit? y or n.')).capitalize()
        if sure == 'Y':
                print('Bye!')
        elif sure == 'N':
            print(book.options())
        else:
            print(f'Enter a valid value. {self.options()}')

    def continue_program(self):
        con = str(input('Do you wish to continue? Type \'y\' for yes and \'n\' for no.')).capitalize()
        if con == 'Y':
            self.options()
        elif con == 'N':
            print('Thank you for your time.')
        else:
            print('Invalid input, try again.')
            self.options()

book=LMS()
book.options()