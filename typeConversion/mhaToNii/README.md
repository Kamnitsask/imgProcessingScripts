### Introduction

Scripts for converting an .mha image to a .nii or .nii.gz (suggested) image.

Scripts are provided only for reference for any interested user. No support can be provided for these.

#### 1. Requirements

- [itk](https://itk.org/): For loading / converting / saving. Possible script can be changed to use simpleITK, but I can't support it.
- [cmake](https://cmake.org/): Required for compilation.
 
#### 2. Compilation

First, make sure the above requirements were intstalled.

The main source code of the conversion script is in ./src/mhaToNii.cpp

To compile it, from the main mhaToNii folder do:

```
cd build
cmake ..
make
```

The cpp script will be compiled if ITK is available on your system. Files and folders will appear in ./build folder. Among them, the executable **./build/src/mhaToNii** will appear. This is what you can use for the conversion.


The compiled executable **mhaToNii** (see above) can be used for conversion. It takes two arguments. First, an input file, which will be your .mha file. Second argument will be the filename of the output nii or nii.gz file. INCLUDING the extension (.nii or .nii.gz, suggesting the second as it's much smaller.). Example:

```
cd ./build/src/
./mhaToNii pathToMhaFile.mha pathWhereToSaveNii.nii.gz
```

#### 3. Support

No support can be provided for these scripts, sorry for this. For questions on how it works, please see documentation of the ITK library.
