# PRA 1 - Web Scraping. Tipología y ciclo de vida de los datos. Universidad Oberta de Catalunya.

El presente proyecto engloba un trabajo de web scrapping sobre la página web de Wikipedia, en donde, se ha centrado el interés en la extracción de información económica de diferentes países del mundo; considerando que Wikipedia posee gran cantidad de información realacionada, sin embargo, la misma se encuentra dispersa entre distintas páginas, de tal manera, que en base al web scrapping se pretende obtener indicadores económicos y concentrarlos en un dataset. 

Para lo cual, en primer lugar obtendremos algunos de los principales indicadores económicos como los siguientes:

- Población (https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population)

- Exportaciones (https://en.wikipedia.org/wiki/List_of_countries_by_exports)

- Importaciones (https://en.wikipedia.org/wiki/List_of_countries_by_imports)

- Principales Socios Comerciales (https://en.wikipedia.org/wiki/List_of_countries_by_leading_trade_partners)

- Exportación de Petroleo (https://en.wikipedia.org/wiki/List_of_countries_by_oil_exports)

- Producción de Petroleo (https://en.wikipedia.org/wiki/List_of_countries_by_oil_production)

Posteriormente, tomando en cuenta que Wikipedia también provee información de estadísticas, comercio y finanzas públicas de cada país, se completará el dataset con el compendio de esta información, generando así un dataset amplio de información estadística relacionada a la economía mundial. Para recabar esta información se ha creado la función wiki_economics que tomará un listado de países y devolverá la información mencionada.

Así mismo, en el archivo main.py, se muestra un extracto del código final del proyecto, el cual, obtiene el primer indicador de Población Mundial y, con la ayuda de la función wiki_economics, complementa el dataset con la información estadística de los primeros diez países de la lista obtenida.

El proyecto se desarrollado por los estudiantes del Máster Universitario en Ciencia de Datos de la UOC: Tatiana Piccolomini y Jonathan Zambrano.  
