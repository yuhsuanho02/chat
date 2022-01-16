def read_file(file):
    lines = []
    with open(file, 'r', encoding='utf-8-sig') as f:
        for line in f:
            lines.append(line.strip())
    return lines
def convert(lines):
    new = []
    person = None
    for line in lines:
        if line == 'Allen':
            person = 'Allen'
            continue
        elif line == 'Tom':
            person = 'Tom'
            continue
        if person:
            new.append(person + ':' + line)
    return new
def write_file(new_file, lines):
    with open(new_file,'w',encoding='utf-8') as nf:
        for nl in lines:
            nf.write(nl + '\n')
def main():
    lines = read_file('input.txt')
    lines = convert(lines)
    write_file('output.txt', lines)

main()




