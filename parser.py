class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.position = 0
        self.ast = {"sections": {}}

    def parse(self):
        while self.position < len(self.tokens):
            token_type, token_value = self.tokens[self.position]
            
            if token_type == "SECTION":
                self.position += 1
                section_name = self.tokens[self.position][1]
                self.ast["sections"][section_name] = []
                self.position += 1  # Move to next token
            elif token_type == "IDENTIFIER":
                self.ast["sections"][section_name].append(token_value)
                self.position += 1
            elif token_type == "LPAREN":
                # Handling linkages
                linkage_name = self.tokens[self.position - 1][1]
                self.position += 1
                params = []
                while self.tokens[self.position][0] != "RPAREN":
                    if self.tokens[self.position][0] == "IDENTIFIER":
                        params.append(self.tokens[self.position][1])
                    self.position += 1
                self.ast["sections"][section_name].append({linkage_name: params})
                self.position += 1  # Move past RPAREN
            else:
                self.position += 1  # Skip unhandled tokens

        return self.ast

# Example usage
parser = Parser(tokens)
ast = parser.parse()
print(ast)
