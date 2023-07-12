# Создание исходного списка субъектов РФ в формате csv
import pandas as pd



def get_csv_regions():
    url = 'https://ru.wikipedia.org/wiki/%D0%A1%D1%83%D0%B1%D1%8A%D0%B5%D0%BA%D1%82%D1%8B_%D0%A0%D0%BE%D1%81%D1%81%D0%B8%D0%B9%D1%81%D0%BA%D0%BE%D0%B9_%D0%A4%D0%B5%D0%B4%D0%B5%D1%80%D0%B0%D1%86%D0%B8%D0%B8'
    data = pd.read_html(url)[2]['Субъект Российской Федерации']
    data = data.apply(lambda x: x.split('[')[0])
    list_to_del = ['Республики','Донецкая Народная Республика','Республика Крым','Луганская Народная Республика','Края','Области','Запорожская область','Херсонская область','Города федерального значения','Севастополь','Автономная область','Автономные округа','Российская Федерация']
    list_regions = list(data.values)
    new_list_regions = list_regions.copy()
    for el in list_regions:
        if el in list_to_del:
            new_list_regions.remove(el)
    new_regions = pd.Series(new_list_regions)
    new_regions = new_regions.apply(lambda x: x.replace('—','-'))
    new_regions.to_csv('data/normal_data/regions.csv',header=['Region'])
    return



if __name__ == '__main__':
    get_csv_regions()