from pprint import pp
from database import Graph, Divider

class GroomerDAO(object):

    def __init__(self):
        self.db = Graph()

    def createGroomer(self, groomer):
        self.db.execute_query("CREATE (g:Pessoa:Groomer{nome:$nome, idade:$idade, salario:$salario, telefone:$telefone})",
        {'nome': groomer.nome, 'idade': groomer.idade, 'salario': groomer.salario, 'telefone': groomer.telefone})
    
    def deleteGroomer(self, nome):
        self.db.execute_query("MATCH(g:Groomer{nome:$nome}) DETACH DELETE g", {'nome': nome})
    
    def updateGroomer(self, groomer, newName):
        self.db.execute_query("MATCH(g:Groomer{nome:$nome}) SET g.nome = $newName, g.idade = $idade, g.telefone = $telefone",
        {'nome': groomer.nome, 'idade': groomer.idade, 'telefone': groomer.telefone, 'newName':newName})

    def readGroomers(self):
        pp(self.db.execute_query("MATCH(g:Groomer) RETURN g"))

    def readGroomerByName(self,nome):
        pp(self.db.execute_query("MATCH(g:Groomer{nome:$nome}) RETURN g", {'nome': nome}))      

class Groomer:
    def __init__(self,nome,idade,telefone):
        self.nome = nome
        self.idade = idade
        self.salario = 1000
        self.telefone = telefone

def viewGroomer():
    groomerDao = GroomerDAO()
    option = input('1. Create\n2. Read\n3. Update\n4. Delete\n5. Sair\n')
    Divider()
    if option == '1':
        groomeraux = Groomer(nome=input("Insira o nome do groomer: "),
                                idade=input("Insira a idade do groomer: "),
                                telefone=input("Insira o telefone do groomer: "))
        groomerDao.createGroomer(groomer=groomeraux)
        Divider()
    elif option == '2':
        option = input("1. Para ler todos os groomers\n2. Para ler um groomer especifico\n")
        if option == '1':
            groomerDao.readGroomers()
            Divider()
        elif option == '2':
            groomerDao.readGroomerByName(nome=input("Insira o nome do groomer para buscar: "))
            Divider()
    elif option == '3':
        groomeraux = Groomer(nome=input("Insira o nome do groomer: "),
                                idade=input("Insira a nova idade do groomer: "),
                                telefone=input("Insira o novo telefone do groomer: "))
        novoNome = input("Insira o novo nome do groomer: ")
        groomerDao.updateGroomer(groomer=groomeraux, newName=novoNome)
        Divider()
    elif option == '4':
        groomerDao.deleteGroomer(nome=input("Insira o nome do groomer a deletar: "))
        Divider()