import numpy as np
import pandas as pd

class Wallet:
 
    # init method or constructor
    def __init__(self, balance):
        self.balance = balance
 

    def set_balance(self , val):
      self.balance = self.balance + val
    
    
    def get_balance(self):
      return self.balance
    
    def remove_balance(self , val):
      self.balance = self.balance - val
