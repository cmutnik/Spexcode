# import csv from googledocs and export as latex table


from astropy.io import ascii
from astropy.table import Table
import numpy as np

docname = 'csv_to_latex.tex'

# read in csv file starting from second row so row of column titles isnt used
#tabdat = ascii.read("11_16_15.csv", header_start=0, data_start=1)
tabdat = ascii.read("11_16_15.csv", delimiter=',', header_start=0, data_start=1)
#print tabdat


tabdat.write(docname, format='latex')


