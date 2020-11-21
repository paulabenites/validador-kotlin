import ply.yacc as yacc
from lexer import tokens

# def p_algoritmo(p):
#     '''algoritmo : imprimir
#                  | asignacion
#                  | expresion
#                  | comparacion
#     '''

def p_algoritmo(p):
    '''algoritmo : iniVariable
    '''

# def p_asignacion(p):
#     'asignacion : VARIABLE IGUAL expresion'


# def p_expresion(p):
#     'expresion : valor'

def p_ini_variable(p):
    '''iniVariable : iniVar
                  | iniVal
    '''


def p_var(p):
    '''iniVar : VAR ID EQUALS valor
            | VAR ID  DOSPUNTOS INT EQUALS ENTERO
            | VAR ID  DOSPUNTOS DOUBLE EQUALS DECIMAL
            | VAR ID  DOSPUNTOS STRING EQUALS CADENA_DE_CARACTERES
    '''


def p_val(p):
    '''iniVal : VAL ID EQUALS valor
            | VAL ID  DOSPUNTOS INT EQUALS ENTERO
            | VAL ID  DOSPUNTOS DOUBLE EQUALS DECIMAL
            | VAL ID  DOSPUNTOS STRING EQUALS CADENA_DE_CARACTERES
    '''


# def p_imprimir(p):
#     'imprimir : PRINT PIZQ expresion PDER'
#
#
# def p_expresion_aritmetica(p):
#     'expresion : valor operadorMat expresion'
#     #Es expresion : no expresion:
#
#
# def p_comparacion(p):
#     'comparacion : expresion operadorComp expresion'
#     # Es expresion : no expresion:
#
#
# def p_operadorComp(p):
#     '''operadorComp : MAYOR
#                     | DIFERENTE
#     '''
#
# def p_operadorMat(p):
#     '''operadorMat : MAS
#                     | RESTA
#                     | PROD
#                     | DIV
#     '''

def p_valor(p):
    '''valor : ENTERO
            | DECIMAL
            | CADENA_DE_CARACTERES
    '''


# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")


parser = yacc.yacc()


# file =open("ejemplo.txt", "r")
# if file.mode=="r":
#     datos=file.read()
#
#
# def sintactico():
#     s = input(datos)
#     while True:
#         result = parser.parse(s)
#         if not s:
#             break
#         print(result)
#
# sintactico()

while True:
    try:
        s = input('calc > ')
    except EOFError:
        break
    if not s: continue
    result = parser.parse(s)
    print(result)