# Создание датасетов 2015-2020
import pandas as pd

if __name__ == '__main__':
    data_child_mortality_rural = pd.read_csv('data/normal_data/child_mortality_rural_1990_2021.csv',index_col=0)
    data_poverty_percent = pd.read_csv('data/normal_data/poverty_percent_by_regions_1995_2020.csv',index_col=0)
    data_welfare_expense_share = pd.read_csv('data/normal_data/welfare_expense_share_2015_2020.csv',index_col=0)
    data_cash_real_income_wages = pd.read_csv('data/normal_data/cash_income_wages_2015_2020.csv',index_col=0)
    data_population = pd.read_csv('data/normal_data/population.csv',index_col=0)
    data_gross_regional_product = pd.read_csv('data/normal_data/gross_regional_product_1996_2020.csv',index_col=0)
    data_regional_production = pd.read_csv('data/normal_data/regional_production_2005_2020.csv',index_col=0)
    data_retail_turnover_per_capita = pd.read_csv('data/normal_data/retail_turnover_per_capita_2000_2021.csv',index_col=0)
    
    
    for year in range(2015,2021):
        main_data = data_child_mortality_rural[['Region',str(year)]]
        main_data.rename({str(year):'child_mortality_rural'},axis=1,inplace=True)

        main_data = main_data.merge(data_poverty_percent[['Region',str(year)]],left_on='Region',right_on='Region',how='left')
        main_data.rename({str(year):'poverty_percent'},axis=1,inplace=True)
        
        main_data = main_data.merge(data_welfare_expense_share[['Region',str(year)]],left_on='Region',right_on='Region',how='left')
        main_data.rename({str(year):'welfare_expense_share'},axis=1,inplace=True)

        ci_str = 'cash_income_'+str(year)
        main_data = main_data.merge(data_cash_real_income_wages[['Region',ci_str]],left_on='Region',right_on='Region',how='left')
        main_data.rename({ci_str:'cash_income'},axis=1,inplace=True)

        main_data = main_data.merge(data_population[['Region',str(year)]],left_on='Region',right_on='Region',how='left')
        main_data.rename({str(year):'population'},axis=1,inplace=True)

        main_data = main_data.merge(data_gross_regional_product[['Region',str(year)]],left_on='Region',right_on='Region',how='left')
        main_data.rename({str(year):'gross_regional_product'},axis=1,inplace=True)

        main_data = main_data.merge(data_regional_production[['Region',str(year)]],left_on='Region',right_on='Region',how='left')
        main_data.rename({str(year):'regional_production'},axis=1,inplace=True)

        main_data = main_data.merge(data_retail_turnover_per_capita[['Region',str(year)]],left_on='Region',right_on='Region',how='left')
        main_data.rename({str(year):'retail_turnover_per_capita'},axis=1,inplace=True)
        

        str_to_save ='data/summary_data/'+str(year)+'.csv'
        main_data.to_csv(str_to_save)