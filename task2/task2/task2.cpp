#include <iostream>
#include <vector>
#include <omp.h> 
#include <iomanip>
#include <numeric>


double f(double x) {
    return 4.0 / (1.0 + x * x);
}

double integrate_omp(int nsteps) {
    double h = 1.0 / nsteps;
    double sum = 0.0;
    
    #pragma omp parallel for reduction(+:sum)
    for (int i = 0; i < nsteps; ++i) {
        double x = (i + 0.5) * h;
        sum += f(x);
    }
    
    return sum * h;
}

int main() {
    int nsteps = 40000000;
    int threads[] = {1, 2, 4, 7, 8, 16, 20, 40};
    
    std::cout << "N,p,t,Sp" << std::endl;
    
    double t1 = 0.0;
    for (int th = 0; th < 8; th++) {
        int p = threads[th];
        omp_set_num_threads(p); 

        std::vector<double> times(10);
        for (int run = 0; run < 10; ++run) {
            double start = omp_get_wtime();
            double result = integrate_omp(nsteps);
            double end = omp_get_wtime();
            times[run] = end - start;
        }

        double avg_time = std::accumulate(times.begin(), times.end(), 0.0) / 10;
        if (p == 1) {
            t1 = avg_time;
        }
        double Sp = t1 / avg_time;
        
        std::cout << nsteps << "," << p << "," << avg_time << "," << Sp << std::endl;
    }
    
    return 0;
}