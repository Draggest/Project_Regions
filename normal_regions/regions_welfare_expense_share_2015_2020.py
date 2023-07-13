# Преобразование таблицы welfare_expense_share_2015_2020.xlsx к истинным субъектам РФ -> CSV

import pandas as pd

if __name__ == '__main__':
    regions = pd.read_csv('data/normal_data/regions.csv',index_col=0)
    data = pd.read_excel('data/social_russia_data/welfare_expense_share_2015_2020.xlsx')

    data.rename({'region':'Region'},axis=1,inplace=True)
    for el in data.columns:
        if type(el) == float:
            data.rename({el:str(int(el))},axis=1,inplace=True)
    data.loc[data[data['Region'] == 'г. Москва'].index[0],'Region'] = 'Москва'
    data.loc[data[data['Region'] == 'Кабардино-Балкарская\nРеспублика'].index[0],'Region'] = 'Кабардино-Балкарская Республика'
    data.loc[data[data['Region'] == 'Карачаево-Черкесская\nРеспублика'].index[0],'Region'] = 'Карачаево-Черкесская Республика'
    data.loc[data[data['Region'] == 'Республика Северная\nОсетия-Алания'].index[0],'Region'] = 'Республика Северная Осетия - Алания'
    data.loc[data[data['Region'] == 'Чувашская Республика'].index[0],'Region'] = 'Чувашская Республика - Чувашия'
    data.loc[data[data['Region'] == 'Кемеровская область'].index[0],'Region'] = 'Кемеровская область - Кузбасс'
    data.loc[data[data['Region'] == 'г. Санкт-Петербург'].index[0],'Region'] = 'Санкт-Петербург'
    data.loc[data[data['Region'] == 'Еврейская автономная область'].index[0],'Region'] = 'Еврейская АО'
    data.loc[data[data['Region'] == 'Ненецкий автономный округ'].index[0],'Region'] = 'Ненецкий АО'
    data.loc[data[data['Region'] == 'Ямало-Ненецкий \nавтономный округ'].index[0],'Region'] = 'Ямало-Ненецкий АО'
    data.loc[data[data['Region'] == 'Ханты-Мансийский \nавтономный округ - Югра'].index[0],'Region'] = 'Ханты-Мансийский АО - Югра'
    data.loc[data[data['Region'] == 'Чукотский автономный округ'].index[0],'Region'] = 'Чукотский АО'

    regions.merge(data,left_on='Region',right_on='Region',how='left').to_csv('data/normal_data/welfare_expense_share_2015_2020.csv')