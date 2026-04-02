#Logica E (and)
#é a logica do login
# email e a Senha Sejam true

verifica_email = True
verifica_senha = False

verifica_login = verifica_email and verifica_senha
print(verifica_login)

if verifica_login:
    print("Entrar no Programa")

#Lógica ou (or)
#SOL no dom    jogo BR    Churras no Dom
#    True        true         true
logica_ou = False or False or False
print(logica_ou)

#NOT
negacao = not True
print(negacao)
