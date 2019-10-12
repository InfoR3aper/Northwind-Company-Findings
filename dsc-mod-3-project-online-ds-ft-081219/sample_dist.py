# Sampling With Replacement
import numpy as np

def get_sample(data, n):
    sample = []
    while len(sample) != n:
        x = np.random.choice(data)
        sample.append(x)
    return sample

# Generating a Sample Mean
def get_sample_mean(sample):
    return sum(sample)/len(sample)

# Creating a Sample Distribution of Sample Means
def create_sample_distribution(data, dist_size=100, n=30):
    sample_dist = [] 
    while len(sample_dist) != dist_size:
        sample = get_sample(data, n)
        sample_mean = get_sample_mean(sample)
        sample_dist.append(sample_mean)
    return sample_dist