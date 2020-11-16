import ply.lex as lex




token = (
    'INT', 'DOUBLE', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'TAB', 'newline',
    'EQUALS', 'DOSPUNTOS', 'COMA',
    'PUNTO','PUNTOS','CADENA_DE_CARACTERES', 'EQUAL', 'NOTEQ', 'LARGE', 'SMALL', 'LRGEQ', 'SMLEQ', 'ID', 'FALSO',
    'VERDAD', 'IPAR', 'DPAR', "INDENT","Int",'Double','Boolean','AND','NOT','OR','NEGATION','ILLAVE','DLLAVE',
    'VAL','VAR'
)

reserveda= ('ELSE','IF','RETURN','PRINT', 'WHILE','DEF')

tokens=token+reserveda
# Regular expression rules for simple tokens
t_PLUS    = r'\+'
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


t_EQUAL   = r'\=\='
t_NOTEQ   = r'\!\='
t_LARGE   = r'\>'
t_SMALL   = r'\<'
t_LRGEQ   = r'\>\='
t_SMLEQ   = r'\<\='
















file =open("codigo.txt", "r")
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