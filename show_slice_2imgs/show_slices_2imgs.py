#!/usr/bin/env python
# Copyright (c) 2018, Konstantinos Kamnitsas
# All rights reserved.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the BSD license. See the accompanying LICENSE file
# or read the terms at https://opensource.org/licenses/BSD-3-Clause.

from __future__ import absolute_import, print_function, division
import numpy as np
import nibabel as nib
import argparse
import matplotlib.pyplot as plt

NUM_SLICES_TO_SHOW = 6

"""
A tiny script that loads two NIFTI files and plots the same slice from both.
This is to enable visual inspection of whether the two nii scans are aligned in the image space (not touching the header).
This uses the same library (nibabel) and steps that DeepMedic uses. It does not touch the header.
Thus, if images are aligned when they are shown, they should be aligned in the image space that DeepMedic works in.
Of course you cant go over all images like this. I would recommend going over just a few and check visually that things are as expected.

You can run it with a command similar to:
python ./show_slices_2imgs.py -i1 ./flair.nii.gz -i2 ./seg.nii.gz -ax 2

"""

def setupArgParser() :
    parser = argparse.ArgumentParser( prog='Viz2Slices', formatter_class=argparse.RawTextHelpFormatter,
    description='''\nRead two images, show same slice, without touching header, to check alignment.''')
    
    parser.add_argument("-i1", dest='inp_1', type=str, default = "./flair.nii.gz", help="Path to 1st nii.")
    parser.add_argument("-i2", dest='inp_2', type=str, default = "./seg.nii.gz", help="Path to 2nd nii.")
    parser.add_argument("-s", dest='slice_i', type=int, default = -1, help="Index of the slice to visualize. -1 will make it take a predefined number of slices along the axis.")
    parser.add_argument("-ax", dest='axis_i', type=int, default = 2, help="Index of axis along which to take the slices.")
    
    return parser


def load_nii(path):
    proxy = nib.load(path)
    img = np.asarray(proxy.get_data())
    hdr = proxy.header
    aff = proxy.affine
    proxy.uncache()
    
    return (img, hdr, aff)


def plot_two_slices(vol_1, vol_2, axis_i, slice_i_given):
    # vol_1 & vol_2 must have been already assured to have same dims.
    # Special handling of slice_num = -1
    if slice_i_given >= 0:
        assert vol_1.shape[axis_i] >= slice_i_given
        slice_inds = [slice_i_given]
    else: # slice_i_given = -1
        
        axis_len = vol_1.shape[axis_i]
        slicing_stride = axis_len // (NUM_SLICES_TO_SHOW + 1)
        slice_inds = range(slicing_stride, axis_len, slicing_stride)[:NUM_SLICES_TO_SHOW]
        print("DEBUG: vol_1.shape=", vol_1.shape)
        print("DEBUG: axis_len=",axis_len)
        print("DEBUG: slicing_stride=",slicing_stride)
        print("DEBUG: slice_inds=",slice_inds)
        assert len(slice_inds) == NUM_SLICES_TO_SHOW
    
    fig, axes = plt.subplots(nrows=2, ncols=len(slice_inds), squeeze=False)
    #plt.subplots_adjust(hspace=0.05,wspace=0.05)
    
    for i, slice_i in zip( range(len(slice_inds)), slice_inds):
        if   axis_i == 0: vol1_sl = vol_1[ slice_i, :, : ]; vol2_sl = vol_2[ slice_i, :, : ]; ax_y=1; ax_x=2
        elif axis_i == 1: vol1_sl = vol_1[ :, slice_i, : ]; vol2_sl = vol_2[ :, slice_i, : ]; ax_y=0; ax_x=2
        elif axis_i == 2: vol1_sl = vol_1[ :, :, slice_i ]; vol2_sl = vol_2[ :, :, slice_i ]; ax_y=0; ax_x=1
        
        axes[0,i].imshow( vol1_sl, cmap='gray')
        axes[1,i].imshow( vol2_sl, cmap='gray')
        # Add labels on the axis.
        # imshow plots on the yaxis the 1st dim of the given array, and xaxis the 2nd given.
        axes[0,i].set_xlabel('Axis-['+str(ax_x)+'] in Scan')
        axes[0,i].set_ylabel('Axis-['+str(ax_y)+'] in Scan')
        axes[1,i].set_xlabel('Axis-['+str(ax_x)+'] in Scan')
        axes[1,i].set_ylabel('Axis-['+str(ax_y)+'] in Scan')

    plt.show()
    
    return fig


if __name__ == '__main__':
    parser = setupArgParser()
    args = parser.parse_args()

    (vol_1, hdr_1, aff_1) = load_nii( args.inp_1 )
    print("INFO: Image #1 shape: ", vol_1.shape)
    (vol_2, hdr_2, aff_2) = load_nii( args.inp_2 )
    print("INFO: Image #2 shape: ", vol_2.shape)
    assert len(vol_1.shape) == len(vol_2.shape)
    assert np.all( np.asarray(vol_1.shape) == np.asarray(vol_2.shape) )

    plot_two_slices(vol_1, vol_2, args.axis_i, args.slice_i)


