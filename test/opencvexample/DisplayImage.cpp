#include <stdio.h>
#include <opencv2/opencv.hpp>
using namespace cv;

int main(int argc, char** argv)
{
         if(argc!= 2)
         {
                            printf("usage:DisplayImage.out <Image_Path>\n");
                            return -1;
                  }

         Mat image;
         image= imread(argv[1], 1);

<span style="white-space:pre">    </span>if(!image.data)
<span style="white-space:pre">    </span>{
                   printf("Noimage data\n");
                   return -1;
         }

         namedWindow("DisplayImage",CV_WINDOW_AUTOSIZE);
         imshow("DisplayImage",image);

         waitKey(0);
         return 0;
}
