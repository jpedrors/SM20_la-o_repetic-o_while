"""
ESCOLHENDO A OPÇÃO
"""

while True:
    print("\nMenu:")
    print("1. pizza")
    print("2. esfirra")
    print("3. coxinha")
    print("4, hamburger")
    print("0, sair")
    
    escolha = input("Escolha uma opção: ")
    
    if escolha == '0':
        print("Saindo...")
        break
    elif escolha == '1':
        print("Você escolheu pizza!")
    elif escolha == '2':
        print("Você escolheu esfirra!")
    elif escolha == '3':
        print("Você escolheu coxinha!")
    elif escolha == '4':
        print("Você escolheu hamburger!")
    else:
        print("Opção inválida! Tente novamente.")