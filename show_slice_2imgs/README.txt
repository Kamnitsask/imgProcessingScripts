A tiny script that loads two NIFTI files and plots the same slice from both.
This is to enable visual inspection of whether the two nii scans are aligned in the image space (not touching the header).
This uses the same library (nibabel) and steps that DeepMedic uses. It does not touch the header.
Thus, if images are aligned when they are shown, they should be aligned in the image space that DeepMedic works in.
Of course you cant go over all images like this. I would recommend going over just a few and check visually that things are as expected.

You can run it with a command similar to:
python ./show_slices_2imgs.py -i1 ./flair.nii.gz -i2 ./seg.nii.gz -ax 2

Regards,
Konstantinos
