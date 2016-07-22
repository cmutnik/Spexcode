#!~/bin/python
# reproduce figure 35 subplots
# EW as function of spectral type
# Corey Mutnik 7/7/16
# Modified:
#   7/13/16 - to only include Yng dwarfs
#   7/20/16 - formatting

from astropy.io import ascii
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as ticker


#EW_spt_table = ascii.read('EW_of_rayner_stars.txt')
EW_spt_table = ascii.read('/Users/cmutnik/work/astro/plots/EW/cool_stars_tab8_EW/obs_EW_vals_160624.txt')

# Create empty lists
yngmainseq, caii, nai, nai_2tac2, ali, mgi_1tac5, mgi_1tac7, uncertainty_mgi_1tac7, uncertainty_caii, uncertainty_nai_2tac2, uncertainty_nai, uncertainty_ali, uncertainty_mgi_1tac5 = [], [], [], [], [], [], [], [], [], [], [], [], []

# Only use Yng Dwarf stars
yngnames = EW_spt_table['spt type_standard_file']
for i in range(len(yngnames)):
	if ('V' in yngnames[i]) & ('IV' not in yngnames[i]):
		yngmainseq.append(yngnames[i])
		caii.append(EW_spt_table['EW_caii'][i])
		nai.append(EW_spt_table['EW_nai'][i])
		nai_2tac2.append(EW_spt_table['EW_nai_2tac2'][i])
		ali.append(EW_spt_table['EW_ali'][i])
		mgi_1tac5.append(EW_spt_table['EW_mgi_1tac5'][i])
		mgi_1tac7.append(EW_spt_table['EW_mgi_1tac7'][i])
		uncertainty_mgi_1tac7.append(EW_spt_table['uncertainty_mgi_1tac7'][i])
		uncertainty_caii.append(EW_spt_table['uncertainty_caii'][i])
		uncertainty_nai_2tac2.append(EW_spt_table['uncertainty_nai_2tac2'][i])
		uncertainty_nai.append(EW_spt_table['uncertainty_nai'][i])
		uncertainty_ali.append(EW_spt_table['uncertainty_ali'][i])
		uncertainty_mgi_1tac5.append(EW_spt_table['uncertainty_mgi_1tac5'][i])

#EW_spt_type = list(EW_spt_table['spt type_standard_file'])
# need modification for only dwarf stars
EW_spt_type = list(yngmainseq)
breakup_spt_type = list(map(list, EW_spt_type))

##
# Mapping for observed stars
##
mapped_val = []
for k in range(len(breakup_spt_type)):
	val = 0
	if breakup_spt_type[k][0] == 'B':
		val += 0
	elif breakup_spt_type[k][0] == 'A':
		val += 10
	elif breakup_spt_type[k][0] == 'F':
		val += 20
	elif breakup_spt_type[k][0] == 'G':
		val += 30
	elif breakup_spt_type[k][0] == 'K':
		val += 40
	elif breakup_spt_type[k][0] == 'M':
		val += 50
	else:
		val += 1000
		print 'what spt type is this:', breakup_spt_type[k][0],' index: ', k
	#print breakup_spt_type[k], val
	
	if breakup_spt_type[k][1] == '1':
		val += 1
	elif breakup_spt_type[k][1] == '2':
		val += 2
	elif breakup_spt_type[k][1] == '3':
		val += 3
	elif breakup_spt_type[k][1] == '4':
		val += 4
	elif breakup_spt_type[k][1] == '5':
		val += 5
	elif breakup_spt_type[k][1] == '6':
		val += 6
	elif breakup_spt_type[k][1] == '7':
		val += 7
	elif breakup_spt_type[k][1] == '8':
		val += 8
	elif breakup_spt_type[k][1] == '9':
		val += 9
	else:
		val += 0
	#print breakup_spt_type[k], val

	mapped_val.append(val)

# used to modify X-tics
x_spec_list = ['B0', 'A0', 'F0', 'G0', 'K0', 'M0']


# plot against EW values calculated for R09 stars
##
# CALCULATED NOT PUBLISHED
##
R09_EW_vals = ascii.read('EW_of_rayner_stars_new_feat_lims_160624_rm_pts.csv')

R09_caii = R09_EW_vals['EW_caii']
R09_nai = R09_EW_vals['EW_nai']
R09_nai_2tac2 = R09_EW_vals['EW_nai_2tac2']
R09_ali = R09_EW_vals['EW_ali']
R09_mgi_1tac5 = R09_EW_vals['EW_mgi_1tac5']
R09_mgi_1tac7 = R09_EW_vals['EW_mgi_1tac7']

R09_uncertainty_mgi_1tac7 = R09_EW_vals['uncertainty_mgi_1tac7']
R09_uncertainty_caii = R09_EW_vals['uncertainty_caii']
R09_uncertainty_nai_2tac2 = R09_EW_vals['uncertainty_nai_2tac2']
R09_uncertainty_nai = R09_EW_vals['uncertainty_nai']
R09_uncertainty_ali = R09_EW_vals['uncertainty_ali']
R09_uncertainty_mgi_1tac5 = R09_EW_vals['uncertainty_mgi_1tac5']

R09_EW_values = list(R09_EW_vals['standard_file'])
breakup_spt_type_R09 = list(map(list, R09_EW_values))


def calculated_R09_EW_values():
	global R09_mapped_val#, calcR09_colors

	R09_mapped_val = []
	for k in range(len(breakup_spt_type_R09)):
		val = 0
		if breakup_spt_type_R09[k][0] == 'B':
			val += 0
		elif breakup_spt_type_R09[k][0] == 'A':
			val += 10
		elif breakup_spt_type_R09[k][0] == 'F':
			val += 20
		elif breakup_spt_type_R09[k][0] == 'G':
			val += 30
		elif breakup_spt_type_R09[k][0] == 'K':
			val += 40
		elif breakup_spt_type_R09[k][0] == 'M':
			val += 50
		else:
			val += 1000
			print 'what spt type is this:', breakup_spt_type_R09[k][0],' index: ', k
		#print breakup_spt_type_R09[k], val
		if breakup_spt_type_R09[k][1] == '1':
			val += 1
		elif breakup_spt_type_R09[k][1] == '2':
			val += 2
		elif breakup_spt_type_R09[k][1] == '3':
			val += 3
		elif breakup_spt_type_R09[k][1] == '4':
			val += 4
		elif breakup_spt_type_R09[k][1] == '5':
			val += 5
		elif breakup_spt_type_R09[k][1] == '6':
			val += 6
		elif breakup_spt_type_R09[k][1] == '7':
			val += 7
		elif breakup_spt_type_R09[k][1] == '8':
			val += 8
		elif breakup_spt_type_R09[k][1] == '9':
			val += 9
		else:
			val += 0
		#print breakup_spt_type_R09[k], val
		R09_mapped_val.append(val)

def obs_calcedR09_6subplots_overlay():

	# call functions for mapping SptTyp and luminosity class
	calculated_R09_EW_values()

	# clear and setup subplots
	plt.clf()
	fig, ax = plt.subplots(3,2)
	
	##
	# Plot EW vals of R09 stars before Obs stars, so Obs stars showup on top
	##
	# initaliaze vars and make empty list
	n_supergiants,n_giants,n_dwarfs,n_missed,index = 0,0,0,0,0
	for jj in R09_EW_values:
		#print jj
		if 'IV' in jj:
			n_giants+=1
			ccc = 'orange'
			mrksym = 'v'#'s'
		elif 'V' in jj:
			n_dwarfs+=1
			ccc='red'
			mrksym = "8"#8,'s','p','$\mu$'
		elif "III" in jj:
			n_giants+=1
			ccc='orange'
			mrksym = 'v'#'s'
		elif 'II' in jj:
			n_supergiants+=1
			ccc='purple'
			mrksym = "^"#'p'
		elif 'I' in jj:
			n_supergiants+=1
			ccc='purple'
			mrksym = "^"#'p'
		else:
			n_missed+=1
			ccc='green'
			mrksym = '$?$'

		#elinewidth=1, capsize=1
		#barsabove=True

		#ax[0,0].errorbar(R09_mapped_val[index], R09_caii[index], yerr=R09_uncertainty_caii[index], color=ccc, fmt='.', capthick=1)
		#ax[0,0].errorbar(R09_mapped_val[index], R09_caii[index], yerr=R09_uncertainty_caii[index], color=ccc, fmt='', capthick=1, marker=mrksym)
		ax[0,0].errorbar(R09_mapped_val[index], R09_caii[index], 
			yerr=R09_uncertainty_caii[index], color=ccc, capthick=1, marker=mrksym, fmt='', mec=ccc, ms=3)#oldms)
		ax[0,1].errorbar(R09_mapped_val[index], R09_nai[index], 
			yerr=R09_uncertainty_nai[index], color=ccc, capthick=1, marker=mrksym, fmt='', mec=ccc, ms=3)
		ax[1,0].errorbar(R09_mapped_val[index], R09_ali[index], 
			yerr=R09_uncertainty_ali[index], color=ccc, capthick=1, marker=mrksym, fmt='', mec=ccc, ms=3)
		ax[1,1].errorbar(R09_mapped_val[index], R09_mgi_1tac5[index], 
			yerr=R09_uncertainty_mgi_1tac5[index], color=ccc, capthick=1, marker=mrksym, fmt='', mec=ccc, ms=3)
		ax[2,0].errorbar(R09_mapped_val[index], R09_mgi_1tac7[index], 
			yerr=R09_uncertainty_mgi_1tac7[index], color=ccc, capthick=1, marker=mrksym, fmt='', mec=ccc, ms=3)
		ax[2,1].errorbar(R09_mapped_val[index], R09_nai_2tac2[index], 
			yerr=R09_uncertainty_nai_2tac2[index], color=ccc, capthick=1, marker=mrksym, fmt='', mec=ccc, ms=3)
		index+=1


	# Ca II (0.866 um)
	ax[0,0].errorbar(mapped_val,caii,yerr=uncertainty_caii,fmt='.',color='black',capthick=1, mec='black', ms=8)
	ax[0,0].set_xlim([0,58.5])
	ax[0,0].set_xticks([0,10,20,30,40,50])
	ax[0,0].set_xticklabels(([]))
	ax[0,0].set_ylabel('EW ($\AA$)')
	ax[0,0].set_ylim([-3.1,7.9]) # limits to exclude outliers

	# Na I (1.14 um)
	ax[0,1].errorbar(mapped_val,nai,yerr=uncertainty_nai,fmt='.',color='black',capthick=1, mec='black', ms=8)#yngms)
	ax[0,1].set_xlim([-1,59])
	ax[0,1].set_xticks([0,10,20,30,40,50])
	ax[0,1].set_xticklabels(([]))
	ax[0,1].set_ylim([-3.4,15.9]) # limits to exclude outliers

	# Al I (1.31 um)
	ax[1,0].errorbar(mapped_val,ali,yerr=uncertainty_ali,fmt='.',color='black',capthick=1, mec='black', ms=8)
	ax[1,0].set_xlim([-1,59])
	ax[1,0].set_xticks([0,10,20,30,40,50])
	ax[1,0].set_xticklabels(([]))
	ax[1,0].set_ylabel('EW ($\AA$)')
	ax[1,0].set_ylim([-1.2,3.6]) # limits to exclude outliers

	# Mg I (1.49 um)
	ax[1,1].errorbar(mapped_val,mgi_1tac5,yerr=uncertainty_mgi_1tac5,fmt='.',color='black',capthick=1, mec='black', ms=8)
	ax[1,1].set_xlim([-1,59])
	ax[1,1].set_xticks([0,10,20,30,40,50])
	ax[1,1].set_xticklabels(([]))
	ax[1,1].set_ylim([-3.9,3.3]) # limits to exclude outliers

	# Mg I (1.71 um)
	ax[2,0].errorbar(mapped_val,mgi_1tac7,yerr=uncertainty_mgi_1tac7,fmt='.',color='black',capthick=1, mec='black', ms=8)
	ax[2,0].set_xlim([-1,59])
	ax[2,0].set_xticks([0,10,20,30,40,50])
	ax[2,0].set_xticklabels((x_spec_list))
	#ax[2,0].set_ylabel(r"EW ($\AA$)")
	#ax[2,0].set_ylabel('EW '+r"($\AA$)")
	ax[2,0].set_ylabel('EW ($\AA$)')
	ax[2,0].set_ylim([-1.4,4.2]) # limits to exclude outliers
	ax[2,0].set_xlabel('Spectral Type')

	# Na I (2.21 um)
	ax[2,1].errorbar(mapped_val,nai_2tac2,yerr=uncertainty_nai_2tac2,fmt='.',color='black',capthick=1, mec='black', ms=8)
	ax[2,1].set_xlim([-1,59])
	ax[2,1].set_xticks([0,10,20,30,40,50])
	ax[2,1].set_xticklabels((x_spec_list))
	ax[2,1].set_ylim([-2.5,8]) # limits to exclude outliers
	ax[2,1].set_xlabel('Spectral Type')
	

	norm_text = (15.9-13.75)/(15.9+3.4)
	# label features
	ax[0,0].annotate( 'Ca II (0.866 $\mu$m)', xy=(2, (7.9 - (7.9+3.1)*norm_text)), weight=500 )
	ax[0,1].annotate( 'Na I (1.14 $\mu$m)', xy=(2, 13.75), weight=500 ) # normalize to this subplot
	ax[1,0].annotate( 'Al I (1.31 $\mu$m)', xy=(2, (3.6 - (3.6+1.2)*norm_text)), weight=500 )
	ax[1,1].annotate( 'Mg I (1.49 $\mu$m)', xy=(2, (3.3 - (3.3+3.9)*norm_text)), weight=500 )
	ax[2,0].annotate( 'Mg I (1.71 $\mu$m)', xy=(2, (4.2 - (4.2+1.4)*norm_text)), weight=500 )
	ax[2,1].annotate( 'Na I (2.21 $\mu$m)', xy=(2, (8.0 - (8.0+2.5)*norm_text)), weight=500 )

	# label by lum class
	ax[0,1].annotate( 'Young Dwarfs', xy=(2, 12), color='black', size=13, weight=1000 )
	ax[0,1].annotate( 'Old Dwarfs', xy=(2, 10.5), color='red', size=13, weight=1000 )
	ax[0,1].annotate( 'Old Giants', xy=(2, 9), color='orange', size=13, weight=1000 )
	ax[0,1].annotate( 'Old Supergiants', xy=(2, 7.5), color='purple', size=13, weight=1000 )
	
	# Create fake data points to go next to labels
	#ax[0,1].scatter(mapped_val,nai, color='black')	

	# set major ytic to show up at integer values
	ax[0,0].yaxis.set_major_locator(ticker.MultipleLocator(2))
	ax[0,1].yaxis.set_major_locator(ticker.MultipleLocator(5))
	ax[1,0].yaxis.set_major_locator(ticker.MultipleLocator(1))
	ax[1,1].yaxis.set_major_locator(ticker.MultipleLocator(2))
	ax[2,0].yaxis.set_major_locator(ticker.MultipleLocator(1))
	ax[2,1].yaxis.set_major_locator(ticker.MultipleLocator(2))

	# set minor ytic to show up every 0.2
	ax[0,0].yaxis.set_minor_locator(ticker.MultipleLocator(0.5))
	ax[0,1].yaxis.set_minor_locator(ticker.MultipleLocator(1))
	ax[1,0].yaxis.set_minor_locator(ticker.MultipleLocator(0.2))
	ax[1,1].yaxis.set_minor_locator(ticker.MultipleLocator(0.5))
	ax[2,0].yaxis.set_minor_locator(ticker.MultipleLocator(0.2))
	ax[2,1].yaxis.set_minor_locator(ticker.MultipleLocator(0.5))

	# set minor xtic to show up every 2
	ax[0,0].xaxis.set_minor_locator(ticker.MultipleLocator(2))
	ax[0,1].xaxis.set_minor_locator(ticker.MultipleLocator(2))
	ax[1,0].xaxis.set_minor_locator(ticker.MultipleLocator(2))
	ax[1,1].xaxis.set_minor_locator(ticker.MultipleLocator(2))
	ax[2,0].xaxis.set_minor_locator(ticker.MultipleLocator(2))
	ax[2,1].xaxis.set_minor_locator(ticker.MultipleLocator(2))

	#plt.tight_layout()
	fig.tight_layout()
	fig.subplots_adjust(hspace=.05, bottom=0.075)#, wspace=0.05)

	plt.savefig('EW_obs_calcDwarfs_R09_err_minscript_160720.png', bbox_inches='tight')


obs_calcedR09_6subplots_overlay()
