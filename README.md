# Omise API Tool

Omise API Tool developing for making user to be more convenient calling Omise 
API in some scenarios developed by Python. This repository uses pipenv to 
manage all dependencies from Pipfile.

```python
pipenv shell
pipenv install
```

create `development.cfg` or `production.cfg` in `config` folder by copying 
templates from `default.cfg` and fill in the values

## flow charge

Python script for generating token, create customer with card then create first
charge

### Usage

```python
>>> import omise
>>> python flow_charge.py
```

## charges wave

Python script for creating amount of charges as you want

### Usage

```python
>>> import omise
>>> python charges_wave.py {customer} {charges_amount}
```

## cards manufacture

Python script for creating amount of cards as you want

### Usage

```python
>>> import omise
>>> python cards_manufacture.py {customer} {cards_amount}
```
