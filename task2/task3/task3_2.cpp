#include <iostream>
#include <vector>
#include <cmath>
#include <omp.h>
#include <iomanip>
#include <numeric>
#include <utility>

void solve_slae_omp(int N, double tau, double eps, int num_threads, std::vector<double>& x, int& iterations) {

    std::vector<double> A(N * N);
    std::vector<double> b(N);
    
    #pragma omp parallel for
    for (int i = 0; i < N * N; ++i) A[i] = 1.0;
    #pragma omp parallel for
    for (int i = 0; i < N; ++i) {
        A[i * N + i] = 2.0;
        b[i] = N + 1;
    }
    
    std::vector<double> r(N);
    std::vector<double> x_new(N);
    
    iterations = 0;
    double norm = 1.0;
    
    #pragma omp parallel
    {
        while (norm > eps) {
            #pragma omp for schedule(static)
            for (int i = 0; i < N; ++i) {
                double sum = 0.0;
                for (int j = 0; j < N; ++j) {
                    sum += A[i * N + j] * x[j];
                }
                r[i] = sum - b[i];
            }
            #pragma omp for schedule(static)
            for (int i = 0; i < N; ++i) {
                x_new[i] = x[i] - tau * r[i];
            }
            double local_norm = 0.0;
            #pragma omp for reduction(+:local_norm) schedule(static)
            for (int i = 0; i < N; ++i) {
                local_norm += r[i] * r[i];
            }
            #pragma omp single
            {
                norm = std::sqrt(local_norm);
                iterations++;
            }
            #pragma omp single
            {
                std::swap(x, x_new);
            }
        }
    }
}

int main() {
    int N = 12000;
    double tau = 1.0 / (N + 1.0); 
    double eps = 1e-5;
    
    int threads[] = {1, 2, 4, 7, 8, 16, 20, 40};
    
    std::cout << "N,p,t,Sp,Iter" << std::endl;
    
    double t1 = 0.0;
    
    for (int th = 0; th < 8; th++) {
        int p = threads[th];
        omp_set_num_threads(p);
        
        std::vector<double> times(10);
        int iterations = 0;
        
        for (int run = 0; run < 10; ++run) {
            std::vector<double> x(N, 0.0);
            
            double start = omp_get_wtime();
            solve_slae_omp(N, tau, eps, p, x, iterations);
            double end = omp_get_wtime();
            
            times[run] = end - start;
        }
        
        double avg_time = std::accumulate(times.begin(), times.end(), 0.0) / 10;
        
        if (p == 1) t1 = avg_time;
        double Sp = t1 / avg_time;
        
        std::cout << N << "," << p << "," 
                  << std::fixed << avg_time << "," << Sp << "," << iterations << std::endl;
    }
    
    return 0;
}