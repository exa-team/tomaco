# Tomaco

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

Like "Tomacco", but without a "c" for copyright concerns.

Tomaco is a Pomodoro app, to leverage your productivity and help you getting things done.

## Instalation

Make sure that you have [_Python 3.7.x_](https://www.python.org/downloads/) and [_Node 10.15.x_](https://nodejs.org/en/download/) installed. We strongly recommend the use of [_pyenv_](https://github.com/pyenv/pyenv) and [_nvm_](https://github.com/nvm-sh/nvm). In fact, the `pipenv install` command is going to run underneath the hood when installing the project via `Makefile`:

```
$ make setup
```

## Running

Since the project needs to serve both the web server and the build process for Javascript/CSS bundling, it's possible to run them in two different processes:

```
$ make run-javascript&
$ make run-python
```

A better option is to run than via the same Makefile task, but in parallel:

```
$ make -j2 run
```

It's going to use Bottle's development server, serving the service through `localhost:8080`, and Brunch building processes to deal with the assets.

## Testing

To run the automated tests for the "Python side of the project", there is a special task for it:

```
$ make test-python
```

As expected, we also have an option for the Javascript portion of the code:

```
$ make test-javascript
```

If you are wiling to test both, simply use `test`:

```
$ make test
```

Linting is a good way of keeping the code quality high. You can have everything you want (Python, Javascript and security checks) in a single task:

```
$ make lint
```

## Contributing

Please read the [CONTRIBUTING.md](CONTRIBUTING.md) guide.
