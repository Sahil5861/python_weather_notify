import schedule, smtplib, requests
from bs4 import BeautifulSoup

city = "Delhi"
url = "https://www.google.com/search?q=" + "weather" + city

my_email = "sahilkhan05861@gmail.com"
your_email = "mdahil5861@gmail.com"
password = "dnwc lhue hepu vugu"
bad_conditions = ["Rainy", "Rain And Snow", "Showers", "Haze", "Cloudy"]



def umbrella_reminder():
    html = requests.get(url).content
    soup = BeautifulSoup(html, 'html.parser')
    temprature = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
    time_sky = soup.find('div', attrs= 'BNeawe tAd8D AP7Wnd').text

    sky = time_sky.split('\n')[1]
    smtp_object = smtplib.SMTP('smtp.gmail.com', 587)
    smtp_object.starttls()
    subject = "Mohammad sahil Umbrella reminder !!"
    smtp_object.login(my_email, password)

    if sky in bad_conditions:
        body = f'Take an umbrella before leaving the house. Weather conditions for today is {sky} and temperature is {temprature} in {city}'

    else:
        body = f'Weather conditions for today is {sky} and temperature is {temprature} in {city}'


    msg = f"Subject: {subject}\n\n {body}\n\nRegard, \nMohammad sahil".encode('utf-8')
    smtp_object.sendmail(my_email, your_email, msg)
    smtp_object.quit()
    print('Email sent !!')



time = "22:07"
schedule.every().day.at(time).do(umbrella_reminder)
while True:
    schedule.run_pending()











