# Преобразование таблицы disabled_total_by_age_2017_2022.csv к истинным субъектам РФ -> CSV , разибитие по годам

import pandas as pd

if __name__ == '__main__':
    regions = pd.read_csv('data/normal_data/regions.csv',index_col=0)
    data = pd.read_csv('data/social_russia_data/disabled_total_by_age_2017_2022.csv')
    
    data['date'] = pd.to_datetime(data['date'])
    data = data[(data['date'].dt.month == 1) & (data['date'].dt.day == 1)]
    data['date'] = data['date'].dt.year
    data.rename({'region':'Region'},axis=1,inplace=True)
    data.drop('total',axis=1,inplace=True)
    data.loc[data[data['Region'] == 'город Москва'].index[0],'Region'] = 'Москва'
    data.loc[data[data['Region'] == 'город Санкт-Петербург'].index[0],'Region'] = 'Санкт-Петербург'
    data.loc[data[data['Region'] == 'Республика Северная Осетия-Алания'].index[0],'Region'] = 'Республика Северная Осетия - Алания'
    data.loc[data[data['Region'] == 'Чувашская Республика'].index[0],'Region'] = 'Чувашская Республика - Чувашия'
    data.loc[data[data['Region'] == 'Кемеровская область'].index[0],'Region'] = 'Кемеровская область - Кузбасс'
    data.loc[data[data['Region'] == 'Еврейская автономная область'].index[0],'Region'] = 'Еврейская АО'
    data.loc[data[data['Region'] == 'Ненецкий автономный округ'].index[0],'Region'] = 'Ненецкий АО'
    data.loc[data[data['Region'] == 'Ямало-Ненецкий автономный округ'].index[0],'Region'] = 'Ямало-Ненецкий АО'
    data.loc[data[data['Region'] == 'Ханты-Мансийский автономный округ'].index[0],'Region'] = 'Ханты-Мансийский АО - Югра'
    data.loc[data[data['Region'] == 'Чукотский автономный округ'].index[0],'Region'] = 'Чукотский АО'
    
    regions.merge(data[data['date'] == 2017],left_on='Region',right_on='Region',how='left').to_csv('data/normal_data/disabled_total_by_age_2017.csv')
    regions.merge(data[data['date'] == 2018],left_on='Region',right_on='Region',how='left').to_csv('data/normal_data/disabled_total_by_age_2018.csv')
    regions.merge(data[data['date'] == 2019],left_on='Region',right_on='Region',how='left').to_csv('data/normal_data/disabled_total_by_age_2019.csv')
    regions.merge(data[data['date'] == 2020],left_on='Region',right_on='Region',how='left').to_csv('data/normal_data/disabled_total_by_age_2020.csv')
    regions.merge(data[data['date'] == 2021],left_on='Region',right_on='Region',how='left').to_csv('data/normal_data/disabled_total_by_age_2021.csv')
    regions.merge(data[data['date'] == 2022],left_on='Region',right_on='Region',how='left').to_csv('data/normal_data/disabled_total_by_age_2022.csv')