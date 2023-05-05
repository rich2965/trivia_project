from sqlalchemy import create_engine, update, MetaData
import pandas as pd
import requests
import json
from bs4 import BeautifulSoup
import time
import random

# initialize engine and the 'movie' table Metadata Object
engine = create_engine('postgresql://root:Tester2965@34.69.30.119:5432/triviapractice')
engine.connect()
meta = MetaData(bind=engine)
MetaData.reflect(meta)
movie_tbl = meta.tables['people_popular']

user_agents = [
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:54.0) Gecko/20100101 Firefox/54.0",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/602.4.8 (KHTML, like Gecko) Version/10.0.3 Safari/602.4.8",
"Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; AS; rv:11.0) like Gecko",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Safari/537.36 Edge/13.10586"
]


def retrieve_page(person_id):
    attempt = 1
    while True:
        try: 
            # URL of IMDb photo gallery page to be scraped
            url = f"https://www.imdb.com/name/{person_id}/"
            # Send a request to the URL
            random_user_agent = random.choice(user_agents)
            headers = {"User-Agent": random_user_agent}
            response = requests.get(url, headers=headers)

            # Parse the HTML content using BeautifulSoup
            soup = BeautifulSoup(response.content, 'html.parser')
            return soup
        except Exception as e:
            print(e)
            if attempt < 4: # 3 attempts before failing.
                attempt += 1

def retrieve_still_image(soup,person_id):
    # Find the div element by class name
    try:
        div_element = soup.find("script", id="__NEXT_DATA__")
        person_data = json.loads(div_element.text)
        image_url_list = []
        primary_image = person_data['props']['pageProps']['mainColumnData']['primaryImage']['url']
        image_url_list.append(primary_image)
        # for i in range(0,4): 
        for i,image_node in zip(range(4),person_data['props']['pageProps']['mainColumnData']['images']['edges']): #Look at only the first 4 images
            image_url = image_node['node']['url'] 
            image_url_list.append(image_url)
        return image_url_list
    except:
        image_url_list = []
        print(f"No still photos found for ID: {person_id}")
        Exception
        return(image_url_list)

def retrieve_knownfor(soup,person_id):
    # Find the div element by class name
    try:
        div_element = soup.find("script", id="__NEXT_DATA__")
        person_data = json.loads(div_element.text)
        knownfor_list = []
        # for i in range(0,4): 
        for i,knownfor_node in zip(range(5),person_data['props']['pageProps']['mainColumnData']['knownFor']['edges']): #Look at only the first 4 images
            knownfor_node_title = knownfor_node['node']['title']['titleText']['text']
            knownfor_list.append(knownfor_node_title)
        return knownfor_list
    except Exception as e:
        knownfor_list = []
        print(f"No known for titles found for person ID: {person_id}")
        print(e)
        return(knownfor_list)
    
def create_update_statement(person_id,update_dict):
    update_statement = update(movie_tbl)
    update_statement = update_statement.values(update_dict)
    update_statement = update_statement.where(movie_tbl.c.person_id == person_id)
    return update_statement

def main():
    # 1) Query against database to obtain a person_id that doesn't have an image associated yet
    query = 'SELECT * FROM people_popular WHERE imagery is null'
    resultset = pd.read_sql_query(sql=query, con=engine.connect())
    person_list = resultset['person_id']

    for person_id in person_list:
        print(f"Processing PersonId: {person_id}")
        imdb_page = retrieve_page(person_id) # 2) Use the person_id and pass it into the IMDb url
        image_url_list = retrieve_still_image(imdb_page,person_id) # 3) Parse the response to get the first still_image URL found. 
        knownfor_list = retrieve_knownfor(imdb_page,person_id)
        update_dict = {"imagery":image_url_list, "knownForList":knownfor_list}
        update_statement = create_update_statement(person_id,update_dict) #4) Create the Update Statement
        engine.execute(update_statement)  #5) Execute the Update Statement
        time.sleep(random.randint(1, 10))


if __name__ == "__main__":
    main()