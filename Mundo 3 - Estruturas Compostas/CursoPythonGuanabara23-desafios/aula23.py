# Exceções

# --------------------------------------------------------------------------------------------------

#   NameError: quando a variável não é definida

#   ValueError: quando se insere uma string quando se espera um número

#   ZeroDivisionError: quando se divide um numero por zero

#   TypeError: quando se divide um número do tipo int por um número em aspas de string
# (essa divisão não é aceita em python, mas em algumas linguagens é permitida)

#   IndexError: quando se aponta um índice que não está dentro do intervalo definido de uma lista
#   (Ex.: lst[3] em uma lista lst=[3,6,4])

#   KeyError: quando se aponta uma chave que não está dentro do intervalo definido de um dicionário
#   (Ex.: dic[3] em uma dicionário dic={3:a,6:b,4:c})

#   ModuleNotFoundError: quando o módulo importado não é encontrado ou não existe

#   entre outras exceções

#--------------------------------------------------------------------------------------------------------

# try ... except...

#--------------------------------------------------------------------------------------------------------

#   Usado para poder controlar o fluxo de quando o programa está funcionando normalmente e de quando o
#   programa dá um erro de exceção

#   Exception:  mostra o tipo de exceção. Na sintaxe Exception as <nome_variavel>, <nome_variavel se torna
#               Exception; colocando <nome_variavel>.__class__ , mostrará a classe do tipo de exceção que
#               foi disparado

# SINTAXE

#   try:
#       <operação>
#   except (OPCIONAL: Exception as <nome_variavel>):
#       <falhou> <nome_variavel> (OPCIONAL: <nome_variavel.__class__ )
#   else:
#       <deu certo>
#   finally:
#       <deu certo / falha>

#   Pode ser necessário múltiplas cláusulas do tipo except, por ter diversos tipos diferentes de erros e exceções