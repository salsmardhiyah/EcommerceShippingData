def chi2(df, col1, col2):    
    #---create the contingency table---
    df_crosstab= pd.crosstab(index = df[col1], columns = df[col2])
    
    #---calculate degree of freedom---
    degree_f = (df_crosstab.shape[0]-1) * (df_crosstab.shape[1]-1)
    
    #---sum up the totals for row and columns---
    df_crosstab.loc[:,'Total']= df_crosstab.sum(axis=1)
    df_crosstab.loc['Total']= df_crosstab.sum()
    
    #---create the expected value dataframe---
    df_exp = df_crosstab.copy()    
    df_exp.iloc[:,:] = np.multiply.outer(
        df_crosstab.sum(1).values,df_crosstab.sum().values) / df_crosstab.sum().sum()            
    
    # calculate chi-square values
    df_chi2 = ((df_crosstab - df_exp)**2) / df_exp    
    df_chi2.loc[:,'Total']= df_chi2.sum(axis=1)
    df_chi2.loc['Total']= df_chi2.sum()
    
    #---get chi-square score---   
    chi_square_score = df_chi2.iloc[:-1,:-1].sum().sum()
    
    #---calculate the p-value---
    from scipy import stats
    from scipy.stats import chi2
    alpha=0.05
    p = stats.distributions.chi2.sf(chi_square_score, degree_f)
    critical_value=chi2.ppf(q=1-alpha,df=degree_f)
    
    print ('chi_square:',chi_square_score)
    print ('critical_value:',critical_value)
    print ('Df:', degree_f)
    print ('p-value:',p)
    print ('alpha:',alpha)
    print ('')
    print ('**Kesimpulan**')
    if p<=alpha:
        print('Reject H0, There is a relationship between variable', col1, 'and Reached On Time (Target Variable)')
    else:
        print('Retain H0, There is no relationship between variable', col1, 'and Reached On Time (Target Variable)') 
    return chi_square_score