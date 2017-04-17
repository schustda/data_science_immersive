import numpy as np
import pandas as pd
import scipy.stats as scs

if __name__ == '__main__':
    data = []
    # make observed data table
    columns = ['race','dp_y','dp_n']
    data.append(['White', 45, 85])
    data.append(['Black', 14, 218])
    df = pd.DataFrame(data = data, columns = columns)
    df.set_index(df['race'],inplace = True)
    del df['race']
    # print("Observed data")
    # print(df)


    # calculate row and column totals
    # print("\nFinding expected values")
    nrow, ncol = df.shape[0], df.shape[1] # number of rows and columns
    # grand total of all four squares. First sums the rows then the columns
    GT = df.sum().sum()
    # iterates through each row and returns the sum to the array
    df_row_tot = sum(df.iloc[:,i] for i in range(1))
    df_col_tot = sum(df.iloc[i,:] for i in range(ncol))
    # print("\nrow totals:")
    # print(df_row_tot)
    # print("\ncolumn totals:")
    # print(df_col_tot)

    # # make expected value table
    GT = df.sum().sum()
    E = np.zeros((nrow, ncol))
    for i in range(nrow):
        for j in range(ncol):
            E[i,j] = round(df_row_tot[i]*df_col_tot[j] / GT, 2)
    print('\nExpected values\n{0}'.format(E))
    #
    # chi2 = 0
    # for i in range(nrow):
    #     for j in range(ncol):
    #         chi2 += ((df.iloc[i,j] - E[i,j])**2/E[i, j])
    # print("\nThe chi-square value is {0:0.2f}".format(chi2))
    #
    # ddof = (nrow-1) * (ncol - 1)
    # print("\nThe degrees of freedom are {0}".format(ddof))
    #
    # print("\nUpon looking at the chisquare table, our value of p is very, very low.")
    # print("So p << alpha, we can reject null hypothesis and conclude there is a")
    # print("relationship between fitness level and smoking habits.")
    #
    # print("Scipy stats give us very low values too (but much easier):")
    # print(scs.chisquare(df.values))
    #
