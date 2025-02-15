import re

# Token types
TOKEN_TYPES = {
    "SECTION": r"\.SECTION",
    "IDENTIFIER": r"[A-Z0-9]+",
    "LPAREN": r"",
    "RPAREN": r"",
    "COMMENT": r"#.*",
    "WHITESPACE": r"\s+",
}

class Lexer:
    def __init__(self, source_code):
        self.source = source_code
        self.tokens = []
    
    def tokenize(self):
        position = 0
        while position < len(self.source):
            match = None
            for token_type, pattern in TOKEN_TYPES.items():
                regex = re.compile(pattern)
                match = regex.match(self.source, position)
                if match:
                    if token_type != "WHITESPACE" and token_type != "COMMENT":
                        self.tokens.append((token_type, match.group(0)))
                    position = match.end()
                    break
            if not match:
                raise SyntaxError(f"Unexpected character at position {position}: {self.source[position]}")
        return self.tokens

# Example usage
code = """
.SECTION STRUCTURE
    BTA1
    BTA2

.SECTION LINKAGES
    BHP1 (BTA1, BTA2)
"""

lexer = Lexer(code)
tokens = lexer.tokenize()
for token in tokens:
    print(token)
