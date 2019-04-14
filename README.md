# Tomaco

Like "Tomacco", but without a "c" for copyright concerns.

Tomaco is a Pomodoro app, to leverage your productivity and help you getting things done.

## Instalation

Make sure that you have [_Python 3.7_](https://www.python.org/downloads/) installed. We strongly recommend the use of [_pyenv_](https://github.com/pyenv/pyenv). In fact, the `pipenv install` command is going to run underneath the hood when installing the project via `Makefile`:

```
$ make setup
```

## Running

To run the project under development mode, run `make run`. It's going to use Bottle's development server, serving the service through `localhost:8080`.

## Contributing

Please read the [CONTRIBUTING.md](CONTRIBUTING.md) guide.
