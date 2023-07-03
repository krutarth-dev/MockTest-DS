from scipy import stats

def perform_hypothesis_test(sample1, sample2):
    t_statistic, p_value = stats.ttest_ind(sample1, sample2)
    return p_value
sample1 = [12, 15, 18, 21, 24]
sample2 = [8, 12, 16, 20, 24]
p_value = perform_hypothesis_test(sample1, sample2)
print("P-value:", p_value)
