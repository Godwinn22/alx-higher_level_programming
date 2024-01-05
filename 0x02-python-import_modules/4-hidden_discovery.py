#!/usr/bin/python3.8
import dis
import types


def print_hidden_names():

    with open("hidden_4.pyc", "rb") as file:
        code = file.read()
    # Disassemble the bytecode
    bytecode = dis.Bytecode(code)

    # Extract and print names that do not start with "__"
    for instruction in bytecode:
        if isinstance(instruction.argval, types.CodeType):
            inner_bytecode = dis.Bytecode(instruction.argval)
            for inner_instruction in inner_bytecode:
                if inner_instruction.opname == 'LOAD_CONST':
                    name = inner_instruction.argval
                    if isinstance(name, str) and not name.startswith('__'):
                        print(name)


if __name__ == "__main__":
    print_hidden_names()
