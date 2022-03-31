#!/usr/bin/env python
# coding: utf-8

# In[53]:


get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')


# In[54]:


import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np


# 1) Write a python program to display all the header tags from wikipedia.org.

# In[55]:


page = requests.get('https://en.wikipedia.org/wiki/Main_Page')
soup = BeautifulSoup(page.text, 'html.parser')
story = soup.find_all(['h1', 'h2', 'h3'])
for i in story:
    print(i)


# 2) Write a python program to display IMDB’s Top rated 100 movies’ data (i.e. name, rating, year of release)
# and make data frame.

# In[56]:


imdb_page=requests.get('https://www.imdb.com/chart/top/')
print(imdb_page)

imdb_soup=BeautifulSoup(imdb_page.content)


# In[22]:


movie_name=imdb_soup.find_all('td',class_='titleColumn')

column_movie=[]
for i in movie_name:
    column_movie.append(i.text.split('\n'))
column_movie=column_movie[:100]  

movies_100=[]
for l in column_movie:
  movies_100.append(l[2].strip())
print(movies_100)


# In[57]:


movie_rate=imdb_soup.find_all('td',class_='ratingColumn imdbRating')

column_rate=[]
for i in movie_rate[0:100]:
    column_rate.append(i.text.strip())
print(column_rate[:100])


# In[58]:


movie_year=imdb_soup.find_all('span',class_='secondaryInfo')
movie_year[:100]

column_year=[]
for i in movie_year[:100]:
    column_year.append(i.text.strip('()'))
print(column_year[:100])


# In[25]:


TopMovies=pd.DataFrame({})
TopMovies['Names']=movies_100
TopMovies['ReleaseYear']=column_year
TopMovies['Rating']=column_rate

TopMovies


# 3) Write a python program to display IMDB’s Top rated 100 Indian movies’ data (i.e. name, rating, year of
# release) and make data frame.

# In[59]:


imdb_page=requests.get('https://www.imdb.com/india/top-rated-indian-movies/')
print(imdb_page)

imdb_soup=BeautifulSoup(imdb_page.content)


# In[60]:


movie_name=imdb_soup.find_all('td',class_='titleColumn')

column_movie=[]
for i in movie_name:
    column_movie.append(i.text.split('\n'))
column_movie=column_movie[:100]  
column_movie

movies_100=[]
for l in column_movie:
  movies_100.append(l[2].strip())
print(movies_100)


# In[61]:


movie_rate=imdb_soup.find_all('td',class_='ratingColumn imdbRating')

column_rate=[]
for i in movie_rate[0:100]:
    column_rate.append(i.text.strip())
print(column_rate[:100])


# In[62]:


movie_year=imdb_soup.find_all('span',class_='secondaryInfo')

column_year=[]
for i in movie_year[:100]:
    column_year.append(i.text.strip('()'))
print(column_year[:100])


# In[63]:


TopMovies=pd.DataFrame({})
TopMovies['Names']=movies_100
TopMovies['ReleaseYear']=column_year
TopMovies['Rating']=column_rate

TopMovies


# 4) Write a python program to scrape product name, price and discounts from https://meesho.com/bagsladies/pl/p7vbp .

# In[64]:


page = requests.get('https://meesho.com/bags-ladies/pl/p7vbp')

soup = BeautifulSoup(page.content, 'html.parser')
    
print(soup.prettify())


# In[65]:


name_list = soup.find_all('p', class_='Text__StyledText-sc-oo0kvp-0 cPgaBh NewProductCard__ProductTitle_Desktop-sc-j0e7tu-4 hofZGw NewProductCard__ProductTitle_Desktop-sc-j0e7tu-4 hofZGw')
name_list_text = []
for item in name_list:
    name_list_text.append(item.text)


# In[66]:


current_price_list = soup.find_all('h5', class_='Text__StyledText-sc-oo0kvp-0 dLSsNI')
current_price_list_text = []
for item in current_price_list:
    current_price_list_text.append(item.text)


# In[67]:


original_price_list = soup.find_all('p', class_='Text__StyledText-sc-oo0kvp-0 hgHnkG Paragraph__StyledParagraphBody2StrikeThrough-sc-69qp0d-0 coIjqc Paragraph__StyledParagraphBody2StrikeThrough-sc-69qp0d-0 coIjqc')
original_price_list_text = []
for item in original_price_list:
    original_price_list_text.append(item.text)


# In[68]:


discount_price_list = soup.find_all('span', class_='Text__StyledText-sc-oo0kvp-0 cZvGTZ')
discount_price_list_text = []
for item in discount_price_list:
    discount_price_list_text.append(item.text)


# In[69]:


df = pd.DataFrame(list(zip(name_list_text, current_price_list_text, original_price_list_text,discount_price_list_text)),
              columns=['Bag Name','Current Price', 'Original Price','Discount'])
df


# 5) Write a python program to scrape cricket rankings from icc-cricket.com.
# a) Top 10 ODI teams in men’s cricket along with the records for matches, points and rating.

# In[70]:


icc_page=requests.get('https://www.icc-cricket.com/rankings/mens/team-rankings/odi')
print(icc_page)

icc_soup=BeautifulSoup(icc_page.content)


# In[71]:


team_name=icc_soup.find_all('span',class_='u-hide-phablet')
team_name[0:10]

column_team=[]
for i in team_name:
    column_team.append(i.text.strip('[]'))
column_team=column_team[:10]  
print(column_team)


# In[72]:


team_matches=icc_soup.find_all('td',class_='rankings-block__banner--matches')

team_match=icc_soup.find_all('td',class_='table-body__cell u-center-text')

column_matches=[]
for i in team_matches:
    column_matches.append(i.text.strip())

for i in range(0,len(team_match),2):
    column_matches.append(team_match[i].text.strip())
column_matches=column_matches[0:10]
column_matches


# In[73]:


team_points=icc_soup.find_all('td',class_='rankings-block__banner--points')

team_match=icc_soup.find_all('td',class_='table-body__cell u-center-text')

column_points=[]
for i in team_points:
    column_points.append(i.text.strip())
column_points

for i in range(1,len(team_match),2):
    column_points.append(team_match[i].text.strip())
column_points=column_points[0:10]
print(column_points)


# In[74]:


team_rating=icc_soup.find_all('td',class_='rankings-block__banner--rating u-text-right')

column_rating=[]
for i in team_rating:
    column_rating.append(i.text.strip())

team_rating=icc_soup.find_all('td',class_='table-body__cell u-text-right rating')

for i in team_rating:
    column_rating.append(i.text.strip())
column_rating=column_rating[0:10]
column_rating


# In[75]:


MenTeam10=pd.DataFrame({})
MenTeam10['Team']=column_team
MenTeam10['Matches']=column_matches
MenTeam10['Points']=column_points
MenTeam10['Ratings']=column_rating

MenTeam10


# b) Top 10 ODI Batsmen along with the records of their team and rating.

# In[76]:


icc_page=requests.get('https://www.icc-cricket.com/rankings/mens/player-rankings/odi/batting')
print(icc_page)

icc_soup=BeautifulSoup(icc_page.content)


# In[77]:


player_name=icc_soup.find_all('div',class_='rankings-block__banner--name-large')

column_name=[]
for i in player_name:
    column_name.append(i.text.strip())

player_name=icc_soup.find_all('td',class_='table-body__cell rankings-table__name name')

for i in player_name:
    column_name.append(i.text.strip())
column_name=column_name[0:10]
print(column_name)


# In[78]:


player_country=icc_soup.find_all('div',class_='rankings-block__banner--nationality')

column_country=[]
for i in player_country:
    column_country.append(i.text.strip())

player_country=icc_soup.find_all('td',class_='table-body__cell nationality-logo rankings-table__team')

for i in player_country:
    column_country.append(i.text.strip())
column_country=column_country[0:10]
print(column_country)


# In[79]:


player_rating=icc_soup.find_all('div',class_='rankings-block__banner--rating')

column_rating=[]
for i in player_rating:
    column_rating.append(i.text.strip())

player_rating=icc_soup.find_all('td',class_='table-body__cell rating')

for i in player_rating:
    column_rating.append(i.text.strip())
column_rating=column_rating[0:10]
print(column_rating)


# In[80]:


MenBatsman10=pd.DataFrame({})
MenBatsman10['Names']=column_name
MenBatsman10['Team']=column_country
MenBatsman10['Rating']=column_rating

MenBatsman10


# c) Top 10 ODI bowlers along with the records of their team and rating.

# In[81]:


icc_page=requests.get('https://www.icc-cricket.com/rankings/mens/player-rankings/odi/bowling')
print(icc_page)

icc_soup=BeautifulSoup(icc_page.content)


# In[82]:


player_name=icc_soup.find_all('div',class_='rankings-block__banner--name-large')

column_name=[]

for i in player_name:
    column_name.append(i.text.strip())

player_name=icc_soup.find_all('td',class_='table-body__cell rankings-table__name name')

for i in player_name:
    column_name.append(i.text.strip())
column_name=column_name[0:10]
print(column_name)


# In[83]:


player_country=icc_soup.find_all('div',class_='rankings-block__banner--nationality')

column_country=[]
for i in player_country:
    column_country.append(i.text.strip().replace('\n',''))


player_country=icc_soup.find_all('td',class_='table-body__cell nationality-logo rankings-table__team')

for i in player_country:
    column_country.append(i.text.strip())
column_country=column_country[0:10]
print(column_country)


# In[84]:


player_rating=icc_soup.find_all('div',class_='rankings-block__banner--rating')

column_rating=[]
for i in player_rating:
    column_rating.append(i.text.strip())
column_rating

player_rating=icc_soup.find_all('td',class_='table-body__cell rating')

for i in player_rating:
    column_rating.append(i.text.strip())
column_rating=column_rating[0:10]
column_rating


# In[85]:


MenBowler10=pd.DataFrame({})
MenBowler10['Names']=column_name
MenBowler10['Team']=column_country
MenBowler10['Rating']=column_rating

MenBowler10


# 6) Write a python program to scrape cricket rankings from icc-cricket.com.
# a) Top 10 ODI teams in women’s cricket along with the records for matches, points and rating.

# In[86]:


icc_page=requests.get('https://www.icc-cricket.com/rankings/womens/team-rankings/odi')
print(icc_page)

icc_soup=BeautifulSoup(icc_page.content)


# In[87]:


team_name=icc_soup.find_all('span',class_='u-hide-phablet')

column_team=[]
for i in team_name:
    column_team.append(i.text.strip('[]'))
column_team=column_team[:10]  
print(column_team)


# In[88]:


team_matches=icc_soup.find_all('td',class_='rankings-block__banner--matches')

column_matches=[]
for i in team_matches:
    column_matches.append(i.text.strip())
column_matches

team_match=icc_soup.find_all('td',class_='table-body__cell u-center-text')

for i in range(0,len(team_match),2):
    column_matches.append(team_match[i].text.strip())
column_matches=column_matches[0:10]
print(column_matches)


# In[89]:


team_points=icc_soup.find_all('td',class_='rankings-block__banner--points')
team_match=icc_soup.find_all('td',class_='table-body__cell u-center-text')


column_points=[]
for i in team_points:
    column_points.append(i.text.strip())
column_points

for i in range(1,len(team_match),2):
    column_points.append(team_match[i].text.strip())
column_points=column_points[0:10]
print(column_points)


# In[90]:


team_rating=icc_soup.find_all('td',class_='rankings-block__banner--rating u-text-right')

column_rating=[]
for i in team_rating:
    column_rating.append(i.text.strip())


team_rating=icc_soup.find_all('td',class_='table-body__cell u-text-right rating')

for i in team_rating:
    column_rating.append(i.text.strip())
column_rating=column_rating[0:10]
column_rating


# In[24]:


WomenTeam10=pd.DataFrame({})
WomenTeam10['Team']=column_team
WomenTeam10['Matches']=column_matches
WomenTeam10['Points']=column_points
WomenTeam10['Ratings']=column_rating

WomenTeam10


# b) Top 10 women’s ODI Batting players along with the records of their team and rating.

# In[91]:


icc_page=requests.get('https://www.icc-cricket.com/rankings/womens/player-rankings/odi/batting')
print(icc_page)

icc_soup=BeautifulSoup(icc_page.content)


# In[92]:


player_name=icc_soup.find_all('div',class_='rankings-block__banner--name-large')

column_name=[]
for i in player_name:
    column_name.append(i.text.strip())

player_name=icc_soup.find_all('td',class_='table-body__cell rankings-table__name name')

for i in player_name:
    column_name.append(i.text.strip())
column_name=column_name[0:10]
print(column_name)


# In[93]:


player_country=icc_soup.find_all('div',class_='rankings-block__banner--nationality')

column_country=[]
for i in player_country:
    column_country.append(i.text.strip())

player_country=icc_soup.find_all('td',class_='table-body__cell nationality-logo rankings-table__team')

for i in player_country:
    column_country.append(i.text.strip())
column_country=column_country[0:10]
print(column_country)


# In[94]:


player_rating=icc_soup.find_all('div',class_='rankings-block__banner--rating')

column_rating=[]
for i in player_rating:
    column_rating.append(i.text.strip())

player_rating=icc_soup.find_all('td',class_='table-body__cell rating')

for i in player_rating:
    column_rating.append(i.text.strip())
column_rating=column_rating[0:10]
print(column_rating)


# In[95]:


WomanBatsman10=pd.DataFrame({})
WomanBatsman10['Names']=column_name
WomanBatsman10['Team']=column_country
WomanBatsman10['Rating']=column_rating

WomanBatsman10


# c) Top 10 women’s ODI all-rounder along with the records of their team and rating.

# In[96]:


icc_page=requests.get('https://www.icc-cricket.com/rankings/womens/player-rankings/odi/all-rounder')
print(icc_page)

icc_soup=BeautifulSoup(icc_page.content)


# In[97]:


player_name=icc_soup.find_all('div',class_='rankings-block__banner--name-large')

column_name=[]
for i in player_name:
    column_name.append(i.text.strip())

player_name=icc_soup.find_all('td',class_='table-body__cell rankings-table__name name')

for i in player_name:
    column_name.append(i.text.strip())
column_name=column_name[0:10]
print(column_name)


# In[98]:


player_country=icc_soup.find_all('div',class_='rankings-block__banner--nationality')

column_country=[]
for i in player_country:
    column_country.append(i.text.strip())

player_country=icc_soup.find_all('td',class_='table-body__cell nationality-logo rankings-table__team')

for i in player_country:
    column_country.append(i.text.strip())
column_country=column_country[0:10]
print(column_country)


# In[99]:


player_rating=icc_soup.find_all('div',class_='rankings-block__banner--rating')

column_rating=[]
for i in player_rating:
    column_rating.append(i.text.strip())

player_rating=icc_soup.find_all('td',class_='table-body__cell rating')

for i in player_rating:
    column_rating.append(i.text.strip())
column_rating=column_rating[0:10]
print(column_rating)


# In[100]:


WomanAll10=pd.DataFrame({})
WomanAll10['Names']=column_name
WomanAll10['Team']=column_country
WomanAll10['Rating']=column_rating

WomanAll10


# 7) Write a python program to scrape details of all the posts from coreyms.com. Scrape the heading, date, content
# and the code for the video from the link for the youtube video from the post.

# In[101]:


post_details ={'Heading':[],
                'Date':[],
                'Content':[],
                'Link':[]}
url=' https://www.coreyms.com.'
page = requests.get(url)
soup=BeautifulSoup(page.text,'html.parser')

# ={'Heading':[]}

page_data=soup.find_all('header',class_="entry-header")
for x in page_data:
    
#Extracting heading
    heading=x.find('h2',class_='entry-title').text
    post_details['Heading'].append(heading)
    
#Extracting date
    date=x.find('time',class_='entry-time').text
    post_details['Date'].append(date)

page_content=soup.find_all('div', class_= 'entry-content')

 #To extract content
L=0
for i in page_content:
    L=L+1
    content=i.find('p').text
    post_details['Content'].append(content)
    
#To extract video link

#Since 5th link is not present it shows none to skip 5th n iterate rest will have to enter blank string bcoz length of all sets has to be same in dict.
    if(L==5):
        link=""
        post_details['Link'].append(link)
        continue
    link=i.find('iframe' ,class_="youtube-player").get('src')
    post_details['Link'].append(link)
   # print(link)
    


df =pd.DataFrame(post_details)
df


# 8) Write a python program to scrape house details from mentioned URL. It should include house title, location,
# area, EMI and price from https://www.nobroker.in/ .Enter three localities which are Indira Nagar, Jayanagar, 
# Rajaji Nagar.

# In[102]:


# Parsing Webpage
page=requests.get("https://www.nobroker.in/property/sale/bangalore/multiple?searchParam=W3sibGF0IjoxMi45OTgxNzMyLCJsb24iOjc3LjU1MzA0NDU5OTk5OTk5LCJwbGFjZUlkIjoiQ2hJSnhmVzREUE05cmpzUktzTlRHLTVwX1FRIiwicGxhY2VOYW1lIjoiUmFqYWppbmFnYXIifSx7ImxhdCI6MTIuOTc4MzY5MiwibG9uIjo3Ny42NDA4MzU2LCJwbGFjZUlkIjoiQ2hJSmtRTjNHS1FXcmpzUk5oQlFKcmhHRDdVIiwicGxhY2VOYW1lIjoiSW5kaXJhbmFnYXIifSx7ImxhdCI6MTIuOTMwNzczNSwibG9uIjo3Ny41ODM4MzAyLCJwbGFjZUlkIjoiQ2hJSjJkZGxaNWdWcmpzUmgxQk9BYWYtb3JzIiwicGxhY2VOYW1lIjoiSmF5YW5hZ2FyIn1d&radius=2.0&city=bangalore&locality=Rajajinagar,&locality=Indiranagar,&locality=Jayanagar")
page

# Define a user-agent which will help in bypassing the detection as a scraper
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36'
}

# Navigating Parse Tree through beautiful soul
soup=BeautifulSoup(page.content, "html.parser")
soup

# Scraping Data from Nobroker website
house_name=soup.find_all('h2',class_="heading-6 flex items-center font-semi-bold m-0")

# Creating Empty list
House_title=[]
House_location=[]
House_area=[]
House_emi=[]
House_price=[]

# Extracting House Title
house_name=soup.find_all('h2',class_="heading-6 flex items-center font-semi-bold m-0")
for i in house_name:
    House_title.append(i.text)    
House_title

# Extracting House location
house_location=soup.find_all('div',class_="mt-0.5p overflow-hidden overflow-ellipsis whitespace-nowrap max-w-70 text-gray-light leading-4 po:mb-0 po:max-w-95")
for i in house_location:
    House_location.append(i.text)    
House_location

# Extracting House area
house_area=soup.find_all('div',class_="p-1.5p flex border-b border-b-solid border-cardbordercolor tp:py-1p tp:px-1.5p tp:border-b-0")
for i in house_area:
    House_area.append(i.text.split()[3])    
House_area

# Extracting EMI details
emi=soup.find_all('div',class_="p-1.5p flex border-b border-b-solid border-cardbordercolor tp:py-1p tp:px-1.5p tp:border-b-0")
for i in emi:
    House_emi.append(i.text.split()[4][11:24].replace('E',''))
House_emi

# Extracting House Price
price=soup.find_all('div',class_="p-1.5p flex border-b border-b-solid border-cardbordercolor tp:py-1p tp:px-1.5p tp:border-b-0")
for i in price:
    House_price.append(i.text.replace('EMI','').split()[5])
House_price

# Creating dataframe for scrap data
House_details=pd.DataFrame({'House_Name':House_title,'Location':House_location,'Area(in_sqft)':House_area,'EMI':House_emi,'Price(in_lakhs_or_crores)':House_price})
print('\033[1m'+'House Listing on NoBroker.com'+'\033[0m')
House_details.head()


# 9) Write a python program to scrape mentioned details from dineout.co.in :
# i) Restaurant name
# ii) Cuisine
# iii) Location
# iv) Ratings
# v) Image URL

# In[103]:


page= requests.get('https://www.dineout.co.in/delhi-restaurants/buffet-special')

soup=BeautifulSoup(page.content)

soup

titles =[]

for i in soup.find_all('div',class_="restnt-info cursor"):
    titles.append(i.text)
titles

location=[]

for i in soup.find_all('div',class_="restnt-loc ellipsis"):
    location.append(i.text)
location


rates=[]

for i in soup.find_all('span',class_="double-line-ellipsis"):
    rates.append(i.text.replace('₹',''))


rates

images=[]
for i in soup.find_all('img',class_="no-img"):
    images.append(i['data-src'])
images

df=pd.DataFrame({'Titles':titles,'Location':location,'Price':rates,'Images_url':images})
df


# 10) Write a python program to scrape first 10 product details which include product name , price , Image URL from
# https://www.bewakoof.com/women-tshirts?ga_q=tshirts
#     
#  # Above link wasn't giving any product list thus using a new url= https://www.bewakoof.com/women-clothing

# In[104]:


url = 'https://www.bewakoof.com/women-clothing'
# Define a user-agent which will help in bypassing the detection as a scraper
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36'
}

# Creating function for data extration
def product(url):
    data= requests.get(url)
    soup= BeautifulSoup(data.content)
    product=[]
    price=[]
    image=[]
    for i in soup.find_all('div',class_="productCardBox"):
    
        product.append(i.find('h3').text)
        
    for i in soup.find_all('div',class_="productPriceBox clearfix"):
        price.append(i.find('span').text.replace("₹",""))
        
    for i in soup.find_all('div',class_="productCardImg false"):
        image.append(i.find('img')['src'])
    #print(product)
        
        
    data= pd.DataFrame({'Product Name':product,'Price': price, "Image URL": image  })  
    data.index +=1
    
    return data

print('\033[1m'+'Top 10 Women T-shirt on Bewakoof.com'+'\033[0m')
product(url)


# In[ ]:




