import requests
from bs4 import BeautifulSoup
import random
import pandas as pd
from sqlalchemy import create_engine
from dateutil.parser import parse
import time

#Connect to SQL Database
engine = create_engine('postgresql://root:Tester2965@34.69.30.119:5432/triviapractice')
engine.connect()

#User_agents to pass in the requests to make it harder to detect as a bot
user_agents = [
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:54.0) Gecko/20100101 Firefox/54.0",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/602.4.8 (KHTML, like Gecko) Version/10.0.3 Safari/602.4.8",
"Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; AS; rv:11.0) like Gecko",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Safari/537.36 Edge/13.10586"
]

# Only looking at 
year_list = list(range(1950,2001))


def retrieve_page(year):
    attempt = 1
    while True:
        try: 
            # Get the HTML content of the Wikipedia page
            url = f"https://en.wikipedia.org/wiki/{year}"
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



def starts_with_date(string, fuzzy=False):
    """
    Return whether the string can be interpreted as a date.

    :param string: str, string to check for date
    :param fuzzy: bool, ignore unknown tokens in string if True
    """
    try: 
        date_string = string.split(' ')[0] + ' ' + string.split(' ')[1]
        parse(date_string, fuzzy=fuzzy)
        return date_string

    except:
        return False


for year in year_list:
    soup = retrieve_page(year)
    if soup:
        print(f"Processing Year: {year}")
        event_year = year

        # Find the first element, Events start
        element_1 = soup.find("span", id="Events")

        # Find the second element, Births Start
        element_2 = soup.find("span", id="Births")

        #Find the third element, Deaths Start
        element_3 = soup.find("span", id="Deaths")
        # print(element_2)

        try:
            # Parse the Events
            # Find all the <li> elements between element_1 and element_2
            all_li_elements = []
            current_element = element_1.find_next("li")

            while current_element != element_2:
                # print(current_element)
                if current_element.name == "li":
                    all_li_elements.append(current_element.text.strip())
                    # print(current_element.text.strip())
                current_element = current_element.next_element

            event_list = []

            for item in all_li_elements:
                event_date = starts_with_date(item)
                event_type = 'historical_event'
                if event_date:
                    # date = starts_with_date(item)
                    # print(date)
                    if '\n' in item:
                        event_date = event_date.split('\n')[0]
                        for event in item.splitlines()[1:]:
                            event_list.append([event_year,event_date,event_type,event])
                    else:
                        event_desc = item.split(' ')[3:]
                        event_desc = ' '.join(event_desc)
                        #item = item.replace(' – ','||').replace(' — ','||').replace(' - ','||')
                        event_list.append([event_year,event_date,event_type,event_desc])
        except:
            print("No Events Found")   

        try:
            # Parse the births
            # Find all the <li> elements between element_1 and element_2
            all_li_birth_elements = []
            current_element = element_2.find_next("li")

            while current_element != element_3:
                # print(current_element)
                if current_element.name == "li":
                    all_li_birth_elements.append(current_element.text.strip())
                    # print(current_element.text.strip())
                current_element = current_element.next_element

            for item in all_li_birth_elements:
                event_date = starts_with_date(item)
                event_type = 'person_birth'
                if event_date:
                    # date = starts_with_date(item)
                    # print(date)
                    if '\n' in item:
                        date = item.split('\n')[0]
                        for event in item.splitlines()[1:]:
                            event_list.append([event_year,date,event_type,event])
                    else:
                        event_desc = item.split(' ')[3:]
                        event_desc = ' '.join(event_desc)
                        event_desc = event_desc + ' is born.'
                        #item = item.replace(' – ','||').replace(' — ','||').replace(' - ','||')
                        event_list.append([event_year,event_date,event_type,event_desc])
        except:
            print("No births found")

        # create a DataFrame from the list
        df = pd.DataFrame(event_list, columns=['event_year', 'event_date','event_type', 'event_desc'])
        # upload to SQL Server
        df.to_sql(name='events',con=engine,if_exists='append',index=None)
    else:
        print(f"Couldn't retrieve data for year: {year}")
    time.sleep(random.randint(1, 10))

