from LinkedIn_Scrapper.scrapper import LinkedIn_Scrapper

def main():
        job = input("Enter job search: ")
        area = input("Enter area search: ")
        scrapper = LinkedIn_Scrapper(job, area)
        jobs = scrapper.scrape_linkedin()
        # scrapper.save_to_csv(jobs)

if __name__ == "__main__":
    main()


main()