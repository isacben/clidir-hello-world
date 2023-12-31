import argparse

description = "say hello to a person"

def run(args: list[str]) -> None:
    parser = argparse.ArgumentParser(prog='cli-app hello person')
    parser.add_argument("name", help="name of the person to greet")
    params = parser.parse_args(args)

    print('Hello', params.name)