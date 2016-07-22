def move_mg():
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
	ax[0,0].annotate( 'Ca II (0.866 $\mu m$)', xy=(2, (7.9 - (7.9+3.1)*norm_text)), weight=500 )
	ax[0,1].annotate( 'Na I (1.14 $\mu m$)', xy=(2, 13.75), weight=500 ) # normalize to this subplot
	ax[1,0].annotate( 'Al I (1.31 $\mu m$)', xy=(2, (3.6 - (3.6+1.2)*norm_text)), weight=500 )
	ax[1,1].annotate( 'Mg I (1.49 $\mu m$)', xy=(2, (3.3 - (3.3+1.5)*norm_text)), weight=500 )
	ax[2,0].annotate( 'Mg I (1.71 $\mu m$)', xy=(2, (4.2 - (4.2+1.4)*norm_text)), weight=500 )
	ax[2,1].annotate( 'Na I (2.21 $\mu m$)', xy=(2, (8.0 - (8.0+2.5)*norm_text)), weight=500 )

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
	plt.savefig('_options/no_symbols_mg_1tac5.png', bbox_inches='tight')
	#plt.savefig('annotate_plot_variations/EW_obs_calcDwarfs_R09_err_ps13_spacing1tac5uneven_xlabel_hspace_bottomtac075_160719.png')


def align_text():
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
	

	# label features
	norm_text = (15.9-13.75)/(15.9+3.4)
	ax[0,0].annotate( 'Ca II (0.866 $\mu m$)', xy=(2, (7.9 - (7.9+3.1)*norm_text)), weight=500 )
	ax[0,1].annotate( 'Na I (1.14 $\mu m$)', xy=(2, 13.75), weight=500 ) # normalize to this subplot
	ax[1,0].annotate( 'Al I (1.31 $\mu m$)', xy=(2, (3.6 - (3.6+1.2)*norm_text)), weight=500 )
	ax[1,1].annotate( 'Mg I (1.49 $\mu m$)', xy=(2, (3.3 - (3.3+1.5)*norm_text)), weight=500 )
	ax[2,0].annotate( 'Mg I (1.71 $\mu m$)', xy=(2, (4.2 - (4.2+1.4)*norm_text)), weight=500 )
	ax[2,1].annotate( 'Na I (2.21 $\mu m$)', xy=(2, (8.0 - (8.0+2.5)*norm_text)), weight=500 )


	##
	# Legend
	##
	# label by lum class
	ax[0,1].annotate( 'Young Dwarfs', xy=(2, 12), color='black', size=13, weight=1000 )
	ax[0,1].annotate( 'Old Dwarfs', xy=(2, 10.5), color='red', size=13, weight=1000 )
	ax[0,1].annotate( 'Old Giants', xy=(2, 9), color='orange', size=13, weight=1000 )
	ax[0,1].annotate( 'Old Supergiants', xy=(2, 7.5), color='purple', size=13, weight=1000 )

	# Add fake data points for legend
	#fakex,fakey = [2,2,2,2], [12,10.5,9,7.5]
	fakex, fakey, mrks, mrsize, fakecol = [1,1,1,1], [12.5,11,9.5,8], ['.','8','v','^'], [18,10,10,10], ['black','red','orange','purple']
	for kk in range(len(fakex)):
		ax[0,1].errorbar(fakex[kk],fakey[kk], marker=mrks[kk], ms=mrsize[kk], color=fakecol[kk],mec=fakecol[kk])
	'''
	# Add shapes to legend, rather than fake data points
	import matplotlib.patches as patches
	#								Patches:(  (x,y), number of vertices, radius, color, edges )
	ax[0,1].add_patch( patches.RegularPolygon( (1.75, 12.0), 3, 0.5, facecolor="black", edgecolor="black" ) )
	ax[0,1].add_patch( patches.RegularPolygon( (1.75, 10.5), 3, 0.6, facecolor="red", edgecolor="red" ) )
	ax[0,1].add_patch( patches.RegularPolygon( (1.75, 9.00), 3, 0.7, facecolor="orange", edgecolor="orange" ) )
	ax[0,1].add_patch( patches.RegularPolygon( (1.75, 7.50), 8, 0.5, facecolor="purple", edgecolor="purple" ) )
	'''


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


	fig.tight_layout()
	fig.subplots_adjust(hspace=.05, bottom=0.075)#, wspace=0.05)

	plt.savefig('_options/align_text.png', bbox_inches='tight')


def align_symbols():
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
	

	# label features
	norm_text = (15.9-13.75)/(15.9+3.4)
	ax[0,0].annotate( 'Ca II (0.866 $\mu m$)', xy=(2, (7.9 - (7.9+3.1)*norm_text)), weight=500 )
	ax[0,1].annotate( 'Na I (1.14 $\mu m$)', xy=(2, 13.75), weight=500 ) # normalize to this subplot
	ax[1,0].annotate( 'Al I (1.31 $\mu m$)', xy=(2, (3.6 - (3.6+1.2)*norm_text)), weight=500 )
	ax[1,1].annotate( 'Mg I (1.49 $\mu m$)', xy=(2, (3.3 - (3.3+1.5)*norm_text)), weight=500 )
	ax[2,0].annotate( 'Mg I (1.71 $\mu m$)', xy=(2, (4.2 - (4.2+1.4)*norm_text)), weight=500 )
	ax[2,1].annotate( 'Na I (2.21 $\mu m$)', xy=(2, (8.0 - (8.0+2.5)*norm_text)), weight=500 )


	##
	# Legend
	##
	# label by lum class
	ax[0,1].annotate( 'Young Dwarfs', xy=(4.1, 12), color='black', size=13, weight=1000 )
	ax[0,1].annotate( 'Old Dwarfs', xy=(4.2, 10.5), color='red', size=13, weight=1000 )
	ax[0,1].annotate( 'Old Giants', xy=(4.3, 9), color='orange', size=13, weight=1000 )
	ax[0,1].annotate( 'Old Supergiants', xy=(4.4, 7.5), color='purple', size=13, weight=1000 )

	# Add fake data points for legend
	#fakex,fakey = [2,2,2,2], [12,10.5,9,7.5]
	fakex, fakey, mrks, mrsize, fakecol = [3,3,3,3], [12.4,10.9,9.4,7.9], ['.','8','v','^'], [17,9,9,9], ['black','red','orange','purple']
	for kk in range(len(fakex)):
		ax[0,1].errorbar(fakex[kk],fakey[kk], marker=mrks[kk], ms=mrsize[kk], color=fakecol[kk],mec=fakecol[kk])
	'''
	# Add shapes to legend, rather than fake data points
	import matplotlib.patches as patches
	#								Patches:(  (x,y), number of vertices, radius, color, edges )
	ax[0,1].add_patch( patches.RegularPolygon( (1.75, 12.0), 3, 0.5, facecolor="black", edgecolor="black" ) )
	ax[0,1].add_patch( patches.RegularPolygon( (1.75, 10.5), 3, 0.6, facecolor="red", edgecolor="red" ) )
	ax[0,1].add_patch( patches.RegularPolygon( (1.75, 9.00), 3, 0.7, facecolor="orange", edgecolor="orange" ) )
	ax[0,1].add_patch( patches.RegularPolygon( (1.75, 7.50), 8, 0.5, facecolor="purple", edgecolor="purple" ) )
	'''


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


	fig.tight_layout()
	fig.subplots_adjust(hspace=.05, bottom=0.075)#, wspace=0.05)

	plt.savefig('_options/align_symbols.png', bbox_inches='tight')


def polt_variations():
	move_mg()
	align_text()
	align_symbols()

polt_variations()

