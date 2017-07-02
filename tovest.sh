TOVEST="Text2Vest"
#TOVEST="fsl5.0-Text2Vest"

if [ -f "design_matrix.txt" ]
then
	$TOVEST design_matrix.txt design.mat
	rm design_matrix.txt
fi
if [ -f "contrast_matrix.txt" ]
then
	$TOVEST contrast_matrix.txt design.con
	rm contrast_matrix.txt
fi
if [ -f "groups.txt" ]
then
	$TOVEST groups.txt design.grp
	rm groups.txt
fi
if [ -f "ftests.txt" ]
then
	$TOVEST ftests.txt design.fts
	rm ftests.txt
fi
