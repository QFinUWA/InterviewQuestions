import random
import math
import matplotlib.pyplot as plt
import numpy as np

density1 = lambda p: math.comb(10, 7)*(p**7)*(1-p)**3
density2 = lambda p: math.comb(100, 70)*(p**70)*(1-p)**30
N = 100000

def mcmc(density):
    samples = []
    last_proposal = 0.5
    for _ in range(N):
        proposal = random.random()

        alpha = density(proposal)/density(last_proposal)

        u = random.random()

        a = min(alpha, 1)

        if u < a:
            last_proposal = proposal
            samples.append(proposal)
        else:
            samples.append(last_proposal)
    return samples



if __name__ == "__main__":
    d1_results = mcmc(density1)
    d2_results = mcmc(density2)
    
    print(f"Trial 1 Mean: {np.mean(d1_results)}")
    print(f"Trial 2 Mean: {np.mean(d2_results)}")

    print(f"Trial 1 Median: {np.median(d1_results)}")
    print(f"Trial 2 Median: {np.median(d2_results)}")

    print(f"Trial 1 95% Confidence Interval: ({np.quantile(d1_results, 0.05)}, {np.quantile(d1_results, 0.95)})")
    print(f"Trial 1 95% Confidence Interval: ({np.quantile(d2_results, 0.05)}, {np.quantile(d2_results, 0.95)})")

    plt.hist(d1_results, bins=50, density=True, alpha=0.5, label="n=10, k=7")
    plt.hist(d2_results, bins=50, density=True, alpha=0.5, label="n=100, k=70")

    plt.legend()
    plt.xlabel("p")
    plt.ylabel("Density")
    plt.title("Overlapping MCMC Histograms")
    plt.show()