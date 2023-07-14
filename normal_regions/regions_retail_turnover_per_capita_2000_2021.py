# Преобразование таблицы retail_turnover_per_capita_2000_2021.xls к истинным субъектам РФ -> CSV 
import pandas as pd

if __name__ == '__main__':
    regions = pd.read_csv('data/normal_data/regions.csv',index_col=0)
    data = pd.read_excel('data/social_russia_data/retail_turnover_per_capita_2000_2021.xls',header=2)
    
    data.rename({'Unnamed: 0':'Region'},axis=1,inplace=True)
    data.drop('Unnamed: 1',axis=1,inplace=True)
    data.drop(0,inplace=True)
    data['Region'] = data['Region'].apply(lambda x: x.strip())
    data.loc[data[data['Region'] == 'Республика Адыгея (Адыгея)'].index[0],'Region'] = 'Республика Адыгея'
    data.loc[data[data['Region'] == 'Республика Северная Осетия-Алания'].index[0],'Region'] = 'Республика Северная Осетия - Алания'
    data.loc[data[data['Region'] == 'Республика Татарстан (Татарстан)'].index[0],'Region'] = 'Республика Татарстан'
    data.loc[data[data['Region'] == 'Город Москва столица Российской Федерации город федерального значения'].index[0],'Region'] = 'Москва'
    data.loc[data[data['Region'] == 'Город Санкт-Петербург город федерального значения'].index[0],'Region'] = 'Санкт-Петербург'
    data.loc[data[data['Region'] == 'Еврейская автономная область'].index[0],'Region'] = 'Еврейская АО'
    data.loc[data[data['Region'] == 'Ненецкий автономный округ (Архангельская область)'].index[0],'Region'] = 'Ненецкий АО'
    data.loc[data[data['Region'] == 'Ямало-Ненецкий автономный округ (Тюменская область)'].index[0],'Region'] = 'Ямало-Ненецкий АО'
    data.loc[data[data['Region'] == 'Ханты-Мансийский автономный округ - Югра (Тюменская область)'].index[0],'Region'] = 'Ханты-Мансийский АО - Югра'
    data.loc[data[data['Region'] == 'Чукотский автономный округ'].index[0],'Region'] = 'Чукотский АО'
    
    regions.merge(data,how='left',left_on='Region',right_on='Region').to_csv('data/normal_data/retail_turnover_per_capita_2000_2021.csv')