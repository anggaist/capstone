from flask import Flask, render_template
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from io import BytesIO
import base64
from bs4 import BeautifulSoup 
import requests

#don't change this
matplotlib.use('Agg')
app = Flask(__name__) #do not change this

#insert the scrapping here
url_get = requests.get('https://www.exchange-rates.org/exchange-rate-history/usd-idr')
soup = BeautifulSoup(url_get.content,"html.parser")
print(soup.prettify()[:500])

#find your right key here
table = soup.find('div', attrs={'class': 'inner'})
print(table.prettify()[1:500])
table.find_all('div', attrs={'class':'chart-stat chart-bottom-item'})[:5]

row = table.find_all('div', attrs={'class':'chart-stat chart-bottom-item'})
row_length = len(row)

temp = [] #initating a list

for i in range(0, row_length):
    
    #get period 
    period = table.find_all('div', attrs={'class':'chart-content'})[i].text
    
    temp.append((period)) 
    
temp 

#change into dataframe
df = pd.DataFrame(temp, columns = ('period'))
df.head())

#insert data wrangling here

df['period'] = df['period'].astype('datetime64[ns]')

df.dtypes
#end of data wranggling 

@app.route("/")
def index(): 
	
	card_data = f'{data["____"].mean().round(2)}' #be careful with the " and ' 

	# generate plot
	ax = ____.plot(figsize = (20,9)) 
	
	# Rendering plot
	# Do not change this
	figfile = BytesIO()
	plt.savefig(figfile, format='png', transparent=True)
	figfile.seek(0)
	figdata_png = base64.b64encode(figfile.getvalue())
	plot_result = str(figdata_png)[2:-1]

	# render to html
	return render_template('index.html',
		card_data = card_data, 
		plot_result=plot_result
		)


if __name__ == "__main__": 
    app.run(debug=True)