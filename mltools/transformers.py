# Helper functions for custom transformations

# BaseEstimator gives your class 2 extra methods get_params() and set_params()
# if you do not use *args and **kargs in your constructor.

# TransformerMixin gives you fit_transform() for free when added as a baseclass.
from sklearn.base import BaseEstimator, TransformerMixin
import numpy as np

# Example from Chapter 2 in hands-on ML 
# attr_addr = CombinedAttributesAdder(add_bedrooms_per_room=False)
# housing_extra_attr = attr_adder.transform(housing.values)

rooms_ix, bedroomis_ix, population_ix, households_ix = 3, 4, 5, 6

class CombinedAttributesAdder(BaseEstimator, TransformerMixin):
    def __init__(self, add_bedrooms_per_room = True): #no *args or*kargs
        self.add_bedrooms_per_room = add_bedrooms_per_room
    def fit(self, X, y=None):
        return self # nothing else to do
    def transform(self, X, y=None):
        rooms_per_household = X[:, rooms_ix] / X[:, households_ix]
        population_per_household = X[:,population_ix] / X[:, households_ix]
        if self.add_bedrooms_per_room:
            bedrooms_per_room = X[:, bedroomis_ix] / X[:, rooms_ix]
            return np.c_[X, rooms_per_household, population_per_household, bedrooms_per_room]
        else:
            return np.c_[X, rooms_per_household, population_per_household]