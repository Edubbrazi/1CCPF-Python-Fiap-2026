verifica_email = True
verifica_senha = False

verifica_login = verifica_email and verifica_senha
print(verifica_login)

logica_ou = False or False or True
print(logica_ou)

negacao = not True
print(negacao)

if not verifica_login:
    print("loga certo ai ...")
else:
    print("entra no programa")