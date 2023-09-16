import re


class SQLParser:
    def __init__(self):
        self.current_token = None
        self.tokens = []
        self.index = 0

    def parse(self, input_sql):
        self.tokens = re.findall(r'\w+|!=|<=|>=|[(),=*]', input_sql)
        self.index = 0
        self.current_token = self.tokens[self.index]

        self.sql()

    def match(self, expected_token):
        if self.current_token == expected_token:
            self.consume()
        else:
            raise ValueError(f"Expected '{expected_token}' but found '{self.current_token}'")

    def consume(self):
        self.index += 1
        if self.index < len(self.tokens):
            self.current_token = self.tokens[self.index]
        else:
            self.current_token = None

    def sql(self):
        self.match('SELECT')
        self.columns()
        self.match('FROM')
        self.match_identifier()  # Use the new function to match identifiers
        if self.current_token == 'WHERE':
            self.match('WHERE')
            self.condition()

    def columns(self):
        if self.current_token == '*':
            self.match('*')
        else:
            self.column()
            while self.current_token == ',':
                self.match(',')
                self.column()

    def column(self):
        self.match_identifier()  # Use the new function to match identifiers

    def condition(self):
        self.match_identifier()  # Use the new function to match identifiers
        self.match('=')
        self.value()

    def value(self):
        if self.current_token == "'":
            self.match("'")
        else:
            self.match('value')

    def match_identifier(self):
        if re.match(r'^[a-zA-Z_][a-zA-Z0-9_]*$', self.current_token):
            self.consume()
        else:
            raise ValueError(f"Error near '{self.current_token}'")


input_sql = "SELECT  * FROM table WHERE column1 = 'value'"
parser = SQLParser()
parser.parse(input_sql)
print("SQL is valid!")
