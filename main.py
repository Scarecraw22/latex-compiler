from latex_lexer import LatexLexer

lexer = LatexLexer()
lexer.build()

file = open("sample_latex.tex", "r")
latex = file.read()
lexer.test(latex)
