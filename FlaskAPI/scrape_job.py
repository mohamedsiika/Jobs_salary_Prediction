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
        
        opened=False
        while not opened:
            try:
                self.driver.find_element(By.XPATH,"//div[@class='css-t3xrds e856ufb4']").click()
                time.sleep(1)
                opened=True
            except NoSuchElementException:
                print('#ERROR: no such element')
                time.sleep(2)    
        # Extract the data for the job
        try:
            company_name=(self.driver.find_element(By.XPATH,"//div[@class='css-87uc0g e1tk4kwz1']").text)
        except:
            company_name=("#N/A")
            pass

        try:
            job_title=(self.driver.find_element(By.XPATH,"//div[@class='css-1vg6q84 e1tk4kwz4']").text)
        except:
            job_title=("#N/A")
            pass

        try:
            location=(self.driver.find_element(By.XPATH,"//div[@class='css-56kyx5 e1tk4kwz5']").text)
        except:
            location=("#N/A")
            pass

        try:
            job_description=(self.driver.find_element(By.XPATH,"//div[@id='JobDescriptionContainer']").text)
        except:
            job_description=("#N/A")
            pass

        try:
            salary_estimate=(self.driver.find_element(By.XPATH,"//div[@class='css-1bluz6i e2u4hf13']").text)
        except:
            salary_estimate=("#N/A")
            pass
        
        try:
            company_size=(self.driver.find_element(By.XPATH,"//div[@id='CompanyContainer']//span[text()='Size']//following-sibling::*").text)
        except:
            company_size=("#N/A")
            pass
        
        try:
            company_type=(self.driver.find_element(By.XPATH,"//div[@id='CompanyContainer']//span[text()='Type']//following-sibling::*").text)
        except:
            company_type=("#N/A")
            pass
            
        try:
            company_sector=(self.driver.find_element(By.XPATH,"//div[@id='CompanyContainer']//span[text()='Sector']//following-sibling::*").text)
        except:
            company_sector=("#N/A")
            pass
            
        try:
            company_industry=(self.driver.find_element(By.XPATH,"//div[@id='CompanyContainer']//span[text()='Industry']//following-sibling::*").text)
        except:
            company_industry=("#N/A")
            pass
            
        try:
            company_founded=(self.driver.find_element(By.XPATH,"//div[@id='CompanyContainer']//span[text()='Founded']//following-sibling::*").text)
        except:
            company_founded=("#N/A")
            pass
            
        try:
            company_revenue=(self.driver.find_element(By.XPATH,"//div[@id='CompanyContainer']//span[text()='Revenue']//following-sibling::*").text)
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
        
