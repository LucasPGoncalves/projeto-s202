from pprint import pp
from database import Graph, Divider

class AnimalDAO(object):

    def __init__(self):
        self.db = Graph()

    def createAnimal(self, animal):
        self.db.execute_query("CREATE (a:Animal:Pet{nome:$nome, idade:$idade, sexo:$sexo})",
        {'nome': animal.nome, 'idade': animal.idade, 'sexo': animal.sexo})
    
    def deleteAnimal(self, nome):
        self.db.execute_query("MATCH(a:Animal{nome:$nome}) DETACH DELETE a", {'nome': nome})
    
    def updateAnimal(self,animal, newName):
        self.db.execute_query("MATCH(a:Animal{nome:$nome}) SET a.nome = $newName, a.idade = $idade, a.sexo = $sexo",
        {'nome': animal.nome, 'idade': animal.idade, 'sexo': animal.sexo,'newName':newName})

    def readAnimals(self):
        pp(self.db.execute_query("MATCH(a:Animal) RETURN a"))

    def readAnimalByName(self,nome):
        pp(self.db.execute_query("MATCH(a:Animal{nome:$nome}) RETURN a", {'nome': nome}))

    def darDono(self,nomeAnimal, nomeDono):
        self.db.execute_query("match(c:Cliente{nome:$nomeDono}), (p:Pet{nome:$nomeAnimal}) CREATE (c)-[:DONO_DE]->(p)",
        {'nomeAnimal': nomeAnimal, 'nomeDono': nomeDono})

        
class Animal:
    def __init__(self,nome,sexo,idade):
        self.nome = nome
        self.sexo = sexo
        self.idade = idade

def viewAnimal():
    animalDao = AnimalDAO()
    option = input('1. Create\n2. Read\n3. Update\n4. Delete\n5. dar Dono\n6. Sair\n')
    Divider()
    if option == '1':
        animalaux =  Animal(nome=input("Insira o nome do animal: "),
                            sexo=input("Insira o sexo do animal: "),
                            idade=input("Insira a idade do animal: ") )
        animalDao.createAnimal(animal=animalaux)
        Divider()
    elif option == '2':
        option = input("1. Para ler todos os animais\n2. Para ler um animal especifico\n")
        if option == '1':
            animalDao.readAnimals()
            Divider()
        elif option == '2':
            animalDao.readAnimalByName(nome=input("Insira o nome do Animal para buscar: "))
            Divider()
    elif option == '3':
        animalaux =  Animal(nome=input("Insira o nome do animal: "),
                            sexo=input("Insira o novo sexo do animal: "),
                            idade=input("Insira a nova idade do animal: ") )
        novoNome = input("Insira o novo nome do animal: ")
        animalDao.updateAnimal(animal=animalaux, newName=novoNome)
        Divider()
    elif option == '4':
        animalDao.deleteAnimal(nome=input("Insira o nome do animal a deleter: "))
        Divider()
    elif option == '5':
        animalDao.darDono(nomeDono=input("Nome do Dono: "), nomeAnimal=input("Nome do Animal: "))
        Divider()
