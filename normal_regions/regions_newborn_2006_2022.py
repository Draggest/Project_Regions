# Преобразование таблицы newborn_2006_2022_monthly.csv к истинным субъектам РФ по годам -> CSV
import pandas as pd

if __name__ == '__main__':
    regions = pd.read_csv('data/normal_data/regions.csv',index_col=0)
    data = pd.read_csv('data/social_russia_data/newborn_2006_2022_monthly.csv', sep=';')
    
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
    data.drop('Unnamed: 198',axis=1,inplace=True)
    
    test_data = regions.merge(data,how='left',left_on='Region',right_on='Region')
    
    for el in test_data.columns[1:]:
        test_data[el] = test_data[el].apply(lambda x: x.replace(',','.'))
        test_data[el] = test_data[el].astype(float).astype(int)
        
    for i in range(2006,2022):
        test_data[str(i)] = test_data[test_data.columns[1]] + test_data[test_data.columns[2]] + test_data[test_data.columns[3]] + test_data[test_data.columns[4]] + test_data[test_data.columns[5]] \
        + test_data[test_data.columns[6]] + test_data[test_data.columns[7]] + test_data[test_data.columns[8]] + test_data[test_data.columns[9]] + test_data[test_data.columns[10]]\
            + test_data[test_data.columns[11]] + test_data[test_data.columns[12]] 
        test_data.drop([test_data.columns[1],test_data.columns[2],test_data.columns[3],test_data.columns[4],test_data.columns[5],test_data.columns[6],test_data.columns[7],\
            test_data.columns[8],test_data.columns[9],test_data.columns[10],test_data.columns[11],test_data.columns[12]],axis=1,inplace=True)
        
    test_data['2022(Jan-May)'] = test_data[test_data.columns[1]] + test_data[test_data.columns[2]] + test_data[test_data.columns[3]] + test_data[test_data.columns[4]] + test_data[test_data.columns[5]]
    test_data.drop([test_data.columns[1],test_data.columns[2],test_data.columns[3],test_data.columns[4],test_data.columns[5]],axis=1,inplace=True)
    
    test_data.to_csv('data/normal_data/newborn_2006_2022.csv')