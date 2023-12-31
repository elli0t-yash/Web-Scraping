import scrapy
import logging


class CountriesSpider(scrapy.Spider):
    name = "countries"
    allowed_domains = ["www.worldometers.info"]
    start_urls = ["https://www.worldometers.info/world-population/population-by-country/"]

    def parse(self, response):
        countries = response.xpath("//td/a")
        for country in countries:
            name = country.xpath("//text()").get()
            link = country.xpath(".//@href").get()

        # yield {
        #     'country_name': name,
        #     'country_link': link 
        # } 

        yield response.follow(url=link, callback=self.parse_country, meta={'country_name': name})

    def parse_country(self, response):
        name = response.request.meta['country_name']
        rows = response.xpath("(//table[@class='table table-striped table-bordered dataTable no-footer'])[1]/tbody/tr") 
        for row in rows:
            population = row.xpath("")