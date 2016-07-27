#!~/bin/python
# Fractional difference plots of EW vals for Yng and Old stars
# Corey Mutnik 160726


from astropy.io import ascii
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as ticker
from uncertainties import ufloat


def Only_Dwarfs():
	# Open file wing EW vals for all Yng stars
	Yng_EW_spt_table = ascii.read('Yng_EW_vals.txt')

	# Create empty lists
	yngmainseq, yngspt, caii, nai, nai_2tac2, ali, mgi_1tac5, mgi_1tac7, uncertainty_mgi_1tac7, uncertainty_caii, uncertainty_nai_2tac2, uncertainty_nai, uncertainty_ali, uncertainty_mgi_1tac5 = [], [], [], [], [], [], [], [], [], [], [], [], [], []

	# empty list for not dwarfs
	#   rm from txt file, making file of only dwarfs
	notDwarfs = []

	# Only use Yng Dwarf stars
	yngspttype = Yng_EW_spt_table['spt_type']
	for i in range(len(yngspttype)):
		if ('V' in yngspttype[i]) & ('IV' not in yngspttype[i]):
			yngspt.append(yngspttype[i])
			yngmainseq.append(Yng_EW_spt_table['standard_file'][i])
			caii.append(Yng_EW_spt_table['EW_caii'][i])
			nai.append(Yng_EW_spt_table['EW_nai'][i])
			nai_2tac2.append(Yng_EW_spt_table['EW_nai_2tac2'][i])
			ali.append(Yng_EW_spt_table['EW_ali'][i])
			mgi_1tac5.append(Yng_EW_spt_table['EW_mgi_1tac5'][i])
			mgi_1tac7.append(Yng_EW_spt_table['EW_mgi_1tac7'][i])
			uncertainty_mgi_1tac7.append(Yng_EW_spt_table['uncertainty_mgi_1tac7'][i])
			uncertainty_caii.append(Yng_EW_spt_table['uncertainty_caii'][i])
			uncertainty_nai_2tac2.append(Yng_EW_spt_table['uncertainty_nai_2tac2'][i])
			uncertainty_nai.append(Yng_EW_spt_table['uncertainty_nai'][i])
			uncertainty_ali.append(Yng_EW_spt_table['uncertainty_ali'][i])
			uncertainty_mgi_1tac5.append(Yng_EW_spt_table['uncertainty_mgi_1tac5'][i])
		else:
			notDwarfs.append(yngspttype[i])

	notDwarfs
	#>>['K0IV(e)', 'K0IV(e)', 'K0 / K2IV(e)', 'K0 / K1III+', 'K0III', 'K2 / K2IV(e)', 'SC5.5-C71e']

# Use this func to make file of only Yng dwarf stars
#Only_Dwarfs()

# open files with needed data
#yngDwarf_EW_spt_table = ascii.read('datFiles/YngDwarfs_EW_vals.txt')
#old_EW_spt_table = ascii.read('datFiles/Old_EW_vals.csv')
#match_yng_old = ascii.read('datFiles/Matched_Yng_Old.list', delimiter="|")
matched_yng_old = ascii.read('datFiles/Matched_Yng_Old_restricted.csv')

# make empty lists
caii_vals, caii_errs = [], []
nai_vals, nai_errs = [], []
ali_vals, ali_errs = [], []
mgi_1tac5_vals, mgi_1tac5_errs = [], []
mgi_1tac7_vals, mgi_1tac7_errs = [], []
nai_2tac2_vals, nai_2tac2_errs = [], []

# uncertainties doesn't work with tables so make a loop
for j in range(len(matched_yng_old)):
	yng_caii = ufloat(matched_yng_old['caii_yng'][j], matched_yng_old['caii_err_yng'][j])
	# Set young star data with uncertainties
	yng_nai = ufloat(matched_yng_old['nai_yng'][j], matched_yng_old['nai_err_yng'][j])
	yng_ali = ufloat(matched_yng_old['ali_yng'][j], matched_yng_old['ali_err_yng'][j])
	yng_mgi_1tac5 = ufloat(matched_yng_old['mgi_1tac5_yng'][j], matched_yng_old['mgi_1tac5_err_yng'][j])
	yng_mgi_1tac7 = ufloat(matched_yng_old['mgi_1tac7_yng'][j], matched_yng_old['mgi_1tac7_err_yng'][j])
	yng_nai_2tac2 = ufloat(matched_yng_old['nai_2tac2_yng'][j], matched_yng_old['nai_2tac2_err_yng'][j])

	# Set cooresponding old star data with uncertainties
	old_caii = ufloat(matched_yng_old['caii_old'][j], matched_yng_old['caii_err_old'][j])
	old_nai = ufloat(matched_yng_old['nai_old'][j], matched_yng_old['nai_err_old'][j])
	old_ali = ufloat(matched_yng_old['ali_old'][j], matched_yng_old['ali_err_old'][j])
	old_mgi_1tac5 = ufloat(matched_yng_old['mgi_1tac5_old'][j], matched_yng_old['mgi_1tac5_err_old'][j])
	old_mgi_1tac7 = ufloat(matched_yng_old['mgi_1tac7_old'][j], matched_yng_old['mgi_1tac7_err_old'][j])
	old_nai_2tac2 = ufloat(matched_yng_old['nai_2tac2_old'][j], matched_yng_old['nai_2tac2_err_old'][j])

	# Starclass from Yng star
	#yng_starclass = matched_yng_old['starclass'][j]# NOT needed inside loop
	# = matched_yng_old['obs_name']
	# = matched_yng_old['standard_file']
	# = matched_yng_old['stand_name']
	# = matched_yng_old['seqnum']
	frac_caii = abs(yng_caii - old_caii) / old_caii
	frac_nai = abs(yng_nai - old_nai) / old_nai
	frac_ali = abs(yng_ali - old_ali) / old_ali
	frac_mgi_1tac5 = abs(yng_mgi_1tac5 - old_mgi_1tac5) / old_mgi_1tac5
	frac_mgi_1tac7 = abs(yng_mgi_1tac7 - old_mgi_1tac7) / old_mgi_1tac7
	frac_nai_2tac2 = abs(yng_nai_2tac2 - old_nai_2tac2) / old_nai_2tac2

	# Append values and uncertainties to separate lists
	
	caii_vals.append(frac_caii.nominal_value)
	caii_errs.append(frac_caii.std_dev)

	nai_vals.append(frac_nai.nominal_value)
	nai_errs.append(frac_nai.std_dev)
	
	ali_vals.append(frac_ali.nominal_value)
	ali_errs.append(frac_ali.std_dev)
	
	mgi_1tac5_vals.append(frac_mgi_1tac5.nominal_value)
	mgi_1tac5_errs.append(frac_mgi_1tac5.std_dev)

	mgi_1tac7_vals.append(frac_mgi_1tac7.nominal_value)
	mgi_1tac7_errs.append(frac_mgi_1tac7.std_dev)

	nai_2tac2_vals.append(frac_nai_2tac2.nominal_value)
	nai_2tac2_errs.append(frac_nai_2tac2.std_dev)


# should be in same order, so this can go outside loop
yng_starclass = matched_yng_old['starclass']

EW_spt_type = list(yng_starclass)
breakup_spt_type = list(map(list, EW_spt_type))


##
# Mapping for observed stars
##
mapped_val = []
for k in range(len(breakup_spt_type)):
	val = 0
	if breakup_spt_type[k][1] == 'F':
		val += 0
	elif breakup_spt_type[k][1] == 'G':
		val += 10
	elif breakup_spt_type[k][1] == 'K':
		val += 20
	elif breakup_spt_type[k][1] == 'M':
		val += 30
	else:
		val += 1000
		print 'what spt type is this:', breakup_spt_type[k][1],' index: ', k
	#print breakup_spt_type[k], val
	
	if breakup_spt_type[k][2] == '1':
		val += 1
	elif breakup_spt_type[k][2] == '2':
		val += 2
	elif breakup_spt_type[k][2] == '3':
		val += 3
	elif breakup_spt_type[k][2] == '4':
		val += 4
	elif breakup_spt_type[k][2] == '5':
		val += 5
	elif breakup_spt_type[k][2] == '6':
		val += 6
	elif breakup_spt_type[k][2] == '7':
		val += 7
	elif breakup_spt_type[k][2] == '8':
		val += 8
	elif breakup_spt_type[k][2] == '9':
		val += 9
	else:
		val += 0
	#print breakup_spt_type[k], val

	mapped_val.append(val)

# used to modify X-tics
x_spec_list = ['F0', 'G0', 'K0', 'M0']



def plot_CaII():
	# CA II (0.888 um)
	plt.clf()
	fig, ax = plt.subplots()
	fig.subplots_adjust(left=0.125)

	plt.xlim(-0.5,34.5)
	#plt.ylim(-.5,7)

	ax.set_xlabel('Spectral Type')
	#ax.set_ylabel('EW ($\AA$)')
	ax.set_ylabel('EW ($\AA$): Yng-Old/Old')

	# X-TICS
	ax.set_xticks([0,10,20,30])
	ax.set_xticklabels((x_spec_list))
	ax.xaxis.set_minor_locator(ticker.MultipleLocator(2))

	# Y-TICS
	ax.yaxis.set_minor_locator(ticker.MultipleLocator(.25))
	ax.yaxis.set_major_locator(ticker.MultipleLocator(1))

	plt.errorbar(mapped_val, caii_vals, yerr=caii_errs,fmt='.',color='black')
	plt.title('Ca II (0.866$\mu$m)')
	plt.savefig('figs/caii_frac_diff.png')


def plot_NaI_1tac14():
	plt.clf()
	fig, ax = plt.subplots()
	fig.subplots_adjust(left=0.125)

	plt.xlim(-0.5,34.5)
	#plt.ylim(-.5,7)

	ax.set_xlabel('Spectral Type')
	#ax.set_ylabel('EW ($\AA$)')
	ax.set_ylabel('EW ($\AA$): Yng-Old/Old')

	# X-TICS
	ax.set_xticks([0,10,20,30])
	ax.set_xticklabels((x_spec_list))
	ax.xaxis.set_minor_locator(ticker.MultipleLocator(2))
	
	# Y-TICS
	ax.yaxis.set_minor_locator(ticker.MultipleLocator(.25))
	ax.yaxis.set_major_locator(ticker.MultipleLocator(1))

	plt.errorbar(mapped_val, nai_vals, yerr=nai_errs,fmt='.',color='black')
	plt.title('Na I (1.14$\mu$m)')
	plt.savefig('figs/nai_1tac14_frac_diff.png')


def plot_AlI():
	plt.clf()
	fig, ax = plt.subplots()
	fig.subplots_adjust(left=0.125)

	plt.xlim(-0.5,34.5)
	#plt.ylim(-.5,7)

	ax.set_xlabel('Spectral Type')
	#ax.set_ylabel('EW ($\AA$)')
	ax.set_ylabel('EW ($\AA$): Yng-Old/Old')

	# X-TICS
	ax.set_xticks([0,10,20,30])
	ax.set_xticklabels((x_spec_list))
	ax.xaxis.set_minor_locator(ticker.MultipleLocator(2))
	
	# Y-TICS
	ax.yaxis.set_minor_locator(ticker.MultipleLocator(.25))
	ax.yaxis.set_major_locator(ticker.MultipleLocator(1))

	plt.errorbar(mapped_val, ali_vals, yerr=ali_errs,fmt='.',color='black')
	plt.title('Al I (1.31$\mu$m)')
	plt.savefig('figs/ali_frac_diff.png')


def plot_MgI_1tac5():
	plt.clf()
	fig, ax = plt.subplots()
	fig.subplots_adjust(left=0.125)

	plt.xlim(-0.5,34.5)
	#plt.ylim(-.5,7)

	ax.set_xlabel('Spectral Type')
	#ax.set_ylabel('EW ($\AA$)')
	ax.set_ylabel('EW ($\AA$): Yng-Old/Old')

	# X-TICS
	ax.set_xticks([0,10,20,30])
	ax.set_xticklabels((x_spec_list))
	ax.xaxis.set_minor_locator(ticker.MultipleLocator(2))
	
	# Y-TICS
	ax.yaxis.set_minor_locator(ticker.MultipleLocator(.25))
	ax.yaxis.set_major_locator(ticker.MultipleLocator(1))

	plt.errorbar(mapped_val, mgi_1tac5_vals, yerr=mgi_1tac5_errs,fmt='.',color='black')
	plt.title('Mg I (1.49$\mu$m)')
	plt.savefig('figs/mgi_1tac5_frac_diff.png')


def plot_MgI_1tac7():
	plt.clf()
	fig, ax = plt.subplots()
	fig.subplots_adjust(left=0.125)

	plt.xlim(-0.5,34.5)
	#plt.ylim(-.5,7)

	ax.set_xlabel('Spectral Type')
	#ax.set_ylabel('EW ($\AA$)')
	ax.set_ylabel('EW ($\AA$): Yng-Old/Old')

	# X-TICS
	ax.set_xticks([0,10,20,30])
	ax.set_xticklabels((x_spec_list))
	ax.xaxis.set_minor_locator(ticker.MultipleLocator(2))
	
	# Y-TICS
	ax.yaxis.set_minor_locator(ticker.MultipleLocator(.25))
	ax.yaxis.set_major_locator(ticker.MultipleLocator(1))

	plt.errorbar(mapped_val, mgi_1tac7_vals, yerr=mgi_1tac7_errs,fmt='.',color='black')
	plt.title('Mg I (1.71$\mu$m)')
	plt.savefig('figs/mgi_1tac7_frac_diff.png')


def plot_NaI_2tac2():
	plt.clf()
	fig, ax = plt.subplots()
	fig.subplots_adjust(left=0.125)

	plt.xlim(-0.5,34.5)
	#plt.ylim(-.5,7)

	ax.set_xlabel('Spectral Type')
	#ax.set_ylabel('EW ($\AA$)')
	ax.set_ylabel('EW ($\AA$): Yng-Old/Old')

	# X-TICS
	ax.set_xticks([0,10,20,30])
	ax.set_xticklabels((x_spec_list))
	ax.xaxis.set_minor_locator(ticker.MultipleLocator(2))
	
	# Y-TICS
	ax.yaxis.set_minor_locator(ticker.MultipleLocator(.25))
	ax.yaxis.set_major_locator(ticker.MultipleLocator(1))

	plt.errorbar(mapped_val, nai_2tac2_vals, yerr=nai_2tac2_errs,fmt='.',color='black')
	plt.title('Na I (2.21$\mu$m)')
	plt.savefig('figs/nai_2tac2_frac_diff.png')



def plot_them_all():
	plot_CaII()
	plot_NaI_1tac14()
	plot_AlI()
	plot_MgI_1tac5()
	plot_MgI_1tac7()
	plot_NaI_2tac2()

plot_them_all()



