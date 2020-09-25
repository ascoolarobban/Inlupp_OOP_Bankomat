import csv
from csv import reader



with open('accounts.csv', 'r+') as read_obj:

    csv_reader = reader(read_obj)
    list_of_rows = list(csv_reader)


    for row in list_of_rows:
        if row[0]== username:
            newBalance = str(float(row[2]) + float(amount))
            row[2] = newBalance
            print(list_of_rows)
            

with open("accounts.csv", "w") as ouf:
    writer = csv.writer(ouf)
    writer.writerows(list_of_rows)
        #         print("\nInsatt summa: ₹",(amount))
        #         print (f"Aktuellt saldo: ₹ {newBalance}")





# with open("accounts.csv", "a+") as file:
#                     csv_app = csv.writer(file)w
#                     csv_app.writerow([username]+[password]+[balance]+[today] +[nowTime])

# with open("accounts.csv", "r+") as csvfile:
#             csv_reader = csv.reader(csvfile,delimiter=',')
#             for row in csv_reader:
#                 if username == row[0]:
#                     balance= row[2]
