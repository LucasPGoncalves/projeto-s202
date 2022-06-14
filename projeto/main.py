from animal import viewAnimal
from groomer import viewGroomer
from cliente import viewClinte
from servicos import viewServicos
from database import Divider

while 1:
    option = input('1. Cliente\n2. Animal\n3. Groomer\n4. Servicos\n5. Sair\n')
    Divider()
    if option == '1':
        viewClinte()
    elif option == '2':
        viewAnimal()
    elif option == '3':
        viewGroomer()
    elif option == '4':
        viewServicos()
    elif option == '5':
        break

