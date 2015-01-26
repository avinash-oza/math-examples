#include "bond_pv.h"

double calculate_df(double r, double t) {
    double result = exp(-1.0*r*t);
    return result;
}

int main() {
    double r = calculate_df(0.5,0.7);
    std::cout << r << std::endl;
}
