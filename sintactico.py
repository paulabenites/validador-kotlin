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
                  | imprimir
                  | readline
                  | firstAndCap
                  | list
                  | conjuntos
                  | tupla
                  | maps
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
def p_maps(p):
    'maps : variable ID EQUALS MAPOF IPAR mapsElemento DPAR'
def p_mapsElemento(p):
    '''
        mapsElemento : CADENA_DE_CARACTERES TO tuplaElemento
                     | CADENA_DE_CARACTERES TO tuplaElemento COMA mapsElemento

    '''
def p_tupla(p):
    '''
        tupla : variable IPAR ID COMA ID DPAR EQUALS PAIR IPAR tuplaElemento COMA tuplaElemento DPAR
    '''
def p_tuplaElemento(p) :
    '''
        tuplaElemento : valor
                      | ID
                      | valorBoolean
                      | LISTOF IPAR listElementos DPAR
                      | SETOF IPAR listElementos DPAR
    '''
def p_conjuntos(p):
    'conjuntos : variable ID EQUALS SETOF IPAR listElementos DPAR'


def p_list(p):
    'list : variable ID EQUALS LISTOF IPAR listElementos DPAR'

def p_listElementos(p):
    '''
        listElementos : valor
                      | ID
                      | valorBoolean
                      | valorBoolean COMA listElementos
                      | valor COMA listElementos
                      | ID COMA listElementos
                      | LISTOF IPAR listElementos DPAR
                      | SETOF IPAR listElementos DPAR

    '''

def p_variable(p):
    '''variable : VAR
                 | VAL
    '''

def p_readline(p):
    '''
        readline : READLINE IPAR DPAR
                 | variable ID EQUALS READLINE IPAR DPAR

    '''
def p_firstAndCap(p):
    '''
        firstAndCap : ID PUNTO FIRST IPAR DPAR
                    | ID PUNTO CAPITALIZE IPAR DPAR

    '''

def p_tipoDeDato(p):
    '''tipoDeDato : DOSPUNTOS INT EQUALS ENTERO
            | DOSPUNTOS DOUBLE EQUALS DECIMAL
            | DOSPUNTOS STRING EQUALS CADENA_DE_CARACTERES
            | DOSPUNTOS BOOLEAN EQUALS valorBoolean
    '''


def p_imprimir(p):
     '''imprimir : PRINT IPAR expresion DPAR
                 | PRINT IPAR valorBoolean DPAR
                 | PRINTLN IPAR expresion DPAR
                 | PRINTLN IPAR valorBoolean DPAR
     '''




# def p_imprimir(p):
#     '''imprimir : PRINT PIZQ valor PDER'
#
#     '''

def p_expresion(p):
    '''expresion : valor
                 | ID

    '''

def p_expresion_aritmetica(p):
    '''expresion : valor operadorMat expresion
                 | ID operadorMat expresion
    '''

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