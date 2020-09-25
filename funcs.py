import os
import time
from datetime import date, datetime
import csv
from csv import reader
today = date.today()
allAccounts = {}
balance = 0
now = datetime.now()
nowTime = now.strftime("%H:%M:%S")





def Clear():
    def clear(): return os.system("clear")
    clear()

def loading():
    for i in range(5):
        print(".", end="")
        time.sleep(1)

def changeBalance(username):
    amount = input("Ange belopp: ₹ ")

    with open("accounts.csv", 'r+') as read_obj:
        csv_reader = reader(read_obj)
        list_of_rows = list(csv_reader)
        for row in list_of_rows:
            if row[0]== username:
                newBalance = str(float(row[2]) + float(amount))
                row[2] = newBalance

    with open("accounts.csv", "w") as ouf:
        writer = csv.writer(ouf)
        writer.writerows(list_of_rows)
        print("\nInsatt summa: ₹",(amount) ,(today), (nowTime))
        print (f"Aktuellt saldo: ₹ {newBalance}")
    

def withdrawl(username,):
    while True:
        amount = input("Ange belopp: ₹ ")
        with open("accounts.csv", 'r+') as read_obj:
            csv_reader = reader(read_obj)
            list_of_rows = list(csv_reader)
            for row in list_of_rows:
                if row[0]== username:
                    
                    newBalance = str(float(row[2]) - float(amount))
                    row[2] = newBalance  
        with open("accounts.csv", "w") as ouf:
            writer = csv.writer(ouf)
            writer.writerows(list_of_rows)     
            print("\nUttag: ₹",amount)
            print (f"Aktuellt saldo: ₹{newBalance}, {(today)}, {(nowTime)}")
        break


class userAccount:
    def __init__(self, account_id, passwords, balance, creationDate, creationTime):
        self.account_id = account_id
        self.passwords = passwords
        self.balance = 0
        self.creationDate = creationDate
        self.creationTime = creationTime
        



    def Balance(self):
        print("\n Aktuellt saldo =", self.balance)


def register():
    while True:
        username = (input("Ange önskat kontonummer (****): "))
        try:
            tryInt = int(username)
        except ValueError:
            print("Använd endast siffror!")
            break

        if (len(username)) != 4:
            print("Ditt kontonummer måste bestå utav 4 siffror.")
            break
        else:
        
            Clear()
            password = (input("Ange pinkod (****): "))

            try:
                tryInt = int(password)
            except ValueError:
                print("använd endast siffror!")
                break

            if (len(password)) != 4:
                print("Ditt lösenord måste bestå utav 4 siffror, försök igen")
                break


            else:
                user = userAccount(username, password, balance, today, nowTime)
                with open("accounts.csv", "a+") as file:
                    csv_app = csv.writer(file)
                    csv_app.writerow([username]+[password]+[balance]+[today] +[nowTime])
                print("Skapar konto", end="")
                loading()
                Clear()
                print(f"\nKontonummer: #{username}, registrerat den:", (today))
                print(
                    "\nTack för att du väljer The Bank Of The Galactic Republic.")
                print("\n----------------------------------\n")
                input("Tryck på Enter för att komma tillbaka till menyn.")
            break


def kontoHantering():
    while True:
        username= input("Ange kontonummer (****):")
        pin = input("Ange pinkod (****):")
        with open("accounts.csv", "r") as csvfile:
            csv_reader = csv.reader(csvfile,delimiter=',')
            login = False
            for row in csv_reader:
                if username == row[0] and pin == row[1]:
                    balance= row[2]
                    login = True
                    print (f"Kontonummer: #{username},\nAktuellt saldo: ₹ {balance}")
                    loginMenu(username, pin)
            break
        if not login:
            print("Kontonummer ej registrerat.")
            loading()

def loginMenu(username,password):
        while True:
            print("----------------------")
            print("****KONTO****")
            print("1. Insättning")
            print("2. Uttag.")
            print("3. Avsluta.")
            print("----------------------")
            selected = int(input("\nAnge Menyval: \t"))
            if (selected == 3):
                Clear()
                print ("\u001b[38;5;198m TACK FÖR ATT DU VÄLJER THE BANK OF THE GALACTIC EMPIRE!\n\u001b[0m")
                time.sleep(3)
                break
            if (selected == 1):
                changeBalance(username)
                
            if (selected == 2):
                withdrawl(username)





def deathstar():
    print('''
    _                                            _
   T T                                          T T
   | |                                          | |
   | |                                          | |
   | |                                          | |
   | |                                          | |
   | |                                          | |
   | |                                          | |
   | |                   ____                   | |
   | |            ___.r-"`--'"-r.____           | |
   | |.-._,.,---~"_/_/  .----.  \_\_"~---,.,_,-.| |
   | ]|.[_]_ T~T[_.-Y  / \  / \  Y-._]T~T _[_].|| |
  [|-+[  ___]| [__  |-=[--()--]=-|  __] |[___  ]+-|]
   | ]|"[_]  l_j[_"-l  \ /  \ /  !-"_]l_j  [_]~|| |
   | |`-' "~"---.,_\"\  "o--o"  /"/_,.---"~" `-'| |
   | |             ~~"^-.____.-^"~~             | |
   | |                                          | |
   | |                                          | |
   | |                                          | |
   | |                                          | |  Thank you for using The Bank Of The Galactic Empire.
   | |                                          | |  In Space Superiority we trust.
   | |                                          | |  -Darth Vader, CEO.
   | |                                          | |
   l_i                                          l_j 




    ''')

if __name__=="__main__":
    print ("Den här filen är inte meningen att köras som Main. Var god använd filen som heter \"Main\". ")
