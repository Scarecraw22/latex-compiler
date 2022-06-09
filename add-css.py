input_file = 'output.html'
output_file = 'output-with-css.html'

with open(input_file) as in_file, open(output_file, 'w') as out_file:
    for line in in_file:
        out_file.write(line)
        if line.strip() == '<meta charset="UTF-8" />':
            out_file.write('\t<link rel="stylesheet" href="mystyle.css">\n')
