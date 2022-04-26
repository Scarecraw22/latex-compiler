import ply.lex as lex


class LatexLexer(object):
    tokens = ("BEGIN_DOC", "END_DOC", "TITLE", "COMMENT",
              "SECTION", "SUBSECTION", "BEGIN_UNORDERED_LIST", "END_UNORDERED_LIST",
              "BEGIN_ORDERED_LIST", "END_ORDERED_LIST", "LIST_ITEM", "ITALIC", "TEXT")

    t_BEGIN_DOC = r'\\begin\{document}'
    t_END_DOC = r'\\end\{document}'
    t_TITLE = r'\\title\{[\w\s\d]*}'
    t_SECTION = r'\\section{[\w\s\d]*}'
    t_SUBSECTION = r'\\subsection{[\w\s\d]*}'
    t_BEGIN_UNORDERED_LIST = r'\\begin{itemize}'
    t_END_UNORDERED_LIST = r'\\end{itemize}'
    t_BEGIN_ORDERED_LIST = r'\\begin{enumerate}'
    t_END_ORDERED_LIST = r'\\end{enumerate}'
    t_LIST_ITEM = r'\\item'
    t_ITALIC = r'\\textit{[\w\s\d]*}'
    t_TEXT = r'[A-Za-z,;:\'"\s\d]+'

    # New line rule
    def t_newline(self, t):
        r'\n+'
        t.lexer.lineno += len(t.value)

    # Comment rule
    def t_COMMENT(self, t):
        r'%.*'
        pass

    # Column finding rule
    def find_column(self, input, token):
        line_start = input.rfind('\n', 0, token.lexpos) + 1
        return (token.lexpos - line_start) + 1

    # Error handling rule
    def t_error(self, t):
        print("Illegal character '%s'" % t.value[0])
        t.lexer.skip(1)

    # Build the lexer
    def build(self, **kwargs):
        self.lexer = lex.lex(module=self, **kwargs)

    def test(self, data):
        self.lexer.input(data)

        next_token = self.lexer.token()
        while next_token is not None:
            print(next_token)
            next_token = self.lexer.token()


