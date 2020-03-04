import discord
import os
import urllib.request
from bs4 import BeautifulSoup

#코로나

# *참고 <변수이름>

# 확진자 = confirmedPatient
# 의심 환자 = suspectedPatient
# 격리 해제 = curedPatient
# 사망자 =  diedPatient

#디스코드
client = discord.Client()

blacklist = ['씨발', '시발', '^^ㅣ발', '병신', '새끼', '지랄', 'ㅅㅂ', 'ㅂㅅ', 'ㅅㄲ', 'ㅈㄹ', '애미', 'ㅇㅁ']

@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    await client.change_presence(status=discord.Status.online, activity=discord.Game("엄준식은 죽었지만 살아있다"))


@client.event
async def on_message(message):
    if message.content == ("안녕"):
        await message.channel.send("나도 안녕")

    if message.content == ("엄"):
        await message.channel.send(file=discord.File("엄.png"))

    if any(x in message.content.lower() for x in blacklist):
        await message.channel.send("욕하지마 ^ㅣ발련아")
        await message.channel.send(file=discord.File("욕하지마.png"))

    if message.content.startswith("코로나"):

        url = 'https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query=%EC%BD%94%EB%A1%9C%EB%82%98'
        html = urllib.request.urlopen(url).read()
        soup = BeautifulSoup(html, 'html.parser')

        people = soup.findAll('strong', {'class': 'num'})
        data_list = []
        for i in people:
            data_list.append(i.get_text().replace('\n', '').replace(' ', ''))
        await message.channel.send("확진자 " + data_list[0] + "\n격리해제 " + data_list[1] + "\n검사 진행 " + data_list[2] + "\n사망자 " + data_list[3])

access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
