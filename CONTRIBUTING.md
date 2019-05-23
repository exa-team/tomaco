# Contributing

As an open source project, we welcome contributions of many forms:

- Code patches
- Documentation improvements
- Bug reports

You can see below a set of conventions that is going to help your Pull Request to be approved by the reviewers.

## Git conventions

We follow the [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0-beta.3/) convention. It's helpful to give us more context about the content of the Pull Request, and what kind of issue (feature, bug, chore) you are contributing for.

We recommend the use of [commitizen](https://github.com/commitizen/cz-cli) as a helper to write commits following the rules above.

## Code conventions

We strongly encourage the use of [pre-commit](https://github.com/pre-commit/pre-commit). During a `git commit`, it'll run automatic lint and formatter tools, like [flake8](http://flake8.pycqa.org/en/latest/), [Black](https://github.com/ambv/black), and [Prettier](https://prettier.io/). Needless to say that we follow [PEP8](https://www.python.org/dev/peps/pep-0008/) for our Python code and [Airbnb's Style Guide](https://github.com/airbnb/javascript) for Javascript code.

We don't have any formal convention for CSS (yet). But we do encourage the use of [BEM](http://getbem.com/) for code organization and naming convention.

## Development conventions

- Test your code using automated tests
- Test your code manually before opening a Pull Request
- Lint your code. Always!
- [Baby Steps](https://henriquebastos.net/programacao/se-usa-baby-steps-no-mundo-real-da-programacao/) is preferable than big Pull Request tickets
- Premature optimization is the [root of all evil](https://medium.com/@thiagoricieri/anti-patterns-by-example-premature-optimization-f46056dd1e39)
- Be respectful and constructive when doing code reviews
