# clidir-hello-world

clidir example Hello World CLI

## Commands

Say hello:

### `cli-app hello person NAME`

```shell
usage: cli-app hello person [-h] name

positional arguments:
  name        name of the person to greet

options:
  -h, --help  show this help message and exit
```

See code: [commands/hello/person.py](commands/hello/person.py)

### `cli-app say bye`

Say goodbye:

```shell
usage: hello-world say bye [-h]

options:
  -h, --help  show this help message and exit
```

See code: [commands/say/bye.py](commands/say/bye.py)