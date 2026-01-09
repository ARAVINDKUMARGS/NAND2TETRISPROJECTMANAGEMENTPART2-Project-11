from JackTokenizer import JackTokenizer
from VMWriter import VMWriter

class CompilationEngine:
    def __init__(self, input_file, output_file):
        self.tokenizer = JackTokenizer(input_file)
        self.vm = VMWriter(output_file)
        self.label_count = 0
        self.compile_class()

    def advance(self):
        if self.tokenizer.has_more_tokens():
            return self.tokenizer.advance()
        return None

    def compile_class(self):
        # Simplified: parse class
        self.advance()  # 'class'
        class_name = self.advance()  # class name
        self.advance()  # '{'
        while True:
            t = self.tokenizer.tokens[self.tokenizer.current]
            if t in ("static", "field"):
                self.compile_class_var()
            elif t in ("constructor", "function", "method"):
                self.compile_subroutine(class_name)
            elif t == "}":
                self.advance()
                break

    def compile_class_var(self):
        # Skip class variable declaration for brevity
        while self.advance() != ";":
            pass

    def compile_subroutine(self, class_name):
        # Skip subroutine keyword
        self.advance()
        # Return type
        self.advance()
        # Function name
        func_name = self.advance()
        self.advance()  # '('
        self.compile_parameter_list()
        self.advance()  # ')'
        self.compile_subroutine_body(func_name)

    def compile_parameter_list(self):
        # Skip for simplicity
        while self.tokenizer.tokens[self.tokenizer.current] != ")":
            self.advance()

    def compile_subroutine_body(self, func_name):
        self.advance()  # '{'
        # Handle var declarations
        while self.tokenizer.tokens[self.tokenizer.current] == "var":
            self.compile_var_dec()
        # Write VM function header
        self.vm.write_function(func_name, 0)  # nLocals simplified
        # Handle statements
        self.compile_statements()
        self.advance()  # '}'

    def compile_var_dec(self):
        while self.advance() != ";":
            pass

    def compile_statements(self):
        while True:
            t = self.tokenizer.tokens[self.tokenizer.current]
            if t == "let":
                self.compile_let()
            elif t == "if":
                self.compile_if()
            elif t == "while":
                self.compile_while()
            elif t == "do":
                self.compile_do()
            elif t == "return":
                self.compile_return()
            else:
                break

    def compile_let(self):
        self.advance()  # let
        var_name = self.advance()
        if self.tokenizer.tokens[self.tokenizer.current] == "[":
            self.advance()  # [
            self.compile_expression()
            self.advance()  # ]
        self.advance()  # =
        self.compile_expression()
        self.advance()  # ;
        self.vm.write_pop("local", 0)  # simplified

    def compile_if(self):
        self.advance()
        self.advance()  # '('
        self.compile_expression()
        self.advance()  # ')'
        self.advance()  # '{'
        self.compile_statements()
        self.advance()  # '}'

    def compile_while(self):
        self.advance()
        self.advance()  # '('
        self.compile_expression()
        self.advance()  # ')'
        self.advance()  # '{'
        self.compile_statements()
        self.advance()  # '}'

    def compile_do(self):
        self.advance()  # do
        self.advance()  # function call
        self.advance()  # '('
        self.advance()  # ')'
        self.advance()  # ;
        self.vm.write_pop("temp", 0)

    def compile_return(self):
        self.advance()  # return
        if self.tokenizer.tokens[self.tokenizer.current] != ";":
            self.compile_expression()
        self.advance()  # ;
        self.vm.write_return()

    def compile_expression(self):
        # Simplified expression: push constants
        token = self.advance()
        if token.isdigit():
            self.vm.write_push("constant", int(token))
