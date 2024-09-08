from time import time
from datetime import date


print("Seconds since January 1, 1970: " + "{:,}".format(time())
      + " or " + "{:.2e}".format(time()) + " in scientific notation")
""" .2e specifies the format: e for scientific notation and 2 for
two decimal places. """
print(date.today().strftime("%B %d %Y"))

# Date, datetime and time objects all have an iternal method
# strftime(format), to represent time in the shape of a string,
# controlled by a specific formatting.
# %B Nom complet du mois dans la langue locale.
# %d Jour du mois sur deux chiffres.
# %Y Année complète sur quatre chiffres.
