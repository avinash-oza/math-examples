#include <limits.h>
#include <cmath>
#include "gtest/gtest.h"
#include "bond_pv.h"

TEST(BondPV, test_calculate_df){
    ASSERT_LT(calculate_df(2, 3) - 0.00247875217, std::pow(10, -9));
}
