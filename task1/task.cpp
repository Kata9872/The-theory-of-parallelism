#include <iostream>
#include <cmath>
#include <vector>

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
    vector<T> values(n);

    for (int i = 0; i < n; ++i){
        values[i] = sin(i*2*pi/n);
    }
    for (const auto& value : values) {
        res+= value;
    }

    cout << res << endl;
    return 0;
}
