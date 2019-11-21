from marshmallow import post_load

from .transcation import Transaction, TransactionSchema
from .transcation_type import TranscationType


class Income(Transaction):
  def __init__(self, description, amount):
    super(Income, self).__init__(description, amount)
  pass