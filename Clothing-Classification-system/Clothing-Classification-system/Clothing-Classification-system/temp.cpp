#include "opencv2/opencv.hpp"

using namespace cv;

int main(int, char**)
{
    CvCapture* capture = cvCaptureFromCAM(1); //Capture using any camera connected to your system
    cvNamedWindow("Camera_Output",1);
    for(;;)
    {
		IplImage* imageIn = cvQueryFrame(capture); //Create image frames from capture
		cvShowImage("Camera_Output", imageIn); //Show image frames on created window
		//imshow("Camera_Output", imageIn);
        if(waitKey(30) >= 0) break;
    }
    // the camera will be deinitialized automatically in VideoCapture destructor
    return 0;
}
