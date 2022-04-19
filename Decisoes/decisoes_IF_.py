nome=input("Digite o nome: ")
idade=int(input("Digite a idade: "))
preferencia="NÃO"
if idade>=65:
    preferencia="SIM"
print("O paciente " + nome + " possui atendimento prioritário? " + preferencia)