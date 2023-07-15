# Фукнция создания интерактивной карты с метками
def create_map(llist):
    import os
    import json
    import random
    import requests
    from ipyleaflet import GeoJSON,Map
    
    region_dict = {'Республика Адыгея':'Adygey',
    'Республика Алтай':'Gorno-Altay',
    'Республика Башкортостан':'Bashkortostan',
    'Республика Бурятия':'Buryat',
    'Республика Дагестан':'Dagestan',
    'Республика Ингушетия':'Ingush',
    'Кабардино-Балкарская Республика':'Kabardin-Balkar',
    'Республика Калмыкия':'Kalmyk',
    'Карачаево-Черкесская Республика':'Karachay-Cherkess',
    'Республика Карелия':'Karelia',
    'Республика Коми':'Komi',
    'Республика Марий Эл':'Mariy-El',
    'Республика Мордовия':'Mordovia',
    'Республика Саха (Якутия)':'Sakha',
    'Республика Северная Осетия - Алания':'North Ossetia',
    'Республика Татарстан':'Tatarstan',
    'Республика Тыва':'Tuva',
    'Удмуртская Республика':'Udmurt',
    'Республика Хакасия':'Khakass',
    'Чеченская Республика':'Chechnya',
    'Чувашская Республика - Чувашия':'Chuvash',
    'Алтайский край':'Altay',
    'Забайкальский край':'Zabaikalskiy Krai',
    'Камчатский край':'Kamchatka',
    'Краснодарский край':'Krasnodar',
    'Красноярский край':'Krasnoyarsk',
    'Пермский край':'Perm',
    'Приморский край':'Primorye',
    'Ставропольский край':'Stavropol',
    'Хабаровский край':'Khabarovsk',
    'Амурская область':'Amur',
    'Архангельская область':'Arkhangelsk',
    'Астраханская область':'Astrakhan',
    'Белгородская область':'Belgorod',
    'Брянская область':'Bryansk',
    'Владимирская область':'Vladimir',
    'Волгоградская область':'Volgograd',
    'Вологодская область':'Vologda',
    'Воронежская область':'Voronezh',
    'Ивановская область':'Ivanovo',
    'Иркутская область':'Irkutsk',
    'Калининградская область':'Kaliningrad',
    'Калужская область':'Kaluga',
    'Кемеровская область - Кузбасс':'Kemerovo',
    'Кировская область':'Kirov',
    'Костромская область':'Kostroma',
    'Курганская область':'Kurgan',
    'Курская область':'Kursk',
    'Ленинградская область':'Leningrad',
    'Липецкая область':'Lipetsk',
    'Магаданская область':'Maga Buryatdan',
    'Московская область':'Moskva',
    'Мурманская область':'Murmansk',
    'Нижегородская область':'Nizhegorod',
    'Новгородская область':'Novgorod',
    'Новосибирская область':'Novosibirsk',
    'Омская область':'Omsk',
    'Оренбургская область':'Orenburg',
    'Орловская область':'Orel',
    'Пензенская область':'Penza',
    'Псковская область':'Pskov',
    'Ростовская область':'Rostov',
    'Рязанская область':'Ryazan',
    'Самарская область':'Samara',
    'Саратовская область':'Saratov',
    'Сахалинская область':'Sakhalin',
    'Свердловская область':'Sverdlovsk',
    'Смоленская область':'Smolensk',
    'Тамбовская область':'Tambov',
    'Тверская область':'Tver',
    'Томская область':'Tomsk',
    'Тульская область':'Tula',
    'Тюменская область':'Tyumen',
    'Ульяновская область':'Ulyanovsk',
    'Челябинская область':'Chelyabinsk',
    'Ярославская область':'Yaroslavl',
    'Москва':'Moscow City',
    'Санкт-Петербург':'City of St. Petersburg',
    'Еврейская АО':'Yevrey',
    'Ненецкий АО':'Nenets',
    'Ханты-Мансийский АО - Югра':'Khanty-Mansiy',
    'Чукотский АО':'Chukot',
    'Ямало-Ненецкий АО':'Yamal-Nenets'}
    
    with open('function/geo_ru.json','r') as file:
        data = json.load(file)

    new_data = {"type": "FeatureCollection",
    "features": []}

    nlist = []
    for el in llist:
        nlist.append(region_dict[el])
    for el in nlist:
        for feature in data['features']:
            if el == feature['properties']['name']:
                new_data['features'].append(feature)
                
    with open('function/second_layer.json','w') as file:
        json.dump(new_data,file)

    def color(feature):
        return {'color':'red'}

    m = Map(center=(66.25, 94.15), zoom=3)

    geo_json = GeoJSON(
        data=data,
        style={
            'opacity': 1, 'dashArray': '9', 'fillOpacity': 0.2, 'weight': 1
        },
        hover_style={
            'color': 'white', 'dashArray': '0', 'fillOpacity': 0.2
        }
    )
    geo_json2 = GeoJSON(
        data=new_data,
        style={
            'opacity': 1, 'dashArray': '9', 'fillOpacity': 0.2, 'weight': 1
        },
        hover_style={
            'color': 'white', 'dashArray': '0', 'fillOpacity': 0.2
        },
        style_callback = color
    )

    m.add_layer(geo_json)
    m.add_layer(geo_json2)
    return m