#!~/bin/python
# turn table from csv to latex format
# Corey Mutnik - 6/25/16

from astropy.io import ascii
from astropy.table import Table#, Column, MaskedColumn

# read in file to be converted
dfile = ascii.read('Table_for_paper_160624.csv')

# only pull desired data from infile
obj = dfile['Object']
ra = dfile['RA']
dec = dfile['DEC']
spt_type = dfile['Lit. Spectral Type']
date = dfile['UT Date']
jmag = dfile['J mag']
SNR = dfile['S/N']
exptime = dfile['Total Exp. Time (s)']
A0_stand = dfile['A0 standard']
Teff = dfile['Teff (K)']
twomass = dfile['2Mass designation']
other_name = dfile['other name']
irtf_stand = dfile['IRTF star used in comparison']

# designate data to write
#   make list out of arrays or list of astropy columns
dat2write = [obj, ra, dec, spt_type, date, jmag, SNR, exptime, A0_stand, Teff, twomass, other_name, irtf_stand]

# column names of data to write
#   strings combined into a tuple
cols2write = ('Object', 'RA', 'DEC', 'Lit. Spectral Type', 'UT Date', 'J', 'SNR', 'Total Exp. Time', 'A0 standard', 'Teff (K)', '2Mass designation', 'other name', 'IRTF star used in comparison')

# units of data to write
#   must be in dictionary format
unitsdict = {'Object': ' ', 'RA': ' ', 'DEC': ' ', 'Lit. Spectral Type': ' ', 'UT Date': ' ', 'J': '(mag)', 'S/N': ' ', 'Total Exp. Time': '(s)', 'A0 standard': ' ', 'Teff': '(K)', '2Mass designation': ' ', 'other name': ' ', 'IRTF star used in comparison': ' '}
#unitsdict = {'J': '(mag)', 'Total Exp. Time': '(s)', 'Teff': '(K)'}

# turn desired data into a table
#   remember to mask empty values
dtable = Table(dat2write, names=cols2write, masked=True)

# write data to designated output file
ascii.write(dtable, 'main_table.tex', Writer=ascii.Latex,
            latexdict={'preamble': r'\begin{center}',
                       'tablefoot': r'\end{center}',
                       'units': unitsdict,
                       'col_align': 'c|c|c|c|c|c|c|c|c|c|c|c|c',
                       'caption': r'Listed here are observed targets with corresponding information.~\label{tab:maintab}'})