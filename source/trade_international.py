import pandas as pd
from urllib.request import urlopen
from bs4 import BeautifulSoup
from wiki_economy import wiki_economy
import numpy as np

def getHTMLContent(link):
    html = urlopen(link)
    soup = BeautifulSoup(html, 'html.parser')
    return soup


def comma_to_none(string):
    '''numero con comas en la escritura se las quito para que quede con formato numerico'''
    string_list = string.split(',')
    new_string = ''.join(string_list[:])
    return new_string


if __name__ == "__main__":

       ## Primer link https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population

    #esta celda es para saber como encontrar la tabla en el html

    content = getHTMLContent('https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population')

    #encontre que la etiqueta que necesito es wikitable sortable plainrowheaders

    table = content.find('table', {'class': 'wikitable sortable plainrowheaders'})
    rows = table.find_all('tr')

    # Me armo el primer data frame con country y population del primer link








    rows_list=[]


    # 
    for row in rows:
        cells = row.find_all('td')
        if len(cells) > 1:
            country = cells[0].find('a').text
            population=cells[1].text
            proporcion=cells[2].text


            rows_list.append([country,population,proporcion])
    Data_1=pd.DataFrame(rows_list,columns = ['Country','Population','_%_world'])
    Data_1['Population']=Data_1.apply(lambda x: comma_to_none(x['Population']),  axis=1)

    #Agrego Palestina a mano parece q como to ma el link
    Data_1['Country'][120]='Palestine'





    lista_paises=Data_1['Country'].tolist()











    ## Segundo Link https://en.wikipedia.org/wiki/List_of_countries_by_exports

    content2 = getHTMLContent('https://en.wikipedia.org/wiki/List_of_countries_by_exports')


    table2 = content2.find('table', {'class': 'wikitable sortable'})
    rows2 = table2.find_all('tr')

    Data_2=pd.DataFrame(columns = ['Country','export_million_USD','_%_GDP','Year_exp_data'])
    rows_list2=[]

    for row in rows2:
        cells2 = row.find_all('td')
        if len(cells2) > 1:
            country= cells2[1].find('a').text
            export_million_USD=cells2[2].text
            porcentaje_GDP=cells2[3].text
            Year_exp_data=cells2[4].text[:-1]
            #print(porcentaje_GDP)
            rows_list2.append([country,export_million_USD,porcentaje_GDP,Year_exp_data])
    Data_2=pd.DataFrame(rows_list2,columns = ['Country','export_million_USD','_%_GDP','Year_exp_data'])
    Data_2['export_million_USD']=Data_2.apply(lambda x: comma_to_none(x['export_million_USD']),  axis=1)




    Data_2['Country']=Data_2['Country'].replace("Côte d'Ivoire",'Ivory Coast')

    Data_2['Country']=Data_2['Country'].replace('Democratic Republic of the Congo','DR Congo')
    Data_2['Country']=Data_2['Country'].replace('Macao','Macau')
    Data_2['Country']=Data_2['Country'].replace("Timor-Leste",'East Timor')



    data_12=pd.merge(Data_1,Data_2, how='outer',on='Country')

    data_12








    ## tercer link https://en.wikipedia.org/wiki/List_of_countries_by_imports

    content3 = getHTMLContent('https://en.wikipedia.org/wiki/List_of_countries_by_imports')

    table3 = content3.find('table', {'class': 'wikitable sortable'}) #esta
    rows3 = table3.find_all('tr')
    Data_3=pd.DataFrame(columns = ['Country','import_million_USD','Year_imp_data'])
    rows_list3=[]

    for row in rows3:
        cells3 = row.find_all('td')
        if len(cells3) > 1:
            country= cells3[1].find('a').text
            import_million_USD=cells3[2].text

            Year_imp_data=cells3[3].text
            #print(porcentaje_GDP)
            rows_list3.append([country,import_million_USD,Year_imp_data])
    Data_3=pd.DataFrame(rows_list3,columns = ['Country','import_million_USD','Year_imp_data'])
    Data_3['import_million_USD']=Data_3.apply(lambda x: comma_to_none(x['import_million_USD']),  axis=1) 




    Data_3['Country']=Data_3['Country'].replace('Cocos Islands','Cocos (Keeling) Islands')
    Data_3['Country']=Data_3['Country'].replace("Côte d'Ivoire",'Ivory Coast')

    Data_3['Country']=Data_3['Country'].replace('Democratic Republic of the Congo','DR Congo')
    #Data_3['Country']=Data_3['Country'].replace('Macao','Macau')

    Data_3['Country']=Data_3['Country'].replace('Macedonia','North Macedonia')
    Data_3['Country']=Data_3['Country'].replace('Republic of the Congo','Congo')
    Data_3['Country']=Data_3['Country'].replace('Saint Helena, Ascension and Tristan da Cunha','Saint Helena, Ascensionand Tristan da Cunha')
    Data_3['Country']=Data_3['Country'].replace("Micronesia",'F.S. Micronesia')
    Data_3['Country']=Data_3['Country'].replace("Timor-Leste",'East Timor')


    data_123=pd.merge(data_12,Data_3, how='outer',on='Country')










    ## Cuarto link https://en.wikipedia.org/wiki/List_of_countries_by_leading_trade_partners

    content4 = getHTMLContent('https://en.wikipedia.org/wiki/List_of_countries_by_leading_trade_partners')





    table4 = content4.find('table', {'class': 'wikitable sortable'}) #esta
    rows4 = table4.find_all('tr')
    Data_4=pd.DataFrame(columns = ['Country','Leading_Export_Market','Leading_Import_Market'])
    rows_list4=[]

    for row in rows4:
        cells4 = row.find_all('td')
        if len(cells4) > 1:
            country= cells4[0].find('a').text

            try:
                Leading_Export_Market=cells4[1].text
            except:
                Leading_Export_Market=np.nan
            try:    
                Leading_Import_Market=cells4[2].text
            except:
                Leading_Import_Market=np.nan

            rows_list4.append([country, Leading_Export_Market,Leading_Import_Market])
    Data_4=pd.DataFrame(rows_list4,columns = ['Country','Leading_Export_Market','Leading_Import_Market'])

    Data_4['Country']=Data_4['Country'].replace('Bosnia','Bosnia and Herzegovina')
    Data_4['Country']=Data_4['Country'].replace('Congo, Democratic Republic of the','DR Congo')
    Data_4['Country']=Data_4['Country'].replace('Federated States of Micronesia','F.S. Micronesia')
    Data_4['Country']=Data_4['Country'].replace('Sao Tome and Principe','São Tomé and Príncipe')
    Data_4['Country']=Data_4['Country'].replace('State of Palestine','Palestine')
    #Data_4['Country']=Data_4['Country'].replace('Macao','Macau')
    Data_4['Country']=Data_4['Country'].replace('Timor Leste','East Timor')

    Data_4['Country']=Data_4['Country'].replace('Swaziland','Eswatini')

    Data_4['Country']=Data_4['Country'].replace('Vatican','Vatican City')


    data_1234=pd.merge(data_123,Data_4, how='outer',on='Country')





    ## Quinto link -https://en.wikipedia.org/wiki/List_of_countries_by_oil_exports


    content5 = getHTMLContent('https://en.wikipedia.org/wiki/List_of_countries_by_oil_exports')

    table5 = content5.find('table', {'class': 'wikitable sortable'}) #esta
    rows5 = table5.find_all('tr')
    Data_5=pd.DataFrame(columns = ['Country','oil_export_bbl_day','year_oil_export_data'])
    rows_list5=[]

    for row in rows5:
        cells5 = row.find_all('td')
        if len(cells5) > 1:
            country= cells5[1].find('a').text

            try:
                oil_export_bbl_day=cells5[2].text
            except:
                oil_export_bbl_day=np.nan
            try:    
                year_oil_export_data=cells5[3].text
            except:
                year_oil_export_data=np.nan

            rows_list5.append([country, oil_export_bbl_day,year_oil_export_data])
    Data_5=pd.DataFrame(rows_list5,columns = ['Country','oil_export_bbl_day','year_oil_export_data'])



    #Data_5['Country']=Data_5['Country'].replace('Cocos Islands','Cocos (Keeling) Islands')
    Data_5['Country']=Data_5['Country'].replace("Côte d'Ivoire",'Ivory Coast')

    #Data_5['Country']=Data_5['Country'].replace('Bosnia','Bosnia and Herzegovina')
    Data_5['Country']=Data_5['Country'].replace('Democratic Republic of the Congo','DR Congo')

    Data_5['Country']=Data_5['Country'].replace('Timor-Leste','East Timor')

    #Data_5['Country']=Data_5['Country'].replace('Swaziland','Eswatini')

    #Data_5['Country']=Data_5['Country'].replace('Vatican','Vatican City')
    #Data_5['Country']=Data_5['Country'].replace('Macedonia','North Macedonia')
    Data_5['Country']=Data_5['Country'].replace('Republic of the Congo','Congo')
    #Data_5['Country']=Data_5['Country'].replace('Saint Helena, Ascension and Tristan da Cunha','Saint Helena, Ascensionand Tristan da Cunha')




    data_12345=pd.merge(data_1234,Data_5, how='outer',on='Country')








     ## Sexto link    -https://en.wikipedia.org/wiki/List_of_countries_by_oil_production

    content6 = getHTMLContent('https://en.wikipedia.org/wiki/List_of_countries_by_oil_production')





    table6 = content6.find('table', {'class': 'wikitable sortable'}) #esta
    rows6 = table6.find_all('tr')
    Data_6=pd.DataFrame(columns = ['Country','oil_production_bbl_day','oil_production_bbl_day_per_capita'])
    rows_list6=[]

    for row in rows6:
        cells6 = row.find_all('td')
        if len(cells6) > 1:
            try:
                country= cells6[1].find('a').text
                oil_production_bbl_day=cells6[2].text
                oil_production_bbl_day_per_capita=cells6[3].text
            except:

                country= cells6[0].find('a').text
                oil_production_bbl_day=cells6[1].text
                oil_production_bbl_day_per_capita=cells6[2].text

            rows_list6.append([country, oil_production_bbl_day,oil_production_bbl_day_per_capita])

    Data_6=pd.DataFrame(rows_list6,columns = ['Country','oil_production_bbl_day','oil_production_bbl_day_per_capita'])

    Data_6['Country']=Data_6['Country'].replace("Côte d'Ivoire",'Ivory Coast')

    #Data_6['Country']=Data_6['Country'].replace('Bosnia','Bosnia and Herzegovina')
    Data_6['Country']=Data_6['Country'].replace('Czechia','Czech Republic')
    Data_6['Country']=Data_6['Country'].replace('Congo-Kinshasa','DR Congo')

    Data_6['Country']=Data_6['Country'].replace('Congo-Brazzaville','Congo')
    #Data_6['Country']=Data_6['Country'].replace('Saint Helena, Ascension and Tristan da Cunha','Saint Helena, Ascensionand Tristan da Cunha')





    data_123456=pd.merge(data_12345,Data_6, how='outer',on='Country')



    ####

    countries = []

    for i in range(len(data_123456['Country'])):
        countries.append(data_123456['Country'][i])

    data = wiki_economy(countries)

    dataset = pd.merge( data_123456, data, on = 'Country', how='left')

    

    dataset.to_csv('/data/wiki_country_data.csv',index=False)

