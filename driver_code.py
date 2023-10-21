from time import sleep 
from faker import Faker
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pickle
from prettytable import PrettyTable

fake = Faker()
def database(data):
    try:
        with open('data.dat','rb') as f:
            raw_data = pickle.load(f)
        with open('data.dat','wb') as f:
            raw_data.append(data)
            print(raw_data)
            pickle.dump(raw_data,f)
            print("\n\nData Updated!")
            table = PrettyTable()
            table.field_names = ["Name", "Mail", "Password", "BirthDate", "Gender"]
            for x in raw_data:
                table.add_row([x[2], x[0], x[1], (str(x[5])+"-"+x[4]+"-"+str(x[3])), x[7]])
            table.align["Name"] = "l"
            print(table)


    except FileNotFoundError:
        with open('data.dat','wb') as f:
            pickle.dump([data,],f)
            print("File Created! Data Added!")

def display():
    with open('data.dat','rb') as f:
        raw_data = pickle.load(f)
        table = PrettyTable()
        table.field_names = ["Name", "Mail", "Password", "BirthDate", "Gender"]
        for x in raw_data:
            table.add_row([x[2], x[0], x[1], (str(x[5])+"-"+x[4]+"-"+str(x[3])), x[7]])
        table.align["Name"] = "l"
        print(table)
def gen_id():
    present_year = 2023
    gen_no = random.randint(0,100)
    profile = fake.profile()
    email = (profile['mail'].split("@")[0]+"_"+str(gen_no)+"@"+profile['mail'].split("@")[1])
    name = profile['name']
    dob = profile['birthdate'].strftime("%d %b %Y").split(" ")
    if int(dob[2])+16>present_year:
        dob[2] = int(dob[2])-18
    elif int(dob[2])<present_year-80:
        dob[2] = int(dob[2])+30
    else:
        dob[2] = int(dob[2])
    password = profile['username'] + str(dob[2]+100)
    gender = profile['sex']
    data = [email,name,dob,password,gender]
    return [email, password, name,dob[2],dob[1],dob[0],dob[0],gender]


def run_driver():

    while True:
        try:
            edge_options = webdriver.EdgeOptions()
            test_ua = f'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{random.randint(99,160)}.0.{random.randint(7777,9999)}.999 Safari/537.36'
            # edge_options.add_argument("--headless=new")
            edge_options.add_argument(f'--user-agent={test_ua}')
            edge_options.add_argument('--no-sandbox')
            edge_options.add_argument("--disable-extensions")
            edge_options.use_chromium = True
            driver = webdriver.Edge(options=edge_options)
            driver.get("https://www.spotify.com/in-en/signup?forward_url=https%3A%2F%2Fopen.spotify.com%2F")
            fields = ['email', 'password', 'displayname', 'year','month', 'day','day']
            values = gen_id()
            print(values)
            for x in range(6):
                input_field = driver.find_element(By.NAME, fields[x])
                value = values[x]
                input_field.send_keys(value)
                input_field.send_keys(Keys.TAB)
            gender_raw = values[7]
            if gender_raw=="M":
                num = 1
            else:
                num=2
            gender_btn = driver.find_element(By.XPATH, f'''/html/body/div[1]/main/div/div/form/fieldset/div/div[{num}]/label/span[1]''')
            gender_btn.click()
            timeout = 10
            driver.find_element(By.TAG_NAME,"body").send_keys(Keys.END)
            sleep(0.1)
            submit = WebDriverWait(driver, timeout).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '#__next > main > div > div > form > div.EmailForm__Center-jwtojv-0.bTvwxQ'))
            )
            submit.click()
            def check_url_change(driver):
                if "https://open.spotify.com" in driver.current_url:
                    database(values)
                return "https://open.spotify.com" in driver.current_url
            WebDriverWait(driver, 30).until(check_url_change)
            driver.quit()

        except Exception as Error:
            print(Error)


# cat is cool
run_driver()
