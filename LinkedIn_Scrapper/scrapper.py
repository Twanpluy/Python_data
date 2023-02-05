import logging
from bs4 import BeautifulSoup
import requests
import csv
import time
import os
import datetime
import json
# TODO: TEST it out

class LinkedIn_Scrapper:
    logging.basicConfig(level=logging.INFO)
    # Variable for the links
    URL = "https://www.linkedin.com/jobs/search/?keywords="
    FILEPATH = "datastore/"

    def __init__(self,job,area):
        self.job = job
        self.area = area
        

    # function Inputs for the job (job title) and area to search for (country))
    def input_search(self) -> str:
        """Input the job and area to search for"""
        self.job = str(input("Enter job search: ")).replace(" ", "%20")
        logging.info(f"The following job will be searched: \n {self.job}")
        self.area = str(input("Enter area search: ")).replace(" ", "%20")
        logging.info(f"The following area will be searched: \n {self.area}")

    # Example: https://www.linkedin.com/jobs/search/?keywords=software%20engineer&location=United%20States
    # @param: create_url job (string), area (string) parameters for the functions
    def create_url(self) -> str:
        """Create the url for the job search, input job (string) and area (string) """
        job = self.job.replace(" ", "%20")
        area = self.area.replace(" ", "%20")
        Search_URL = f"{self.URL}{job}&location={area}"
        return Search_URL

    # function the scraper
    def scrape_linkedin(self):
        """Scrape the linkedin jobs page and return a list of jobs"""
        logging.info(f"The following url will be used: \n {self.create_url()}")
        jobs = []
        response = requests.get(self.create_url())
        soup = BeautifulSoup(response.content, "html.parser")

        # export html to file for testing
        with open("datastore/linkedin.html", "w") as f:
            f.write(str(soup))
            f.close()


        # Find all the job cards
        Find_All_Job = soup.find_all("div", class_="base-card relative w-full hover:no-underline focus:no-underline base-card--link base-search-card base-search-card--link job-search-card")
        #write find all job in cards to file
        with open("datastore/find_job.html", "w") as f:
            f.write(str(Find_All_Job))
            f.close()

        # Loop through the job cards and extract the data
        for job in Find_All_Job:
            if job.find("span", class_="job-search-card__salary") is not None:
                job_id =  job.find("div", class_="data-job-id")
            else:
                job_id = "No job id"  
            
            if job.find("h3", class_="base-search-card__title") is not None:
                title = job.find("h3", class_="base-search-card__title").text.strip()
            else:
                title = "No title"          
            # title = job.find("h3", class_="base-search-card__title").text.strip()

            if job.find("h4", class_="base-search-card__subtitle") is not None:
                company = job.find("h4", class_="base-search-card__subtitle").text.strip()
            else:
                company = "No company"    

            # company = job.find("h4", class_="base-search-card__subtitle").text.strip()
            if job.find("span", class_="job-search-card__location") is not None:
                location = job.find("span", class_="job-search-card__location").text.strip()
            else:
                location = "No location"    
            # location = job.find("span", class_="job-search-card__location").text.strip()
            if job.find("span", class_="job-search-card__salary") is not None:
                salary = job.find("span", class_="job-search-card__salary").text.strip()
            else:
                salary = "No salary"    
            # salary = job.find("span", class_="job-search-card__salary").text.strip()

        # Get job description for each job, need to open the job page tab
            job_link = job.find("a", class_="base-card__full-link")["href"]
            time.sleep(0.3)
            job_response = requests.get(job_link)
            time.sleep(0.3)
            job_soup = BeautifulSoup(job_response.content, "html.parser")
            job_soup.find("div", class_="show-more-less-html__markup show-more-less-html__markup--clamp-after-5") 
            job_description = job_soup.find("div", class_="show-more-less-html__markup show-more-less-html__markup--clamp-after-5").text.strip()  
            jobs.append({
                "Job ID": job_id,
                "Title": title,
                "Company": company,
                "Location": location,
                "Salary": salary,
                "Description": job_description

            })
            return jobs

    # function to save the data to a csv file
    def save_to_json(self, jobs):
        """Save to json file"""
        date = datetime.datetime.now()
        complete_file_path = f"{self.FILEPATH}{self.job}_{self.area}_{date}"
        complete_file_path = complete_file_path.replace(" ", "_").replace(":", "_").replace(".", "_").replace("-", "_")
        logging.info(f"{complete_file_path}")
        file = open(f"{complete_file_path}.json", "w")
        json.dump(jobs, file, indent=4)

        


