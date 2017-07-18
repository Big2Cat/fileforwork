#include<opencv2/core/core.hpp>

#include<opencv2/highgui/highgui.hpp>

int main()

{

    cv::Mat image;

    image=cv::imread("1.jpg");


    cv::imshow("example",image);

    cv::waitKey(5000);

    return 0;

}
