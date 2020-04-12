from artprice_scrapper import ArtPriceScraper

if __name__ == '__main__':
    with ArtPriceScraper() as scraper:
        scraper.start()
