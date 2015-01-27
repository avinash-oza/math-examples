#include <iostream>
#include <cmath>
#include "lib/bisect.h"
#include "lib/bond_pv.h"

int main() {
//    std::cout << f_chpt5(-2.0) << std::endl;
//    std::cout << f_chpt5(3.0) << std::endl;
//  std::cout << BisectionMethod(-2.0,3.0,std::pow(10.0,-6.0),std::pow(10.0, -9.0)) << std::endl;
    std::cout << calculate_df(0.7, 3) << std::endl;
}
