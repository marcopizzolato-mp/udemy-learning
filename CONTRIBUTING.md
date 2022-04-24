# Developer Documentation

## Set up development environment

This project uses `poetry`, which you can install with:

```commandline
pip install poetry
```

To build the Python development environment, navigate to the base directory of this
project and run:
```commandline
poetry install
```

If that doesn't work, a new virtual environment can be created via a new shell with:

```commandline
poetry shell
```

To see the available commands using poetry, run:
```commandline
poetry --help
```

## Stripping notebook outputs
After cloning the repo, run the following to install the
[`nbstripout`](https://github.com/kynan/nbstripout) git filter, which excludes notebook
outputs from commits:

```
poetry run nbstripout --install
```

Check the status with:

```
poetry run nbstripout --status
```

## Including data in your project

By default, anything committed under the `data/` directory will be committed as a
[Git-LFS](https://git-lfs.github.com/) file, to minimise the impact any large
files have on diffs, checkouts etc. Any data files (raw or processed) that you
wish to share and version should be stored here.


## Developer task automation

Common development tasks are automated using [`invoke`](https://www.pyinvoke.org).

To see what these do, run:

```
> invoke --list
Available tasks:

  clean                  Clean up all test and build artifacts
  clean-build            Clean up build artifacts
  clean-test             Clean up test artifacts
  format                 Format the code using isort and Black
  show-coverage-report   Generate HTML coverage report and open in browser
  test                   Run all tests
  test-flake             Run flake8 syntax checker
  test-types             Run type checking
  test-unittests         Run unit tests
```


## Development workflow

1. Make a branch.
2. Make a change.
3. `invoke clean` to clean up files and directories which might have been generated
 by previous tests, builds, etc.
4. `invoke format` to tidy up the code
5. `invoke test` to run all the tests
6. Commit the change.
7. Repeat from step 2 as required.
8. Push new branch to GitLab.
9. Create a merge request.
10. Assign for code review.

**Note**: Standard practice is that the original developer of the branch is responsible
for making changes in order to fix issues that come up in code review. Others
committing to the branch can cause issues if the original developer decides to add a
further commit, so it is best avoided. Code review is also an opportunity for the
developer to learn, which should not be missed, so further changes should always be
done in consultation.


## Unit tests

The unit tests for this package use the Python library `pytest` module. This is a
test runner that provides useful output and also has some further features which can
be used to write tests more effectively.  If
you are not familiar with this, see: https://docs.pytest.org/en/latest/

If you're new to writing tests, you should also note that unit tests usually
follow the pattern like:
    1. set up initial conditions (dummy input variables, configuration parameters)
    2. execute the code under test (with the generated inputs)
    3. assert that the expected result has occurred (using the `assert` keyword)

This might typically look like:

```python
# test_capitalize.py

import pytest

from some_library import capital_case

def test_capital_case():
    assert capital_case('semaphore') == 'Semaphore'

def test_raises_exception_on_non_string_arguments():
    with pytest.raises(TypeError):
        capital_case(9)
```


### Reviewing test coverage

The `invoke test` utility should display a coverage report at the end of the
unittests to show which lines are missing test coverage, e.g.:

```
----------- coverage: platform win32, python 3.7.6-final-0 -----------
Name                                                       Stmts   Miss Branch BrPart  Cover   Missing
------------------------------------------------------------------------------------------------------
ricardo\ee\industrial_sites\some_module\submodule_a.py    97      4     46      4    94%   132->139, 143->144, 144, 165->176, 166->167, 167, 252, 262
ricardo\ee\industrial_sites\some_module\submodule_b.py    68      1     25      0    99%   168
------------------------------------------------------------------------------------------------------
TOTAL                                                        473      5     71      4    98%

4 files skipped due to complete coverage.

Required test coverage of 80.0% reached. Total coverage: 98.35%
```

Chasing 100% test coverage is a fools errand. Don't bother. That said, it may be
worth checking the missing statements in case you're missing coverage of critical
functionality.

An easy way to review missed coverage is with the HTML coverage report. Generate this
and load it in a browser with `invoke show-coverage-report`.

## Making releases off the `master` branch

1. Ensure `master` is up-to-date locally.
2. Bump the [semantic version](https://semver.org/) tag with one of the following:
    - `poetry version major` for major API breaking changes
    - `poetry version minor` for new backwards-compatible functionality
    - `poetry version patch` for backwards-compatible bug fixes
3. Check the new version number with `poetry version --short`.
4. Make a tag equivalent to the current version number of the package
    -  Substitute the output from step 3 into: `git tag -a v{poetry version --short} -m "v{poetry version --short}"`
5. Push the new commit and the tag to GitLab with `git push --follow-tags`

N.B.: Please try to avoid using the other valid bump rules supported by Poetry
(prepatch, preminor, premajor, prerelease).

### Helpful commands
1. The current semantic version can be checked with: `poetry version`.
2. A local version of the package can be built with: `poetry build`.


## Troubleshooting

### Data files aren't being included in my Python package

Add the name of the file or files that you want to include to the include list
under the `[tool.poetry]` section of the `pyproject.toml` file. For an example, see
[here](https://python-poetry.org/docs/pyproject/#include-and-exclude).
