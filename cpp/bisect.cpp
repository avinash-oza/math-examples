#include <iostream>
#include <stdlib.h>
//#include <math.h>
#include <unistd.h>
#include <cmath>
#include "bisect.h"

double f_chpt5(double x)
{
    return std::pow(x,4.0) - 5.0*x*x + 4.0 - 1.0/(1.0 + exp(x*x*x));
}

double BisectionMethod(double a, double b, double tol_int, double tol_approx)
{
    std::cout << tol_int << " " << tol_approx << std::endl;
    double Xm = 0;
    double Xl = a;
    double Xr = b;
    while (std::max(std::abs(f_chpt5(Xl)), std::abs(f_chpt5(Xr))) > tol_approx || (Xr - Xl) > tol_int)
    {      
        Xm = (Xl + Xr) / 2.0;
        if ((f_chpt5(Xl) * f_chpt5(Xr)) < 0) {
            Xr = Xm;
//          std::cout << "Left ";
        }
        else {
            Xl = Xm;
//          std::cout << "Right ";
        }

//      std::cout << "Xl: " << f_chpt5(Xl) << " Xr: " << f_chpt5(Xr) << " Xm: " <<Xm << std::endl;
//      std::cout <<"Max " << std::max(std::abs(f_chpt5(Xl)), std::abs(f_chpt5(Xr))) << std::endl;
//      std::cout << "Diff:" << (Xr - Xl) << " " << (bool) ((Xr-Xl) > tol_int) << std::endl;
        std::cout << Xm << std::endl;
        usleep(100000.0*1);
    }  
    return Xm;
}

int main() {
//    std::cout << f_chpt5(-2.0) << std::endl;
//    std::cout << f_chpt5(3.0) << std::endl;
    std::cout << BisectionMethod(-2.0,3.0,std::pow(10.0,-6.0),std::pow(10.0, -9.0)) << std::endl;
}
