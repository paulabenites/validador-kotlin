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
                  | expresion
    '''

# def p_asignacion(p):
#     'asignacion : VARIABLE IGUAL expresion'


# def p_expresion(p):
#     'expresion : valor'

def p_ini_variable(p):
    '''iniVariable : variable ID tipoDeDato
                    | variable ID EQUALS valor
                    | variable ID EQUALS valorBoolean

    '''

def p_variable(p):
    '''variable : VAR
                 | VAL
    '''



def p_tipoDeDato(p):
    '''tipoDeDato : DOSPUNTOS INT EQUALS ENTERO
            | DOSPUNTOS DOUBLE EQUALS DECIMAL
            | DOSPUNTOS STRING EQUALS CADENA_DE_CARACTERES
            | DOSPUNTOS BOOLEAN EQUALS valorBoolean
    '''



# def p_imprimir(p):
#     'imprimir : PRINT PIZQ expresion PDER'
#
#

# def p_imprimir(p):
#     '''imprimir : PRINT PIZQ valor PDER'
#
#     '''

def p_expresion(p):
    '''expresion : valor

    '''

def p_expresion_aritmetica(p):
    'expresion : valor operadorMat expresion'
    #Es expresion : no expresion:





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

def p_operadorMat(p):
    '''operadorMat : PLUS
                    | MINUS
                    | TIMES
                    | DIVIDE
    '''


def p_valor(p):
    '''valor : ENTERO
            | DECIMAL
            | CADENA_DE_CARACTERES

    '''

def p_valorBoolean(p):
    '''valorBoolean : TRUE
                     | FALSE


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