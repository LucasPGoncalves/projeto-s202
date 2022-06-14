from pprint import pp
from database import Graph, Divider

class ClienteDAO(object):

    def __init__(self):
        self.db = Graph()

    def createCliente(self, cliente):
        self.db.execute_query("CREATE (c:Pessoa:Cliente{nome:$nome, idade:$idade, telefone:$telefone, email:$email})",
        {'nome': cliente.nome, 'idade': cliente.idade, 'telefone': cliente.telefone, 'email': cliente.email})
    
    def deleteCliente(self, nome):
        self.db.execute_query("MATCH(c:Cliente{nome:$nome}) DETACH DELETE c", {'nome': nome})
    
    def updateCliente(self, cliente, newName):
        self.db.execute_query("MATCH(c:Cliente{nome:$nome}) SET c.nome = $newName, c.idade = $idade, c.telefone = $telefone, c.email = $email",
        {'nome': cliente.nome, 'idade': cliente.idade, 'telefone': cliente.telefone, 'email': cliente.email ,'newName':newName})

    def readClientes(self):
        pp(self.db.execute_query("MATCH(c:Cliente) RETURN c"))

    def readClienteByName(self,nome):
        pp(self.db.execute_query("MATCH(c:Cliente{nome:$nome}) RETURN c", {'nome': nome}))

class Cliente:
    def __init__(self,nome,telefone,idade,email):
        self.nome = nome
        self.telefone = telefone
        self.idade = idade
        self.email = email

def viewClinte():
    clienteDao = ClienteDAO()
    option = input('1. Create\n2. Read\n3. Update\n4. Delete\n5. Sair\n')
    Divider()
    if option == '1':
        clienteaux =  Cliente(nome=input("Insira o nome do cliente: "),
                                telefone=input("Insira o telefone do cliente: "),
                                idade=input("Insira a idade do cliente: "),
                                email=input("Insira o email do cliente: ") )
        clienteDao.createCliente(cliente=clienteaux)
        Divider()
    elif option == '2':
        option = input("1. Para ler todos os clientes\n2. Para ler um cliente especifico\n")
        if option == '1':
            clienteDao.readClientes()
            Divider()
        elif option == '2':
            clienteDao.readClienteByName(nome=input("Insira o nome do cliente para buscar: "))
            Divider()
    elif option == '3':
        clienteaux = Cliente(nome=input("Insira o nome do cliente: "),
                                telefone=input("Insira o novo telefone do cliente: "),
                                idade=input("Insira a nova idade do cliente: "),
                                email=input("Insira o novo email do cliente: ") )
        novoNome = input("Insira o novo nome do cliente: ")
        clienteDao.updateCliente(cliente=clienteaux, newName=novoNome)
        
    elif option == '4':
        clienteDao.deleteCliente(nome=input("Insira o nome do cliente a deletar: "))
        Divider()

        