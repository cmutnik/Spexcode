#!~/bin/python
# reproduce figure 35 subplots
# EW as function of spectral type
# Corey Mutnik 7/7/16
# Modified:
#   7/13/16 - to only include Yng dwarfs
#   7/20/16 - formatting
#   7/21/16 - changed MgI ylim and added symbols to legend
#   7/25/16 - $\mu m$ --> $\mu$m

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


# only use observed main sequence stars (Dwarfs)


'''
caii2, newnamelist = [], []
for i in range(len(yngnames)):
	if yngnames[i][2] != 'V':
		print yngnames[i]
	elif yngnames[i][2] == 'V': 
		caii2.append(EW_spt_table['EW_caii'])
		newnamelist.append(yngnames[i])
#>>
	B6/B7Vn_HD 147196
	K0IV(e)_GSC 06801-00186 (oldSpx)
	K0IV(e)_GSC 06801-00186
	K0 / K2IV(e)_ScoPMS 214
	K0 / K1III+_HD 141813
	K0III_HD 14311
	K2 / K2IV(e)_ScoPMS 44
	M2.5V_ScoPMS 008b
	SC5.5-C71e_HIP 78721
'''
#--------------------------------------------------------------
###
#EW_spt_type = list(EW_spt_table['spt type_standard_file'])
# need modification for only dwarf stars
EW_spt_type = list(yngmainseq)
###
#--------------------------------------------------------------
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

def determine_maxmin_of_feat_for_plots():
	featname = ['caii (0.866)', 'nai (1.14)' , 'nai (2.2)', 'ali', 'mgi (1.5)', 'mgi (1.7)']
	obsspecfeat = [caii, nai , nai_2tac2, ali, mgi_1tac5, mgi_1tac7]
	unobsspecfeat = [uncertainty_caii, uncertainty_nai , uncertainty_nai_2tac2, uncertainty_ali, uncertainty_mgi_1tac5, uncertainty_mgi_1tac7]
	R09specfeat = [R09_caii, R09_nai , R09_nai_2tac2, R09_ali, R09_mgi_1tac5, R09_mgi_1tac7]
	unR09specfeat = [R09_uncertainty_caii, R09_uncertainty_nai , R09_uncertainty_nai_2tac2, R09_uncertainty_ali, R09_uncertainty_mgi_1tac5, R09_uncertainty_mgi_1tac7]
	for k in range(len(obsspecfeat)):
		# where max values occur
		obsmaxloc = np.where(obsspecfeat[k] == max(obsspecfeat[k]))[0][0]
		R09maxloc = np.where(R09specfeat[k] == max(R09specfeat[k]))[0][0]

		# determine max value of obs and R09
		if max(obsspecfeat[k]) > max(R09specfeat[k]):
			fullmax = max(obsspecfeat[k]) + abs(unobsspecfeat[k][obsmaxloc])
		else:
			fullmax = max(R09specfeat[k]) + abs(unR09specfeat[k][R09maxloc])

		print '#>>\tmax obs', featname[k], ': ', max(obsspecfeat[k]), '+/-', unobsspecfeat[k][obsmaxloc] 
		print '#>>\tmax R09 ', featname[k], ': ', max(R09specfeat[k]), '+/-', unR09specfeat[k][R09maxloc]
		print '#>>\tmax obs/R09', featname[k], '+ abs(err): ', fullmax,'\n'
	#>>	max obs/R09 caii (0.866) + abs(err):  6.18662591 
	#>>	max obs/R09 nai (1.14) + abs(err):  15.1546614 
	#>>	max obs/R09 nai (2.2) + abs(err):  7.79198858 
	#>>	max obs/R09 ali + abs(err):  10.8101025747 
	#>>	max obs/R09 mgi (1.5) + abs(err):  3.27391617 
	#>>	max obs/R09 mgi (1.7) + abs(err):  4.0867987


	for k in range(len(obsspecfeat)):
		# where min values occur
		obsminloc = np.where(obsspecfeat[k] == min(obsspecfeat[k]))[0][0]
		R09minloc = np.where(R09specfeat[k] == min(R09specfeat[k]))[0][0]
		# determine min value of obs and R09
		if min(obsspecfeat[k]) < min(R09specfeat[k]):
			fullmin = min(obsspecfeat[k]) - abs(unobsspecfeat[k][obsminloc])
		else:
			fullmin = min(R09specfeat[k]) - abs(unR09specfeat[k][R09minloc])
		print '#>>\tmin obs', featname[k], ': ', min(obsspecfeat[k]), '+/-', unobsspecfeat[k][obsminloc] 
		print '#>>\tmin R09 ', featname[k], ': ', min(R09specfeat[k]), '+/-', unR09specfeat[k][R09minloc]
		print '#>>\tmin obs/R09', featname[k], '+ abs(err): ', fullmin,'\n'
	#>>	min obs/R09 caii (0.866) + abs(err):  -11.2875918347
	#>>	min obs/R09 nai (1.14) + abs(err):  -4.25659769306
	#>>	min obs/R09 nai (2.2) + abs(err):  -2.42791078
	#>>	min obs/R09 ali + abs(err):  -6.13226769689
	#>>	min obs/R09 mgi (1.5) + abs(err):  -5.6629104
	#>>	min obs/R09 mgi (1.7) + abs(err):  -2.4242548
#determine_maxmin_of_feat_for_plots()


def sep_plots_old():
	#plt.figure(1)
	plt.clf()
	fig1, ax1 = plt.subplots()
	plt.xlim(-2,42)
	plt.ylim(-5,10)
	plt.scatter(mapped_val,caii, color='black')
	plt.title('Ca II (0.866$\mu$m)')
	##plt.xlabel('Teff')
	#plt.xlabel('F0:0, F9:9, G:10, K:20, M:30, L:40, T-S:100')
	plt.ylabel('EW ($\AA$)')
	#plt.gca().invert_xaxis()
	fig1.subplots_adjust(left=0.125)
	###------------------------------------------------------------
	# Fix x axis labels
	###
	# set limits
	#ax.set_ylim(-2,2)
	#ax.set_xlim(-0.5,45)
	# add some text for labels, title and axes ticks
	ax1.set_xlabel('Spectral Type')
	ax1.set_ylabel('EW ($\AA$)')
	### POSSIBLY: put titles inside plots, like rayner did
	#ax.set_title('Ca II (0.866 $\mu$m)')
	##plt.xlabel('F0:0, F9:9, G:10, K:20, M:30, L:40, T-S:100')
	ax1.set_xticks([0,10,20,30,40,50])
	ax1.set_xticklabels((x_spec_list))
	# X-TICS
	#ax = plt.axes()
	#ax.xaxis.set_major_locator(ticker.MultipleLocator(5))
	ax1.xaxis.set_minor_locator(ticker.MultipleLocator(2))
	ax1.yaxis.set_minor_locator(ticker.MultipleLocator(.5))
	###------------------------------------------------------------
	plt.savefig('_CaII_EWall.png')


	#plt.figure(2)
	plt.clf()
	fig2, ax2 = plt.subplots()
	plt.xlim(-2,42)
	plt.ylim(-2,10)
	plt.scatter(mapped_val,nai, color='black')
	plt.title('Na I (1.14$\mu$m)')
	#plt.xlabel('F0:0, F9:9, G:10, K:20, M:30, L:40, T-S:100')
	plt.ylabel('EW ($\AA$)')
	fig2.subplots_adjust(left=0.125)
	###------------------------------------------------------------
	# Fix x axis labels
	###
	# set limits
	#ax.set_ylim(-2,2)
	#ax.set_xlim(-0.5,45)
	# add some text for labels, title and axes ticks
	ax2.set_xlabel('Spectral Type')
	ax2.set_ylabel('EW ($\AA$)')
	### POSSIBLY: put titles inside plots, like rayner did
	#ax.set_title('Ca II (0.866 $\mu$m)')
	ax2.set_xticks([0,10,20,30,40])# + 1.5*width)
	ax2.set_xticklabels((x_spec_list))
	# X-TICS
	#ax = plt.axes()
	#ax.xaxis.set_major_locator(ticker.MultipleLocator(5))
	ax2.xaxis.set_minor_locator(ticker.MultipleLocator(2))
	ax2.yaxis.set_minor_locator(ticker.MultipleLocator(.5))
	###------------------------------------------------------------
	plt.savefig('_NaI_1.14_EWall.png')


	#plt.figure(3)
	plt.clf()
	fig3, ax3 = plt.subplots()
	plt.xlim(-2,42)
	plt.ylim(-4,10)
	plt.scatter(mapped_val,nai_2tac2,color='black')
	plt.title('Na I (2.21$\mu$m)')
	plt.ylabel('EW ($\AA$)')
	fig3.subplots_adjust(left=0.125)
	###------------------------------------------------------------
	# Fix x axis labels
	###
	# set limits
	#ax.set_ylim(-2,2)
	#ax.set_xlim(-0.5,45)
	# add some text for labels, title and axes ticks
	ax3.set_xlabel('Spectral Type')
	ax3.set_ylabel('EW ($\AA$)')
	### POSSIBLY: put titles inside plots, like rayner did
	#ax.set_title('Ca II (0.866 $\mu$m)')
	ax3.set_xticks([0,10,20,30,40])# + 1.5*width)
	ax3.set_xticklabels((x_spec_list))
	# X-TICS
	#ax = plt.axes()
	#ax.xaxis.set_major_locator(ticker.MultipleLocator(5))
	ax3.xaxis.set_minor_locator(ticker.MultipleLocator(2))
	ax3.yaxis.set_minor_locator(ticker.MultipleLocator(.5))
	###------------------------------------------------------------
	plt.savefig('_NaI_2.2_EWall.png')

	#plt.figure(4)
	plt.clf()
	fig4, ax4 = plt.subplots()
	plt.scatter(mapped_val,ali,color='black')
	plt.title('Al I (1.31$\mu$m)')
	#plt.xlabel('F0:0, F9:9, G:10, K:20, M:30, L:40, T-S:100')
	plt.ylabel('EW ($\AA$)')
	#plt.xlim(18,62)
	plt.xlim(-2,42)
	plt.ylim(-2,8)
	fig4.subplots_adjust(left=0.125)
	###------------------------------------------------------------
	# Fix x axis labels
	###
	ax4.set_xlabel('Spectral Type')
	ax4.set_ylabel('EW ($\AA$)')
	ax4.set_xticks([0,10,20,30,40])
	ax4.set_xticklabels((x_spec_list))
	# X-TICS
	ax4.xaxis.set_minor_locator(ticker.MultipleLocator(2))
	ax4.yaxis.set_minor_locator(ticker.MultipleLocator(.5))
	###------------------------------------------------------------
	plt.savefig('_AlI_EWall.png')


	#plt.figure(5)
	plt.clf()
	fig5, ax5 = plt.subplots()
	plt.scatter(mapped_val,mgi_1tac5,color='black')
	plt.title('Mg I (1.49$\mu$m)')
	#plt.xlabel('F0:0, F9:9, G:10, K:20, M:30, L:40, T-S:100')
	plt.ylabel('EW ($\AA$)')
	#plt.xlim(18,62)
	plt.xlim(-2,42)
	plt.ylim(-2,5)
	fig5.subplots_adjust(left=0.125)
	###------------------------------------------------------------
	# Fix x axis labels
	###
	ax5.set_xlabel('Spectral Type')
	ax5.set_ylabel('EW ($\AA$)')
	ax5.set_xticks([0,10,20,30,40])
	ax5.set_xticklabels((x_spec_list))
	# X-TICS
	ax5.xaxis.set_minor_locator(ticker.MultipleLocator(2))
	ax5.yaxis.set_minor_locator(ticker.MultipleLocator(.5))
	###------------------------------------------------------------
	plt.savefig('_MgI_1tac49_EWall.png')


	#plt.figure(6)
	plt.clf()
	fig6, ax6 = plt.subplots()
	plt.scatter(mapped_val,mgi_1tac7,color='black')
	plt.title('Mg I (1.71$\mu$m)')
	#plt.xlabel('F0:0, F9:9, G:10, K:20, M:30, L:40, T-S:100')
	plt.ylabel('EW ($\AA$)')
	#plt.xlim(18,62)
	plt.xlim(-2,42)
	#plt.ylim(-5,10)
	plt.ylim(-2,5)
	fig6.subplots_adjust(left=0.125)
	###------------------------------------------------------------
	# Fix x axis labels
	###
	ax6.set_xlabel('Spectral Type')
	ax6.set_ylabel('EW ($\AA$)')
	ax6.set_xticks([0,10,20,30,40])
	ax6.set_xticklabels((x_spec_list))
	# X-TICS
	ax6.xaxis.set_minor_locator(ticker.MultipleLocator(2))
	ax6.yaxis.set_minor_locator(ticker.MultipleLocator(.5))
	###------------------------------------------------------------
	plt.savefig('_MgI_1tac7_EWall.png')


	#plt.figure(8)
	plt.clf()
	fig8, ax8 = plt.subplots()
	plt.errorbar(mapped_val,mgi_1tac7,yerr=uncertainty_mgi_1tac7,fmt='.',color='black')
	plt.title('Mg I (1.71$\mu$m)')
	#plt.xlabel('F0:0, F9:9, G:10, K:20, M:30, L:40, T-S:100')
	plt.ylabel('EW ($\AA$)')
	#plt.xlim(18,62)
	plt.xlim(-2,42)
	#plt.ylim(-5,10)
	plt.ylim(-2,5)
	fig8.subplots_adjust(left=0.125)
	###------------------------------------------------------------
	# Fix x axis labels
	###
	ax8.set_xlabel('Spectral Type')
	ax8.set_ylabel('EW ($\AA$)')
	ax8.set_xticks([0,10,20,30,40])
	ax8.set_xticklabels((x_spec_list))
	# X-TICS
	ax8.xaxis.set_minor_locator(ticker.MultipleLocator(2))
	ax8.yaxis.set_minor_locator(ticker.MultipleLocator(.5))
	###------------------------------------------------------------
	plt.savefig('_MgI_1tac7_EWall_err.png')


	#plt.figure(9)
	plt.clf()
	fig9, ax9 = plt.subplots()
	plt.errorbar(mapped_val,caii,yerr=uncertainty_caii,fmt='.',color='black')
	plt.title('Ca II (0.866$\mu$m)')
	#plt.xlabel('F0:0, F9:9, G:10, K:20, M:30, L:40, T-S:100')
	plt.ylabel('EW ($\AA$)')
	plt.xlim(-2,42)
	plt.ylim(-5,10)
	fig9.subplots_adjust(left=0.125)
	###------------------------------------------------------------
	# Fix x axis labels
	###
	ax9.set_xlabel('Spectral Type')
	ax9.set_ylabel('EW ($\AA$)')
	ax9.set_xticks([0,10,20,30,40])
	ax9.set_xticklabels((x_spec_list))
	# X-TICS
	ax9.xaxis.set_minor_locator(ticker.MultipleLocator(2))
	ax9.yaxis.set_minor_locator(ticker.MultipleLocator(.5))
	###------------------------------------------------------------
	plt.savefig('_CaII_EWall_err.png')


	#plt.figure(10)
	plt.clf()
	fig10, ax10 = plt.subplots()
	plt.errorbar(mapped_val,nai_2tac2,yerr=uncertainty_nai_2tac2,fmt='.',color='black')
	plt.title('Na I (2.21$\mu$m)')
	#plt.xlabel('F0:0, F9:9, G:10, K:20, M:30, L:40, T-S:100')
	plt.ylabel('EW ($\AA$)')
	#plt.xlim(18,62)
	plt.xlim(-2,42)
	plt.ylim(-4,10)
	fig10.subplots_adjust(left=0.125)
	###------------------------------------------------------------
	# Fix x axis labels
	###
	ax10.set_xlabel('Spectral Type')
	ax10.set_ylabel('EW ($\AA$)')
	ax10.set_xticks([0,10,20,30,40])
	ax10.set_xticklabels((x_spec_list))
	# X-TICS
	ax10.xaxis.set_minor_locator(ticker.MultipleLocator(2))
	ax10.yaxis.set_minor_locator(ticker.MultipleLocator(.5))
	###------------------------------------------------------------
	plt.savefig('_NaI_2.2_EWall_err.png')


	#plt.figure(11)
	plt.clf()
	fig11, ax11 = plt.subplots()
	plt.errorbar(mapped_val,nai,yerr=uncertainty_nai,fmt='.',color='black')
	plt.title('Na I (1.14$\mu$m)')
	#plt.xlabel('F0:0, F9:9, G:10, K:20, M:30, L:40, T-S:100')
	plt.ylabel('EW ($\AA$)')
	plt.xlim(-2,42)
	plt.ylim(-2,10)
	fig11.subplots_adjust(left=0.125)
	###------------------------------------------------------------
	# Fix x axis labels
	###
	ax11.set_xlabel('Spectral Type')
	ax11.set_ylabel('EW ($\AA$)')
	ax11.set_xticks([0,10,20,30,40])
	ax11.set_xticklabels((x_spec_list))
	# X-TICS
	ax11.xaxis.set_minor_locator(ticker.MultipleLocator(2))
	ax11.yaxis.set_minor_locator(ticker.MultipleLocator(.5))
	###------------------------------------------------------------
	plt.savefig('_NaI_1.14_EWall_err.png')


	#plt.figure(12)
	plt.clf()
	fig12, ax12 = plt.subplots()
	plt.errorbar(mapped_val,ali,yerr=uncertainty_ali,fmt='.',color='black')
	plt.title('Al I (1.31$\mu$m)')
	#plt.xlabel('F0:0, F9:9, G:10, K:20, M:30, L:40, T-S:100')
	plt.ylabel('EW ($\AA$)')
	plt.xlim(-2,42)
	plt.ylim(-2,4)
	fig12.subplots_adjust(left=0.125)
	###------------------------------------------------------------
	# Fix x axis labels
	###
	ax12.set_xlabel('Spectral Type')
	ax12.set_ylabel('EW ($\AA$)')
	ax12.set_xticks([0,10,20,30,40])
	ax12.set_xticklabels((x_spec_list))
	# X-TICS
	ax12.xaxis.set_minor_locator(ticker.MultipleLocator(2))
	ax12.yaxis.set_minor_locator(ticker.MultipleLocator(.5))
	###------------------------------------------------------------
	plt.savefig('_AlI_EWall_err.png')


	#plt.figure(13)
	plt.clf()
	fig13, ax13 = plt.subplots()
	plt.errorbar(mapped_val,mgi_1tac7,yerr=uncertainty_mgi_1tac5,fmt='.',color='black')
	plt.title('Mg I (1.49$\mu$m)')
	#plt.xlabel('F0:0, F9:9, G:10, K:20, M:30, L:40, T-S:100')
	plt.ylabel('EW ($\AA$)')
	plt.xlim(-2,42)
	plt.ylim(-2,5)
	fig13.subplots_adjust(left=0.125)
	###------------------------------------------------------------
	# Fix x axis labels
	###
	ax13.set_xlabel('Spectral Type')
	ax13.set_ylabel('EW ($\AA$)')
	ax13.set_xticks([0,10,20,30,40])
	ax13.set_xticklabels((x_spec_list))
	# X-TICS
	ax13.xaxis.set_minor_locator(ticker.MultipleLocator(2))
	ax13.yaxis.set_minor_locator(ticker.MultipleLocator(.5))
	###------------------------------------------------------------
	plt.savefig('_MgI_1tac49_EWall_err.png')
#sep_plots_old()


def published_EW_values():
	''' Data published by Rayner'''
	# open published data
	pub_vals = ascii.read('published_table9_no_err_mod2fit_rm_pts.csv')
	# published values
	pub_obj = pub_vals['Object']
	pub_spt_typ = pub_vals['Spectral Type']
	pub_caii = pub_vals['Ca II (0.866 mum)']
	pub_nai = pub_vals['Na I (1.14 mum)']
	pub_ali = pub_vals['Al I (1.313 mum)']
	pub_mgi_1tac5 = pub_vals['Mg I (1.485 mum)']
	pub_mgi_1tac7 = pub_vals['Mg I (1.711 mum)']
	pub_nai_2tac2 = pub_vals['Na I (2.206 mum)']	

	# Open Rayner Data
	def published_data():
		global publ_map_vals, R09_colors

		publ_spt_type = list(pub_spt_typ)
		breakup_spt_type = list(map(list, publ_spt_type))	

		publ_map_vals = []
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

			publ_map_vals.append(val)	

		##
		# UNFINISHED...THIS METHOD MISSES SOME AND JUST DEEMS THEM PURPLE
		##
		# separate by luminosity class...dwarfs, giants, supergiants
		R09_colors = []
		failedlist,failedindex = [],[]
		for xx in breakup_spt_type:
			#if xx[-1] == 'V' and xx[-2] != 'I':
			if xx[-1]=='V':
				R09_colors.append('red')
			elif (xx[-1] == xx[-2] == xx[-3]) or ():
				R09_colors.append('orange')
			else:
				failedindex.append(len(R09_colors))
				failedlist.append(publ_spt_type[len(R09_colors)])
				R09_colors.append('purple')
		
		##
		# USE THIS
		##
		unfinished_colors = []
		for jj in publ_spt_type:
			#print jj
			if "III" in jj:
				unfinished_colors.append('black')

	def subplots():	
		published_data()

		plt.clf()

		fig, ax = plt.subplots(3,2)

		# title
		#ax[0,0].set_title('Published: Red')
		#ax[0,1].set_title('Calculated: Black')
		
		# Ca II (0.866 um)
		ax[0,0].scatter(publ_map_vals,pub_caii, color=R09_colors, alpha=0.8)
		ax[0,0].scatter(mapped_val,caii, color='black')
		ax[0,0].set_xlim([-2,55])
		ax[0,0].set_xticks([0,10,20,30,40,50])
		ax[0,0].set_xticklabels(([]))
		ax[0,0].set_ylabel('EW ($\AA$)')
		
		# Na I (1.14 um)
		ax[0,1].scatter(publ_map_vals,pub_nai, color=R09_colors, alpha=0.8)
		ax[0,1].scatter(mapped_val,nai, color='black')
		ax[0,1].set_xlim([-2,55])
		ax[0,1].set_xticks([0,10,20,30,40,50])
		ax[0,1].set_xticklabels(([]))

		# Al I (1.31 um)
		ax[1,0].scatter(publ_map_vals,pub_ali, color=R09_colors, alpha=0.8)
		ax[1,0].scatter(mapped_val,ali, color='black')
		ax[1,0].set_xlim([-2,55])
		ax[1,0].set_xticks([0,10,20,30,40,50])
		ax[1,0].set_xticklabels(([]))
		ax[1,0].set_ylabel('EW ($\AA$)')

		# Mg I (1.49 um)
		ax[1,1].scatter(publ_map_vals,pub_mgi_1tac5, color=R09_colors, alpha=0.8)
		ax[1,1].scatter(mapped_val,mgi_1tac5, color='black')
		ax[1,1].set_xlim([-2,55])
		ax[1,1].set_xticks([0,10,20,30,40,50])
		ax[1,1].set_xticklabels(([]))

		# Mg I (1.71 um)
		ax[2,0].scatter(publ_map_vals,pub_mgi_1tac7, color=R09_colors, alpha=0.8)
		ax[2,0].scatter(mapped_val,mgi_1tac7, color='black')
		ax[2,0].set_xlim([-2,55])
		ax[2,0].set_xticks([0,10,20,30,40,50])
		ax[2,0].set_xticklabels((x_spec_list))
		ax[2,0].set_ylabel('EW ($\AA$)')

		# Na I (2.21 um)
		ax[2,1].scatter(publ_map_vals,pub_nai_2tac2, color=R09_colors, alpha=0.8)
		ax[2,1].scatter(mapped_val,nai_2tac2, color='black')
		ax[2,1].set_xlim([-2,55])
		ax[2,1].set_xticks([0,10,20,30,40,50])
		ax[2,1].set_xticklabels((x_spec_list))

		# set ylims
		#ax[0,0].set_ylim([-5,10])
		ax[0,0].set_ylim([0,7])
		ax[0,1].set_ylim([-3,12])
		ax[1,0].set_ylim([-2,4])
		ax[1,1].set_ylim([-2,4])
		ax[2,0].set_ylim([-2,5])
		ax[2,1].set_ylim([-2,8])

		# label features
		#ax[0,0].annotate('Test', xy=(1, 0), xycoords='axes fraction', fontsize=16,xytext=(-5, 5), textcoords='offset points',ha='right', va='bottom')
		ax[0,0].annotate('Ca II (0.866 $\mu$m)', xy=(2, 6))
		ax[0,1].annotate('Na I (1.14 $\mu$m)', xy=(2, 10))
		ax[1,0].annotate('Al I (1.31 $\mu$m)', xy=(2, 3))
		ax[1,1].annotate('Mg I (1.49 $\mu$m)', xy=(2, 3))
		ax[2,0].annotate('Mg I (1.71 $\mu$m)', xy=(2, 4))
		ax[2,1].annotate('Na I (2.21 $\mu$m)', xy=(2, 6.5))

		# turn off x-axis labels
		#ax[0,0].axes.get_xaxis().set_visible(False)

		plt.tight_layout()
		#plt.show()
		plt.savefig('unfinised_coloring_pub_luminosity_classes.png')

	def subplots_err():
		published_data()
		plt.clf()
		fig, ax = plt.subplots(3,2)
		# Ca II (0.866 um)
		ax[0,0].scatter(publ_map_vals,pub_caii, color=R09_colors, alpha=0.8)
		ax[0,0].errorbar(mapped_val,caii,yerr=uncertainty_caii,fmt='.',color='black')
		ax[0,0].scatter(mapped_val,caii, color='black')
		ax[0,0].set_xlim([-2,55])
		ax[0,0].set_xticks([0,10,20,30,40,50])
		ax[0,0].set_xticklabels(([]))
		ax[0,0].set_ylabel('EW ($\AA$)')

		# Na I (1.14 um)
		ax[0,1].scatter(publ_map_vals,pub_nai, color=R09_colors, alpha=0.8)
		ax[0,1].errorbar(mapped_val,nai,yerr=uncertainty_nai,fmt='.',color='black')
		ax[0,1].scatter(mapped_val,nai, color='black')
		ax[0,1].set_xlim([-2,55])
		ax[0,1].set_xticks([0,10,20,30,40,50])
		ax[0,1].set_xticklabels(([]))

		# Al I (1.31 um)
		ax[1,0].scatter(publ_map_vals,pub_ali, color=R09_colors, alpha=0.8)
		ax[1,0].errorbar(mapped_val,ali,yerr=uncertainty_ali,fmt='.',color='black')
		ax[1,0].set_xlim([-2,55])
		ax[1,0].set_xticks([0,10,20,30,40,50])
		ax[1,0].set_xticklabels(([]))
		ax[1,0].set_ylabel('EW ($\AA$)')

		# Mg I (1.49 um)
		ax[1,1].scatter(publ_map_vals,pub_mgi_1tac5, color=R09_colors, alpha=0.8)
		ax[1,1].errorbar(mapped_val,mgi_1tac5,yerr=uncertainty_mgi_1tac5,fmt='.',color='black')
		ax[1,1].set_xlim([-2,55])
		ax[1,1].set_xticks([0,10,20,30,40,50])
		ax[1,1].set_xticklabels(([]))

		# Mg I (1.71 um)
		ax[2,0].scatter(publ_map_vals,pub_mgi_1tac7, color=R09_colors, alpha=0.8)
		ax[2,0].errorbar(mapped_val,mgi_1tac7,yerr=uncertainty_mgi_1tac7,fmt='.',color='black')
		ax[2,0].set_xlim([-2,55])
		ax[2,0].set_xticks([0,10,20,30,40,50])
		ax[2,0].set_xticklabels((x_spec_list))
		ax[2,0].set_ylabel('EW ($\AA$)')

		# Na I (2.21 um)
		ax[2,1].scatter(publ_map_vals,pub_nai_2tac2, color=R09_colors, alpha=0.8)
		ax[2,1].errorbar(mapped_val,nai_2tac2,yerr=uncertainty_nai_2tac2,fmt='.',color='black')
		ax[2,1].set_xlim([-2,55])
		ax[2,1].set_xticks([0,10,20,30,40,50])
		ax[2,1].set_xticklabels((x_spec_list))

		# set ylims
		ax[0,0].set_ylim([-1.5,5.4])
		ax[0,1].set_ylim([-3,6.6])
		ax[1,0].set_ylim([-5,2.5])
		ax[1,1].set_ylim([-.6,2.2])
		ax[2,0].set_ylim([-.6,2.9])
		ax[2,1].set_ylim([-2.2,4.9])

		# label features
		ax[0,0].annotate('Ca II (0.866 $\mu$m)', xy=(2, (5.*4.4/5.9)))
		ax[0,1].annotate('Na I (1.14 $\mu$m)', xy=(2, 5)) # normalize to this subplot...xy=(2, (5*ymax/5.9))
		ax[1,0].annotate('Al I (1.31 $\mu$m)', xy=(2, (5.*2.5/5.9)))
		ax[1,1].annotate('Mg I (1.49 $\mu$m)', xy=(2, (5.*2.2/5.9)))
		ax[2,0].annotate('Mg I (1.71 $\mu$m)', xy=(2, (5.*2.9/5.9)))
		ax[2,1].annotate('Na I (2.21 $\mu$m)', xy=(2, (5.*4.9/5.9)))

		# turn off x-axis labels
		#ax[0,0].axes.get_xaxis().set_visible(False)

		# set major ytic to show up at integer values
		ax[0,0].yaxis.set_major_locator(ticker.MultipleLocator(1))
		ax[0,1].yaxis.set_major_locator(ticker.MultipleLocator(1))
		ax[1,0].yaxis.set_major_locator(ticker.MultipleLocator(1))
		ax[1,1].yaxis.set_major_locator(ticker.MultipleLocator(1))
		ax[2,0].yaxis.set_major_locator(ticker.MultipleLocator(1))
		ax[2,1].yaxis.set_major_locator(ticker.MultipleLocator(1))

		# set minor ytic to show up every 0.2
		ax[0,0].yaxis.set_minor_locator(ticker.MultipleLocator(0.2))
		ax[0,1].yaxis.set_minor_locator(ticker.MultipleLocator(0.2))
		ax[1,0].yaxis.set_minor_locator(ticker.MultipleLocator(0.2))
		ax[1,1].yaxis.set_minor_locator(ticker.MultipleLocator(0.2))
		ax[2,0].yaxis.set_minor_locator(ticker.MultipleLocator(0.2))
		ax[2,1].yaxis.set_minor_locator(ticker.MultipleLocator(0.2))

		# set minor xtic to show up every 2
		ax[0,0].xaxis.set_minor_locator(ticker.MultipleLocator(2))
		ax[0,1].xaxis.set_minor_locator(ticker.MultipleLocator(2))
		ax[1,0].xaxis.set_minor_locator(ticker.MultipleLocator(2))
		ax[1,1].xaxis.set_minor_locator(ticker.MultipleLocator(2))
		ax[2,0].xaxis.set_minor_locator(ticker.MultipleLocator(2))
		ax[2,1].xaxis.set_minor_locator(ticker.MultipleLocator(2))

		# set precision of axis tics
		#ax[0,0].yaxis.set_major_formatter(plt.FormatStrFormatter('%i'))  # integers

		plt.tight_layout()

		#plt.show()
		plt.savefig('suplots_err.png')


	subplots()	
	subplots_err()
#published_EW_values()


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


def obs_calcedR09_6subplots_overlay_outliers():
	# call functions for mapping SptTyp and luminosity class
	calculated_R09_EW_values()

	# clear and setup subplots
	plt.clf()

	#fig, ax = plt.subplots(3,2, sharex=True, sharey=True) #sharex=True removes need for "set_xticklabels(([]))" or...
	#fig, ax = plt.subplots(3,2, sharex='col', sharey='row')
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
			mrksym = "1"#'p'
		elif 'I' in jj:
			n_supergiants+=1
			ccc='purple'
			mrksym = "1"#'p'
		else:
			n_missed+=1
			ccc='green'
			mrksym = '$?$'
		
		#elinewidth=1, capsize=1
		#barsabove=True
		ax[0,0].errorbar(R09_mapped_val[index], R09_caii[index], 
			yerr=R09_uncertainty_caii[index], color=ccc, capthick=1, marker=mrksym, fmt='', ms=3)
		ax[0,1].errorbar(R09_mapped_val[index], R09_nai[index], 
			yerr=R09_uncertainty_nai[index], color=ccc, capthick=1, marker=mrksym, fmt='', ms=3)
		ax[1,0].errorbar(R09_mapped_val[index], R09_ali[index], 
			yerr=R09_uncertainty_ali[index], color=ccc, capthick=1, marker=mrksym, fmt='', ms=3)
		ax[1,1].errorbar(R09_mapped_val[index], R09_mgi_1tac5[index], 
			yerr=R09_uncertainty_mgi_1tac5[index], color=ccc, capthick=1, marker=mrksym, fmt='', ms=3)
		ax[2,0].errorbar(R09_mapped_val[index], R09_mgi_1tac7[index], 
			yerr=R09_uncertainty_mgi_1tac7[index], color=ccc, capthick=1, marker=mrksym, fmt='', ms=3)
		ax[2,1].errorbar(R09_mapped_val[index], R09_nai_2tac2[index], 
			yerr=R09_uncertainty_nai_2tac2[index], color=ccc, capthick=1, marker=mrksym, fmt='', ms=3)
		index+=1
		
		#print 'n_supergiants: ', n_supergiants #>>n_supergiants: 55
		#print 'n_giants: ', n_giants #>>n_giants: 80
		#print 'n_dwarfs: ', n_dwarfs #>>n_dwarfs: 59
		#print 'n_missed: ', n_missed #>>n_missed: 0



	# Ca II (0.866 um)
	ax[0,0].errorbar(mapped_val,caii,yerr=uncertainty_caii,fmt='.',color='black',capthick=1)
	ax[0,0].scatter(mapped_val,caii, color='black')
	ax[0,0].set_xlim([0,58.5])
	ax[0,0].set_xticks([0,10,20,30,40,50])
	ax[0,0].set_xticklabels(([]))
	ax[0,0].set_ylabel('EW ($\AA$)')
	ax[0,0].set_ylim([-11.4,6.2]) # limits to include outliers
	#ax[0,0].set_ylim([-11.3,6.2])#[-11.2875918347, 6.18662591])

	# Na I (1.14 um)
	ax[0,1].errorbar(mapped_val,nai,yerr=uncertainty_nai,fmt='.',color='black',capthick=1)
	ax[0,1].scatter(mapped_val,nai, color='black')
	ax[0,1].set_xlim([-1,59])
	ax[0,1].set_xticks([0,10,20,30,40,50])
	ax[0,1].set_xticklabels(([]))
	ax[0,1].set_ylim([-4.3,15.2]) # limits to include outliers
	#ax[0,1].set_ylim([-4.3,15.2])#[-4.25659769306, 15.1546614])

	# Al I (1.31 um)
	ax[1,0].errorbar(mapped_val,ali,yerr=uncertainty_ali,fmt='.',color='black',capthick=1)
	ax[1,0].set_xlim([-1,59])
	ax[1,0].set_xticks([0,10,20,30,40,50])
	ax[1,0].set_xticklabels(([]))
	ax[1,0].set_ylabel('EW ($\AA$)')
	#ax[1,0].set_ylim([-1.2,3.6]) # limits to exclude outliers
	ax[1,0].set_ylim([-6.2,11]) # limits to include outliers
	#[-6.13226769689, 10.8101025747])

	# Mg I (1.49 um)
	ax[1,1].errorbar(mapped_val,mgi_1tac5,yerr=uncertainty_mgi_1tac5,fmt='.',color='black',capthick=1)
	ax[1,1].set_xlim([-1,59])
	ax[1,1].set_xticks([0,10,20,30,40,50])
	ax[1,1].set_xticklabels(([]))
	#ax[1,1].set_ylim([])
	ax[1,1].set_ylim([-5.7,3.9]) # limits to include outliers
	#[-5.6629104, 3.27391617])

	# Mg I (1.71 um)
	ax[2,0].errorbar(mapped_val,mgi_1tac7,yerr=uncertainty_mgi_1tac7,fmt='.',color='black',capthick=1)
	ax[2,0].set_xlim([-1,59])
	ax[2,0].set_xticks([0,10,20,30,40,50])
	ax[2,0].set_xticklabels((x_spec_list))
	#ax[2,0].set_ylabel(r"EW ($\AA$)")
	#ax[2,0].set_ylabel('EW '+r"($\AA$)")
	ax[2,0].set_ylabel('EW ($\AA$)')
	ax[2,0].set_ylim([-2.5,4.2]) # limits to include outliers
	#[-2.4242548, 4.0867987])

	# Na I (2.21 um)
	ax[2,1].errorbar(mapped_val,nai_2tac2,yerr=uncertainty_nai_2tac2,fmt='.',color='black',capthick=1)
	ax[2,1].set_xlim([-1,59])
	ax[2,1].set_xticks([0,10,20,30,40,50])
	ax[2,1].set_xticklabels((x_spec_list))
	ax[2,1].set_ylim([-2.7,7.9]) # limits to include outliers
	#[-2.42791078, 7.79198858])


	'''
	# label features
	ax[0,0].annotate('Ca II (0.866 $\mu m$)', xy=(2, (5.*4.4/5.9)))
	ax[0,1].annotate('Na I (1.14 $\mu m$)', xy=(2, 5)) # normalize to this subplot...xy=(2, (5*ymax/5.9))
	ax[1,0].annotate('Al I (1.31 $\mu m$)', xy=(2, (5.*2.5/5.9)))
	ax[1,1].annotate('Mg I (1.49 $\mu m$)', xy=(2, (5.*2.2/5.9)))
	ax[2,0].annotate('Mg I (1.71 $\mu m$)', xy=(2, (5.*2.9/5.9)))
	ax[2,1].annotate('Na I (2.21 $\mu m$)', xy=(2, (5.*4.9/5.9)))
	'''

	# turn off x-axis tics & labels
	#ax[0,0].axes.get_xaxis().set_visible(False)

	# set major ytic to show up at integer values
	ax[0,0].yaxis.set_major_locator(ticker.MultipleLocator(1))
	ax[0,1].yaxis.set_major_locator(ticker.MultipleLocator(1))
	ax[1,0].yaxis.set_major_locator(ticker.MultipleLocator(1))
	ax[1,1].yaxis.set_major_locator(ticker.MultipleLocator(1))
	ax[2,0].yaxis.set_major_locator(ticker.MultipleLocator(1))
	ax[2,1].yaxis.set_major_locator(ticker.MultipleLocator(1))

	# set minor ytic to show up every 0.2
	ax[0,0].yaxis.set_minor_locator(ticker.MultipleLocator(0.2))
	ax[0,1].yaxis.set_minor_locator(ticker.MultipleLocator(0.2))
	ax[1,0].yaxis.set_minor_locator(ticker.MultipleLocator(0.2))
	ax[1,1].yaxis.set_minor_locator(ticker.MultipleLocator(0.2))
	ax[2,0].yaxis.set_minor_locator(ticker.MultipleLocator(0.2))
	ax[2,1].yaxis.set_minor_locator(ticker.MultipleLocator(0.2))

	# set minor xtic to show up every 2
	ax[0,0].xaxis.set_minor_locator(ticker.MultipleLocator(2))
	ax[0,1].xaxis.set_minor_locator(ticker.MultipleLocator(2))
	ax[1,0].xaxis.set_minor_locator(ticker.MultipleLocator(2))
	ax[1,1].xaxis.set_minor_locator(ticker.MultipleLocator(2))
	ax[2,0].xaxis.set_minor_locator(ticker.MultipleLocator(2))
	ax[2,1].xaxis.set_minor_locator(ticker.MultipleLocator(2))


	# set precision of axis tics
	#ax[0,0].yaxis.set_major_formatter(plt.FormatStrFormatter('%i'))  # integers

	#plt.tight_layout()
	fig.tight_layout()
	fig.subplots_adjust(hspace=.05)



	plt.savefig('EW_obs_calcR09_err_outliers.png')


def obs_calcedR09_6subplots_overlay_mediumPS_WORKS():
	# call functions for mapping SptTyp and luminosity class
	calculated_R09_EW_values()

	# clear and setup subplots
	plt.clf()

	#fig, ax = plt.subplots(3,2, sharex=True, sharey=True) #sharex=True removes need for "set_xticklabels(([]))" or...
	#fig, ax = plt.subplots(3,2, sharex='col', sharey='row')
	fig, ax = plt.subplots(3,2)
	
	# put y-axis on RHS
	#ax[0,1].yaxis.tick_right()
	#ax[1,1].yaxis.tick_right()
	#ax[2,1].yaxis.tick_right()

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
			mrksym = "1"#'p'
		elif 'I' in jj:
			n_supergiants+=1
			ccc='purple'
			mrksym = "1"#'p'
		else:
			n_missed+=1
			ccc='green'
			mrksym = '$?$'

		#elinewidth=1, capsize=1
		#barsabove=True

		#ax[0,0].errorbar(R09_mapped_val[index], R09_caii[index], yerr=R09_uncertainty_caii[index], color=ccc, fmt='.', capthick=1)
		#ax[0,0].errorbar(R09_mapped_val[index], R09_caii[index], yerr=R09_uncertainty_caii[index], color=ccc, fmt='', capthick=1, marker=mrksym)
		ax[0,0].errorbar(R09_mapped_val[index], R09_caii[index], 
			yerr=R09_uncertainty_caii[index], color=ccc, capthick=1, marker=mrksym, fmt='', ms=3)
		ax[0,1].errorbar(R09_mapped_val[index], R09_nai[index], 
			yerr=R09_uncertainty_nai[index], color=ccc, capthick=1, marker=mrksym, fmt='', ms=3)
		ax[1,0].errorbar(R09_mapped_val[index], R09_ali[index], 
			yerr=R09_uncertainty_ali[index], color=ccc, capthick=1, marker=mrksym, fmt='', ms=3)
		ax[1,1].errorbar(R09_mapped_val[index], R09_mgi_1tac5[index], 
			yerr=R09_uncertainty_mgi_1tac5[index], color=ccc, capthick=1, marker=mrksym, fmt='', ms=3)
		ax[2,0].errorbar(R09_mapped_val[index], R09_mgi_1tac7[index], 
			yerr=R09_uncertainty_mgi_1tac7[index], color=ccc, capthick=1, marker=mrksym, fmt='', ms=3)
		ax[2,1].errorbar(R09_mapped_val[index], R09_nai_2tac2[index], 
			yerr=R09_uncertainty_nai_2tac2[index], color=ccc, capthick=1, marker=mrksym, fmt='', ms=3)
		index+=1

	#print 'n_supergiants: ', n_supergiants #>>n_supergiants: 55
	#print 'n_giants: ', n_giants #>>n_giants: 80
	#print 'n_dwarfs: ', n_dwarfs #>>n_dwarfs: 59
	#print 'n_missed: ', n_missed #>>n_missed: 0


	# Ca II (0.866 um)
	ax[0,0].errorbar(mapped_val,caii,yerr=uncertainty_caii,fmt='.',color='black',capthick=1)
	ax[0,0].scatter(mapped_val,caii, color='black')
	ax[0,0].set_xlim([0,58.5])
	ax[0,0].set_xticks([0,10,20,30,40,50])
	ax[0,0].set_xticklabels(([]))
	ax[0,0].set_ylabel('EW ($\AA$)')
	ax[0,0].set_ylim([-3.1,7.9]) # limits to exclude outliers

	# Na I (1.14 um)
	ax[0,1].errorbar(mapped_val,nai,yerr=uncertainty_nai,fmt='.',color='black',capthick=1)
	ax[0,1].scatter(mapped_val,nai, color='black')
	ax[0,1].set_xlim([-1,59])
	ax[0,1].set_xticks([0,10,20,30,40,50])
	ax[0,1].set_xticklabels(([]))
	ax[0,1].set_ylim([-3.4,15.9]) # limits to exclude outliers

	# Al I (1.31 um)
	ax[1,0].errorbar(mapped_val,ali,yerr=uncertainty_ali,fmt='.',color='black',capthick=1)
	ax[1,0].set_xlim([-1,59])
	ax[1,0].set_xticks([0,10,20,30,40,50])
	ax[1,0].set_xticklabels(([]))
	ax[1,0].set_ylabel('EW ($\AA$)')
	ax[1,0].set_ylim([-1.2,3.6]) # limits to exclude outliers

	# Mg I (1.49 um)
	ax[1,1].errorbar(mapped_val,mgi_1tac5,yerr=uncertainty_mgi_1tac5,fmt='.',color='black',capthick=1)
	ax[1,1].set_xlim([-1,59])
	ax[1,1].set_xticks([0,10,20,30,40,50])
	ax[1,1].set_xticklabels(([]))
	ax[1,1].set_ylim([-3.9,3.3]) # limits to exclude outliers

	# Mg I (1.71 um)
	ax[2,0].errorbar(mapped_val,mgi_1tac7,yerr=uncertainty_mgi_1tac7,fmt='.',color='black',capthick=1)
	ax[2,0].set_xlim([-1,59])
	ax[2,0].set_xticks([0,10,20,30,40,50])
	ax[2,0].set_xticklabels((x_spec_list))
	#ax[2,0].set_ylabel(r"EW ($\AA$)")
	#ax[2,0].set_ylabel('EW '+r"($\AA$)")
	ax[2,0].set_ylabel('EW ($\AA$)')
	ax[2,0].set_ylim([-1.4,4.2]) # limits to exclude outliers

	# Na I (2.21 um)
	ax[2,1].errorbar(mapped_val,nai_2tac2,yerr=uncertainty_nai_2tac2,fmt='.',color='black',capthick=1)
	ax[2,1].set_xlim([-1,59])
	ax[2,1].set_xticks([0,10,20,30,40,50])
	ax[2,1].set_xticklabels((x_spec_list))
	ax[2,1].set_ylim([-2.5,8]) # limits to exclude outliers

	"""
	# label features (old)
	ax[0,0].annotate( 'Ca II (0.866 $\mu m$)', xy=(2, 7) )
	ax[0,1].annotate( 'Na I (1.14 $\mu m$)', xy=(2, 13.75) ) # normalize to this subplot...xy=(2, (5*ymax/5.9))
	ax[1,0].annotate( 'Al I (1.31 $\mu m$)', xy=(2, 2.8) )
	ax[1,1].annotate( 'Mg I (1.49 $\mu m$)', xy=(2, 2.25) )
	ax[2,0].annotate( 'Mg I (1.71 $\mu m$)', xy=(2, 3.4) )
	ax[2,1].annotate( 'Na I (2.21 $\mu m$)', xy=(2, 6.2) )
	"""
	norm_text = (15.9-13.75)/(15.9+3.4)
	# label features
	ax[0,0].annotate( 'Ca II (0.866 $\mu$m)', xy=(2, (7.9 - (7.9+3.1)*norm_text)) )
	ax[0,1].annotate( 'Na I (1.14 $\mu$m)', xy=(2, 13.75) ) # normalize to this subplot
	ax[1,0].annotate( 'Al I (1.31 $\mu$m)', xy=(2, (3.6 - (3.6+1.2)*norm_text)) )
	ax[1,1].annotate( 'Mg I (1.49 $\mu$m)', xy=(2, (3.3 - (3.3+3.9)*norm_text)) )
	ax[2,0].annotate( 'Mg I (1.71 $\mu$m)', xy=(2, (4.2 - (4.2+1.4)*norm_text)) )
	ax[2,1].annotate( 'Na I (2.21 $\mu$m)', xy=(2, (8.0 - (8.0+2.5)*norm_text)) )

	# label by lum class
	ax[0,1].annotate( 'Young Dwarfs', xy=(2, 11.75), color='black', size='medium' )#size='x-small'
	ax[0,1].annotate( 'Old Dwarfs', xy=(2, 9.75), color='red', size='medium' )#size='small'
	ax[0,1].annotate( 'Old Giants', xy=(2, 7.75), color='orange', size='medium' )#size='large'
	ax[0,1].annotate( 'Old Supergiants', xy=(2, 5.75), color='purple', size='medium' )#size='xx-large'

	# turn off x-axis tics & labels
	#ax[0,0].axes.get_xaxis().set_visible(False)

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


	# set precision of axis tics
	#ax[0,0].yaxis.set_major_formatter(plt.FormatStrFormatter('%i'))  # integers

	#plt.tight_layout()
	fig.tight_layout()
	fig.subplots_adjust(hspace=.05)



	#plt.show()
	plt.savefig('EW_obs_calcDwarfs_R09_err_medium_160713.png')


def obs_calcedR09_6subplots_overlay_160720():
	'''
	# To make plots iteratively
	yngms = raw_input("Enter numerical val yngms: ")
	oldms = raw_input("Enter numerical val oldms: ")
	yngms,oldms = float(yngms), float(oldms)
	plt.savefig('160720_comp_plots/new/___'+str(yngms)+'_Olds'+str(oldms)+'_160720.png', bbox_inches='tight')
	'''

	

	# call functions for mapping SptTyp and luminosity class
	calculated_R09_EW_values()

	# clear and setup subplots
	plt.clf()

	#fig, ax = plt.subplots(3,2, sharex=True, sharey=True) #sharex=True removes need for "set_xticklabels(([]))" or...
	#fig, ax = plt.subplots(3,2, sharex='col', sharey='row')
	fig, ax = plt.subplots(3,2)
	
	# put y-axis on RHS
	#ax[0,1].yaxis.tick_right()
	#ax[1,1].yaxis.tick_right()
	#ax[2,1].yaxis.tick_right()

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

	#print 'n_supergiants: ', n_supergiants #>>n_supergiants: 55
	#print 'n_giants: ', n_giants #>>n_giants: 80
	#print 'n_dwarfs: ', n_dwarfs #>>n_dwarfs: 59
	#print 'n_missed: ', n_missed #>>n_missed: 0


	##
	# Formatting errorbars
	##
	#   markeredgewidth == mew
	#   markeredgecolor == mec


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
	
	"""# need to remove one indent to use commented section below
		# scatter - make all marker sized the smae for Yng stars
		ax[0,0].scatter(mapped_val,caii, color='black', s=5)
		ax[0,1].scatter(mapped_val,nai, color='black', s=5)
		ax[1,0].scatter(mapped_val,ali, color='black', s=5)
		ax[1,1].scatter(mapped_val,mgi_1tac5, color='black', s=5)
		ax[2,0].scatter(mapped_val,mgi_1tac7, color='black', s=5)
		ax[2,1].scatter(mapped_val,nai_2tac2, color='black', s=5)

		# label features (old)
		ax[0,0].annotate( 'Ca II (0.866 $\mu m$)', xy=(2, 7) )
		ax[0,1].annotate( 'Na I (1.14 $\mu m$)', xy=(2, 13.75) ) # normalize to this subplot...xy=(2, (5*ymax/5.9))
		ax[1,0].annotate( 'Al I (1.31 $\mu m$)', xy=(2, 2.8) )
		ax[1,1].annotate( 'Mg I (1.49 $\mu m$)', xy=(2, 2.25) )
		ax[2,0].annotate( 'Mg I (1.71 $\mu m$)', xy=(2, 3.4) )
		ax[2,1].annotate( 'Na I (2.21 $\mu m$)', xy=(2, 6.2) )
	 """
	# turn off x-axis tics & labels
	#ax[0,0].axes.get_xaxis().set_visible(False)

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

	# set precision of axis tics
	#ax[0,0].yaxis.set_major_formatter(plt.FormatStrFormatter('%i'))  # integers

	#plt.tight_layout()
	fig.tight_layout()
	fig.subplots_adjust(hspace=.05, bottom=0.075)#, wspace=0.05)



	#plt.show()
	plt.savefig('EW_obs_calcDwarfs_R09_err_mu_m_160720.png', bbox_inches='tight')
	#plt.savefig('annotate_plot_variations/EW_obs_calcDwarfs_R09_err_ps13_spacing1tac5uneven_xlabel_hspace_bottomtac075_160719.png')


def obs_calcedR09_6subplots_160721():
	'''
	# To make plots iteratively
	yngms = raw_input("Enter numerical val yngms: ")
	oldms = raw_input("Enter numerical val oldms: ")
	yngms,oldms = float(yngms), float(oldms)
	plt.savefig('160720_comp_plots/new/___'+str(yngms)+'_Olds'+str(oldms)+'_160720.png', bbox_inches='tight')
	'''

	

	# call functions for mapping SptTyp and luminosity class
	calculated_R09_EW_values()

	# clear and setup subplots
	plt.clf()

	#fig, ax = plt.subplots(3,2, sharex=True, sharey=True) #sharex=True removes need for "set_xticklabels(([]))" or...
	#fig, ax = plt.subplots(3,2, sharex='col', sharey='row')
	fig, ax = plt.subplots(3,2)
	
	# put y-axis on RHS
	#ax[0,1].yaxis.tick_right()
	#ax[1,1].yaxis.tick_right()
	#ax[2,1].yaxis.tick_right()

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

	#print 'n_supergiants: ', n_supergiants #>>n_supergiants: 55
	#print 'n_giants: ', n_giants #>>n_giants: 80
	#print 'n_dwarfs: ', n_dwarfs #>>n_dwarfs: 59
	#print 'n_missed: ', n_missed #>>n_missed: 0


	##
	# Formatting errorbars
	##
	#   markeredgewidth == mew
	#   markeredgecolor == mec


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
	ax[1,1].set_ylim([-1.5,3.3]) # limits to exclude outliers

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
	
	"""# need to remove one indent to use commented section below
		# scatter - make all marker sized the smae for Yng stars
		ax[0,0].scatter(mapped_val,caii, color='black', s=5)
		ax[0,1].scatter(mapped_val,nai, color='black', s=5)
		ax[1,0].scatter(mapped_val,ali, color='black', s=5)
		ax[1,1].scatter(mapped_val,mgi_1tac5, color='black', s=5)
		ax[2,0].scatter(mapped_val,mgi_1tac7, color='black', s=5)
		ax[2,1].scatter(mapped_val,nai_2tac2, color='black', s=5)

		# label features (old)
		ax[0,0].annotate( 'Ca II (0.866 $\mu m$)', xy=(2, 7) )
		ax[0,1].annotate( 'Na I (1.14 $\mu m$)', xy=(2, 13.75) ) # normalize to this subplot...xy=(2, (5*ymax/5.9))
		ax[1,0].annotate( 'Al I (1.31 $\mu m$)', xy=(2, 2.8) )
		ax[1,1].annotate( 'Mg I (1.49 $\mu m$)', xy=(2, 2.25) )
		ax[2,0].annotate( 'Mg I (1.71 $\mu m$)', xy=(2, 3.4) )
		ax[2,1].annotate( 'Na I (2.21 $\mu m$)', xy=(2, 6.2) )
	 """
	# turn off x-axis tics & labels
	#ax[0,0].axes.get_xaxis().set_visible(False)

	norm_text = (15.9-13.75)/(15.9+3.4)
	# label features
	ax[0,0].annotate( 'Ca II (0.866 $\mu$m)', xy=(2, (7.9 - (7.9+3.1)*norm_text)), weight=500 )
	ax[0,1].annotate( 'Na I (1.14 $\mu$m)', xy=(2, 13.75), weight=500 ) # normalize to this subplot
	ax[1,0].annotate( 'Al I (1.31 $\mu$m)', xy=(2, (3.6 - (3.6+1.2)*norm_text)), weight=500 )
	ax[1,1].annotate( 'Mg I (1.49 $\mu$m)', xy=(2, (3.3 - (3.3+1.5)*norm_text)), weight=500 )
	ax[2,0].annotate( 'Mg I (1.71 $\mu$m)', xy=(2, (4.2 - (4.2+1.4)*norm_text)), weight=500 )
	ax[2,1].annotate( 'Na I (2.21 $\mu$m)', xy=(2, (8.0 - (8.0+2.5)*norm_text)), weight=500 )

	'''#160721
	###
	# Legend w/o shapes
	###
	# label by lum class
	ax[0,1].annotate( 'Young Dwarfs', xy=(2, 12), color='black', size=13, weight=1000 )
	ax[0,1].annotate( 'Old Dwarfs', xy=(2, 10.5), color='red', size=13, weight=1000 )
	ax[0,1].annotate( 'Old Giants', xy=(2, 9), color='orange', size=13, weight=1000 )
	ax[0,1].annotate( 'Old Supergiants', xy=(2, 7.5), color='purple', size=13, weight=1000 )
	'''

	##
	# Legend w/ shapes
	##
	# label by lum class
	ax[0,1].annotate( 'Young Dwarfs', xy=(4.1, 12), color='black', size=13, weight=1000 )
	ax[0,1].annotate( 'Old Dwarfs', xy=(4.2, 10.5), color='red', size=13, weight=1000 )
	ax[0,1].annotate( 'Old Giants', xy=(4.3, 9), color='orange', size=13, weight=1000 )
	ax[0,1].annotate( 'Old Supergiants', xy=(4.4, 7.5), color='purple', size=13, weight=1000 )

	# Add fake data points for legend
	#fakex,fakey = [3,3,3,3], [12.4,10.9,9.4,7.9]
	fakex, fakey, mrks, mrsize, fakecol = [3,3,3,3], [12.4,10.9,9.375,7.95], ['.','8','v','^'], [17,9,9,9], ['black','red','orange','purple']
	for kk in range(len(fakex)):
		ax[0,1].errorbar(fakex[kk],fakey[kk], marker=mrks[kk], ms=mrsize[kk], color=fakecol[kk],mec=fakecol[kk])

	

	# Create fake data points to go next to labels
	#ax[0,1].scatter(mapped_val,nai, color='black')	

	# set major ytic to show up at integer values
	ax[0,0].yaxis.set_major_locator(ticker.MultipleLocator(2))
	ax[0,1].yaxis.set_major_locator(ticker.MultipleLocator(5))
	ax[1,0].yaxis.set_major_locator(ticker.MultipleLocator(1))
	ax[1,1].yaxis.set_major_locator(ticker.MultipleLocator(1))
	ax[2,0].yaxis.set_major_locator(ticker.MultipleLocator(1))
	ax[2,1].yaxis.set_major_locator(ticker.MultipleLocator(2))

	# set minor ytic to show up every 0.2
	ax[0,0].yaxis.set_minor_locator(ticker.MultipleLocator(0.5))
	ax[0,1].yaxis.set_minor_locator(ticker.MultipleLocator(1))
	ax[1,0].yaxis.set_minor_locator(ticker.MultipleLocator(0.2))
	ax[1,1].yaxis.set_minor_locator(ticker.MultipleLocator(0.25))
	ax[2,0].yaxis.set_minor_locator(ticker.MultipleLocator(0.2))
	ax[2,1].yaxis.set_minor_locator(ticker.MultipleLocator(0.5))

	# set minor xtic to show up every 2
	ax[0,0].xaxis.set_minor_locator(ticker.MultipleLocator(2))
	ax[0,1].xaxis.set_minor_locator(ticker.MultipleLocator(2))
	ax[1,0].xaxis.set_minor_locator(ticker.MultipleLocator(2))
	ax[1,1].xaxis.set_minor_locator(ticker.MultipleLocator(2))
	ax[2,0].xaxis.set_minor_locator(ticker.MultipleLocator(2))
	ax[2,1].xaxis.set_minor_locator(ticker.MultipleLocator(2))

	# set precision of axis tics
	#ax[0,0].yaxis.set_major_formatter(plt.FormatStrFormatter('%i'))  # integers

	#plt.tight_layout()
	fig.tight_layout()
	fig.subplots_adjust(hspace=.05, bottom=0.075)#, wspace=0.05)



	#plt.show()
	plt.savefig('EW_obs_calcDwarfs_R09_mg1tac5_160725.png', bbox_inches='tight')
	#plt.savefig('annotate_plot_variations/EW_obs_calcDwarfs_R09_err_ps13_spacing1tac5uneven_xlabel_hspace_bottomtac075_160719.png')





#obs_calcedR09_6subplots_overlay_160720()
obs_calcedR09_6subplots_160721()

print '\n\nLOOK AT "tmp_options.py" FOR VARATIONS IN PLOTS\n\n'




