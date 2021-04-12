# Importación de librerias
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

# Función para obtención de información económica general 
def wiki_economy(countries):
    # Inicialización de variables temporales
    data = []
    counter = 0
    # Se adapta el nombre de los países
    countries = [i.replace(' ','_') for i in countries]
    for item in countries:
        # Lectura de página html
        pais = item
        str = 'https://en.wikipedia.org/wiki/Economy_of_' + pais
        page = requests.get(str)
        soup = bs(page.content)
        # Búsqueda de tabla de datos
        table = soup.find('table', class_='infobox')
        # Si no existen datos se crea registro vacío
        if table != None:
            title = table.find(class_='infobox-title adr')
        if table == None or title == None:
            data.append(pd.DataFrame(columns = ['Country'], 
                                     index = range(1)))
            data[counter].iloc[0] = [item]
            counter += 1
        else:
            # Si existe tabla de datos
            # Se obtienen las entradas de encabezados
            headers = []
            for datos in table:
                headers.append(table.find_all('th'))
            # Se obtiene el texto de los encabezados
            head = []
            for i in range(len(headers[0])):
                head.append(headers[0][i].text)
            # Se obtienen las entradas de los datos (cuerpo de la tabla)
            bodys = []
            for datos in table:
                bodys.append(table.find_all('td'))
            # Se obtiene el texto de los datos
            body = []
            for i in range(len(bodys[0])):
                body.append(bodys[0][i].text)
            # Se eliminan las entradas del ancabezado que corresponden
            # a los grupos de datos
            if 'Statistics' in head:
                head.remove('Statistics')
            if 'External' in head:
                head.remove('External')
            if 'Public finances' in head:
                head.remove('Public finances')
            # Se eliminan valores iniciales y finales de los datos
            # que no son de utilidad
            if (len(body)-1==len(head)):
                body = body[0:len(body)-1]
            else:
                body = body[1:len(body)-1]
           # Se eliminan los caracteres especiales y espacios
            body = [body[i].replace('\n','') for i in range(len(body))]
            body = [body[i].replace('\u200b',' ') for i in range(len(body))]
            body = [body[i].replace('\xa0',' ') for i in range(len(body))]
            body = [body[i].strip() for i in range(len(body))]
            # Se inserta la columna "Country" en el encabezado
            head.insert(0,'Country')
            # Se inserta nombre del país en los datos
            body.insert(0,item)
            #Se crea la entrada de datos en la variable temporal
            data.append(pd.DataFrame(columns = head, index = range(1)))
            data[counter].iloc[0] = body
            counter += 1
    # Finalmente, se crea la tabla con todas las entradas generadas
    df = pd.concat(data)
    df = df.drop(['Population', 'Exports', 'Imports'], axis = 1)
    return(df)
