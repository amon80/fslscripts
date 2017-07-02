# Fsl scripts
Some scripts written in python to easily generate the files needed by FSL program Randomise.

Currently, to files for the following studies are provided:
- Two sample unpaired T Test. 

    python unpairedtwosamplegeneratorion.py <\# subjects in group1> <\#subjects in group2>
- Two sample paired T Test.

    python pairedtwosamplegeneration.py <\# subjects>
- ANOVA: 1 factor 4 level.

    python anova1factor4levelgeneration.py <\# subjects>

Python scripts work with both python 2 & 3. Shell script can be easily modified to use Neurodebian FSL instead of the regular one.
