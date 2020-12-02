import ply.yacc as yacc
from lexer import tokens
reglas = []

#Estructura final para el cuerpo de un algoritmo--PAULA BENITES-VICTOR ALVARADO-SCARLET ESPINOZA
def p_algoritmo(p):
    '''algoritmo : cuerpo
                  | cuerpo algoritmo
    '''
    linea = "Linea: " + str(p.lineno(1)) + " Columna: " + str(p.lexpos(1)) + " p_algoritmo"
    reglas.append(linea)


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
    linea = "Linea: " + str(p.lineno(1)) + " Columna: " + str(p.lexpos(1)) + " p_cuerpo"
    reglas.append(linea)


#declara una funcion -- Scarlet Espinoza
def p_fun(p):
    '''fun : FUN ID IPAR DPAR ILLAVE algoritmo DLLAVE
            | FUN ID IPAR entrada_fun DPAR ILLAVE algoritmo DLLAVE
            | FUN ID IPAR DPAR DOSPUNTOS tipos ILLAVE algoritmo RETURN return DLLAVE
            | FUN ID IPAR entrada_fun DPAR DOSPUNTOS tipos ILLAVE RETURN return DLLAVE
            | FUN ID IPAR entrada_fun DPAR DOSPUNTOS tipos ILLAVE algoritmo RETURN return DLLAVE
            | FUN ID IPAR entrada_fun DPAR EQUALS return
    '''
    linea = "Linea: " + str(p.lineno(1))  + " Columna: " + str(p.lexpos(1)) + " p_fun"

    reglas.append(linea)

# Declara un while -- Scarlet Espinoza
def p_while(p):
    'while : WHILE IPAR entradaIf DPAR ILLAVE algoritmo DLLAVE '
    linea = "Linea: " + str(p.lineno(1))  + " Columna: " + str(p.lexpos(1)) + " p_while"

    reglas.append(linea)
#Funcion que incrementa o decrementa el valor d euna variable PERO ASIGNANDOLO -- Scarlet Espinoza
def p_valorInDecAsignacion(p):
    'valorInDecAsignacion : ID incDecAsignaacion ENTERO'
    linea = "Linea: " + str(p.lineno(1)) +  " Columna: " + str(p.lexpos(1)) + " p_valorInDecAsignacion"

    reglas.append(linea)
#Funcion que incrementa o decrementa el valor d euna variable -- Scarlet Espinoza   a++
def p_valorIncDec(p):
    'valorIncDec : ID incrementoDec'
    linea = "Linea: " + str(p.lineno(1)) + " Columna: " + str(p.lexpos(1)) + " p_valorIncDec"

    reglas.append(linea)

# funcion que define decremento o incremento -- Scarlet Espinoza
def p_incrementoDec(p):
    '''incrementoDec : MASMAS
                | MENOSMENOS
    '''
    linea = "Linea: " + str(p.lineno(1)) + " Columna: " + str(p.lexpos(1)) + " p_incrementoDec"

    reglas.append(linea)

# funcion que define otro dipo de incremento o decremento ( += o -=) --Scarlet Espinoza
def p_incDecAsignacion(p):
    '''incDecAsignaacion : MASIGUAL
                | MENOSIGUAL
    '''
    linea = "Linea: " + str(p.lineno(1)) + " Columna: " + str(p.lexpos(1)) + " p_incDecAsignacion"

    reglas.append(linea)

#Declara un for -- Victor Alvarado
def p_for(p):
    'for : FOR condicionFor ILLAVE algoritmo DLLAVE'
    linea = "Linea: " + str(p.lineno(1)) + " Columna: " + str(p.lexpos(1)) + " p_for"

    reglas.append(linea)

#Declara el cuerpo del for -- Victor Alvarado
def p_condicionFor(p):
    '''condicionFor : IPAR ID IN ID DPAR
                    | IPAR ID IN ENTERO PUNTO PUNTO ENTERO DPAR
                    | IPAR ID IN ENTERO PUNTO PUNTO ENTERO STEP ENTERO DPAR
    '''
    linea = "Linea: " + str(p.lineno(1)) + " Columna: " + str(p.lexpos(1)) + " p_condicionFor"

    reglas.append(linea)


# definicion de if -- Paula Benites
def p_if(p):
    ''' if : IF IPAR entradaIf DPAR ILLAVE algoritmo DLLAVE
            | IF IPAR entradaIf DPAR return
            | IF IPAR entradaIf DPAR ILLAVE algoritmo DLLAVE else
            | IF IPAR entradaIf DPAR return else
    '''
    linea = "Linea: " + str(p.lineno(1)) + " Columna: " + str(p.lexpos(1)) + " p_if"

    reglas.append(linea)

# definicion de ELSE
def p_else(p):
    '''else : ELSE ILLAVE algoritmo DLLAVE
            | ELSE return
    '''
    linea = "Linea: " + str(p.lineno(1)) + " Columna: " + str(p.lexpos(1)) + " p_else"

    reglas.append(linea)


# Entrada de if (operadores logicos y valores booleanos)
def p_entradaIf(p):
    '''entradaIf : valorBoolean
                | expLogicas
                | expresionRelacional
     '''
    linea = "Linea: " + str(p.lineno(1)) + " Columna: " + str(p.lexpos(1)) + " p_entradaIf"

    reglas.append(linea)


# define expresiones que se pueden retornar en una funcion  --Scarlet Espinoza
def p_return(p):
    '''return :  expLogicas
               | expresion
               | valorBoolean
               | expresionRelacional
    '''
    linea = "Linea: " + str(p.lineno(1)) + " Columna: " + str(p.lexpos(1)) + " p_return"

    reglas.append(linea)


# estos son los datos que recibe como entrada las funciones --Scarlet Espinoza
def p_entrada_fun(p):
    '''entrada_fun : ID DOSPUNTOS tipos
                    | ID DOSPUNTOS tipos COMA entrada_fun

    '''
    linea = "Linea: " + str(p.lineno(1)) + " Columna: " + str(p.lexpos(1)) + " p_entrada_fun"

    reglas.append(linea)


def p_tipos(p):
    '''tipos : INT
             | DOUBLE
             | BOOLEAN
             | STRING
    '''
    linea = "Linea: " + str(p.lineno(1)) + " Columna: " + str(p.lexpos(1)) + " p_tipos"

    reglas.append(linea)


def p_ini_variable(p):
    '''iniVariable : variable ID tipoDeDato
                    | variable ID EQUALS valor
                    | variable ID EQUALS valorBoolean
                    | variable ID EQUALS expLogicas
                    | variable ID EQUALS expresionRelacional
                    | variable ID EQUALS funColecciones
                    | variable ID EQUALS READLINE IPAR DPAR
                    | variable ID EQUALS expresion

    '''
    linea = "Linea: " + str(p.lineno(1)) +  " Columna: " + str(p.lexpos(1)) + " p_ini_variable"

    reglas.append(linea)


def p_imprimir(p):
    '''imprimir : PRINT IPAR elementosPrint DPAR
                | PRINTLN IPAR elementosPrint DPAR
    '''
    linea = "Linea: " + str(p.lineno(1)) + " Columna: " + str(p.lexpos(1)) + " p_imprimir"

    reglas.append(linea)


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
    linea = "Linea: " + str(p.lineno(1)) + " Columna: " + str(p.lexpos(1)) + " p_elementosPrint"
    reglas.append(linea)

# colecciones que se pueden imprimir (tuplas, listas,set,mapas) --
def p_imprimirColecciones(p):
    '''imprimirColecciones : PAIR IPAR tuplaElemento COMA tuplaElemento DPAR
                            | MAPOF IPAR mapsElemento DPAR
                            | LISTOF IPAR listElementos DPAR
                            | SETOF IPAR listElementos DPAR

    '''
    linea = "Linea: " + str(p.lineno(1)) + " Columna: " + str(p.lexpos(1)) + " p_imprimirColecciones"
    reglas.append(linea)

# Funciones de las colecciones (listas, maps, sets y strings) -- PAULA BENITES
def p_funColecciones(p):
    '''funColecciones : indexCol
                    | slice
                    | size
                    | isEmpty
                    | funMap
                    | getMap
    '''
    linea = "Linea: " + str(p.lineno(1)) + " Columna: " + str(p.lexpos(1)) + " p_funColecciones"
    reglas.append(linea)

# indexacion de colecciones lista[1] -- PAULA BENITES
def p_indexCol(p):
    '''indexCol : ID ICOR ENTERO DCOR
                | ID ICOR ID DCOR
    '''
    linea = "Linea: " + str(p.lineno(1)) + " " + "Columna: " + str(p.lexpos(1)) + " p_indexCol"
    reglas.append(linea)

# slicing a.slice(1..2) -- PAULA BENITES
def p_slice(p):
    '''slice : ID PUNTO SLICE IPAR ENTERO PUNTO PUNTO ENTERO DPAR
    '''
    linea = "Linea: " + str(p.lineno(1)) + " " + "Columna: " + str(p.lexpos(1)) + " p_slice"
    reglas.append(linea)

# size -- PAULA BENITES
def p_size(p):
    '''size : ID PUNTO SIZE
            | coleccion PUNTO SIZE
            '''
    linea = "Linea: " + str(p.lineno(1)) + " " + "Columna: " + str(p.lexpos(1)) + " p_size"
    reglas.append(linea)
# funcion isEmpty() -- PAULA BENITES
def p_isEmpty(p):
    '''isEmpty : ID PUNTO ISEMPTY IPAR DPAR
            | coleccion PUNTO ISEMPTY IPAR DPAR
            '''
    linea = "Linea: " + str(p.lineno(1)) + " " + "Columna: " + str(p.lexpos(1)) + " p_isEmpty"
    reglas.append(linea)

# funcion a.get("cadena") -- PAULA BENITES
def p_getMap(p):
    ''' getMap : ID PUNTO GET IPAR CADENA_DE_CARACTERES DPAR
                | MAPOF IPAR mapsElemento DPAR PUNTO GET IPAR CADENA_DE_CARACTERES DPAR
    '''
    linea = "Linea: " + str(p.lineno(1)) + " " + "Columna: " + str(p.lexpos(1)) + " p_getMap"
    reglas.append(linea)


# funciones con diccionarios -- PAULA BENITES
def p_funMap(p):
    '''funMap : ID PUNTO KEYS
             | ID PUNTO VALUES
             | MAPOF IPAR mapsElemento DPAR PUNTO VALUES
    '''
    linea = "Linea: " + str(p.lineno(1)) + " " + "Columna: " + str(p.lexpos(1)) + " p_funMap"
    reglas.append(linea)


# inicializacion de maps
def p_maps(p):
    'maps : variable ID EQUALS MAPOF IPAR mapsElemento DPAR'

    linea = "Linea: " + str(p.lineno(1)) + " Columna: " + str(p.lexpos(1)) + " p_maps"
    reglas.append(linea)

# Elementos que se colocan dentro del maps mapOf(ELEMENTO)
def p_mapsElemento(p):
    '''
        mapsElemento : CADENA_DE_CARACTERES TO tuplaElemento
                     | CADENA_DE_CARACTERES TO tuplaElemento COMA mapsElemento
    '''
    linea = "Linea: " + str(p.lineno(1)) + " " + "Columna: " + str(p.lexpos(1)) +" p_mapsElemento"
    reglas.append(linea)

# Inicializacion de tupla-- VICTOR ALVARADO
def p_tupla(p):
    '''
        tupla : variable IPAR ID COMA ID DPAR EQUALS PAIR IPAR tuplaElemento COMA tuplaElemento DPAR
    '''
    linea = "Linea: " + str(p.lineno(1)) + " " + "Columna: " + str(p.lexpos(1)) + " p_tupla"
    reglas.append(linea)


# elementos que se pueden poner dentro de una tupla-- VICTOR ALVARADO
def p_tuplaElemento(p) :
    '''tuplaElemento : valor
                      | ID
                      | valorBoolean
                      | LISTOF IPAR listElementos DPAR
                      | SETOF IPAR listElementos DPAR
    '''
    linea = "Linea: " + str(p.lineno(1)) + " " + "Columna: " + str(p.lexpos(1)) + " p_tuplaElemento"
    reglas.append(linea)


# Declaracion de un set(conjunto)--VICTOR ALVARADO
def p_conjuntos(p):
    'conjuntos : variable ID EQUALS SETOF IPAR listElementos DPAR'
    linea = "Linea: " + str(p.lineno(1)) + " " + "Columna: " + str(p.lexpos(1)) + " p_conjuntos"
    reglas.append(linea)


# Declaracion de una lista-- VICTOR ALVARADO
def p_list(p):
    'list : variable ID EQUALS LISTOF IPAR listElementos DPAR'
    linea = "Linea: " + str(p.lineno(1)) + " " + "Columna: " + str(p.lexpos(1)) + " p_list"
    reglas.append(linea)

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
    linea = "Linea: " + str(p.lineno(1)) + " " + "Columna: " + str(p.lexpos(1)) + " p_listElementos"
    reglas.append(linea)

# colecciones (list, set y maps)
def p_coleccion(p):
    '''coleccion : LISTOF IPAR listElementos DPAR
                | SETOF IPAR listElementos DPAR
                | MAPOF IPAR mapsElemento DPAR
                '''
    linea = "Linea: " + str(p.lineno(1)) + " " + "Columna: " + str(p.lexpos(1)) + " p_coleccion"
    reglas.append(linea)

# Definicion para el inicio de una variable-- VICTOR ALVARADO
def p_variable(p):
    '''variable : VAR
                 | VAL
    '''
    linea = "Linea: " + str(p.lineno(1)) + " " + "Columna: " + str(p.lexpos(1)) + " p_variable"
    reglas.append(linea)

# Lectura de datos-- VICTOR ALVARADO
def p_readline(p):
    '''
        readline : READLINE IPAR DPAR
                 | variable ID EQUALS READLINE IPAR DPAR
    '''
    linea = "Linea: " + str(p.lineno(1)) + " " + "Columna: " + str(p.lexpos(1)) + " p_readline"
    reglas.append(linea)


# funciones de String first y capitalize-- VICTOR ALVARADO
def p_firstAndCap(p):
    '''
        firstAndCap : ID PUNTO FIRST IPAR DPAR
                    | ID PUNTO CAPITALIZE IPAR DPAR
    '''
    linea = "Linea: " + str(p.lineno(1)) + " " + "Columna: " + str(p.lexpos(1)) + " p_firstAndCap"
    reglas.append(linea)

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
    linea = "Linea: " + str(p.lineno(1)) + " " + "Columna: " + str(p.lexpos(1)) + " p_tipoDeDato"
    reglas.append(linea)

#tipos de datos para declaracion de variables sin asignación de valores ej. val a : Int--VICTOR ALVARADO
def p_tipoDeDato2(p):
    '''tipoDeDato2 : DOSPUNTOS INT
            | DOSPUNTOS DOUBLE
            | DOSPUNTOS STRING
            | DOSPUNTOS BOOLEAN
    '''
    linea = "Linea: " + str(p.lineno(1)) + " " + "Columna: " + str(p.lexpos(1)) + " p_tipoDeDato2"
    reglas.append(linea)

def p_definicionVariables(p):
    '''definicionVariables : ID EQUALS valor
                           | ID EQUALS valorBoolean
                           | ID EQUALS expresion
    '''
    linea = "Linea: " + str(p.lineno(1)) + " " + "Columna: " + str(p.lexpos(1)) + " p_definicionVariables"
    reglas.append(linea)

def p_expresion(p):
    '''expresion : valor
                 | ID
    '''
    linea = "Linea: " + str(p.lineno(1)) + " " + "Columna: " + str(p.lexpos(1)) + " p_expresion"
    reglas.append(linea)

# funcion para definir una expresion matematica--Scarlet Espinoza
def p_expresion_aritmetica(p):
    '''expresion : valor operadorMat expresion
                 | ID operadorMat expresion
    '''
    linea = "Linea: " + str(p.lineno(1)) + " " + "Columna: " + str(p.lexpos(1)) + " p_expresion_aritmetica"
    reglas.append(linea)

# funcion para definir una expresion relacional--Scarlet Espinoza
def p_expresion_relacional(p):
    '''expresionRelacional : elementoRelacional operadorRelacional elementoRelacional

    '''
    linea = "Linea: " + str(p.lineno(1)) + " " + "Columna: " + str(p.lexpos(1)) + " p_expresion_relacional"
    reglas.append(linea)

# Estos son los elementos que se pueden operar con operadores relacionales -- Scarlet Espinoza
def p_elementoRelacional(p):
    '''elementoRelacional : ENTERO
                        | DECIMAL
                        | ID
                        | valorBoolean
       '''
    linea = "Linea: " + str(p.lineno(1)) + " " + "Columna: " + str(p.lexpos(1)) + " p_elementoRelacional"
    reglas.append(linea)

# funcion que define los operadores matematicos -- Scarlet Espinoza
def p_operadorMat(p):
    '''operadorMat : PLUS
                    | MINUS
                    | TIMES
                    | DIVIDE
    '''

    linea = "Linea: " + str(p.lineno(1)) + " " + "Columna: " + str(p.lexpos(1)) + " p_operadorMat"
    reglas.append(linea)

# funcion que define los elementos que tiene Valor --Scarlet Espinoza
def p_valor(p):
    '''valor : ENTERO
            | DECIMAL
            | CADENA_DE_CARACTERES
   '''
    linea = "Linea: " + str(p.lineno(1)) + " " + "Columna: " + str(p.lexpos(1)) + " p_valor"
    reglas.append(linea)

# expresiones logicas true||true, true&&true -- PAULA BENITES
def p_expLogicas(p):
    '''expLogicas : boolID opLogico boolID
                | NEGATION boolID
    '''
    linea = "Linea: " + str(p.lineno(1)) + " " + "Columna: " + str(p.lexpos(1)) + " p_expLogicas"
    reglas.append(linea)

# valor booleano y ID
def p_boolID(p):
    '''boolID : ID
            | valorBoolean
    '''
    linea = "Linea: " + str(p.lineno(1)) + " " + "Columna: " + str(p.lexpos(1)) + " p_boolID"
    reglas.append(linea)

# operadores Logicos ||, && y !
def p_opLogico(p):
    '''opLogico : AND
                | OR
    '''
    linea = "Linea: " + str(p.lineno(1)) + " " + "Columna: " + str(p.lexpos(1)) + " p_opLogico"
    reglas.append(linea)

def p_valorBoolean(p):
    '''valorBoolean : TRUE
                     | FALSE
    '''
    linea = "Linea: " + str(p.lineno(1)) + " " + "Columna: " + str(p.lexpos(1)) + " p_valorBoolean"
    reglas.append(linea)

# funcion que define los tipos de operadores relacionales --ScarletEspinoza
def p_operadorRelacional(p):
    '''operadorRelacional : EQUAL
                         | NOTEQ
                         | LARGE
                         | SMALL
                         | LRGEQ
                         | SMLEQ
    '''
    linea = "Linea: " + str(p.lineno(1)) + " " + "Columna: " + str(p.lexpos(1)) + " p_operadorRelacional"
    reglas.append(linea)

# Error rule for syntax errors
def p_error(p):
    if p is not None:
        reglas.append("Linea: %s Columna: %s Error en: '%s'" % (p.lineno,p.lexpos, p.value))
    else:
        reglas.append('Error en syntax')



# file =open("Ejemplos/AlgoritmoBenites.txt")
# s=file.read()
# print(s)


def reglas_sintactico(s):
    parser = yacc.yacc()
    result = parser.parse(s,tracking=True)
    print(reglas)
    retorno_reglas = reglas.copy()
    reglas.clear()

    return retorno_reglas


# while True:
#     try:
#         s = input('calc > ')
#     except EOFError:
#         break
#     if not s: continue
#     result = parser.parse(s)
#     print(result)