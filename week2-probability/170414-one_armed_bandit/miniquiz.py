import pandas as pd
import scipy.stats as scs
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('data/pages.csv')
# df.set_index(df['page'])
# df.drop(page)
df.set_index(df['page'],inplace = True)
del df['page']
# H0: The different pages do not have any effect
df['mean_rpv'] = df['registrations']/df['visitors']
# Ha: The different pages have an effect
df['variance_rpv'] = df['mean_rpv'] * (1 - df['mean_rpv'])
df['standard_error'] = (df['variance_rpv']/df['visitors'])**2

norm1 = scs.norm(df['mean_rpv'][0],df['standard_error'][0])

#plotting

fig = plt.figure()
ax = plt.subplot(1,1,1)
x = np.linspace(scs.norm.mean() - 4* scs.norm.std(),scs.norm.mean() + 4* scs.norm.std())

# ax.plot(x,dqnorm1(x))
plt.show



# def z_test(ctr_old, ctr_new, nobs_old, nobs_new,
#            effect_size=0., two_tailed=True, alpha=.05):
#
#     """Perform z-test to compare two proprtions (e.g., click through rates (ctr)).
#
#         Note: if you set two_tailed=False, z_test assumes H_A is that the effect is
#         non-negative, so the p-value is computed based on the weight in the upper tail.
#
#         Arguments:
#             ctr_old (float):    baseline proportion (ctr)
#             ctr_new (float):    new proportion
#             nobs_old (int):     number of observations in baseline sample
#             nobs_new (int):     number of observations in new sample
#             effect_size (float):    size of effect
#             two_tailed (bool):  True to use two-tailed test; False to use one-sided test
#                                 where alternative hypothesis if that effect_size is non-negative
#             alpha (float):      significance level
#
#         Returns:
#             z-score, p-value, and whether to reject the null hypothesis
#     """
#     conversion = (ctr_old * nobs_old + ctr_new * nobs_new) / \
#                  (nobs_old + nobs_new)
#
#     se = sqrt(conversion * (1 - conversion) * (1 / nobs_old + 1 / nobs_new))
#
#     z_score = (ctr_new - ctr_old - effect_size) / se
#
#     if two_tailed:
#         p_val = (1 - scs.norm.cdf(abs(z_score))) * 2
#     else:
#         # Because H_A: estimated effect_size > effect_size
#         p_val = 1 - scs.norm.cdf(z_score)
#
#     reject_null = p_val < alpha
#     print 'z-score: %s, p-value: %s, reject null: %s' % (z_score, p_val, reject_null)
#     return z_score, p_val, reject_null
