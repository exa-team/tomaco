# Contributing

As an open source project, we welcome contributions of many forms:

- Code patches
- Documentation improvements
- Bug reports

You can see below a set of conventions that is going to help your Pull Request to be approved by the reviewers.

## Git conventions

We follow the [_Conventional Commits_](https://www.conventionalcommits.org/en/v1.0.0-beta.3/) convention. It's helpful to give us more context about the content of the Pull Request, and what kind of issue (feature, bug, chore) you are contributing for.

We recommend the use of [_commitizen_](https://github.com/commitizen/cz-cli) as a helper to write commits following the rules above.

## Python conventions

We strongly encourage you to use [_pre-commit_](https://github.com/pre-commit/pre-commit). During a `git commit`, it'll run automatic _lint_ and _formatter_ tools, like [_flake8_](http://flake8.pycqa.org/en/latest/) and [_Black_](https://github.com/ambv/black). Needless to say that we follow [_PEP8_](https://www.python.org/dev/peps/pep-0008/) for our _Python_ code.
