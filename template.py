
#TODO: make universal with parameters, create script for it.
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import logging as log


reds = sns.color_palette("Reds", as_cmap=True)
reds.set_over('k')
# parameters: num_heatmaps, dataframe(s) path,

shapeSet = None

num_heatmaps = 3
if num_heatmaps == 1:
	shape = (1,1)
elif num_heatmaps == 2:
	shape = (1,2)
elif num_heatmaps == 3:
	shape = (1,3)
elif num_heatmaps == 4:
	shape = (2,2)
elif num_heatmaps == 5:
	shape = (1,5)
elif num_heatmaps == 6:
	shape = (2,3)
else:
	log.error("num_heatmaps parameter not between 1 and 6.")

if shapeSet is not None: #user specified input
	
	shape = shapeSet

for i in range(4):
	for l in range(1, 3+1):
		fig, axn = plt.subplots(nrows=1, ncols=3, figsize=(15,6))
		fig.tight_layout(rect=[0.025, 0.025, .9, .9]) #where the 3 heatmaps are
		cbar_ax = fig.add_axes([.91, .3, .03, .4]) #dimensions: [left, bottom, width, height] in fractions of figure width and height.

		if l == 1:
			label_labda = ", " + r"$\lambda = 1$"
		elif l == 2:
			label_labda = ", " + r"$\lambda = 2$"
		elif l == 3:
			label_labda = ", " + r"$\lambda = 3$"
		else:
			label_labda = ""
			print("wrong l")

		if i == 0:
			label_k_c = ", " + r"$k_c = n^{1 / (\beta + 1)}$"
		elif i == 1:
			label_k_c = ", " + r"$k_c = n^{1 / (\beta + 0.5)}$"
		elif i == 2:
			label_k_c = ", " + r"$k_c = n^{1 / \beta}$"
		elif i == 3:
			label_k_c = ", " + r"$k_c = k_{max}$"
		else:
			label_k_c = ""
			print("wrong i")

		for j, ax in enumerate(axn.flat):
			if j == 0:
				df = df_hill_dict[i][l]
				ax.set_title("Hill estimator" + label_k_c + label_labda)
			elif j == 1:
				df = df_moments_dict[i][l]
				ax.set_title("Moments estimator" + label_k_c + label_labda)
			elif j == 2:
				df = df_kernel_dict[i][l]
				ax.set_title("Kernel estimator" + label_k_c + label_labda)
			sns.heatmap(df, ax=ax,
						vmin= 0,
						vmax= 1,
						cmap= reds,
						xticklabels= [elt // 100000 for elt in cols], yticklabels=[elt // 100000 for elt in rows][::-1],
						annot = True,
						cbar= j == 0,
						cbar_kws={'label': 'root mean squared error', 'extend' : 'max'},
						cbar_ax=None if j else cbar_ax)

		plt.setp(axn, xlabel='Nruns' + r"$(\cdot 10^5)$")
		plt.setp(axn[0], ylabel='N' + r"$(\cdot 10^5)$")
		plt.suptitle('Estimator performance for '  r"$\beta$ = {}".format(str(ple)), weight="bold", size= 'x-large')
		plt.savefig('./Figures/labdas/Heatmap_ple{}_rows{}cols{}k_c={}labda={}.png'.format(str(ple), str(len(rows)), str(len(cols)), str(i), str(l)))
