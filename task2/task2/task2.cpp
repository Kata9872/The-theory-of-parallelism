#include <iostream>
#include <vector>
#include <omp.h> 
#include <iomanip>


double f(double x) {
    return 4.0 / (1.0 + x * x);
}

double integrate_omp(int nsteps, int num_threads) {
    double h = 1.0 / nsteps;
    double sum = 0.0;
    
    omp_set_num_threads(num_threads);
    #pragma omp parallel
    {
        double local_sum = 0.0;
        
        #pragma omp for
        for (int i = 0; i < nsteps; ++i) {
            double x = (i + 0.5) * h;
            local_sum += f(x);
        }
        #pragma omp atomic
        sum += local_sum;
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
        
        double start = omp_get_wtime();
        double result = integrate_omp(nsteps, p);
        double end = omp_get_wtime();
        double time = end - start;
        
        if (p == 1) {
            t1 = time;
        }
        double Sp = t1 / time;
        
        std::cout << nsteps << "," << p << "," << time << "," << Sp << std::endl;
    }
    
    return 0;
}