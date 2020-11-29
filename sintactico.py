import ply.yacc as yacc
from lexer import tokens
reglas = []

#Estructura final para el cuerpo de un algoritmo--PAULA BENITES-VICTOR ALVARADO-SCARLET ESPINOZA
def p_algoritmo(p):
    '''algoritmo : cuerpo
                  | cuerpo algoritmo
    '''
    reglas.append("p_algoritmo")

#Estructura final para el cuerpo de un algoritmo--PAULA BENITES-VICTOR ALVARADO-SCARLET ESPINOZA
def p_cuerpo(p):
    '''cuerpo : iniVariable
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
                  | fun
                  | if
                  | for
                  | while
                  | valorIncDec
                  | valorInDecAsignacion
                  | definicionVariables
                  | valor operadorMat expresion
                  | ID operadorMat expresion
    '''
    reglas.append("p_cuerpo")

#declara una funcion -- Scarlet Espinoza
def p_fun(p):
    '''fun : FUN ID IPAR DPAR ILLAVE algoritmo DLLAVE
            | FUN ID IPAR entrada_fun DPAR ILLAVE algoritmo DLLAVE
            | FUN ID IPAR DPAR DOSPUNTOS tipos ILLAVE algoritmo RETURN return DLLAVE
            | FUN ID IPAR entrada_fun DPAR DOSPUNTOS tipos ILLAVE algoritmo RETURN return DLLAVE
            | FUN ID IPAR entrada_fun DPAR EQUALS return
    '''
    reglas.append("p_fun")

# Declara un while -- Scarlet Espinoza
def p_while(p):
    'while : WHILE IPAR entradaIf DPAR ILLAVE algoritmo DLLAVE '
    reglas.append("p_while")

#Funcion que incrementa o decrementa el valor d euna variable PERO ASIGNANDOLO -- Scarlet Espinoza
def p_valorInDecAsignacion(p):
    'valorInDecAsignacion : ID incDecAsignaacion ENTERO'
    reglas.append("p_valorInDecAsignacion")

#Funcion que incrementa o decrementa el valor d euna variable -- Scarlet Espinoza   a++
def p_valorIncDec(p):
    'valorIncDec : ID incrementoDec'
    reglas.append("p_valorIncDec")

# funcion que define decremento o incremento -- Scarlet Espinoza
def p_incrementoDec(p):
    '''incrementoDec : MASMAS
                | MENOSMENOS
    '''
    reglas.append("p_incrementoDec")

# funcion que define otro dipo de incremento o decremento ( += o -=) --Scarlet Espinoza
def p_incDecAsignacion(p):
    '''incDecAsignaacion : MASIGUAL
                | MENOSIGUAL
    '''
    reglas.append("p_incDecAsignacion")

#Declara un for -- Victor Alvarado
def p_for(p):
    'for : FOR condicionFor ILLAVE algoritmo DLLAVE'
    reglas.append("p_for")

#Declara el cuerpo del for -- Victor Alvarado
def p_condicionFor(p):
    '''condicionFor : IPAR ID IN ID DPAR
                    | IPAR ID IN ENTERO PUNTO PUNTO ENTERO DPAR
                    | IPAR ID IN ENTERO PUNTO PUNTO ENTERO STEP ENTERO DPAR
    '''
    reglas.append("p_condicionFor")


# definicion de if -- Paula Benites
def p_if(p):
    ''' if : IF IPAR entradaIf DPAR ILLAVE algoritmo DLLAVE
            | IF IPAR entradaIf DPAR return
            | IF IPAR entradaIf DPAR ILLAVE algoritmo DLLAVE else
            | IF IPAR entradaIf DPAR return else
    '''
    reglas.append("p_if")


# definicion de ELSE
def p_else(p):
    '''else : ELSE ILLAVE algoritmo DLLAVE
            | ELSE return
    '''
    reglas.append("p_else")


# Entrada de if (operadores logicos y valores booleanos)
def p_entradaIf(p):
    '''entradaIf : valorBoolean
                | expLogicas
                | expresionRelacional
     '''
    reglas.append("p_entradaIf")


# define expresiones que se pueden retornar en una funcion  --Scarlet Espinoza
def p_return(p):
    '''return :  expLogicas
               | expresion
               | valorBoolean
               | expresionRelacional
    '''
    reglas.append("p_return")


# estos son los datos que recibe como entrada las funciones --Scarlet Espinoza
def p_entrada_fun(p):
    '''entrada_fun : ID DOSPUNTOS tipos
                    | ID DOSPUNTOS tipos COMA entrada_fun

    '''
    reglas.append("p_entrada_fun")


def p_tipos(p):
    '''tipos : INT
             | DOUBLE
             | BOOLEAN
             | STRING
    '''
    reglas.append("p_tipos")


def p_ini_variable(p):
    '''iniVariable : variable ID tipoDeDato
                    | variable ID EQUALS valor
                    | variable ID EQUALS valorBoolean
                    | variable ID EQUALS expLogicas
                    | variable ID EQUALS expresionRelacional
                    | variable ID EQUALS funColecciones
                    | variable ID EQUALS READLINE IPAR DPAR
    '''
    reglas.append("p_ini_variable")


def p_imprimir(p):
    '''imprimir : PRINT IPAR elementosPrint DPAR
                | PRINTLN IPAR elementosPrint DPAR
    '''
    reglas.append("p_imprimir")


# Elementos que se pueden colocar dentro de print(elemento) -- PAULA BENITES
def p_elementosPrint(p):
    '''elementosPrint : funColecciones
                    | coleccion
                    | expresion
                    | valorBoolean
                    | expLogicas
                    | expresionRelacional
                    | imprimirColecciones
                    | firstAndCap
                    | getMap
    '''
    reglas.append("p_elementosPrint")


# colecciones que se pueden imprimir (tuplas, listas,set,mapas) --
def p_imprimirColecciones(p):
    '''imprimirColecciones : PAIR IPAR tuplaElemento COMA tuplaElemento DPAR
                            | MAPOF IPAR mapsElemento DPAR
                            | LISTOF IPAR listElementos DPAR
                            | SETOF IPAR listElementos DPAR

    '''
    reglas.append("p_imprimirColecciones")


# Funciones de las colecciones (listas, maps, sets y strings) -- PAULA BENITES
def p_funColecciones(p):
    '''funColecciones : indexCol
                    | slice
                    | size
                    | isEmpty
                    | funMap
                    | getMap
    '''
    reglas.append("p_funColecciones")

# indexacion de colecciones lista[1] -- PAULA BENITES
def p_indexCol(p):
    '''indexCol : ID ICOR ENTERO DCOR
                | ID ICOR ID DCOR
    '''
    reglas.append("p_indexCol")


# slicing a.slice(1..2) -- PAULA BENITES
def p_slice(p):
    '''slice : ID PUNTO SLICE IPAR ENTERO PUNTO PUNTO ENTERO DPAR
    '''
    reglas.append("p_slice")


# size -- PAULA BENITES
def p_size(p):
    '''size : ID PUNTO SIZE
            | coleccion PUNTO SIZE
            '''
    reglas.append("p_size")

# funcion isEmpty() -- PAULA BENITES
def p_isEmpty(p):
    '''isEmpty : ID PUNTO ISEMPTY IPAR DPAR
            | coleccion PUNTO ISEMPTY IPAR DPAR
            '''
    reglas.append("p_isEmpty")


# funcion a.get("cadena") -- PAULA BENITES
def p_getMap(p):
    ''' getMap : ID PUNTO GET IPAR CADENA_DE_CARACTERES DPAR
                | MAPOF IPAR mapsElemento DPAR PUNTO GET IPAR CADENA_DE_CARACTERES DPAR
    '''
    reglas.append("p_getMap")


# funciones con diccionarios -- PAULA BENITES
def p_funMap(p):
    '''funMap : ID PUNTO KEYS
             | ID PUNTO VALUES
             | MAPOF IPAR mapsElemento DPAR PUNTO VALUES
    '''
    reglas.append("p_funMap")


# inicializacion de maps
def p_maps(p):
    'maps : variable ID EQUALS MAPOF IPAR mapsElemento DPAR'
    reglas.append("p_maps")

# Elementos que se colocan dentro del maps mapOf(ELEMENTO)
def p_mapsElemento(p):
    '''
        mapsElemento : CADENA_DE_CARACTERES TO tuplaElemento
                     | CADENA_DE_CARACTERES TO tuplaElemento COMA mapsElemento
    '''
    reglas.append("p_mapsElemento")

# Inicializacion de tupla-- VICTOR ALVARADO
def p_tupla(p):
    '''
        tupla : variable IPAR ID COMA ID DPAR EQUALS PAIR IPAR tuplaElemento COMA tuplaElemento DPAR
    '''
    reglas.append("p_tupla")


# elementos que se pueden poner dentro de una tupla-- VICTOR ALVARADO
def p_tuplaElemento(p) :
    '''tuplaElemento : valor
                      | ID
                      | valorBoolean
                      | LISTOF IPAR listElementos DPAR
                      | SETOF IPAR listElementos DPAR
    '''
    reglas.append("p_tuplaElemento")


# Declaracion de un set(conjunto)--VICTOR ALVARADO
def p_conjuntos(p):
    'conjuntos : variable ID EQUALS SETOF IPAR listElementos DPAR'
    reglas.append("p_conjuntos")


# Declaracion de una lista-- VICTOR ALVARADO
def p_list(p):
    'list : variable ID EQUALS LISTOF IPAR listElementos DPAR'
    reglas.append("p_list")


# Elementos que se pueden poner dentro de una tupla- VICTOR ALVARADO
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
    reglas.append("p_listElementos")


# colecciones (list, set y maps)
def p_coleccion(p):
    '''coleccion : LISTOF IPAR listElementos DPAR
                | SETOF IPAR listElementos DPAR
                | MAPOF IPAR mapsElemento DPAR
                '''
    reglas.append("p_coleccion")


# Definicion para el inicio de una variable-- VICTOR ALVARADO
def p_variable(p):
    '''variable : VAR
                 | VAL
    '''
    reglas.append("p_variable")


# Lectura de datos-- VICTOR ALVARADO
def p_readline(p):
    '''
        readline : READLINE IPAR DPAR
                 | variable ID EQUALS READLINE IPAR DPAR
    '''
    reglas.append("p_readline")


# funciones de String first y capitalize-- VICTOR ALVARADO
def p_firstAndCap(p):
    '''
        firstAndCap : ID PUNTO FIRST IPAR DPAR
                    | ID PUNTO CAPITALIZE IPAR DPAR
    '''
    reglas.append("p_firstAndCap")


# tipos de datos-- VICTOR ALVARADO
def p_tipoDeDato(p):
    '''tipoDeDato : DOSPUNTOS INT EQUALS ENTERO
            | DOSPUNTOS DOUBLE EQUALS DECIMAL
            | DOSPUNTOS STRING EQUALS CADENA_DE_CARACTERES
            | DOSPUNTOS BOOLEAN EQUALS valorBoolean
            | DOSPUNTOS BOOLEAN EQUALS expLogicas
            | DOSPUNTOS BOOLEAN EQUALS expresionRelacional
            | tipoDeDato2
    '''
    reglas.append("p_tipoDeDato")


#tipos de datos para declaracion de variables sin asignación de valores ej. val a : Int--VICTOR ALVARADO
def p_tipoDeDato2(p):
    '''tipoDeDato2 : DOSPUNTOS INT
            | DOSPUNTOS DOUBLE
            | DOSPUNTOS STRING
            | DOSPUNTOS BOOLEAN
    '''
    reglas.append("p_tipoDeDato2")


def p_definicionVariables(p):
    '''definicionVariables : ID EQUALS valor
                           | ID EQUALS valorBoolean
    '''
    reglas.append("p_definicionVariables")

def p_expresion(p):
    '''expresion : valor
                 | ID
    '''
    reglas.append("p_expresion")


# funcion para definir una expresion matematica--Scarlet Espinoza
def p_expresion_aritmetica(p):
    '''expresion : valor operadorMat expresion
                 | ID operadorMat expresion
    '''
    reglas.append("p_expresion_aritmetica")


# funcion para definir una expresion relacional--Scarlet Espinoza
def p_expresion_relacional(p):
    '''expresionRelacional : elementoRelacional operadorRelacional elementoRelacional

    '''
    reglas.append("p_expresion_relacional")


# Estos son los elementos que se pueden operar con operadores relacionales -- Scarlet Espinoza
def p_elementoRelacional(p):
    '''elementoRelacional : ENTERO
                        | DOUBLE
                        | ID
                        | valorBoolean
       '''
    reglas.append("p_elementoRelacional")


# funcion que define los operadores matematicos -- Scarlet Espinoza
def p_operadorMat(p):
    '''operadorMat : PLUS
                    | MINUS
                    | TIMES
                    | DIVIDE
    '''
    reglas.append("p_operadorMat")


# funcion que define los elementos que tiene Valor --Scarlet Espinoza
def p_valor(p):
    '''valor : ENTERO
            | DECIMAL
            | CADENA_DE_CARACTERES
   '''
    reglas.append("p_valor")


# expresiones logicas true||true, true&&true -- PAULA BENITES
def p_expLogicas(p):
    '''expLogicas : boolID opLogico boolID
                | NEGATION boolID
    '''
    reglas.append("p_expLogicas")


# valor booleano y ID
def p_boolID(p):
    '''boolID : ID
            | valorBoolean
    '''
    reglas.append("p_boolID")


# operadores Logicos ||, && y !
def p_opLogico(p):
    '''opLogico : AND
                | OR
    '''
    reglas.append("p_opLogico")


def p_valorBoolean(p):
    '''valorBoolean : TRUE
                     | FALSE
    '''
    reglas.append("p_valorBoolean")


# funcion que define los tipos de operadores relacionales --ScarletEspinoza
def p_operadorRelacional(p):
    '''operadorRelacional : EQUAL
                         | NOTEQ
                         | LARGE
                         | SMALL
                         | LRGEQ
                         | SMLEQ
    '''
    reglas.append("p_operadorRelacional")

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

# file =open("Ejemplos/AlgoritmoBenites.txt")
# s=file.read()
# print(s)


def reglas_sintactico(s):
    parser = yacc.yacc()
    result = parser.parse(s)
    print(result)
    retorno_reglas = reglas.copy()
    reglas.clear()
    # del reglas[:]
    return retorno_reglas

# result = parser.parse(s)
# print(result)
# file.close()



# while True:
#     try:
#         s = input('calc > ')
#     except EOFError:
#         break
#     if not s: continue
#     result = parser.parse(s)
#     print(result)