# Fsl scripts
Some scripts written in python to easily generate the files needed by FSL program Randomise. Also some other utilities scripts are provided.

Currently, the following generation files are provided:
- Two sample unpaired T Test. 

	python unpairedtwosamplegeneratorion.py <# subjects in group1> <\#subjects in group2>
- Two sample paired T Test.

	python pairedtwosamplegeneration.py <# subjects>
- ANOVA: 1 factor 4 level.

	python anova1factor4levelgeneration.py <# subjects>

Moreover, an addition script is provided to normalize the permutation vector files output by FSL with the option -N.

	python normalizefslperm.py <FSL Permutation File Path>

Python scripts work with both python 2 & 3. The shell script "tovest.sh" can be easily modified to use Neurodebian FSL instead of the regular one.
