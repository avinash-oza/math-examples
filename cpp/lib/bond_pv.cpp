#include "bond_pv.h"

double calculate_df(double r, double t) {
    double result = exp(-1.0*r*t);
    return result;
}

