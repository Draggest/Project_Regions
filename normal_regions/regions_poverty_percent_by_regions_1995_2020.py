import pandas as pd

if __name__ == '__main__':
    regions = pd.read_csv('data/normal_data/regions.csv',index_col=0)
    data = pd.read_csv('data/social_russia_data/poverty_percent_by_regions_1992_2020.csv')
    
    pivot_data = data.pivot_table('poverty_percent',index='region',columns='year').reset_index()
    pivot_data.rename({'region':'Region'},axis=1,inplace=True)
    pivot_data['Region'] = pivot_data['Region'].apply(lambda x: x.strip())
    for el in pivot_data.columns:
        pivot_data.rename({el:str(el).strip()},axis=1,inplace=True)
    
    pivot_data.loc[pivot_data[pivot_data['Region'] == 'Республика Адыгея (Адыгея)'].index[0],'Region'] = 'Республика Адыгея'
    pivot_data.loc[pivot_data[pivot_data['Region'] == 'Республика Северная Осетия-Алания'].index[0],'Region'] = 'Республика Северная Осетия - Алания'
    pivot_data.loc[pivot_data[pivot_data['Region'] == 'Республика Татарстан (Татарстан)'].index[0],'Region'] = 'Республика Татарстан'
    pivot_data.loc[pivot_data[pivot_data['Region'] == 'Город Москва столица Российской Федерации город федерального значения'].index[0],'Region'] = 'Москва'
    pivot_data.loc[pivot_data[pivot_data['Region'] == 'Город Санкт-Петербург город федерального значения'].index[0],'Region'] = 'Санкт-Петербург'
    pivot_data.loc[pivot_data[pivot_data['Region'] == 'Еврейская автономная область'].index[0],'Region'] = 'Еврейская АО'
    pivot_data.loc[pivot_data[pivot_data['Region'] == 'Ненецкий автономный округ (Архангельская область)'].index[0],'Region'] = 'Ненецкий АО'
    pivot_data.loc[pivot_data[pivot_data['Region'] == 'Ямало-Ненецкий автономный округ (Тюменская область)'].index[0],'Region'] = 'Ямало-Ненецкий АО'
    pivot_data.loc[pivot_data[pivot_data['Region'] == 'Ханты-Мансийский автономный округ - Югра (Тюменская область)'].index[0],'Region'] = 'Ханты-Мансийский АО - Югра'
    pivot_data.loc[pivot_data[pivot_data['Region'] == 'Чукотский автономный округ'].index[0],'Region'] = 'Чукотский АО'
    
    res = regions.merge(pivot_data,left_on='Region',right_on='Region',how='left')
    res.drop(['1992','1993','1994'],axis=1,inplace=True)
    
    res.to_csv('data/normal_data/poverty_percent_by_regions_1995_2020.csv')
