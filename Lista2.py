import math

#Questão 1
class Circulo:
    def __init__(self, raio):
        self.raio = raio

    def calcular_area(self):
        return math.pi * (self.raio * self.raio)

circulo = Circulo(4)
print(f'Área do círculo: {circulo.calcular_area():.2f}')

#Questão 2
class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        
    def detalhes(self):
        return f'O Titulo é: {self.titulo} e o Autor é: {self.autor}'
    
livro = Livro('Harry Potter: Relíquias da morte parte 2', 'J.K Rowling')
print(livro.detalhes())

#Questão 3

class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
        
    def calcular_area(self):
        return self.base * self.altura
        
retangulo = Retangulo(5, 2)
print(f'A área do retângulo é: {retangulo.calcular_area()}')  

#Questão 4

class ContaBancaria:
    def __init__(self, titular, saldo = 0):
        self.saldo = saldo
        self.titular = titular
        
    def depositar(self, valordep):
        self.saldo += valordep
        
    def sacar(self, valordep):
        if valordep <= self.saldo:
            self.saldo -= valordep
        else:
            print('Saldo Insuficiente!')
            
    def mostrarsaldo(self):
        return f'Saldo atual: {self.saldo:.2f}'
    
contabancaria = ContaBancaria('Yuri', 5000)
contabancaria.depositar(1000)
contabancaria.sacar(500)
print(contabancaria.mostrarsaldo())

#Questão 5

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
    def falar(self):
        print(f'Meu nome é, {self.nome}, e tenho {self.idade} anos')

pessoa = Pessoa('Yuri', 19)
pessoa.falar()

#Questão 6

class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
        
    def calcular_total(self):
        return self.preco * self.quantidade
    
produto = Produto('Pringles', 15, 3)
print(f'O Produto é, {produto.nome}, e o Valor total é: {produto.calcular_total()}')

#Questao 7

class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        
    def detalhes(self):
        return f'A Marca do carro é: {self.marca}; O modelo do carro é: {self.modelo}; O ano do carro é: {self.ano}.'
    
carro = Carro('Toyota','Corolla', 2013)
print(carro.detalhes())

#Questão 8

class Aluno:
    def __init__(self, nome, notas):
        self.nome = nome
        self.notas = notas

    def calcular_media(self):
        return sum(self.notas) / len(self.notas)

aluno = Aluno("Ana", [5, 9, 10, 9])
print(f'O nome do aluno é: {aluno.nome}, e as médias da nota são: {aluno.calcular_media()}') 

#Questão 9

class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
        
    def calcular_perimetro(self):
        return self.lado1 + self.lado2 + self.lado3
    
triangulo = Triangulo(5, 5, 7)
print(f'O Perímetro desse triângulo é: {triangulo.calcular_perimetro()}')

#Questão 10

class Funcionario:
    def __init__(self, nome, salario, cargo):
        self.nome = nome
        self.salario = salario
        self.cargo = cargo

    def aumentar_salario(self, percentual):
        aumento = self.salario * (percentual / 100)
        self.salario += aumento

funcionario = Funcionario("Yuri", 5000, "Gerente")
funcionario.aumentar_salario(20)
print(funcionario.salario)  

        
        
        
        
              
