class ATM:
    def __init__(self):
        self.money = {'2000': 0, '500': 0, '200': 0, '100': 0}
        self.total = 0
    def status(self):
        for item in self.money.items():
            print(item)
        print('The total amount present is :', self.total)
    def load_amt(self, n):
        self.total += n
        while n > 0:
            if n >= 2000:
                self.money['2000'] += 1
                n -= 2000
            elif n >= 500:
                self.money['500'] += 1
                n -= 500
            elif n >= 200:
                self.money['200'] += 1
                n -= 200
            elif n >= 100:
                self.money['100'] += 1
                n -= 100
        print('Money loaded')
    def manual_load(self):
        amt = int(input("Enter the total amount you wish to enter: "))
        n = [0, 0, 0, 0]
        if amt >= 2000:
            n[0] = int(input(f'Enter the number of 2000 notes({amt//2000} at max): '))
            if n[0]*2000 <= amt:
                amt -= 2000 * n[0]
                if amt == 0:
                    self.money['2000'] += n[0]
                    self.money['500'] += n[1]
                    self.money['200'] += n[2]
                    self.money['100'] += n[3]
                    self.total += (2000 * n[0] + 500 * n[1] + 200 * n[2] + 100 * n[3])
                    print('Amount loaded successfully')
                    return
            else:
                print('The notes exceed the amount you want to enter')
                return 
        if amt >= 500:
            n[1] = int(input(f'Enter the number of 500 notes({amt//500} at max): '))
            if n[1]*500 <= amt:
                amt -= 500 * n[1]
                if amt == 0:
                    self.money['2000'] += n[0]
                    self.money['500'] += n[1]
                    self.money['200'] += n[2]
                    self.money['100'] += n[3]
                    self.total += (2000 * n[0] + 500 * n[1] + 200 * n[2] + 100 * n[3])
                    print('Amount loaded successfully')
                    return
            else: 
                print('The notes exceed the amount you want to enter')
                return
        if amt >= 200:
            n[2] = int(input(f'Enter the number of 200 notes({amt//200} at max): '))
            if n[2]*200 <= amt:
                amt -= 200 * n[2]
                if amt == 0:
                    self.money['2000'] += n[0]
                    self.money['500'] += n[1]
                    self.money['200'] += n[2]
                    self.money['100'] += n[3]
                    self.total += (2000 * n[0] + 500 * n[1] + 200 * n[2] + 100 * n[3])
                    print('Amount loaded successfully')
                    return
            else: 
                print('The notes exceed the amount you want to enter')
                return 
        if amt >= 100:
            n[3] = int(input(f'Enter the number of 100 notes: ({amt//100} at max)'))
            if n[3]*100 == amt:
                self.money['2000'] += n[0]
                self.money['500'] += n[1]
                self.money['200'] += n[2]
                self.money['100'] += n[3]
                self.total += (2000 * n[0] + 500 * n[1] + 200 * n[2] + 100 * n[3])
                print('Amount loaded successfully')
            else:
                print('The notes do not satisfy the amount you want to enter')
                return

        
        
    def withdraw_amt(self, n):
        if self.total < n:
            print('Not Enough money in ATM')
        else:
            count = {'2000': 0, '500': 0, '200': 0, '100': 0}
            amount_left = n
            for key in ['2000', '500', '200', '100']:
                while amount_left >= int(key) and self.money[key] > 0:
                    count[key] += 1
                    amount_left -= int(key)
                    self.money[key] -= 1
            if amount_left == 0:
                self.total -= n
                print('Transaction successful')
            else:
                print('Not enough denominations')
    
atm = ATM()
def Menu():
    print('Enter 1 to automatically load to atm\nEnter 2 to manually load\nEnter 3 to withdraw\nEnter 4 to see ATM status \nEnter 5 to exit')

while True:
    try:
        Menu()
        a = int(input('Enter your choice:'))
        if a == 1:
            k = int(input('Enter amt you want to load:'))
            atm.load_amt(k)
        elif a==2:
            atm.manual_load()
        elif a ==3:
            k = int(input('Enter amt you want to withdraw:'))
            atm.withdraw_amt(k)
        elif a == 4:
            atm.status()
        elif a ==5:
            break
    except:
        print('Something went wrong')
