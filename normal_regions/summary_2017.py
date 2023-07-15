# Создание итогового датасета по 2107 году из преобразованных данных
import pandas as pd

if __name__ == '__main__':
    data_child_mortality_rural = pd.read_csv('data/normal_data/child_mortality_rural_1990_2021.csv',index_col=0)
    data_child_mortality_urban = pd.read_csv('data/normal_data/child_mortality_urban_1990_2021.csv',index_col=0)
    data_disabled_total_by_age = pd.read_csv('data/normal_data/disabled_total_by_age_2017.csv',index_col=0)
    data_poverty_percent = pd.read_csv('data/normal_data/poverty_percent_by_regions_1995_2020.csv',index_col=0)
    data_welfare_expense_share = pd.read_csv('data/normal_data/welfare_expense_share_2015_2020.csv',index_col=0)
    data_cash_real_income_wages = pd.read_csv('data/normal_data/cash_income_wages_2015_2020.csv',index_col=0)
    data_population = pd.read_csv('data/normal_data/population.csv',index_col=0)
    data_gross_regional_product = pd.read_csv('data/normal_data/gross_regional_product_1996_2020.csv',index_col=0)
    data_regional_production = pd.read_csv('data/normal_data/regional_production_2005_2020.csv',index_col=0)
    data_retail_turnover_per_capita = pd.read_csv('data/normal_data/retail_turnover_per_capita_2000_2021.csv',index_col=0)
    data_alco = pd.read_csv('data/normal_data/alco_2005_2018.csv',index_col=0)
    data_drugs = pd.read_csv('data/normal_data/drugs_2005_2018.csv',index_col=0)
    data_newborn = pd.read_csv('data/normal_data/newborn_2006_2022.csv',index_col=0)
    
    main_data_2017 = data_child_mortality_rural[['Region','2017']]
    main_data_2017.rename({'2017':'child_mortality_rural'},axis=1,inplace=True)

    main_data_2017 = main_data_2017.merge(data_child_mortality_urban[['Region','2017']],left_on='Region',right_on='Region',how='left')
    main_data_2017.rename({'2017':'child_mortality_urban'},axis=1,inplace=True)

    main_data_2017 = main_data_2017.merge(data_disabled_total_by_age.drop('date',axis=1),left_on='Region',right_on='Region',how='left')

    main_data_2017 = main_data_2017.merge(data_poverty_percent[['Region','2017']],left_on='Region',right_on='Region',how='left')
    main_data_2017.rename({'2017':'poverty_percent'},axis=1,inplace=True)

    main_data_2017 = main_data_2017.merge(data_welfare_expense_share[['Region','2017']],left_on='Region',right_on='Region',how='left')
    main_data_2017.rename({'2017':'welfare_expense_share'},axis=1,inplace=True)

    main_data_2017 = main_data_2017.merge(data_cash_real_income_wages[['Region','cash_income_2017','wage_paid_2017']],left_on='Region',right_on='Region',how='left')

    main_data_2017 = main_data_2017.merge(data_population[['Region','2017']],left_on='Region',right_on='Region',how='left')
    main_data_2017.rename({'2017':'population'},axis=1,inplace=True)

    main_data_2017 = main_data_2017.merge(data_gross_regional_product[['Region','2017']],left_on='Region',right_on='Region',how='left')
    main_data_2017.rename({'2017':'gross_regional_product'},axis=1,inplace=True)

    main_data_2017 = main_data_2017.merge(data_regional_production[['Region','2017']],left_on='Region',right_on='Region',how='left')
    main_data_2017.rename({'2017':'regional_production'},axis=1,inplace=True)

    main_data_2017 = main_data_2017.merge(data_retail_turnover_per_capita[['Region','2017']],left_on='Region',right_on='Region',how='left')
    main_data_2017.rename({'2017':'retail_turnover_per_capita'},axis=1,inplace=True)

    main_data_2017 = main_data_2017.merge(data_alco[['Region','2017']],left_on='Region',right_on='Region',how='left')
    main_data_2017.rename({'2017':'alco'},axis=1,inplace=True)

    main_data_2017 = main_data_2017.merge(data_drugs[['Region','2017']],left_on='Region',right_on='Region',how='left')
    main_data_2017.rename({'2017':'drugs'},axis=1,inplace=True)

    main_data_2017 = main_data_2017.merge(data_newborn[['Region','2017']],left_on='Region',right_on='Region',how='left')
    main_data_2017.rename({'2017':'newborn'},axis=1,inplace=True)
    
    main_data_2017.to_csv('data/summary_data/2017.csv')