from database import Graph, Divider
from datetime import date
from pprint import pp

class ServicoDAO():
    def __init__(self):
        self.db = Graph()

    def createServico(self, nomeGroomer, nomeAnimal, servico, data, valor, id):
        self.db.execute_query("MATCH(g:Groomer{nome:$nomeGroomer}), (p:Pet{nome:$nomeAnimal}) CREATE (g)-[:CUIDA{servico:$servico, data:$data, valor:$valor, id:$id}]->(p)",
        {'nomeGroomer':nomeGroomer,'nomeAnimal':nomeAnimal,'servico':servico,'data':data,'valor':valor, 'id':id})

    def readServicos(self):
        pp(self.db.execute_query("MATCH(g:Groomer)-[c:CUIDA]->(p:Pet) RETURN g.nome, p.nome, c.servico"))
    
    def readGroomerServico(self, nome):
        pp(self.db.execute_query("MATCH(g:Groomer{nome:$nome})-[c:CUIDA]->(p:Pet) RETURN g.nome, p.nome, c.servico",
        {'nome': nome}))

    def readPetServicos(self, nome):
        pp(self.db.execute_query("MATCH(g:Groomer)-[c:CUIDA]->(p:Pet{nome:$nome}) RETURN g.nome, p.nome, c.servico",
        {'nome': nome}))

    def deleteServicos(self, id):
        self.db.execute_query("MATCH(g:Groomer)-[c:CUIDA{id:$id}]->(p:Pet) DELETE c",
        {'id': id})
    
    def addGroomerSalary(self, nome):
        self.db.execute_query("MATCH(g:Groomer{nome:$nome})-[c:CUIDA]->(p:Pet) SET g.salario = g.salario + c.valor",
        {'nome': nome})
    
    def subtractGroomerSalary(self, nome, id):
        self.db.execute_query("MATCH(g:Groomer{nome:$nome})-[c:CUIDA{id:$id}]->(p:Pet) SET g.salario = g.salario - c.valor",
        {'nome': nome, 'id': id})

def viewServicos():
    servicoDAO = ServicoDAO()
    option = input('1. Create\n2. Read\n3. Delete\n4. Sair\n')
    Divider()
    if option == '1':
        nome = input("Insira o nome do groomer: ")
        servicoDAO.createServico(nomeGroomer=nome, 
                                    nomeAnimal=input("Insira o nome do animal: "), 
                                    servico=input("Insira o servico: "), 
                                    data=date(int(input("Insira o ano: ")),int(input("Insira o mes: ")), int(input("Insira o dia: "))).strftime("%d/%m/%Y"),
                                    valor=int(input("Insira o valor: ")),
                                    id= int(input("Insira o id: ")))
        servicoDAO.addGroomerSalary(nome)
        Divider()
    elif option == '2':
        option = input("1. Para ler todos os servicos\n2. Para ler um servicos especificos\n")
        Divider()
        if option == '1':
            servicoDAO.readServicos()
            Divider()
        elif option == '2':
            option = input("1. Para ler servicos de um groomer espicifico\n2. Para ler um servicos de um animal\n")
            Divider()
            if option == '1':
                servicoDAO.readGroomerServico(nome=input("Insira o nome do groomer: "))
                Divider()
            elif option == '2':
                servicoDAO.readPetServicos(nome=input("Insira o nome do animal: "))
                Divider()
    
    elif option == '3':
        nome = input("Insira o nome do groomer: ")
        id = int(input("Insira o id do servico a deletar: "))
        servicoDAO.subtractGroomerSalary(nome,id)
        servicoDAO.deleteServicos(id)
        Divider()


