
def imc():
   nomePaciente = input("Digite o nome do paciente: ")
   telefonePaciente = input("Digite o telefone do paciente: ")
   peso = float(input("Digite o peso do paciente: "))
   altura = float(input("Digite a altura do paciente: "))
   imc = peso / (altura*altura)
   print(f'O imc do paciente {nomePaciente} é {imc:.1f}')

imc()
