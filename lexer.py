import ply.lex as lex

# Definicion de palagbras reservada ---> Paula Benites
reservada= {
            'var':"VAR",'val':"VAL",
            'Int':"INT",'Double':"DOUBLE",'Boolean':"BOOLEAN", 'String':"STRING",
            'true':"TRUE",'false':"FALSE",
            'print' : "PRINT",'println' : "PRINTLN",'readline' : "READLINE",
            'isEmpty' : "ISEMPTY",'size':"SIZE",'slice':"SLICE",
            "values" : "VALUES", "keys" : "KEYS",
            'else' : "ELSE", "if" : "IF",
            'while' : "WHILE",
            'for' : "FOR", 'step':"STEP",'in':"IN",
            'fun' : "FUN", 'return' : "RETURN", 'to' : "TO",
            'listOf':"LISTOF",'setOf':"SETOF",'mapOf':"MAPOF",'Pair' : "PAIR",
            'first':"FIRST",'capitalize':"CAPITALIZE"
}


# Definicion de las lista de tokens --> Victor Alvardado
tokens = [
    'ENTERO', 'DECIMAL', 'ID', 'CADENA_DE_CARACTERES',
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE',
    'EQUALS', 'DOSPUNTOS', 'COMA','PUNTO','PUNTOS', 'EQUAL',
    'LARGE', 'SMALL', 'NOTEQ', 'LRGEQ', 'SMLEQ',
    'ILLAVE','DLLAVE', 'IPAR', 'DPAR','ICOR','DCOR',
    'AND','NOT','OR','NEGATION',
    "INDENT", 'newline','TAB',

] + list(reservada.values())

# Regular expression rules for simple tokens -- Paula Benites
t_PLUS    = r'\+'
t_ILLAVE    = r'\{'
t_DLLAVE    = r'\}'
t_ICOR    = r'\['
t_DCOR    = r'\]'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_IPAR  = r'\('
t_DPAR  = r'\)'
t_EQUALS  = r'='
t_DOSPUNTOS = r':'
t_PUNTO     =r'\.'
t_COMA      =r'\,'
t_CADENA_DE_CARACTERES = r"\"[a-zA-Z0-9\s]*\"|'[a-zA-Z0-9\s]*'"
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

# definicion de la funciones exectp estructuras de control -- > Scarlet Espinoza
# Reglas de correspondencia


def t_DECIMAL(t):
    r'\d+\.\d+'
    t.value = float(t.value[::])
    return t

def t_ENTERO(t):
    r'\d+'
    t.value = int(t.value)
    return t


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


# Codigo para leer Archivo
#
# file =open("ejemplo.txt", "r")
# if file.mode=="r":
#     datos=file.read()


lexer = lex.lex()
#
# #
# def leerLexer1():
#     lexer.input(datos)
#     while True:
#         tk = lexer.token()
#         if not tk:
#             break
#         print(str(tk))
# leerLexer1()