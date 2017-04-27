
#include <cstdio>
#include <cmath>

#include "itkImage.h"
#include "itkImageFileReader.h"
#include "itkImageFileWriter.h"
#include "itkMetaDataObject.h"
#include "itkNiftiImageIO.h"

#include <string>
#include <sstream> //for ostringstream.
#include <fstream>

typedef std::vector<std::string> vectorOfStringsType;	
typedef std::vector<vectorOfStringsType> vectorOfVectorOfStringsType;

typedef float InputPixelType;
const unsigned int   DimensionOfNii = 3;
typedef itk::Image< InputPixelType, DimensionOfNii > InputImageType;



InputImageType::Pointer loadAnyImageItk( std::string niiFullFilepathname ) {
    
    typedef itk::ImageFileReader<InputImageType> ReaderType;

    ReaderType::Pointer reader = ReaderType::New();
    reader->SetFileName(niiFullFilepathname);
    
    try {
        reader->Update();
    } catch (itk::ExceptionObject& e) {
        std::cerr << e.GetDescription() << std::endl;
        exit(1);  // You can choose to do something else, of course.
    }

    //InputImageType::Pointer inputImage = reader->GetOutput();
    InputImageType::Pointer inputImage = reader->GetOutput();
    
    return inputImage;

}									
											
int saveImageItk( std::string outputFullFilepathname, InputImageType::Pointer & outputImageItk) {

  typedef itk::ImageFileWriter< InputImageType >  Writer1Type;
  Writer1Type::Pointer writer1 = Writer1Type::New();

  writer1->SetInput( outputImageItk );
  writer1->SetFileName( outputFullFilepathname );
  //writer1->SetImageIO( itk::NiftiImageIO::New() ); //seems like this is useless.

  // Execution of the writer is triggered by invoking the \code{Update()} method.
  try
    {
    writer1->Update();
    }
  catch (itk::ExceptionObject & e)
    {
    std::cerr << "exception in file writer " << std::endl;
    std::cerr << e.GetDescription() << std::endl;
    std::cerr << e.GetLocation() << std::endl;
    return 1;
    }

  return 0;
}


int main( int argc, char* argv[]){
	// First command line argument: input mha file
	// Second command line argument: filename to give to output. Must be ending with .nii so that the conversion happens. Eg "./output1.nii"
	
	std::cout << "Reading Args.\n";
	std::string inputFullFilepathname = argv[1]; // "/vol/bitbucket/kk2412/data/BRATS2015_processed_training/HGG/brats_2013_pat0001_1/Flair.mha";
	std::string ouputFullFilepathname = argv[2]; // "/vol/bitbucket/kk2412/data/BRATS2015_processed_training/HGG/brats_2013_pat0001_1/Flair.nii";

	std::cout << "Input image: " << inputFullFilepathname << "\n";
	std::cout << "Output image: " << ouputFullFilepathname << "\n";

	InputImageType::Pointer inputImage;
	inputImage = loadAnyImageItk( inputFullFilepathname );
   
	saveImageItk( ouputFullFilepathname, inputImage);

	std::cout << "DONE.\n";
}
