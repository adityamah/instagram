
from selenium import webdriver
import time
mails=["akhtamahendra@gmail.com","a.khtamahendra@gmail.com","ak.htamahendra@gmail.com","akh.tamahendra@gmail.com","akht.amahendra@gmail.com","akhta.mahendra@gmail.com","akhtam.ahendra@gmail.com","akhtama.hendra@gmail.com","akhtamah.endra@gmail.com","akhtamahe.ndra@gmail.com"] #Add 10 emails within the quotes
users=["ahmad","zakky","rahman","firhan","noer","mashitoh","ahung","Isabelle","Apolline","Cameron"] #Add 10 usernames within the quotes
names=["schoolworshipper","zetachunk","caiklot_23","broughtfunctional","floridasidereal","roiderbankspolythene","grimacingunique","icehockeyinterfere","polyethenetoyah","rawchickencelery"] #Add 10 names within the quotes
pas="Input Password"
for x in range (0,len(mails)): 
browser=webdriver.Firefox()
browser.get("https://instagram.com")
time.sleep(2)
email=browser.find_elements_by_class_name("_qy55y")[0]
name=browser.find_elements_by_class_name("_qy55y")[1]
username=browser.find_elements_by_class_name("_qy55y")[2]
password=browser.find_elements_by_class_name("_qy55y")[3]
email.send_keys(mails[x])
name.send_keys(names[x])
browser.execute_script("document.getElementsByClassName(\"_qy55y\")[2].value=\"\"")
username.send_keys(users[x])
password.send_keys(pas)
time.sleep(2)
browser.find_elements_by_class_name("_1on88")[1].click()
browser.quit()


