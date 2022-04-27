import ply.lex as lex


class LatexLexer(object):
    tokens = (
        'AUTHOR',
        'BEGIN_DOCUMENT',
        'BEGIN_OLIST',
        'BEGIN_ULIST',
        'BEGIN_TABULAR',
        'BOLD',
        'CENTERLINE',
        'CHAPTER',
        'COLUMN_DIVIDER',
        'COLUMN_PATTERN_BORDERLESS',
        'COLUMN_PATTERN_BORDERED',
        'DOCUMENTCLASS',
        'END_DOCUMENT',
        'END_OLIST',
        'END_ULIST',
        'END_TABULAR',
        'GRAPHICS_PATH',
        'HLINE',
        'INCLUDE_GRAPHICS',
        'ITALIC',
        'ITEM',
        'LBRACE',
        'NEW_LINE',
        'NULL',
        'PARAGRAPH',
        'RBRACE',
        'ROW_END',
        'SECTION',
        'SUBSECTION',
        'SUBSUBSECTION',
        'TEXT',
        'TITLE',
        'UNDERLINE',
        'URL',
        'USE_PACKAGE',
    )

    t_AUTHOR = r'\\author'
    t_BEGIN_DOCUMENT = r'\\begin\{document\}'
    t_BEGIN_OLIST = r'\\begin\{enumerate\}'
    t_BEGIN_ULIST = r'\\begin\{itemize\}'
    t_BEGIN_TABULAR = r'\\begin\{tabular\}'
    t_BOLD = r'\\textbf'
    t_CENTERLINE = r'\\centerline'
    t_CHAPTER = r'\\chapter'
    t_COLUMN_DIVIDER = r'&'
    t_COLUMN_PATTERN_BORDERLESS = r'\{[lcr](\s[lcr])*\}'
    t_COLUMN_PATTERN_BORDERED = r'\{(\|\s[lcr]\s)+\|\}'
    t_DOCUMENTCLASS = r'\\documentclass.*'
    t_END_DOCUMENT = r'\\end\{document\}'
    t_END_OLIST = r'\\end\{enumerate\}'
    t_END_ULIST = r'\\end\{itemize\}'
    t_END_TABULAR = r'\\end\{tabular\}'
    t_GRAPHICS_PATH = r'\\graphicspath'
    t_INCLUDE_GRAPHICS = r'\\includegraphics'
    t_ITALIC = r'\\textit'
    t_ITEM = r'\\item'
    t_LBRACE = r'\{'
    t_NEW_LINE = r'\\newline'
    t_NULL = r'\0'
    t_PARAGRAPH = r'\\paragraph'
    t_RBRACE = r'\}'
    t_ROW_END = r'\\\\'
    t_SECTION = r'\\section'
    t_SUBSECTION = r'\\subsection'
    t_SUBSUBSECTION = r'\\subsubsection'
    t_TEXT = r'[\w\d\.,!?@#/\'\"<>\(\)\-+=\/^\*:;|\[\]]+'
    t_TITLE = r'\\title'
    t_UNDERLINE = r'\\underline'
    t_URL = r'\\url'
    t_USE_PACKAGE = r'\\usepackage.*'

    # New line rule
    def t_newline(self, t):
        r'\n+'
        t.lexer.lineno += t.value.count("\n")

    # Comment rule
    def t_comment(self, t):
        r'%.*\n'
        pass

    def t_hline(self, t):
        r'\\hline'
        pass

    t_ignore = ' '

    # Column finding rule
    def find_column(self, input, token):
        line_start = input.rfind('\n', 0, token.lexpos) + 1
        return (token.lexpos - line_start) + 1

    # Error handling rule
    def t_error(self, t):
        print("Illegal character '%s'" % t.value[0])
        t.lexer.skip(1)

    def __init__(self):
        self.lexer = lex.lex(module=self)

    # Build the lexer
    def build(self, **kwargs):
        self.lexer = lex.lex(module=self, **kwargs)

    def test(self, data):
        self.lexer.input(data)

        next_token = self.lexer.token()
        while next_token is not None:
            print(next_token)
            next_token = self.lexer.token()
