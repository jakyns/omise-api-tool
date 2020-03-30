# Omise API Tool

Omise API Tool developing for making user to be more convenient calling Omise 
API in some scenarios developed by Python. This repository uses pipenv to 
manage all dependencies from Pipfile.

## Dependencies

- Python 3.7.3
- [Pipfile](https://github.com/pypa/pipfile)

## Installation

Copy environment file `.env.xxx` to  `.env` according to your environment and add necessary values.

Initiate virtual environment and generate Pipfile and Pipfile.lock by running:

```sh
pipenv lock
```

Install dependencies and get into virtual environment.

```sh
pipenv install && pipenv shell
```

Pipenv will automatically loads environment varibles from `.env` variables,
if they exist.

## Usage

## flow charge

Python script for generating token, create customer with card then create first
charge

```python
>>> import omise
>>> python flow_charge.py
```

## charges wave

Python script for creating amount of charges as you want

```python
>>> import omise
>>> python charges_wave.py {customer} {charges_amount}
```

## cards manufacture

Python script for creating amount of cards as you want

```python
>>> import omise
>>> python cards_manufacture.py {customer} {cards_amount}
```
