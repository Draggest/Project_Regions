# Преобразование таблицы population.xlsx к истинным субъектам РФ -> CSV
import pandas as pd
import re

if __name__ == '__main__':
    regions = pd.read_csv('data/normal_data/regions.csv',index_col=0)
    data = pd.read_excel('data/social_russia_data/population.xlsx',header=1)
    
    data.drop('Unnamed: 1',axis=1,inplace=True)
    data.rename({'Unnamed: 0':'Region'},axis=1,inplace=True)
    data.loc[data[data['Region'] == 'Город Москва столица Российской Федерации город федерального значения'].index[0],'Region'] = 'Москва'
    data.loc[data[data['Region'] == 'Республика Северная Осетия-Алания'].index[0],'Region'] = 'Республика Северная Осетия - Алания'
    data.loc[data[data['Region'] == 'Республика Татарстан (Татарстан)'].index[0],'Region'] = 'Республика Татарстан'
    data.loc[data[data['Region'] == 'Республика Адыгея (Адыгея)'].index[0],'Region'] = 'Республика Адыгея'
    data.loc[data[data['Region'] == 'Город Санкт-Петербург город федерального значения'].index[0],'Region'] = 'Санкт-Петербург'
    data.loc[data[data['Region'] == 'Еврейская автономная область'].index[0],'Region'] = 'Еврейская АО'
    data.loc[data[data['Region'] == 'Ненецкий автономный округ (Архангельская область)'].index[0],'Region'] = 'Ненецкий АО'
    data.loc[data[data['Region'] == 'Ямало-Ненецкий автономный округ (Тюменская область)'].index[0],'Region'] = 'Ямало-Ненецкий АО'
    data.loc[data[data['Region'] == 'Ханты-Мансийский автономный округ - Югра (Тюменская область)'].index[0],'Region'] = 'Ханты-Мансийский АО - Югра'
    data.loc[data[data['Region'] == 'Чукотский автономный округ'].index[0],'Region'] = 'Чукотский АО'
    
    res = []
    for el in data['Region']:
        if el.strip() in list(regions['Region']):
            res.append(data[data['Region'] == el].index[0])
    next_index_res = []
    for i in range(len(res)):
        next_index_res.append(res[i]+1)
    
    series_region = data.loc[res]['Region']
    series_region = series_region.reset_index()
    series_region.drop('index',axis=1,inplace=True)
    
    data_w_reg = data.drop('Region',axis=1)
    data_new = data_w_reg.loc[next_index_res]
    data_new = data_new.reset_index()
    data_new.drop('index',axis=1,inplace=True)
    
    merge_data = series_region.join(data_new)
    
    test_data = regions.merge(merge_data,left_on='Region',right_on='Region',how='left')
    for el in test_data.columns[1:]:
        test_data.rename({el:''.join(re.findall('[0-9]',el))},axis=1,inplace=True)
    
    test_data.to_csv('data/normal_data/population.csv')