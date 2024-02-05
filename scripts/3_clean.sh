cd data
pwd
mv  dicom-1/* dicom-0/
mv  dicom-2/* dicom-0/
mv  dicom-3/* dicom-0/

rm -rf dicom-1
rm -rf dicom-2
rm -rf dicom-3

rm -rf dicom-0/0226134 # Data and Mask slice numbers not the same