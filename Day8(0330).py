#웹 스크랩핑 실습

import requests
from bs4 import BeautifulSoup

url = 'https://movie.daum.net/ranking/reservation'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

ol = soup.select_one('.list_movieranking')
li_list = ol.find_all('li')
print(li_list)

movie = []

for li in li_list:
    rank = li.select_one('.rank_num').text
    name = li.select_one('.link_txt').text
    see = li.select_one('.ico_see').text
    grade = li.select_one('.txt_grade').text
    num = li.select_one('.txt_num').text[:-1]
    mvdate = li.select_one('.txt_info > .txt_num').text
    
    movie.append([rank,name,see,grade,num,mvdate])
    print(rank,name,see,grade,num,mvdate)
    
print(movie)

import pandas as pd #데이터 프레임을 csv파일로 csv파일을 데이터 프레임 파일로 만들어야함

df = pd.DataFrame(movie, columns = ['순위','영화명','관람가','평점','예매율','개봉일'])

df.to_csv('movie_info.csv',index=False, encoding='cp949')
    
df=pd.read_csv('movie_info.csv',encoding='cp949')#형변화 해주기(오브젝트라서)
    
print(df.info())
print(df[(df['평점']>8)])

import matplotlib
import matplotlib.pyplot as plt
matplotlib.rcParams['font.family'] = 'Malgun Gothic'

df['개봉일'] = pd.to_datetime(df['개봉일'],format='%y.%m.%d')
#print(df.info())

df_weekly = df.resample('W', on='개봉일').mean(numeric_only = True )#숫자가 아닌것은 워닝이 뜨기 때문에 뉴머릭 쓴다
df_weekly = df_weekly.fillna(0)#nan 처리
print(df_weekly)

plt.plot(df_weekly.index,df_weekly['예매율'])
plt.show()


