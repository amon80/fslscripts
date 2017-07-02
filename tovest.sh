if [ -f "design_matrix.txt" ]
then
	fsl5.0-Text2Vest design_matrix.txt design.mat
	rm design_matrix.txt
fi
if [ -f "contrast_matrix.txt" ]
then
	fsl5.0-Text2Vest contrast_matrix.txt design.con
	rm contrast_matrix.txt
fi
if [ -f "groups.txt" ]
then
	fsl5.0-Text2Vest groups.txt design.grp
	rm groups.txt
fi
if [ -f "ftests.txt" ]
then
	fsl5.0-Text2Vest ftests.txt design.fts
	rm ftests.txt
fi
