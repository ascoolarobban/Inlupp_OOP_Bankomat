import funcs
from funcs import register
# from funcs import login
from funcs import Clear
from funcs import kontoHantering
from funcs import deathstar
Clear()
while True:
    print("\u001b[38;5;198m ©Robin Ellingsen 2020 -THE BANK OF THE GALACTIC EMPIRE®\n\u001b[0m")
    print(r'''
████████╗██╗  ██╗███████╗    ██████╗  █████╗ ███╗   ██╗██╗  ██╗    
╚══██╔══╝██║  ██║██╔════╝    ██╔══██╗██╔══██╗████╗  ██║██║ ██╔╝    
   ██║   ███████║█████╗      ██████╔╝███████║██╔██╗ ██║█████╔╝     
   ██║   ██╔══██║██╔══╝      ██╔══██╗██╔══██║██║╚██╗██║██╔═██╗     
   ██║   ██║  ██║███████╗    ██████╔╝██║  ██║██║ ╚████║██║  ██╗    
   ╚═╝   ╚═╝  ╚═╝╚══════╝    ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝    
 ██████╗ ███████╗    ████████╗██╗  ██╗███████╗                     
██╔═══██╗██╔════╝    ╚══██╔══╝██║  ██║██╔════╝                     
██║   ██║█████╗         ██║   ███████║█████╗                       
██║   ██║██╔══╝         ██║   ██╔══██║██╔══╝                       
╚██████╔╝██║            ██║   ██║  ██║███████╗                     
 ╚═════╝ ╚═╝            ╚═╝   ╚═╝  ╚═╝╚══════╝                     
 ██████╗  █████╗ ██╗      █████╗  ██████╗████████╗██╗ ██████╗      
██╔════╝ ██╔══██╗██║     ██╔══██╗██╔════╝╚══██╔══╝██║██╔════╝      
██║  ███╗███████║██║     ███████║██║        ██║   ██║██║           
██║   ██║██╔══██║██║     ██╔══██║██║        ██║   ██║██║           
╚██████╔╝██║  ██║███████╗██║  ██║╚██████╗   ██║   ██║╚██████╗      
 ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝ ╚═════╝   ╚═╝   ╚═╝ ╚═════╝      
███████╗███╗   ███╗██████╗ ██╗██████╗ ███████╗                     
██╔════╝████╗ ████║██╔══██╗██║██╔══██╗██╔════╝                     
█████╗  ██╔████╔██║██████╔╝██║██████╔╝█████╗                       
██╔══╝  ██║╚██╔╝██║██╔═══╝ ██║██╔══██╗██╔══╝                       
███████╗██║ ╚═╝ ██║██║     ██║██║  ██║███████╗██╗                  
╚══════╝╚═╝     ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝╚═╝''')
    print("----------------------")
    print("****HUVUDMENYMENY****")
    print("1. Skapa konto")
    print("2. Logga in.")
    print("3. Avsluta.")
    print("----------------------")
    selected = int(input("\nAnge Menyval: \t"))
    Clear()
    if (selected == 3):
        # print ("\nTACK FÖR ATT DU VÄLJER THE BANK OF THE GALACTIC EMPIRE!")
        Clear()
        deathstar()
        break
    if (selected == 1):
        register()
        
    if (selected == 2):
        kontoHantering()
