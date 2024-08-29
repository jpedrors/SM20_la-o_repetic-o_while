while True:
    # Come um pedaço de bolo (faz alguma coisa)
    print("A Jaqueline aceita namorar com o Moises?")
    
    # Verifica se ainda tem bolo
    tem_bolo = input("tem alguma esperança? (s/n) ")
    
    # Se não tiver mais bolo, paramos
    if tem_bolo.lower() == 'n':
        break