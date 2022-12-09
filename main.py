from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import pandas as pd
import time
url = 'https://clutch.co/web-developers'

driver=webdriver.Chrome("C:\chromedriver.exe")
driver.get(url)
time.sleep(1)
def get_content(xpath,i):
    name_comp= driver.find_elements(By.XPATH,xpath)
    return name_comp[i].text

def get_link(class_name,att,i):
    list_items= driver.find_elements(By.CLASS_NAME,class_name)
    return list_items[i].get_attribute(att)

def op_excel(rows):
    headers=['Company', 'Website', 'Location', 'Contact', 'Rating', 'Review Count','Hourly Rate', 'Min Project Size', 'Employee Size']
    df = pd.DataFrame(rows,columns=headers)
    df.to_excel('Output.xlsx', sheet_name='Sheet1', index=False)

def get_total_pages(className , attribute):
    content = driver.find_elements(By.CLASS_NAME, className)
    no_of_pages = content[-1].get_attribute(attribute)
    return int(no_of_pages)

total_pages=get_total_pages("page-link" , "data-page")    
total_comp_on_page=driver.find_elements(By.XPATH,"//ul[@class='directory-list']/li")
no_of_comp=(len(total_comp_on_page))
companies=[]
for n in range(no_of_comp):
    driver=webdriver.Chrome("C:\chromedriver.exe")
    driver.get(url+"?page="+str(n))
    # print(url+"?page="+str(n))
    total_comp_on_page=driver.find_elements(By.XPATH,"//ul[@class='directory-list']/li")
    no_of_comp=(len(total_comp_on_page))

    for i in range(no_of_comp):
        try:          
            company=[]
            company_name=get_content("//h3[@class='company_info']/a",i)
            website=get_link('website-link__item','href',i)
            location=get_content("//div[@class='list-item custom_popover'][3]/span",i)
            contact_no="NA(Login REQUIRED)"
            raiting=get_content("//div[@class='rating-reviews sg-rating']/span",i)
            rating_count=get_content("//a[@class='reviews-link sg-rating__reviews directory_profile']",i)
            per_hour_pay=get_content("//div[@class='list-item custom_popover'][1]/span",i)
            min_project_size=get_content("//div[@class='list-item block_tag custom_popover']/span",i)
            no_of_emp=get_content("//div[@class='list-item custom_popover'][2]/span",i)
            company.append(company_name)
            company.append(website)
            company.append(location)
            company.append(contact_no)
            company.append(raiting)
            company.append(rating_count)
            company.append(per_hour_pay)
            company.append(min_project_size)
            company.append(no_of_emp)
            companies.append(company)
        except:
            pass
    # print(companies)
op_excel(companies)