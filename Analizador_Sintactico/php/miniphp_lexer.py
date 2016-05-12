import ply.lex as lex
import sys

#######
# palabras reservadas php
# http://php.net/manual/es/reserved.keywords.php
#####

# list of tokens
tokens = (

    # Reserverd words
    'BREAK',    
    'ELSE', 
    'ECHO', 
    'FOR',
    'IF', 
    'RETURN', 
    'WHILE', 
    'REQUIRE',
    'TRUE',
    'FALSE',
    'FUNCTION',
    'SWITCH',
    'CASE',
    'DEFAULT',
    'CLASS',
    'PUBLIC',
    'PRIVATE',
    'PROTECTED',
   
    # Symbols
    'PLUS',
    'PLUSPLUS',
    'MINUS',
    'MINUSMINUS',
    'TIMES',
    'DIVIDE',
    'LESS',
    'LESSEQUAL',
    'GREATER',
    'GREATEREQUAL',
    'EQUAL',
    'DEQUAL', 
    'DISTINT', 
    'ISEQUAL',
    'SEMICOLON',
    'COMMA',
    'LPAREN',
    'RPAREN',
    #~ 'LBRACKET',
    #~ 'RBRACKET',
    'LBLOCK',
    'RBLOCK',
    'COLON',
    'AMPERSANT',
    'STRING',

    # Others   
    'ID',
    'NUMBER',
    'OPEN_TAG',
    'CLOSE_TAG',
    'FUNCTION_NAME',

)

# Regular expressions rules for a simple tokens 
t_PLUS   = r'\+'
t_MINUS  = r'-'
t_TIMES  = r'\*'
t_DIVIDE = r'/'
t_EQUAL  = r'='
t_LESS   = r'<'
t_GREATER = r'>'
t_SEMICOLON = ';'
t_COMMA  = r','
t_LPAREN = r'\('
t_RPAREN  = r'\)'
#~ t_LBRACKET = r'\['
#~ t_RBRACKET = r'\]'
t_LBLOCK   = r'{'
t_RBLOCK   = r'}'
t_COLON   = r':'
t_AMPERSANT = r'\&'
t_DISTINT = r'!'


def t_FALSE(t):
    r'false'
    return t

def t_TRUE(t):
    r'true'
    return t
    
def t_CLASS(t):
    r'class'
    return t    
    
def t_PRIVATE(t):
    r'private'
    return t
    
def t_PUBLIC(t):
    r'public'
    return t
    
def t_PROTECTED(t):
    r'protected'
    return t

def t_STRING(t):
    r'(\"(.)*?\"|\'(.)*?\')'
    return t

def t_REQUIRE(t):
    r'require'
    return t

def t_WHILE(t):
    r'while'
    return t
    
def t_FUNCTION(t):
    r'function'
    return t
    
def t_SWITCH(t):
    r'switch'
    return t
    
def t_CASE(t):
    r'case'
    return t
    
def t_DEFAULT(t):
    r'default'
    return t

def t_OPEN_TAG(t):
    r'(<\?|<%)php'
    return t

def t_CLOSE_TAG(t):
    r'\?>|\%>'
    return t

def t_BREAK(t):
	r'break'
	return t

def t_ELSE(t):
	r'else'
	return t

def t_ECHO(t):
	r'echo'
	return t

def t_FOR(t):
	r'for'
	return t

def t_IF(t):
	r'if'
	return t

def t_RETURN(t):
	r'return'
	return t

def t_NUMBER(t):
    r'\d+(\.\d+)?'
    t.value = float(t.value)
    return t

def t_ID(t):
    r'\$ \w+(_\d\w)*'
    return t

def t_LESSEQUAL(t):
	r'<='
	return t

def t_GREATEREQUAL(t):
	r'>='
	return t

def t_DEQUAL(t):
	r'!='
	return t

def t_ISEQUAL(t):
	r'=='
	return t
    
def t_MINUSMINUS(t):
	r'--'
	return t

def t_PLUSPLUS(t):
	r'\+\+'
	return t
	
def t_FUNCTION_NAME(t):
    r'[a-zA-Z_\x7f-\xff][a-zA-Z0-9_\x7f-\xff]*'
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_comments(t):
    r'/\*(.|\n)*?\*/'
    t.lexer.lineno += t.value.count('\n')

def t_comments_C99(t):
    r'//(.)*?\n'
    t.lexer.lineno += 1

def t_error(t):
    print ("Lexical error: " + str(t.value[0]))
    t.lexer.skip(1)
    
def test(data, lexer):
	lexer.input(data)
	while True:
		tok = lexer.token()
		if not tok:
			break
		print (tok)
		
t_ignore = ' \t'

lexer = lex.lex()

if __name__ == '__main__':
	if (len(sys.argv) > 1):
		fin = sys.argv[1]
	else:
		fin = 'prueba.php'
	f = open(fin, 'r')
	data = f.read()
	print (data)
	lexer.input(data)
	test(data, lexer)
	input()

