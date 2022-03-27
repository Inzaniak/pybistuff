from autoscraper import AutoScraper

# Create the model
url = 'https://medium.com/@inzaniak'
wanted_list = ["Build a Web Scraping Python Project from Start to Finish", "5 things you need to learn as a Python beginner"]

scraper = AutoScraper()
result = scraper.build(url, wanted_list)
print(result)

# Save the model
scraper.save('scrapers/medium.json')

# Load the model
del scraper
scraper = AutoScraper()
scraper.load('scrapers/medium.json')
scraper.get_result_similar(url)
