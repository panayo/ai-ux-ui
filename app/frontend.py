# import sqlite3
# import streamlit as st
# from io import BytesIO
# from selenium import webdriver
# from PIL import Image
# from urllib.parse import urlparse
# import pytesseract
# from nltk.tokenize.treebank import TreebankWordDetokenizer
# import re
# from nltk.corpus import stopwords
# import nltk 
# from collections import Counter
# from wordcloud import WordCloud
# import matplotlib.pyplot as plt
# from urllib.parse import urlparse
# import os

# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager

# @st.experimental_singleton
# def get_driver():
#     return webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)



# def website_screenshot(url : str, width : int = 1920,
#                        height : int = 1080,full_website : bool = False ):

#     driver = get_driver()
                       
#     options = webdriver.ChromeOptions()
#     options.headless = True
#     options.add_argument('--disable-extensions')
#     options.add_argument('--headless')
#     options.add_argument('--disable-gpu')
#     options.add_argument('--no-sandbox')
#     options.add_argument('start-maximized')
#     options.add_argument('disable-infobars')
#     driver = webdriver.Chrome(options=options)
#     driver.get(url)
    
#     if full_website:
#         S = lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)
#         driver.set_window_size(S('Width'),S('Height'))
#         screenshot = driver.get_screenshot_as_png()
#         screenshot_bytes = BytesIO(screenshot)

#     else:
#         screenshot = driver.get_screenshot_as_png()
#         screenshot_bytes = BytesIO(screenshot)

#     screenshot_img = Image.open(screenshot_bytes)
#     driver.quit()
#     return screenshot_img


# def wordcloud(img):
#     custom_config = r'--oem 3 --psm 6'
#     website_text = pytesseract.image_to_string(img, config=custom_config)
#     website_text = website_text.lower()

#     for character in '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~\n©»«™—':
#         website_text = website_text.replace(character,' ')
#     website_text = re.sub(' +', ' ', website_text)
#     word_tokens = nltk.word_tokenize(website_text)
#     stop = set(stopwords.words("english"))
#     word_tokens = [word for word in word_tokens if word not in stop]
#     word_tokens = [word for word in word_tokens if len(word)>1]

#     website_text = TreebankWordDetokenizer().detokenize(word_tokens)
    
#     word_count = Counter(word_tokens)

#     wordcloud = WordCloud(width = 800, height = 800,
#                 background_color ='white',
#                 stopwords = stop,
#                 min_font_size = 10).generate(website_text)

#     st.set_option('deprecation.showPyplotGlobalUse', False)

#     plt.imshow(wordcloud, interpolation='bilinear')
#     plt.axis("off")
#     plt.tight_layout(pad = 0)
#     plt.savefig("wordcloud.png")
#     #plt.show()
#     #st.pyplot()
#     st.image("wordcloud.png",caption="Wordcloud",width=300)

# st.title("Welcome to the UX Web Analyzer")
# st.markdown("[Panayotis Papoutsis](https://www.linkedin.com/in/panayotis-papoutsis/)")
# url = st.text_input("Enter a valid url to analyze:")
# full_website = st.checkbox("Full website screenshot?")

# st.button('Submit')
# col1, col2 = st.columns([2,1])

# if url:
#     parsed_url = urlparse(url)
#     if parsed_url.scheme and parsed_url.netloc:
#         try:
#             if full_website :
#                 img = website_screenshot(url,full_website=full_website)
#                 # st.write('test ok')
#             else:
#                 #st.write('test ok')
#                 img = website_screenshot(url)
#             #conn = sqlite3.connect('screenshots.db')
#             #c = conn.cursor()
#             #c.execute("CREATE TABLE IF NOT EXISTS screenshots (url text, full_website boolean)")
#             #c.execute("INSERT INTO screenshots (url, full_website) VALUES (?,?)",(url, full_website))
#             #conn.commit()
#             #conn.close()
#             with col1:
#                 wordcloud(img=img)
#                 #st.image('./app/scoring.png',caption='Scoring of the Website (demo)',width = 300)
#                 #st.image('./app/scoring.png',caption='Scoring of the Website (demo)',width = 300)
#             with col2:
#                 st.image(img, caption='Screenshot of the Website',width=300)
#                 st.image('./app/scoring.png',caption='Scoring of the Website (demo)',width = 300)    
#         except:
#             st.error("An error occurred while trying to access the URL. Please check if the URL is valid and try again.")
#     else:
#         st.error("Please enter a valid URL.")
# else:
#     st.info("Please enter a URL to analyze.")

import streamlit as st

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@st.experimental_memo(show_spinner=False,suppress_st_warning=True)
def get_driver():
    return webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

options = Options()
options.add_argument('--disable-gpu')
options.add_argument('--headless')

driver = get_driver()
driver.get('http://example.com')

st.code(driver.page_source)

