#include <iostream>
#include <vector>
#include <omp.h> 
#include <iomanip> 
#include <numeric>


int main(){

    int sizes[] = {20000, 40000};
    int threads[] = {1,2,4,7,8,16,20,40};

    std::cout << "N,p,t,Sp" << std::endl;

    for (int n = 0; n < 2; n++){
        int N = sizes[n];
        double t1 = 0;

        for (int th = 0; th < 8; th++){
            int p = threads[th];
            omp_set_num_threads(p);
            std::vector<double> times(10);

            for (int run = 0; run < 10; ++run) {
                std::vector<double> A(N*N);
                std::vector<double> X(N);
                std::vector<double> Y(N, 0.0);

                #pragma omp parallel
                {
                    #pragma omp for
                    for (int i = 0; i < N*N; ++i){
                        A[i] = 1.0;
                    }
                    #pragma omp for
                    for (int i = 0; i < N; ++i){
                        X[i] = 1.0;
                    }

                    double start = omp_get_wtime();
                    #pragma omp for
                    for (int i = 0; i < N; ++i){
                        double sum = 0.0;
                        for (int j = 0; j < N; ++j){
                            sum += A[i*N+j] * X[j];
                        }
                        Y[i] = sum;
                    }
                    double end = omp_get_wtime();
                    
                    #pragma omp single
                    times[run] = end - start;
                }
            }
            double avg_time = std::accumulate(times.begin(), times.end(), 0.0) / 10;
            
            if (p == 1){
                t1 = avg_time;
            }
            double Sp = t1/avg_time;

            std::cout << N << "," << p << "," 
            << avg_time << "," << Sp << std::endl;
        }
    }
    return 0;
}