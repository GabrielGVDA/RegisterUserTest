usuarios_cadastrados = []

def cadastro_perfeito(): 
    cadastro_perfeito = input("você possui um historico de renda perfeito? ")
if cadastro_perfeito == "s":
    print("preencha o formulario")
else:
    print("Obrigado pela participação")
    
nome_do_usuario = input("Digite seu nome: ")
idade_do_usuario = int(input("Digite a sua idade: "))
renda_do_usuario = int(input("Digite a sua renda: "))

usuario_info = {
    "Nome": nome_do_usuario,
    "Idade": idade_do_usuario,
    "Renda": renda_do_usuario
}

usuarios_cadastrados.append(usuario_info)

print("Informações cadastradas:")
for chave, valor in usuario_info.items():
    print(f"{chave}: {valor}")

if idade_do_usuario <= 18 and renda_do_usuario <= 1000:
    print("Obrigado pela participação")
else:
    print("Obrigado pela participação")

def usuario_fon():
    print(f"Número total de usuários cadastrados: {len(usuarios_cadastrados)}") 
    print("Nomes dos usuários cadastrados:")
    for usuario in usuarios_cadastrados:
        print(usuario["Nome"])

usuario_fon()