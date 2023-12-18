data=[ ['Harry Potter','JK Rowling',12,'$2'],
        ['Start With Why','Simon Sinek',1,'$1.5'],
        ['Programming With Python','John Smith',0,'$1.5'],
        ['Piyush','piyush',3,'$2']]

class LMS:
    
    def options(self):
        print('**********LIBRARY MANAGEMENT SYSTEM**********')
        print('LIBRARY \n 1. AVALIABLE BOOKS \n 2. BUY BOOK \n 3. EXIT ')
        try :
            view = int(input('Enter your option from 1 to 4:'))
        
            if view == 1:
                self.readfile()

            elif view == 2:
                self.buyabook()
        
            elif view == 3:
                self.exit_program()
        
            else:
                print('Please enter a valid number!')
                self.options()
                
        except ValueError as e:
            print(f'Invalid input! {e}')
            print(book.options())
            
    def readfile(self):  
       print(data)

    def buyabook(self):
        print("Enter the details of the book you want to buy.")
        try :
            
            btitle= input('Enter the title of the book:').title()
            for i in data:
                if i[0]== btitle:
                   print(i[i][3])

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