## web crawling

정보를 수집하는 행위를 말한다.

```python
# 필요한 패키지 설치
from GoogleImageScrapper import GoogleImageScraper
import os
import time

sleep_between_interactions = 1
# 웹드라버 경로
webdriver_path = os.getcwd()+".\\webdriver\\chromedriver.exe"
# 이미지 경로
image_path = os.getcwd()+".\\images"

#search_keys= ["woodpecker","owl"]
search_keys= ["raccoon"]
number_of_images = 10
headless = False
#min_resolution = (width,height)
min_resolution=(0,0)
#max_resolution = (width,height)
max_resolution=(2000,2000)
for search_key in search_keys:
    image_scrapper = GoogleImageScraper(webdriver_path,image_path,search_key,number_of_images,headless,min_resolution,max_resolution)
    image_urls = image_scrapper.find_image_urls()
    image_scrapper.save_images(image_urls)
    time.sleep(sleep_between_interactions)
```

### 인터파크 크롤링

```python
from selenium import webdriver as wd
from bs4 import BeautifulSoup as bs
from selenium.webdriver.common.by import By
# 명시적 대기를 위해 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

# 상품 정보를 담는 클레스
class TourInfo:
    # 맴버변수 (실제 컬럼보다는 작게 세팅했음)
    title = ''
    price = ''
    area  = ''
    link  = ''
    img   = ''
    contents = ''
    # 생성자
    def __init__(self, title, price, area, link, img, contents=None ):
        self.title = title
        self.price = price
        self.area  = area
        self.link  = link
        self.img   = img
        self.contents = contents

# 사전에 필요한 정보를 로드 => 디비혹스 쉘, 베치 파일에서 인자로 받아서 세팅

main_url = 'http://tour.interpark.com/' 
keyword  = '골프'
# 상품 정보를 담는 리스트 (TourInfo 리스트)
tour_list = []

# 윈도우용
driver = wd.Chrome(executable_path='.\\webdriver\\chromedriver.exe')
# 사이트 접속 (get)
driver.get(main_url)

# 검색창을 찾아서 검색어 입력
# id : SearchGNBText
driver.find_element_by_id('SearchGNBText').send_keys(keyword)
# 수정할경우 => 뒤에 내용이 붙어버림 => .clear() -> send_keys('내용')
# 검색 버튼 클릭
time.sleep(2)
driver.find_element_by_css_selector('button.search-btn').click()

# 잠시 대기 => 페이가 로드되고 나서 즉각적으로 데이터를 획득 하는 행위는 
# 명시적 대기 => 특정 요소가 로케이트(발결된때까지) 대기
try:
    element = WebDriverWait(driver, 10).until(
        # 지정한 한개 요소가 올라면 웨이트 종료
        EC.presence_of_element_located( (By.CLASS_NAME, 'oTravelBox') )
    )
except Exception as e:
    print( '오류 발생', e)
# 암묵적 대기 => DOM이 다 로드 될때까지 대기 하고 먼저 로드되면 바로 진행
# 요소를 찾을 특정 시간 동안 DOM 풀링을 지시 예를 들어 10 초이내 라로 
# 발견 되면 진행
driver.implicitly_wait( 10 )
# 절대기 대기 => time.sleep(10) -> 클라우드 페어(디도스 방어  솔류션)
# 더보기 눌러서 => 게시판 진입 
driver.find_element_by_css_selector('.oTravelBox>.boxList>.moreBtnWrap>.moreBtn').click()
```



### 네이버 크롤링

버튼이름이나 변수명은 자주 바뀐다

```python
# 사전에 필요한 정보를 로드 => 디비혹스 쉘, 베치 파일에서 인자로 받아서 세팅

main_url = 'http://www.naver.com/' 
keyword  = '한화에어로스페이스'
# 상품 정보를 담는 리스트 (TourInfo 리스트)
tour_list = []
# 크롬 열기
driver = wd.Chrome(executable_path='.\\webdriver\\chromedriver.exe')
driver.get(main_url)
driver.find_element_by_id('query').send_keys(keyword)
driver.close()
```



## camelot

.pdf 파일의 표를 추출하는 법

```python
pip install camelot

import camelot
#import sys
tables=camelot.read_pdf('foo.pdf')

tables[0].df
# 엑셀파일로 저장
tables[0].to_excel('table0.xlsx')
```

