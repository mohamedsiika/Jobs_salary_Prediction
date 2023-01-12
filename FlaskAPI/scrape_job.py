from selenium.webdriver.common.by import By
from selenium import webdriver
from shutil import which
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
import time
import pandas as pd

class scraping:
    def __init__(self,url,path="F:/siika/repos/Jobs_salary_Prediction/chromedriver"):
        self.options = Options()
        self.options.add_argument("window-size=1920,1080")
        #Enter your chromeself.driver.exe path below
        self.chrome_path = path
        self.driver = webdriver.Chrome(executable_path=self.chrome_path, options=self.options)
        self.driver.get(url)

    def scrape_one_job(self):
        #Enter your chromeself.driver.exe path below
        # Navigate to the job card page
        # Wait for the page to load
        self.driver.implicitly_wait(3)
        try:
            self.driver.find_element(By.XPATH,".//span[@class='SVGInline modal_closeIcon']").click()
            time.sleep(1)
        except:
            time.sleep(2)
            pass
        opened=False
        while not opened:
            try:
                self.driver.find_element(By.XPATH,"//div[@class='css-1rzz8ht ecgq1xb2']").click()
                time.sleep(1)
                opened=True
            except NoSuchElementException:
                print('#ERROR: no such element')
                time.sleep(2)    
        # Extract the data for the job
        try:
            company_name=(self.driver.find_element(By.XPATH,"//div[@class='css-16nw49e e11nt52q1']").text)
        except:
            company_name=("#N/A")
            pass

        try:
            job_title=(self.driver.find_element(By.XPATH,"//div[@class='css-17x2pwl e11nt52q6']").text)
        except:
            job_title=("#N/A")
            pass

        try:
            location=(self.driver.find_element(By.XPATH,"//div[@class='css-1v5elnn e11nt52q2']").text)
        except:
            location=("#N/A")
            pass

        try:
            job_description=(self.driver.find_element(By.XPATH,"//div[@id='JobDescriptionContainer']").text)
        except:
            job_description=("#N/A")
            pass

        self.driver.find_element(By.XPATH,"//div[@class='css-1iqg1r5 e1eh6fgm0']//span[text()='Company']").click()
        self.driver.implicitly_wait(3)

        
        try:
            company_size=(self.driver.find_element(By.XPATH,"//div[@class='css-vugejy es5l5kg0']//label[text()='Size']//following-sibling::*").text)
        except:
            company_size=("#N/A")
            pass
        
        try:
            company_type=(self.driver.find_element(By.XPATH,"//div[@class='css-vugejy es5l5kg0']//label[text()='Type']//following-sibling::*").text)
        except:
            company_type=("#N/A")
            pass
            
        try:
            company_sector=(self.driver.find_element(By.XPATH,"//div[@class='css-vugejy es5l5kg0']//label[text()='Sector']//following-sibling::*").text)
        except:
            company_sector=("#N/A")
            pass
            
        try:
            company_industry=(self.driver.find_element(By.XPATH,"//div[@class='css-vugejy es5l5kg0']//label[text()='Industry']//following-sibling::*").text)
        except:
            company_industry=("#N/A")
            pass
            
        try:
            company_founded=(self.driver.find_element(By.XPATH,"//div[@class='css-vugejy es5l5kg0']//label[text()='Founded']//following-sibling::*").text)
        except:
            company_founded=("#N/A")
            pass
            
        try:
            company_revenue=(self.driver.find_element(By.XPATH,"//div[@class='css-vugejy es5l5kg0']//label[text()='Revenue']//following-sibling::*").text)
        except:
            company_revenue=("#N/A")
            pass


        # Save the data for the job
        job = {
        'company_name': company_name,
        'job_title': job_title,
        'location': location,
        'job_description': job_description,
        'company_size': company_size,
        'company_type': company_type,
        'company_sector': company_sector,
        'company_industry': company_industry,
        'company_founded': company_founded,
        'company_revenue': company_revenue
        }
        
        
    # Close the webself.driver
        self.driver.quit()

        return job
        
