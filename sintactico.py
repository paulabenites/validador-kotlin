import ply.yacc as yacc
from lexer import tokens


def p_algoritmo(p):
    '''algoritmo : iniVariable
                  | expresion
                  | expresionRelacional
                  | imprimir
                  | readline
                  | firstAndCap
                  | list
                  | conjuntos
                  | tupla
                  | maps
                  | funColecciones
                  | expLogicas
    '''


# def p_expresion(p):
#     'expresion : valor'

def p_ini_variable(p):
    '''iniVariable : variable ID tipoDeDato
                    | variable ID EQUALS valor
                    | variable ID EQUALS valorBoolean
                    | variable ID EQUALS expLogicas
                    | variable ID EQUALS expresionRelacional
    '''


def p_imprimir(p):
    '''imprimir : PRINT IPAR elementosPrint DPAR
                | PRINTLN IPAR elementosPrint DPAR
    '''

# Elementos que se pueden colocar dentro de print(elemento) -- PAULA BENITES
def p_elementosPrint(p):
    '''elementosPrint : funColecciones
                    | coleccion
                    | expresion
                    | valorBoolean
                    | expLogicas
                    | expresionRelacional
    '''

# Funciones de las colecciones (listas, maps, sets y strings) -- PAULA BENITES
def p_funColecciones(p):
    '''funColecciones : indexCol
                    | slice
                    | size
                    | isEmpty
                    | funMap
                    | getMap

    '''

# indexacion de colecciones lista[1] -- PAULA BENITES
def p_indexCol(p):
    '''indexCol : ID ICOR ENTERO DCOR
                | ID ICOR ID DCOR
    '''


# slicing a.slice(1..2) -- PAULA BENITES
def p_slice(p):
    '''slice : ID PUNTO SLICE IPAR ENTERO PUNTO PUNTO ENTERO DPAR
    '''


# size -- PAULA BENITES
def p_size(p):
    '''size : ID PUNTO SIZE
            | coleccion PUNTO SIZE
            '''

# funcion isEmpty() -- PAULA BENITES
def p_isEmpty(p):
    '''isEmpty : ID PUNTO ISEMPTY IPAR DPAR
            | coleccion PUNTO ISEMPTY IPAR DPAR
            '''

# funcion a.get("cadena") -- PAULA BENITES
def p_getMap(p):
    ''' getMap : ID PUNTO GET IPAR CADENA_DE_CARACTERES DPAR
                | MAPOF IPAR mapsElemento DPAR PUNTO GET IPAR CADENA_DE_CARACTERES DPAR
    '''

# funciones con diccionarios -- PAULA BENITES
def p_funMap(p):
    '''funMap : ID PUNTO KEYS
             | ID PUNTO VALUES
             | MAPOF IPAR mapsElemento DPAR PUNTO VALUES
    '''


# inicializacion de maps
def p_maps(p):
    'maps : variable ID EQUALS MAPOF IPAR mapsElemento DPAR'


# Elementos que se colocan dentro del maps mapOf(ELEMENTO)
def p_mapsElemento(p):
    '''
        mapsElemento : CADENA_DE_CARACTERES TO tuplaElemento
                     | CADENA_DE_CARACTERES TO tuplaElemento COMA mapsElemento

    '''

# Inicializacion de tupla
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
                      | expresionRelacional
                      | expLogicas
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

# funciones de String
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
            | DOSPUNTOS BOOLEAN EQUALS expLogicas
            | DOSPUNTOS BOOLEAN EQUALS expresionRelacional
    '''

# colecciones (list, set y maps)
def p_coleccion(p):
    '''coleccion : LISTOF IPAR listElementos DPAR
                | SETOF IPAR listElementos DPAR
                | MAPOF IPAR mapsElemento DPAR
                '''


def p_expresion(p):
    '''expresion : valor
                 | ID

    '''
# funcion para definir una expresion matematica--Scarlet Espinoza
def p_expresion_aritmetica(p):
    '''expresion : valor operadorMat expresion
                 | ID operadorMat expresion
    '''
# funcion para definir una expresion relacional--Scarlet Espinoza
def p_expresion_relacional(p):
    '''expresionRelacional : elementoRelacional operadorRelacional elementoRelacional

    '''
#Estos son los elementos que se pueden operar con operadores relacionales -- Scarlet Espinoza
def p_elementoRelacional(p):
    '''elementoRelacional : ENTERO
                        | DOUBLE
                        | ID
                        | valorBoolean
       '''




# funcion que define los operadores matematicos -- Scarletr Espinoza
def p_operadorMat(p):
    '''operadorMat : PLUS
                    | MINUS
                    | TIMES
                    | DIVIDE
    '''

#funcion que define los elementos que tiene Valor --Scarlet Espinoza
def p_valor(p):
    '''valor : ENTERO
            | DECIMAL
            | CADENA_DE_CARACTERES
   '''

# expresiones logicas true||true, true&&true -- PAULA BENITES
def p_expLogicas(p):
    '''expLogicas : boolID opLogico boolID
                | NEGATION boolID
    '''


# valor booleano y ID
def p_boolID(p):
    '''boolID : ID
            | valorBoolean
    '''


# operadores Logicos ||, && y !
def p_opLogico(p):
    '''opLogico : AND
                | OR
    '''

def p_valorBoolean(p):
    '''valorBoolean : TRUE
                     | FALSE


    '''
# funcion que define los tipos de operadores relacionales --ScarletEspinoza
def p_operadorRelacional(p):
    '''operadorRelacional : EQUAL
                         | NOTEQ
                         | LARGE
                         | SMALL
                         | LRGEQ
                         | SMLEQ
    '''


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