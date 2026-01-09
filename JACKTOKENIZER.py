import re

KEYWORDS = {
    "class", "constructor", "function", "method", "field", "static",
    "var", "int", "char", "boolean", "void", "true", "false", "null",
    "this", "let", "do", "if", "else", "while", "return"
}

SYMBOLS = set("{}()[].,;+-*/&|<>=~")

class JackTokenizer:
    def __init__(self, input_file):
        with open(input_file, 'r') as f:
            self.code = f.read()
        self.tokens = []
        self.current = 0
        self.tokenize()

    def remove_comments(self):
        pattern = r"//.*?$|/\*.*?\*/"
        self.code = re.sub(pattern, "", self.code, flags=re.DOTALL | re.MULTILINE)

    def tokenize(self):
        self.remove_comments()
        token_pattern = r'"[^"\n]*"|[{}()[\].,;+\-*/&|<>=~]|[A-Za-z_]\w*|\d+'
        for match in re.finditer(token_pattern, self.code):
            self.tokens.append(match.group())

    def has_more_tokens(self):
        return self.current < len(self.tokens)

    def advance(self):
        token = self.tokens[self.current]
        self.current += 1
        return token

    def token_type(self, token):
        if token in KEYWORDS:
            return "keyword"
        elif token in SYMBOLS:
            return "symbol"
        elif token.isdigit():
            return "integerConstant"
        elif token.startswith('"') and token.endswith('"'):
            return "stringConstant"
        else:
            return "identifier"
