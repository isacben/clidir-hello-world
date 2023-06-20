import sys

import clidir 

def main() -> int:
    args = sys.argv[1:]
    clidir.run(args)
    
    return 0

if __name__ == "__main__":
    exit(main())
