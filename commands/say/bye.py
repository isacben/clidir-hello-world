import argparse

description = "say good bye"

def run(args: list[str]) -> None:
    parser = argparse.ArgumentParser(prog='cli-app say bye')
    parser.parse_args(args)
   
    print('Good bye!')
