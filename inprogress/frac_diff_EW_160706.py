from astropy.io import ascii
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as ticker


#EW_spt_table = ascii.read('EW_of_rayner_stars.txt')
EW_spt_table = ascii.read('/Users/cmutnik/work/astro/plots/EW/cool_stars_tab8_EW/obs_EW_vals_160624.txt')


caii = EW_spt_table['EW_caii']
nai = EW_spt_table['EW_nai']
nai_2tac2 = EW_spt_table['EW_nai_2tac2']
ali = EW_spt_table['EW_ali']
mgi_1tac5 = EW_spt_table['EW_mgi_1tac5']
mgi_1tac7 = EW_spt_table['EW_mgi_1tac7']
uncertainty_mgi_1tac7 = EW_spt_table['uncertainty_mgi_1tac7']
uncertainty_caii = EW_spt_table['uncertainty_caii']
uncertainty_nai_2tac2 = EW_spt_table['uncertainty_nai_2tac2']
uncertainty_nai = EW_spt_table['uncertainty_nai']
uncertainty_ali = EW_spt_table['uncertainty_ali']
uncertainty_mgi_1tac5 = EW_spt_table['uncertainty_mgi_1tac5']


EW_spt_type = list(EW_spt_table['spt type_standard_file'])
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


def sep_plots():
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
#sep_plots()


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
		ax[0,0].annotate('Ca II (0.866 $\mu m$)', xy=(2, 6))
		ax[0,1].annotate('Na I (1.14 $\mu m$)', xy=(2, 10))
		ax[1,0].annotate('Al I (1.31 $\mu m$)', xy=(2, 3))
		ax[1,1].annotate('Mg I (1.49 $\mu m$)', xy=(2, 3))
		ax[2,0].annotate('Mg I (1.71 $\mu m$)', xy=(2, 4))
		ax[2,1].annotate('Na I (2.21 $\mu m$)', xy=(2, 6.5))

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
		ax[0,0].annotate('Ca II (0.866 $\mu m$)', xy=(2, (5.*4.4/5.9)))
		ax[0,1].annotate('Na I (1.14 $\mu m$)', xy=(2, 5)) # normalize to this subplot...xy=(2, (5*ymax/5.9))
		ax[1,0].annotate('Al I (1.31 $\mu m$)', xy=(2, (5.*2.5/5.9)))
		ax[1,1].annotate('Mg I (1.49 $\mu m$)', xy=(2, (5.*2.2/5.9)))
		ax[2,0].annotate('Mg I (1.71 $\mu m$)', xy=(2, (5.*2.9/5.9)))
		ax[2,1].annotate('Na I (2.21 $\mu m$)', xy=(2, (5.*4.9/5.9)))

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
##
# Clunky but avoids error message and actaully works
##
#def Ha_le_loo_yer_it_worked():
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
	calcR09_colors = []
	for jj in R09_EW_values:
		#print jj
		if 'IV' in jj:
			n_giants+=1
			ccc = 'orange'
		elif 'V' in jj:
			n_dwarfs+=1
			ccc='red'
		elif "III" in jj:
			n_giants+=1
			ccc='orange'
		elif 'II' in jj:
			n_supergiants+=1
			ccc='purple'
		elif 'I' in jj:
			n_supergiants+=1
			ccc='purple'
		else:
			n_missed+=1
			ccc='green'
		ax[0,0].errorbar(R09_mapped_val[index],R09_caii[index],yerr=R09_uncertainty_caii[index], color=ccc)#, alpha=0.8)
		ax[0,1].errorbar(R09_mapped_val[index],R09_nai[index],yerr=R09_uncertainty_nai[index], color=ccc)#, alpha=0.8)
		ax[1,0].errorbar(R09_mapped_val[index],R09_ali[index],yerr=R09_uncertainty_ali[index], color=ccc)#, alpha=0.8)
		ax[1,1].errorbar(R09_mapped_val[index],R09_mgi_1tac5[index],yerr=R09_uncertainty_mgi_1tac5[index], color=ccc)#, alpha=0.8)
		ax[2,0].errorbar(R09_mapped_val[index],R09_mgi_1tac7[index],yerr=R09_uncertainty_mgi_1tac7[index], color=ccc)#, alpha=0.8)
		ax[2,1].errorbar(R09_mapped_val[index],R09_nai_2tac2[index],yerr=R09_uncertainty_nai_2tac2[index], color=ccc)#, alpha=0.8)

		index+=1

	#print 'n_supergiants: ', n_supergiants #>>n_supergiants: 55
	#print 'n_giants: ', n_giants #>>n_giants: 80
	#print 'n_dwarfs: ', n_dwarfs #>>n_dwarfs: 59
	#print 'n_missed: ', n_missed #>>n_missed: 0



	# Ca II (0.866 um)
	ax[0,0].errorbar(mapped_val,caii,yerr=uncertainty_caii,fmt='.',color='black')
	ax[0,0].scatter(mapped_val,caii, color='black')
	ax[0,0].set_xlim([-2,55])
	ax[0,0].set_xticks([0,10,20,30,40,50])
	ax[0,0].set_xticklabels(([]))
	ax[0,0].set_ylabel('EW ($\AA$)')

	# Na I (1.14 um)
	ax[0,1].errorbar(mapped_val,nai,yerr=uncertainty_nai,fmt='.',color='black')
	ax[0,1].scatter(mapped_val,nai, color='black')
	ax[0,1].set_xlim([-2,55])
	ax[0,1].set_xticks([0,10,20,30,40,50])
	ax[0,1].set_xticklabels(([]))

	# Al I (1.31 um)
	ax[1,0].errorbar(mapped_val,ali,yerr=uncertainty_ali,fmt='.',color='black')
	ax[1,0].set_xlim([-2,55])
	ax[1,0].set_xticks([0,10,20,30,40,50])
	ax[1,0].set_xticklabels(([]))
	ax[1,0].set_ylabel('EW ($\AA$)')

	# Mg I (1.49 um)
	ax[1,1].errorbar(mapped_val,mgi_1tac5,yerr=uncertainty_mgi_1tac5,fmt='.',color='black')
	ax[1,1].set_xlim([-2,55])
	ax[1,1].set_xticks([0,10,20,30,40,50])
	ax[1,1].set_xticklabels(([]))

	# Mg I (1.71 um)
	ax[2,0].errorbar(mapped_val,mgi_1tac7,yerr=uncertainty_mgi_1tac7,fmt='.',color='black')
	ax[2,0].set_xlim([-2,55])
	ax[2,0].set_xticks([0,10,20,30,40,50])
	ax[2,0].set_xticklabels((x_spec_list))
	ax[2,0].set_ylabel('EW ($\AA$)')

	# Na I (2.21 um)
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
	ax[0,0].annotate('Ca II (0.866 $\mu m$)', xy=(2, (5.*4.4/5.9)))
	ax[0,1].annotate('Na I (1.14 $\mu m$)', xy=(2, 5)) # normalize to this subplot...xy=(2, (5*ymax/5.9))
	ax[1,0].annotate('Al I (1.31 $\mu m$)', xy=(2, (5.*2.5/5.9)))
	ax[1,1].annotate('Mg I (1.49 $\mu m$)', xy=(2, (5.*2.2/5.9)))
	ax[2,0].annotate('Mg I (1.71 $\mu m$)', xy=(2, (5.*2.9/5.9)))
	ax[2,1].annotate('Na I (2.21 $\mu m$)', xy=(2, (5.*4.9/5.9)))

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
	plt.savefig('EW_obs_calcR09_6suplots_err.png')
obs_calcedR09_6subplots_overlay()
#Ha_le_loo_yer_it_worked()







###
# Keeps Giving Error Message:
#>> length of rgba sequence should be either 3 or 4
###
'''
def map_lum_classes_old():
	""" classify R09 stars as dwarfs, giants, or supergiants """
	global calcR09_colors

	calcR09_colors = []
	n_supergiants,n_giants,n_dwarfs,n_missed=0,0,0,0
	for jj in R09_EW_values:
		#print jj
		if 'IV' in jj:
			n_giants+=1
			calcR09_colors.append('red')
		elif 'V' in jj:
			n_dwarfs+=1
			calcR09_colors.append('purple')
		elif "III" in jj:
			n_giants +=1
			calcR09_colors.append('red')
		elif 'II' in jj:
			n_supergiants+=1
			calcR09_colors.append('orange')
		elif 'I' in jj:
			n_supergiants+=1
			calcR09_colors.append('orange')
		else:
			n_missed+=1
			#calcR09_colors.append('green')
			print jj

	# recast as array
	#calcR09_colors = np.array(calcR09_colors)

	print 'n_supergiants: ', n_supergiants
	print 'n_giants: ', n_giants
	print 'n_dwarfs: ', n_dwarfs
	print 'n_missed: ', n_missed
	print 'n_total: ', (n_supergiants +  n_giants + n_dwarfs + n_missed)
	print 'len(R09_EW_values): ', len(R09_EW_values)
def map_lum_classes_PlzWrk():
	global R09_mapped_val, calcR09_colors

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

	n_supergiants,n_giants,n_dwarfs,n_missed = 0,0,0,0
	calcR09_colors = []
	for jj in R09_EW_values:
		#print jj
		if 'IV' in jj:
			n_giants+=1
			calcR09_colors.append('red')
		elif 'V' in jj:
			n_dwarfs+=1
			calcR09_colors.append('purple')
		elif "III" in jj:
			n_giants +=1
			calcR09_colors.append('red')
		elif 'II' in jj:
			n_supergiants+=1
			calcR09_colors.append('orange')
		elif 'I' in jj:
			n_supergiants+=1
			calcR09_colors.append('orange')
		else:
			n_missed+=1
			#calcR09_colors.append('green')
			print jj
'''
##
# Older Method
##
'''
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
def subplots_obs_calcedR09_overlay():
	# call function(s) for mapping SptTyp and luminosity class
	calculated_R09_EW_values()
	
	# This dont work as intended
	#map_lum_classes_old()
	#map_lum_classes_PlzWrk()

	# clear and setup subplots
	plt.clf()
	fig, ax = plt.subplots(3,2)

	# Ca II (0.866 um)
	ax[0,0].errorbar(R09_mapped_val,R09_caii,yerr=R09_uncertainty_caii, color=calcR09_colors, alpha=0.8)
	ax[0,0].errorbar(mapped_val,caii,yerr=uncertainty_caii,fmt='.',color='black')
	ax[0,0].scatter(mapped_val,caii, color='black')
	ax[0,0].set_xlim([-2,55])
	ax[0,0].set_xticks([0,10,20,30,40,50])
	ax[0,0].set_xticklabels(([]))
	ax[0,0].set_ylabel('EW ($\AA$)')

	# Na I (1.14 um)
	ax[0,1].errorbar(R09_mapped_val,R09_nai,yerr=R09_uncertainty_nai, color=calcR09_colors, alpha=0.8)
	ax[0,1].errorbar(mapped_val,nai,yerr=uncertainty_nai,fmt='.',color='black')
	ax[0,1].scatter(mapped_val,nai, color='black')
	ax[0,1].set_xlim([-2,55])
	ax[0,1].set_xticks([0,10,20,30,40,50])
	ax[0,1].set_xticklabels(([]))

	# Al I (1.31 um)
	ax[1,0].errorbar(R09_mapped_val,R09_ali,yerr=R09_uncertainty_ali, color=calcR09_colors, alpha=0.8)
	ax[1,0].errorbar(mapped_val,ali,yerr=uncertainty_ali,fmt='.',color='black')
	ax[1,0].set_xlim([-2,55])
	ax[1,0].set_xticks([0,10,20,30,40,50])
	ax[1,0].set_xticklabels(([]))
	ax[1,0].set_ylabel('EW ($\AA$)')

	# Mg I (1.49 um)
	ax[1,1].errorbar(R09_mapped_val,R09_mgi_1tac5,yerr=R09_uncertainty_mgi_1tac5, color=calcR09_colors, alpha=0.8)
	ax[1,1].errorbar(mapped_val,mgi_1tac5,yerr=uncertainty_mgi_1tac5,fmt='.',color='black')
	ax[1,1].set_xlim([-2,55])
	ax[1,1].set_xticks([0,10,20,30,40,50])
	ax[1,1].set_xticklabels(([]))

	# Mg I (1.71 um)
	ax[2,0].errorbar(R09_mapped_val,R09_mgi_1tac7,yerr=R09_uncertainty_mgi_1tac7, color=calcR09_colors, alpha=0.8)
	ax[2,0].errorbar(mapped_val,mgi_1tac7,yerr=uncertainty_mgi_1tac7,fmt='.',color='black')
	ax[2,0].set_xlim([-2,55])
	ax[2,0].set_xticks([0,10,20,30,40,50])
	ax[2,0].set_xticklabels((x_spec_list))
	ax[2,0].set_ylabel('EW ($\AA$)')

	# Na I (2.21 um)
	ax[2,1].errorbar(R09_mapped_val,R09_nai_2tac2,yerr=R09_uncertainty_nai_2tac2, color=calcR09_colors, alpha=0.8)
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
	ax[0,0].annotate('Ca II (0.866 $\mu m$)', xy=(2, (5.*4.4/5.9)))
	ax[0,1].annotate('Na I (1.14 $\mu m$)', xy=(2, 5)) # normalize to this subplot...xy=(2, (5*ymax/5.9))
	ax[1,0].annotate('Al I (1.31 $\mu m$)', xy=(2, (5.*2.5/5.9)))
	ax[1,1].annotate('Mg I (1.49 $\mu m$)', xy=(2, (5.*2.2/5.9)))
	ax[2,0].annotate('Mg I (1.71 $\mu m$)', xy=(2, (5.*2.9/5.9)))
	ax[2,1].annotate('Na I (2.21 $\mu m$)', xy=(2, (5.*4.9/5.9)))

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
	plt.savefig('EW_obs_calcedR09_suplots_err_doesntwrk.png')
subplots_obs_calcedR09_overlay()
'''
