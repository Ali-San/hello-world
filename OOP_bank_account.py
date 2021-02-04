'''
This is a small program I wrote to use what I learned from:
https://dbader.org/blog/python-dunder-methods
'''

class Account():
    '''A simple account class.'''
    
    # Object initialization
    def __init__(self, owner, amount=0):
        '''This is the constructor that lets us create objects from this class.'''
        self.owner = owner
        self.amount = amount
        self._transactions = []
    
    # Object Representation (a favor to your fellow coders, and your future self)
    def __repr__(self):
        return 'Account({!r}, {!r})'.format(self.owner, self.amount)
        
    def __str__(self):
        return 'Account of {} with starting amount of: {}'.format(self.owner, self.amount)
    
    # Iteration
    def __len__(self):
        return len(self._transactions)
    
    def __getitem__(self, position):
        return self._transactions[position]
    
    def __reversed__(self):
        return self[::-1]
    
    # Operator overloading for comparing accounts (remember to 'from functools import total_ordering' to get the whole thing)
    def __eq__(self, other):
        return self.balance == other.balance
    
    def __lt__(self, other):
        return self.balance < other.balance
    
    # Operator overloading for merging accounts
    def __add__(self, other):
        owner = '{}&{}'.format(self.owner, other.owner)
        start_amount = self.amount + other.amount
        acc = Account(owner, start_amount)
        for t in self._transactions + other._transactions:
            acc.add_transaction(t)
        return acc
    
    # Context management support (__enter__, __exit__) and the 'with' statement
    def __enter__(self):
        print('ENTER WITH: Making backup of transactions for rollback')
        self._copy_transactions = list(self._transactions)
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print('EXIT WITH:', end=' ')
        if exc_type:
            self._transactions = self._copy_transactions
            print('Rolling back to previous transactions')
            print('Transaction resulted in {} ({})'.format(exc_type.__name__, exc_val))
        else:
            print('Transaction OK')
    
    # this could also be __call__
    def print_statement(self):
        print('Start amount: {}'.format(self.amount))
        print('Transactions: ')
        for transaction in self:
            print(transaction)
        print('\nBalance: {}'.format(self.balance))
    
    # a method to add transactions to the self._transactions list
    def add_transaction(self, amount):
        if not isinstance(amount, int):
            raise ValueError("Please use int for amount.")
        self._transactions.append(amount)
    
    # a method to print the accounts last 10 movements
    def last_10_moves(self):
        reversed = self._transactions[::-1]
        for i in range(len(reversed)):
            if i < 10:
                print(reversed[i])
    
    # a property method to get the balance
    @property
    def balance(self):
        return self.amount + sum(self._transactions)

# this was a 'helper method' in the tutorial but for whatever reason it doesn't work that way (I couldn't find an answer anywhere), but it works as a function, so here it is
def validate_transaction(acc, amount_to_add):
    with acc as a:
        print('Adding {} to account'.format(amount_to_add))
        a.add_transaction(amount_to_add)
        print('New balance would be: {}'.format(a.balance))
        if a.balance < 0:
            raise ValueError('Sorry, cannot go in debt!')


# program starts here
all_acc = {}

# welcome message, explain options
print("Welcome to Play-Pretend Bank, where your imaginary savings are forever safe.", end='\n\n')
# print("Choose an operation from the options below:\n\n☆ 1\tOpen an account\n☆ 2\tMake a deposit/Withdraw money from your account\n☆ 3\tCheck account balance\n☆ 4\tSee account statement\n☆ 5\tMerge accounts\n☆ 6\tExit bank")

while True:
    print("\nChoose an operation from the options below:\n\n☆ 1\tOpen an account\n☆ 2\tMake a deposit/Withdraw money from your account\n☆ 3\tCheck account balance\n☆ 4\tSee account statement\n☆ 5\tMerge accounts\n☆ 6\tExit bank")
    user_input = int(input("\nEnter the operation number: "))
    
    # open account 1
    if user_input == 1:
        print("Please tell me your name and make a first deposit.")
        open_name = input("Enter your name: ")
        open_amount = int(input("Enter the amount you would like to deposit: "))
        acc = Account(open_name, open_amount)
        if len(all_acc) == 0:
            all_acc[1] = acc
            print("Done. Your account number is 1")
        else:
            all_acc[len(all_acc) + 1] = acc
            print("Done. Your account number is {}".format(len(all_acc)))

    # deposit / withdraw 2
    elif user_input == 2:
        print("If you want to make a deposit, enter a positive number.\nIf you would like to withdraw money, enter a negative number.")
        acc_num = int(input("Enter account number: "))
        transaction = int(input("Enter amount: "))
        all_acc[acc_num].add_transaction(transaction)
    
    # get account balance 3
    elif user_input == 3:
        acc_num = int(input("Enter account number: "))
        print("The current balance for account number {} is {}".format(acc_num, all_acc[acc_num].balance))
    
    # get account statement 4
    elif user_input == 4:
        acc_num = int(input("Please enter account number: "))
        print("\n\n\nStatement of all activity for account number {}:".format(acc_num), end="\n\n")
        print("Balance: {}".format(all_acc[acc_num].balance))
        print("Total number of transactions: {}".format(len(all_acc[acc_num])))
        print("Last 10 movements:")
        all_acc[acc_num].last_10_moves()
    
    # merge accounts 5
    elif user_input == 5:
        if len(all_acc) < 2:
            print("I need at least 2 accounts, I only have 1. Please open another account.")
        else:
            acc_1 = int(input("Enter the first account's number: "))
            acc_2 = int(input("Enter the second account's number: "))
            all_acc[len(all_acc) + 1] = all_acc[acc_1] + all_acc[acc_2]
            all_acc[len(all_acc)].print_statement()
    
    # exit bank
    elif user_input == 6:
        print("Thank you for doing business with us.\nGoodbye.")
        break
    # if user_input is not valid:
    else:
        print("Please enter a valid operation number (1 to 6).")