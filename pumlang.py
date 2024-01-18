import sys


class Interpreter:

    def __init__(self):
        self.vars = {}

    def run(self, c):
        lines = c.split('\n')
        while lines:
            line = lines[0].strip()
            if line.startswith('if '):
                a = lines
                pairs = []
                for j in range(len(a)):
                    if a[j] == "{":
                        c = 0
                        for i in range(j, len(a)):
                            if a[i] == "{":
                                c += 1
                            if a[i] == "}":
                                c -= 1
                            if c == 0:
                                pairs.append([j, i])
                                break
                a = pairs[0]
                condition = line[3:]
                if '{' not in lines[lines.index(line) + 1]:
                    print(f"Syntax error: missing {'{'} in line: {line, lines.index(line) + 1}")
                    quit()
                if self.eval(condition):
                    block_lines, i = self.get_block(lines, lines.index(line))
                    self.run_block(block_lines)
                    lines = lines[a[1]:]
                else:
                    lines = lines[a[1]:]
            elif line.startswith('while '):
                a = lines
                pairs = []
                for j in range(len(a)):
                    if a[j] == "{":
                        c = 0
                        for i in range(j, len(a)):
                            if a[i] == "{":
                                c += 1
                            if a[i] == "}":
                                c -= 1
                            if c == 0:
                                pairs.append([j, i])
                                break
                a = pairs[0]
                condition = line[6:]
                if '{' not in lines[lines.index(line) + 1]:
                    print(f"Syntax error: missing {'{'} in line: {line, lines.index(line) + 1}")
                    quit()
                block_lines, i = self.get_block(lines, lines.index(line))
                while self.eval(condition):
                    self.run_block(block_lines)
                lines = lines[a[1]:]
            elif line.startswith('int '):
                var_name, expr = line[4:].split('=')
                var_name = var_name.strip()
                expr = expr.strip()
                if '.' in expr:
                    print(f"SyntaxError: The wrong data type is selected in line: {line, lines.index(line)}")
                    quit()
                try:
                    var_type = expr.strip().split()[0]
                except IndexError:
                    print(f"The value of the expression is not entered in line:{line, lines.index(line)}")
                    quit()
                value = self.eval(expr)
                self.vars[var_name] = {'type': var_type, 'value': value}
            elif line.startswith('input '):
                if 'int' in line:
                    var_name = line[10:].strip()
                    if var_name == "":
                        print(f"NameError: Variable name not specified in line: {line, lines.index(line)}")
                        quit()
                    user_input = input()
                    if '.' in user_input:
                        print(f"SyntaxError: The wrong data type is selected in line: {line, lines.index(line)}")
                        quit()
                    self.vars[var_name] = {'type': user_input, 'value': self.eval(user_input)}
                elif 'float' in line:
                    var_name = line[12:].strip()
                    if var_name == "":
                        print(f"NameError: Variable name not specified in line: {line, lines.index(line)}")
                        quit()
                    user_input = input()
                    if '.' not in user_input:
                        user_input += '.0'
                    self.vars[var_name] = {'type': user_input, 'value': self.eval(user_input)}
                else:
                    print(f"IndexError: The data type of the input arguments is not specified in line: {line, lines.index(line)}")
                    quit()
            elif line.startswith('float '):
                var_name, expr = line[6:].split('=')
                var_name = var_name.strip()
                expr = expr.strip()
                if '.' not in expr:
                    expr += '.0'
                try:
                    var_type = expr.strip().split()[0]
                except IndexError:
                    print(f"The value of the expression is not entered in line:{line, lines.index(line)}")
                    quit()
                value = self.eval(expr)
                self.vars[var_name] = {'type': var_type, 'value': value}
            elif line.startswith('bool '):
                var_name, expr = line[5:].split('=')
                var_name = var_name.strip()
                expr = expr.strip()
                if expr != 'True' and expr != 'False':
                    print(f"Incorrect value for a Boolean variable in line: {line, lines.index(line)}")
                    quit()
                var_type = expr.strip().split()[0]
                value = self.eval(expr)
                self.vars[var_name] = {'type': var_type, 'value': value}
            elif line.startswith('print '):
                expr = line[6:]
                value = self.eval(expr)
                print(value)
            elif line.startswith('quit'):
                quit()
            elif '=' in line:
                try:
                    var_name, expr = line.split('=')
                except ValueError:
                    print(f"ValueError the symbol = is missing in the line: {line, lines.index(line)}")
                    quit()
                var_name = var_name.strip()
                expr = expr.strip()
                try:
                    var_type = expr.strip().split()[0]
                except IndexError:
                    print(f"The value of the expression is not entered in line:{line, lines.index(line)}")
                    quit()
                value = self.eval(expr)
                self.vars[var_name] = {'type': var_type, 'value': value}
            elif line.startswith('Russia'):
                quit()
            else:
                print(f"Syntax error: + {line, lines.index(line) + 1}")
                quit()
            lines.pop(0)

    def run_block(self, lines):
        if len(lines) == 0:
            return
        indent = len(lines[0]) - len(lines[0].lstrip())
        for line in lines:
            if len(line) - len(line.lstrip()) != indent:
                raise Exception("Syntax error: indentation")
        self.run('\n'.join(lines))

    def get_block(self, lines, start):
        indent = len(lines[start]) - len(lines[start].lstrip())
        block_lines = [lines[start].strip()]
        i = start + 1
        while i < len(lines) and len(lines[i]) > 0 and len(lines[i].strip()) > 0 and len(lines[i]) - len(
                lines[i].lstrip()) == indent:
            block_lines.append(lines[i].strip())
            i += 1

        a = block_lines
        pairs = []
        for j in range(len(a)):
            if a[j] == "{":
                c = 0
                for i in range(j, len(a)):
                    if a[i] == "{":
                        c += 1
                    if a[i] == "}":
                        c -= 1
                    if c == 0:
                        pairs.append([j, i])
                        break
        a = pairs[0]

        return block_lines[a[0] + 1:a[1]], i - 1

    def eval(self, expr):
        if expr.isdigit():
            return int(expr)
        elif '.' in expr:
            return float(expr)
        elif expr in ['True', 'False']:
            return expr
        elif expr in self.vars:
            return self.vars[expr]['value']
        elif 'and' in expr:
            left, right = expr.split('and')
            return self.eval(left.strip()) and self.eval(right.strip())
        elif '<=' in expr:
            left, right = expr.split('<=')
            return self.eval(left.strip()) <= self.eval(right.strip())
        elif '>=' in expr:
            left, right = expr.split('>=')
            return self.eval(left.strip()) >= self.eval(right.strip())
        elif '>' in expr:
            left, right = expr.split('>')
            return self.eval(left.strip()) > self.eval(right.strip())
        elif '<' in expr:
            left, right = expr.split('<')
            return self.eval(left.strip()) < self.eval(right.strip())
        elif '==' in expr:
            left, right = expr.split('==')
            return self.eval(left.strip()) == self.eval(right.strip())
        elif '!=' in expr:
            left, right = expr.split('!=')
            return self.eval(left.strip()) != self.eval(right.strip())
        elif '+' in expr:
            left, right = expr.split('+')
            return self.eval(left.strip()) + self.eval(right.strip())
        elif '-' in expr:
            left, right = expr.split('-')
            if not left:
                return 0 - self.eval(right.strip())
            else:
                return self.eval(left.strip()) - self.eval(right.strip())
        elif '*' in expr:
            left, right = expr.split('*')
            return self.eval(left.strip()) * self.eval(right.strip())
        elif '/' in expr:
            left, right = expr.split('/')
            return self.eval(left.strip()) / self.eval(right.strip())
        elif '//' in expr:
            left, right = expr.split('//')
            return self.eval(left.strip()) // self.eval(right.strip())
        elif '%' in expr:
            left, right = expr.split('%')
            return self.eval(left.strip()) % self.eval(right.strip())
        else:
            print("Incorrect operation or uses the name of a variable that is not defined in the code")
            quit()


Run_code = Interpreter()
code = open(sys.argv[1], 'r')
Run_code.run(code.read())
