
# Tomaco

[![Build Status](https://travis-ci.org/exa-team/tomaco.svg?branch=master)](https://travis-ci.org/exa-team/tomaco)
[![Coverage Status](https://coveralls.io/repos/github/exa-team/tomaco/badge.svg)](https://coveralls.io/github/exa-team/tomaco)
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

Like "Tomacco", but without a "c" for copyright concerns.

Tomaco is a Pomodoro app, to leverage your productivity and help you getting things done.

## Instalation
Make sure that you have [_Python 3.7.x_](https://www.python.org/downloads/) and [_Node 10.15.x_](https://nodejs.org/en/download/) installed. We strongly recommend the use of [_pyenv_](https://github.com/pyenv/pyenv) and [_nvm_](https://github.com/nvm-sh/nvm). In fact, the `pipenv install` command is going to run underneath the hood when installing the project via `Makefile`:

```
$ make setup
```

If you prefer to user Docker. But make sure that you have [Docker]([https://www.docker.com/get-started](https://www.docker.com/get-started)) installed.

```
$ make docker-setup
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

Or you can run application with Docker:
```
$ make docker-run
```

It's going to use Flask's development server, serving the service through `localhost:8080`, and Brunch building processes to deal with the assets.

### Authenticating via Github

In order to use the authentication engine (which relies on Github underneath the hood), you might need some extra steps to run your application:

- [Create a Github app](https://developer.github.com/apps/building-github-apps/creating-a-github-app/)
- For development purposes, you can set the `Authorization callback URL` as `http://localhost:8080/login/complete`
- Copy the `client id` and `client secret` from Github
- Pass them to the application via environment var:

```
$ GITHUB_CLIENT_ID=<client_id> GITHUB_CLIENT_SECRET=<client_secret> make -j2 run
```

If you are using Docker, you must define the app environments in `services.tomaco.environment`
```
GITHUB_CLIENT_ID: "your-id"
GITHUB_CLIENT_SECRET: "your-secret"
```

## Debugging
If you want to use `pdb` as debug tool when using Docker, you must attach a new  tty to be able to execute commands. In a new terminal:
```
$ docker attach tomaco
```
To access the running instance of docker application, just run:
```
$ docker exec -it tomaco bash
```

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

Or using docker:
```
$ make test-docker
```

Linting is a good way of keeping the code quality high. You can have everything you want (Python, Javascript and security checks) in a single task:

```
$ make lint
```

## Contributing

Please read the [CONTRIBUTING.md](CONTRIBUTING.md) guide.
