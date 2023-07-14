# Объединение таблиц regional_production_2005_2016.csv и regional_production_2017_2020.csv, преобразование к истинным субъектам РФ -> CSV 
import pandas as pd

if __name__ == '__main__':
    regions = pd.read_csv('data/normal_data/regions.csv',index_col=0)
    data1 = pd.read_csv('data/social_russia_data/regional_production_2005_2016.csv')
    data2 = pd.read_csv('data/social_russia_data/regional_production_2017_2020.csv')
    
    data1.rename({'region':'Region'},axis=1,inplace=True)
    data2.rename({'region':'Region'},axis=1,inplace=True)

    data1 = data1.groupby(by='Region',as_index=False).sum()
    data2 = data2.groupby(by='Region',as_index=False).sum()
    
    data1['Region'] = data1['Region'].apply(lambda x: x.strip())
    data1.loc[data1[data1['Region'] == 'Республика Адыгея (Адыгея)'].index[0],'Region'] = 'Республика Адыгея'
    data1.loc[data1[data1['Region'] == 'Республика Северная Осетия-Алания'].index[0],'Region'] = 'Республика Северная Осетия - Алания'
    data1.loc[data1[data1['Region'] == 'Республика Татарстан (Татарстан)'].index[0],'Region'] = 'Республика Татарстан'
    data1.loc[data1[data1['Region'] == 'Город Москва столица Российской Федерации город федерального значения'].index[0],'Region'] = 'Москва'
    data1.loc[data1[data1['Region'] == 'Город Санкт-Петербург город федерального значения'].index[0],'Region'] = 'Санкт-Петербург'
    data1.loc[data1[data1['Region'] == 'Еврейская автономная область'].index[0],'Region'] = 'Еврейская АО'
    data1.loc[data1[data1['Region'] == 'Ненецкий автономный округ (Архангельская область)'].index[0],'Region'] = 'Ненецкий АО'
    data1.loc[data1[data1['Region'] == 'Ямало-Ненецкий автономный округ (Тюменская область)'].index[0],'Region'] = 'Ямало-Ненецкий АО'
    data1.loc[data1[data1['Region'] == 'Ханты-Мансийский автономный округ - Югра (Тюменская область)'].index[0],'Region'] = 'Ханты-Мансийский АО - Югра'
    data1.loc[data1[data1['Region'] == 'Чукотский автономный округ'].index[0],'Region'] = 'Чукотский АО'

    data2['Region'] = data2['Region'].apply(lambda x: x.strip())
    data2.loc[data2[data2['Region'] == 'Республика Адыгея (Адыгея)'].index[0],'Region'] = 'Республика Адыгея'
    data2.loc[data2[data2['Region'] == 'Республика Северная Осетия-Алания'].index[0],'Region'] = 'Республика Северная Осетия - Алания'
    data2.loc[data2[data2['Region'] == 'Республика Татарстан (Татарстан)'].index[0],'Region'] = 'Республика Татарстан'
    data2.loc[data2[data2['Region'] == 'Город Москва столица Российской Федерации город федерального значения'].index[0],'Region'] = 'Москва'
    data2.loc[data2[data2['Region'] == 'Город Санкт-Петербург город федерального значения'].index[0],'Region'] = 'Санкт-Петербург'
    data2.loc[data2[data2['Region'] == 'Еврейская автономная область'].index[0],'Region'] = 'Еврейская АО'
    data2.loc[data2[data2['Region'] == 'Ненецкий автономный округ (Архангельская область)'].index[0],'Region'] = 'Ненецкий АО'
    data2.loc[data2[data2['Region'] == 'Ямало-Ненецкий автономный округ (Тюменская область)'].index[0],'Region'] = 'Ямало-Ненецкий АО'
    data2.loc[data2[data2['Region'] == 'Ханты-Мансийский автономный округ - Югра (Тюменская область)'].index[0],'Region'] = 'Ханты-Мансийский АО - Югра'
    data2.loc[data2[data2['Region'] == 'Чукотский автономный округ'].index[0],'Region'] = 'Чукотский АО'
        
    merge_data = data1.merge(data2,how='outer',left_on='Region',right_on='Region')
    regions.merge(merge_data,how='left',left_on='Region',right_on='Region').to_csv('data/normal_data/regional_production_2005_2020.csv')