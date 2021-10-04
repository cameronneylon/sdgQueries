from pathlib import Path
from boolean_parser import Parser
from parsing.parser_classes import search_term

INPUT_QUERY_DIRECTORY = Path('input_queries')
TEST_FILE = 'SDG02_2021.txt'

Parser.build_parser(clauses=[search_term])
parser = Parser()

with open(INPUT_QUERY_DIRECTORY/TEST_FILE) as f:
    query = f.read()

result = parser.parse(query)

print()
