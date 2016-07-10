import logging.config

logging.config.fileConfig('logging.conf')
logger = logging.getLogger('simpleLogger')

balance = 500  # amount of money user currently has


def deposit(amount):
    """
    :param amount: int, adds the specified amount of money to the balance
    """
    logger.debug('inside deposit, the amount has type: ' + str(type(amount)))
    assert isinstance(amount, int), 'amount must be an integer'

    global balance
    balance += amount


def withdraw(amount):
    """
    :param amount: int, decreases the specified amount of money to the balance
    """
    assert isinstance(amount, int), 'amount must be an integer'

    global balance
    balance -= amount
