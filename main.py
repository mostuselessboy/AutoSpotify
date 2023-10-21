import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QLineEdit, QCheckBox, QListWidget, QListWidgetItem
from PyQt5.QtGui import QPixmap, QIcon, QFontDatabase, QFont,QMovie
from PyQt5.QtCore import Qt
from time import sleep 
from faker import Faker
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pickle
import threading
fake = Faker()

class SpotifyApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        QFontDatabase.addApplicationFont("Poppins-Regular.ttf")
        QFontDatabase.addApplicationFont("Silkscreen-Regular.ttf")
        layout = QVBoxLayout()
        nav_layout = QVBoxLayout()
        spotify_logo = QLabel(self)
        movie = QMovie('i-2.gif') 
        spotify_logo.setMovie(movie)
        spotify_logo.setAlignment(Qt.AlignCenter)

        movie.start()


        spotify_title = QLabel(' Spotify Generator ')
        spotify_title.setFont(QFont("Poppins", 44))
        spotify_subtitle = QLabel('<SELENIUM STATS HERE>')
        spotify_subtitle.setFont(QFont("Poppins", 14))
        nav_layout.addWidget(spotify_logo)
        nav_layout.addWidget(spotify_title)
        nav_layout.addWidget(spotify_subtitle)
        main_layout = QHBoxLayout()
        column1_layout = QVBoxLayout()
        headless_checkbox = QCheckBox('Headless')
        limited_run_checkbox = QCheckBox('Limited Run')
        limited_run_input = QLineEdit()
        limited_run_input.setPlaceholderText("Enter Run Count.") 
        url_input = QLineEdit()
        url_input.setPlaceholderText("Enter URL for Profile/Playlist.") 
        start_spotify_button = QPushButton('Create Account 🧔')
        column1_layout.addWidget(limited_run_checkbox)
        column1_layout.addWidget(limited_run_input)
        column1_layout.addWidget(headless_checkbox)
        column1_layout.addWidget(url_input)
        column2_layout = QVBoxLayout()
        item_list = QListWidget()

        #ADD DATA FROM FILE
        with open('data.dat','rb') as f:
            raw_data = pickle.load(f)
            for num, x in enumerate(raw_data):
                # data = x[2]+": "+ x[0]+": "+ x[1]+": "+ (str(x[5])+"-"+x[4]+"-"+str(x[3]))+": "+ x[7]
                if x[7] == 'M':
                    data = "🍀" +str(num+1) +" " +x[2]
                else:
                    data = "🍁" +str(num+1) +" " +x[2]
                item_list.addItem(QListWidgetItem(data))

        column2_layout.addWidget(item_list)
        main_layout.addLayout(column1_layout)
        main_layout.addLayout(column2_layout)
        like_button = QPushButton('Like Playlist💖')
        follow_button = QPushButton('Follow User🍀')
        button_layout = QHBoxLayout()
        button_layout.addWidget(start_spotify_button)
        button_layout.addWidget(like_button)
        button_layout.addWidget(follow_button)


        # Add navigation bar and main window to the main layout
        layout.addLayout(nav_layout)
        layout.addLayout(main_layout)
        layout.addLayout(button_layout)

        # Apply stylesheets for Spotify-inspired design
        self.setStyleSheet("""background-color: #1db954;color: white;padding: 10px;""")
        spotify_title.setStyleSheet("margin:0; background:#121212; border-radius:10px;")
        spotify_logo.setStyleSheet("background:#FF4136; padding:0; border-radius:10px;")
        spotify_subtitle.setStyleSheet("margin:0; font-weight:bold; color:rgb(203, 245, 92); background:rgb(64, 0, 115); border-radius:10px; font-family:'silkscreen'; font-size:30px;")
        item_list.setStyleSheet("background-color: #121212; color: white; font-family:'Poppins'; font-size:20px; border: 1px solid #535353; border-radius:10px;")
        limited_run_checkbox.setStyleSheet("background-color: #121212; color: white; font-family:'Poppins'; font-size:20px; border: 1px solid #535353; border-radius:10px;")
        headless_checkbox.setStyleSheet("background-color: #121212; color: white; font-family:'Poppins'; font-size:20px; border: 1px solid #535353; border-radius:10px;")
        limited_run_input.setStyleSheet("background-color: #FF74A2; color: #FFCCD3; font-family:'Poppins'; font-size:20px; border: 1px solid #535353; border-radius:10px;")
        url_input.setStyleSheet("background-color: #FF4136; color: #FFCCD3; font-family:'Poppins'; font-size:20px; border: 1px solid #535353; border-radius:10px;")
        start_spotify_button.setStyleSheet("QPushButton{ font-weight:bold; font-family:'Poppins'; color:rgb(203, 245, 92); background:#121212; border-radius:10px; font-size:20px; padding: 10px } QPushButton:hover{ color:#121212; background:rgb(203, 245, 92); }")
        like_button.setStyleSheet("QPushButton{ font-weight:bold; font-family:'Poppins'; color:rgb(203, 245, 92); background:#121212; border-radius:10px; font-size:20px; padding: 10px } QPushButton:hover{ color:#121212; background:rgb(203, 245, 92); }")
        follow_button.setStyleSheet("QPushButton{ font-weight:bold; font-family:'Poppins'; color:rgb(203, 245, 92); background:#121212; border-radius:10px; font-size:20px; padding: 10px } QPushButton:hover{ color:#121212; background:rgb(203, 245, 92); }")


        nav_layout.setAlignment(Qt.AlignTop)
        spotify_logo.setAlignment(Qt.AlignCenter)
        spotify_title.setAlignment(Qt.AlignCenter)
        spotify_subtitle.setAlignment(Qt.AlignCenter)

        self.setLayout(layout)
        self.setWindowTitle('AutoSpotify')
        self.setWindowIcon(QIcon("spotify_logo.png"))
        self.setGeometry(100, 100, 800, 600)
        self.show()


        def genProfile():
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

        def updateDatabase(data):
            try:
                with open('data.dat','rb') as f:
                    raw_data = pickle.load(f)
                with open('data.dat','wb') as f:
                    raw_data.append(data)
                    pickle.dump(raw_data,f)

            except FileNotFoundError:
                with open('data.dat','wb') as f:
                    pickle.dump([data,],f)

        def startDriver():
            # spotify_subtitle.setText("hi")

            count = int(limited_run_input.text())
            total_count = count
            count = 1
            error = 0
            start_spotify_button.setText(f"Create Account ({count}/{total_count})")
            while count!=total_count+1:
                try:
                    spotify_subtitle.setText("Opening EdgeDriver")
                    edge_options = webdriver.EdgeOptions()
                    test_ua = f'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{random.randint(99,160)}.0.{random.randint(1000,9999)}.999 Safari/537.36'
                    edge_options.add_argument("--headless=new")
                    edge_options.add_argument(f'--user-agent={test_ua}')
                    edge_options.add_argument('--no-sandbox')
                    edge_options.add_argument("--disable-extensions")
                    edge_options.use_chromium = True
                    driver = webdriver.Edge(options=edge_options)
                    spotify_subtitle.setText("Browser Configurations..")
                    driver.get("https://www.spotify.com/in-en/signup?forward_url=https%3A%2F%2Fopen.spotify.com%2F")
                    spotify_subtitle.setText("Opening Spotify")
                    fields = ['email', 'password', 'displayname', 'year','month', 'day','day']
                    values = genProfile()
                    spotify_subtitle.setText(f"Generating Fake ID: {values[2]}")
                    for x in range(6):
                        input_field = driver.find_element(By.NAME, fields[x])
                        value = values[x]
                        input_field.send_keys(value)
                        # input_field.send_keys(Keys.TAB)
                        spotify_subtitle.setText(f"{values[2]}: {fields[x]} Updated!")
                    gender_raw = values[7]
                    if gender_raw=="M":
                        num = 1
                    else:
                        num=2
                    gender_btn = driver.find_element(By.XPATH, f'''/html/body/div[1]/main/div/div/form/fieldset/div/div[{num}]/label/span[1]''')
                    gender_btn.click()
                    spotify_subtitle.setText(f"{values[2]}Gender Updated!")
                    timeout = 10
                    driver.find_element(By.TAG_NAME,"body").send_keys(Keys.END)
                    sleep(0.1)
                    submit = WebDriverWait(driver, timeout).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR, '#__next > main > div > div > form > div.EmailForm__Center-jwtojv-0.bTvwxQ'))
                    )
                    submit.click()
                    spotify_subtitle.setText("Waiting For Authentication..")

                    def check_url_change(driver):
                        if "https://open.spotify.com" in driver.current_url:
                            updateDatabase(values)
                            spotify_subtitle.setText("🎊SUCCESSFUL!🎉")
                            item_list.clear()
                            with open('data.dat','rb') as f:
                                raw_data = pickle.load(f)
                                raw_data = raw_data[::-1]
                                len_raw_data = len(raw_data)
                                for num, x in enumerate(raw_data):
                                    # data = x[2]+": "+ x[0]+": "+ x[1]+": "+ (str(x[5])+"-"+x[4]+"-"+str(x[3]))+": "+ x[7]
                                    if x[7] == 'M':
                                        data = "🍀" +str(len_raw_data-num) +" " +x[2]
                                    else:
                                        data = "🍁" +str(len_raw_data - num) +" " +x[2]
                                    item_list.addItem(QListWidgetItem(data))
                            # item_list.scrollToBottom()

                        return "https://open.spotify.com" in driver.current_url
                    WebDriverWait(driver, 10).until(check_url_change)
                    driver.quit()

                except Exception as Error:
                    print(Error)
                    error+=1
                    spotify_subtitle.setText("Failure!❌")
                count=count+1
                start_spotify_button.setText(f"Create Account ({count}/{total_count})")
            spotify_subtitle.setText(f"Stats: {total_count-error} ✅ {error} ❌")
        def THREAD_startDriver():
            thrd = threading.Thread(target=startDriver)
            thrd.start()
        start_spotify_button.clicked.connect(THREAD_startDriver)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = SpotifyApp()
    sys.exit(app.exec_())
