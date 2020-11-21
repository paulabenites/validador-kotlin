import ply.lex as lex

# Definicion de palagbras reservada ---> Paula Benites
reservada= {
            'print' : "PRINT",'println' : "println",'readline' : "readline",
            'pair' : "pair",
            'isEmpty' : "isEmpty",
            "values" : "values", "keys" : "keys",
            'else' : "else", "if" : "if",
            'while' : "while",
           'for' : "for",
           'fun' : "fun", 'return' : "return", 'to' : "to"
}


# Definicion de las lista de tokens --> Victor Alvardado
tokens = [
    'INT', 'DOUBLE', 'FALSO', 'VERDAD', 'ID', 'CADENA_DE_CARACTERES',
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE',
    'EQUALS', 'DOSPUNTOS', 'COMA','STRING','PUNTO','PUNTOS', 'EQUAL',
    'LARGE', 'SMALL', 'NOTEQ', 'LRGEQ', 'SMLEQ',
    'ILLAVE','DLLAVE', 'IPAR', 'DPAR',
    'AND','NOT','OR','NEGATION',
    "INDENT", 'newline','TAB',
    'LISTOF',"SETOF","MAPOF", "STEP","IN", 'VAL','VAR', "Int",'Double','Boolean',
] + list(reservada.values())

# tokens=token+reserveda
# Regular expression rules for simple tokens -- Paula Benites
t_PLUS    = r'\+'
t_ILLAVE    = r'\{'
t_DLLAVE    = r'\}'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_IPAR  = r'\('
t_DPAR  = r'\)'
t_EQUALS  = r'='
t_DOSPUNTOS = r':'
t_PUNTO     =r'\.'
t_COMA      =r'\,'
t_CADENA_DE_CARACTERES = r'(\".*\"|[a-zA-Z]+\s*)'
t_TAB       =r'\t'
t_ignore_COMMENT = r'\/\/.*'
t_EQUAL   = r'\=\='
t_NOTEQ   = r'\!\='
t_LARGE   = r'\>'
t_SMALL   = r'\<'
t_LRGEQ   = r'\>\='
t_SMLEQ   = r'\<\='
t_AND = r'\&\&'
t_OR  = r'\|\|'
t_NEGATION=r'\!'

# t_VAR= r'var'
# t_VAL= r'val'


# definicion de la funciones exectp estructuras de control -- > Scarlet Espinoza
# Reglas de correspondencia

def t_VAR(token):
    r'var\s'
    token.value = str(token.value)
    return token

def t_VAL(token):
    r'val\s'
    token.value = str(token.value)
    return token

def t_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_Int(token):
    r'Int'
    token.value = str(token.value)
    return token


def t_STRING(token):
    r'String=\String\s'
    token.value = str(token.value)
    return token




def t_Double(token):
    r'Double=|Double\s'
    token.value = str(token.value)
    return token


def t_DOUBLE(t):
    r'\d+\.\d+'
    t.value = float(t.value[::])
    return t


def t_Boolean(token):
    r'Boolean=|Boolean\s'
    token.value = str(token.value)
    return token


def t_VERDAD(token):
    r'true\s'
    token.value = str(token.value)
    return token


def t_FALSO(token):
    r'false\s'
    token.value = str(token.value)
    return token


def t_SIZE(token):
    r'size\s'
    token.value = str(token.value)
    return token

#Paula Benites hice el If y Else


#Paula Benites hice listof
def t_LISTOF(token):
    r'listOf'
    token.value = str(token.value)
    return token

# SCARLET ESPINOZA HICE EL SET OF 
def t_SETOF(token):
    r'setOf'
    token.value = str(token.value)
    return token
#VICTOR ALVARADO HICE EL MAPOF
def t_MAPOF(token):
    r'mapOf'
    token.value = str(token.value)
    return token


def t_STEP(token):
    r'step\s'
    token.value = str(token.value)
    return token


def t_IN(token):
    r'in\s'
    token.value = str(token.value)
    return token



def t_ID(token):
    '([a-zA-Z_][a-zA-Z0-9_]*)'
    # token.value = str(token.value)
    token.type = reservada.get(token.value, 'ID')

    return token

def t_newline(token):
    r'\n+'
    token.lexer.lineno += len(token.value)

def t_whitespace(token):
    r'\s+'
    pass

# Error handling rule
def t_error(token):
    print("Error caracter no definido en token:'%s'" % token.value[0])
    token.lexer.skip(1)
    return token


# Codigo para leer Archivo --> Victor Alvarado

file =open("EjemplosAlvarado.txt", "r")
if file.mode=="r":
    datos=file.read()


lexer = lex.lex()


def leerLexer1():
    lexer.input(datos)
    while True:
        tk = lexer.token()
        if not tk:
            break
        print(str(tk))
leerLexer1()