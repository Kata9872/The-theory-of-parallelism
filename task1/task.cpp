#include <iostream>
#include <cmath>

using namespace std;

int main() {
    #ifdef USE_FLOAT
    using T = float;
    const T pi = 3.141593;
#else
    using T = double;
    const T pi = 3.141593;
#endif

    const int n = 10000000;
    T res = 0;

    for (int i = 0; i < n; ++i){
        res += sin(i*2*pi/n);
    }

    cout << res << endl;
    return 0;
}
