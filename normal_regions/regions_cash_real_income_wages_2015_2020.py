# # Преобразование таблицы cash_real_income_wages_2015_2020.xlsx к истинным субъектам РФ -> CSV (cash_income + wages)

import pandas as pd

if __name__ == '__main__':
    regions = pd.read_csv('data/normal_data/regions.csv',index_col=0)
    data1 = pd.read_excel('data/social_russia_data/cash_real_income_wages_2015_2020.xlsx')
    data2 = pd.read_excel('data/social_russia_data/cash_real_income_wages_2015_2020.xlsx',sheet_name='formal_wage_paid')
    
    data1.rename({'region':'Region'},axis=1,inplace=True)
    for el in data1.columns:
        if type(el) == float:
            data1.rename({el:'cash_income_'+str(int(el))},axis=1,inplace=True)
    
    data2.rename({'region':'Region'},axis=1,inplace=True)
    for el in data2.columns:
        if type(el) == float:
            data2.rename({el:'wage_paid_'+str(int(el))},axis=1,inplace=True)
            
    list_to_change = [data1,data2]
    for el in list_to_change:
        el.loc[el[el['Region'] == 'г. Москва'].index[0],'Region'] = 'Москва'
        el.loc[el[el['Region'] == 'Кабардино-Балкарская\nРеспублика'].index[0],'Region'] = 'Кабардино-Балкарская Республика'
        el.loc[el[el['Region'] == 'Карачаево-Черкесская\nРеспублика'].index[0],'Region'] = 'Карачаево-Черкесская Республика'
        el.loc[el[el['Region'] == 'Республика Северная\nОсетия-Алания'].index[0],'Region'] = 'Республика Северная Осетия - Алания'
        el.loc[el[el['Region'] == 'Чувашская Республика'].index[0],'Region'] = 'Чувашская Республика - Чувашия'
        el.loc[el[el['Region'] == 'Кемеровская область'].index[0],'Region'] = 'Кемеровская область - Кузбасс'
        el.loc[el[el['Region'] == 'г. Санкт-Петербург'].index[0],'Region'] = 'Санкт-Петербург'
        el.loc[el[el['Region'] == 'Еврейская автономная область'].index[0],'Region'] = 'Еврейская АО'
        el.loc[el[el['Region'] == 'Ненецкий автономный округ'].index[0],'Region'] = 'Ненецкий АО'
        el.loc[el[el['Region'] == 'Ямало-Ненецкий \nавтономный округ'].index[0],'Region'] = 'Ямало-Ненецкий АО'
        el.loc[el[el['Region'] == 'Ханты-Мансийский \nавтономный округ - Югра'].index[0],'Region'] = 'Ханты-Мансийский АО - Югра'
        el.loc[el[el['Region'] == 'Чукотский автономный округ'].index[0],'Region'] = 'Чукотский АО'
        
    merge_data = data1.merge(data2,left_on='Region',right_on='Region',how='inner')
    
    regions.merge(merge_data,left_on='Region',right_on='Region',how='left').to_csv('data/normal_data/cash_income_wages_2015_2020.csv')