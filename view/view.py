import text
from datetime import datetime

def menu() -> int:
    print(text.menu[0])
    for i in range(1, len(text.menu)):
        print(f"\t{i}. {text.menu[i]}")
    while True:
       selected = input(text.select_menu)
       if int(selected) > 0 and int(selected) <= len(text.menu):
           return int(selected)
       print(text.invalid_selection)

def show_nodes(node):
    if node:
        print(f'{node}: {node.value}')
    print(text.empty_node)


def print_message(message):
    print(message)

def add_node():
    new_node = {}
    for key, value in text.new_node.items():
        new_node[key] = input(value)
        new_node[key] = datetime.strptime(value)
    return new_node
