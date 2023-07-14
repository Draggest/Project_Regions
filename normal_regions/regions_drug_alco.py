# Объединение листов alco из тамблицы drug_alco.xlsx, преобразование к истинным субъектам -> CSV 
import pandas as pd

if __name__ == '__main__':
    regions = pd.read_csv('data/normal_data/regions.csv',index_col=0)
    data = pd.read_excel('data/social_russia_data/drug_alco.xlsx')
    data2 = pd.read_excel('data/social_russia_data/drug_alco.xlsx',sheet_name='alco1718')
    
    data.rename({'region':'Region'},axis=1,inplace=True)
    data['Region'] = data['Region'].apply(lambda x: x.strip())
    for el in data.columns:
        if type(el) == float:
            data.rename({el:str(int(el))},axis=1,inplace=True)
    data.loc[data[data['Region'] == 'Республика Адыгея (Адыгея) (до 03.06.2014)'].index[0],'Region'] = 'Республика Адыгея'
    data.loc[data[data['Region'] == 'Республика Северная Осетия-Алания'].index[0],'Region'] = 'Республика Северная Осетия - Алания'
    data.loc[data[data['Region'] == 'Республика Татарстан (Татарстан)'].index[0],'Region'] = 'Республика Татарстан'
    data.loc[data[data['Region'] == 'Кемеровская область'].index[0],'Region'] = 'Кемеровская область - Кузбасс'
    data.loc[data[data['Region'] == 'г. Москва'].index[0],'Region'] = 'Москва'
    data.loc[data[data['Region'] == 'г. Санкт-Петербург'].index[0],'Region'] = 'Санкт-Петербург'
    data.loc[data[data['Region'] == 'Еврейская автономная область'].index[0],'Region'] = 'Еврейская АО'
    data.loc[data[data['Region'] == 'Ненецкий автономный округ (Архангельская область)'].index[0],'Region'] = 'Ненецкий АО'
    data.loc[data[data['Region'] == 'Ямало-Ненецкий автономный округ (Тюменская область)'].index[0],'Region'] = 'Ямало-Ненецкий АО'
    data.loc[data[data['Region'] == 'Ханты-Мансийский автономный округ - Югра (Тюменская область)'].index[0],'Region'] = 'Ханты-Мансийский АО - Югра'
    data.loc[data[data['Region'] == 'Чукотский автономный округ'].index[0],'Region'] = 'Чукотский АО'
    
    data2.rename({'region':'Region'},axis=1,inplace=True)
    data2['Region'] = data2['Region'].apply(lambda x: x.strip())
    for el in data2.columns:
        if type(el) == float:
            data2.rename({el:str(int(el))},axis=1,inplace=True)
    data2.loc[data2[data2['Region'] == 'Чувашская Республика'].index[0],'Region'] = 'Чувашская Республика - Чувашия'
    data2.loc[data2[data2['Region'] == 'Архангельская область без автономного округа'].index[0],'Region'] = 'Архангельская область'
    data2.loc[data2[data2['Region'] == 'Кемеровская область'].index[0],'Region'] = 'Кемеровская область - Кузбасс'
    data2.loc[data2[data2['Region'] == 'Тюменская область без автономного округа'].index[0],'Region'] = 'Тюменская область'
    data2.loc[data2[data2['Region'] == 'город Москва'].index[0],'Region'] = 'Москва'
    data2.loc[data2[data2['Region'] == 'город Санкт - Петербург'].index[0],'Region'] = 'Санкт-Петербург'
    data2.loc[data2[data2['Region'] == 'Еврейская автономная область'].index[0],'Region'] = 'Еврейская АО'
    data2.loc[data2[data2['Region'] == 'Ненецкий автономный округ'].index[0],'Region'] = 'Ненецкий АО'
    data2.loc[data2[data2['Region'] == 'Ямало-Hенецкий АО'].index[0],'Region'] = 'Ямало-Ненецкий АО'
    data2.loc[data2[data2['Region'] == 'Ханты-Мансийский АО'].index[0],'Region'] = 'Ханты-Мансийский АО - Югра'
    data2.loc[data2[data2['Region'] == 'Чукотский автономный округ'].index[0],'Region'] = 'Чукотский АО'
    
    test_data = regions.merge(data,how='left',left_on='Region',right_on='Region')
    test_data.merge(data2,how='left',left_on='Region',right_on='Region').to_csv('data/normal_data/alco_2005_2018.csv')