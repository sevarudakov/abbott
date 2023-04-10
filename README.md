## System requirements

1. Install Python 3+

## Install Python dependencies:

    pip3 install -r requirements.txt

## Create config.ini file

For security reasons, the full configuration object is not committed to this repository. 
To configure the project, you need to copy `config.example.ini` file:

    cp config.example.ini config.ini

After you've done that, make sure to provide all the configuration options there.

## How to run the tests

You must navigate to the `tests` directory first:

    cd tests

### Running all test cases

```console
pytest
```

### Running positive test case scenarios

```console
pytest -m positive
```

### Running negative test case scenarios

```console
pytest -m negative
```

### Running test cases in parallel

Option `-n` that you can pass to `pytest` controls how many parallel threads will be executed when running the tests. 
Example:

```console
pytest -n 5 --browser "chrome"
```