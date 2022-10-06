# Limpa o Terminal
import os
os.system("cls")

# Função Mãe
def main():
    cabeçalho()
    menu_de_escolha()

# Cabeçalho do Trabalho    
def cabeçalho():
    print ("Este é um projeto de estudo sobre Sistemas de Numeração na disciplina Ciencias e Tecnologia")
    print ("Aluno: Eduardo Ribeiro de Araújo.  Docente: Dr°.Murilo Guerreiro Arouca")
    print ("Universidade Federal da Bahia")
    print ("\nConversor de Sistemas de Numeração")

# Função Menu
def menu_de_escolha(): 
    print ("\nEscolha qual tipo de conversão deseja fazer !!!")
    print ("1 - Decimal para Binário")
    print ("2 - Decimal para Octal")
    print ("3 - Decimal para Hexadecimal")
    escolha = int (input("Digite: "))
    if escolha == 1:
        n = int (input("Escolha o número decimal a ser convertido para binário: "))
        dec_to_bin(n)
    elif escolha == 2:
        n = int (input("Escolha o número decimal a ser convertido para octal: "))
    elif escolha == 3:
        n = int (input("Escolha o número decimal a ser convertido para hecadecimal: "))
        

# Função de Conversão de Decimal para Binário
def dec_to_bin(n):
    if n != 0:
        n_convertido = []
        binario = []
        escolha_user = n
        while n >= 2:
            n_convertido.append(n % 2)
            n = n // 2
        if n == 1:
            n_convertido.append(n)

        # Bloco que Inverte a lista
        tam = len(n_convertido) - 1
        while tam >= 0:
            binario.append(n_convertido[tam])
            tam = tam - 1
        print ("O número", escolha_user, "em binário é: ",(binario))
    else:
        print ("O número 0 em binário é: 0")










































main()
