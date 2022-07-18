#include <iostream>
#include <Eigen/Dense>

using namespace std;

using Eigen::Matrix2d;
using Eigen::Matrix3d;
using Eigen::Vector3d;


int main()
{
    Matrix2d m;
    m(0,0) = 3; m(1,0) = 2.5; m(0,1)= -1; m(1,1) = m(1,0) + m(0,1);
    std::cout << m << std::endl;

    Matrix3d m3 = Matrix3d::Random();
    m3 = (m3 + Matrix3d::Constant(1.2)) * 50;
    std::cout << "m3 = " << std::endl << m3 << std::endl;

    Vector3d v3(1,2,3);
    std::cout << "m3 * v3 = " << std::endl << m3 * v3 << endl;

    v3 << 2, 4, 6;
    cout << v3 << endl;
    std::cout << "m3 * v3 = " << std::endl << m3 * v3 << endl;
}