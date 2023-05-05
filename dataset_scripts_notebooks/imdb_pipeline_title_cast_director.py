from sqlalchemy import create_engine, update, MetaData
import pandas as pd
import requests
import json
from bs4 import BeautifulSoup
import time
import random

user_agents = [
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:54.0) Gecko/20100101 Firefox/54.0",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/602.4.8 (KHTML, like Gecko) Version/10.0.3 Safari/602.4.8",
"Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; AS; rv:11.0) like Gecko",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Safari/537.36 Edge/13.10586"
]

# initialize engine and the 'movie' table Metadata Object
engine = create_engine('postgresql://root:Tester2965@34.69.30.119:5432/triviapractice')
engine.connect()
meta = MetaData(bind=engine)
MetaData.reflect(meta)
movie_tbl = meta.tables['movie_us_popular']

def retrieve_page(title_id):
    attempt = 1
    while True:
        try: 
            # URL of IMDb photo gallery page to be scraped
            url = f"https://www.imdb.com/title/{title_id}"
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


def retrieve_characters(soup,title_id):
    # Find the div element by class name
    try:
        div_element = soup.find("script", id="__NEXT_DATA__")
        character_data = json.loads(div_element.text)
        character_list = []
        person_id_list = []
        # for i in range(0,4): 
        for i,knownfor_node in zip(range(5),character_data['props']['pageProps']['mainColumnData']['cast']['edges']): #Look at only the first 4 images
            person_id = knownfor_node['node']['name']['id']
            person_name = knownfor_node['node']['name']['nameText']['text']
            character_name = knownfor_node['node']['characters'][0]['name']
            character_list.append(f"{character_name} ({person_name})")
            person_id_list.append(person_id)
        return character_list,person_id_list
         
    except:
        storyline = None
        print(f"No characters found for TitleID: {title_id}")
        Exception
        return(storyline)

def retrieve_director(soup,title_id):
    # Find the div element by class name
    try:
        div_element = soup.find("script", id="__NEXT_DATA__")
        data = json.loads(div_element.text)
        director_data = data['props']['pageProps']['mainColumnData']['directors'][0]
        director_id = director_data['credits'][0]["name"]["id"]
        director_name = director_data['credits'][0]["name"]["nameText"]["text"]

        return director_id,director_name
         
    except:
        storyline = None
        print(f"No characters found for TitleID: {title_id}")
        Exception
        return(storyline)


def create_update_statement(title_id,update_dict):
    update_statement = update(movie_tbl)
    update_statement = update_statement.values(update_dict)
    update_statement = update_statement.where(movie_tbl.c.id == title_id)
    return update_statement
def main():
    # 1) Query against database to obtain a title_id that doesn't have an image associated yet, filter by movie types only at the moment
    query = 'SELECT * FROM movie_us_popular_vw'
    resultset = pd.read_sql_query(sql=query, con=engine.connect())
    title_list = resultset['id']

    # 2) Use the title_id and pass it into the IMDb url = "https://www.imdb.com/title/{title_id}/mediaindex?refine=still_frame"
    # 3) Parse the response to get the first still_image URL found. 

    for title_id in title_list:
        print(f"Processing TitleID: {title_id}")
        imdb_page = retrieve_page(title_id)
        characters_list,people_list = retrieve_characters(imdb_page,title_id)
        director_id,director_name = retrieve_director(imdb_page,title_id)
        update_dict = {"characters":characters_list, "peopleList":people_list,"director_id":director_id,"directorName":director_name}
        update_statement = create_update_statement(title_id,update_dict)
        engine.execute(update_statement)
        time.sleep(random.randint(1, 10))

if __name__ == "__main__":
    main()