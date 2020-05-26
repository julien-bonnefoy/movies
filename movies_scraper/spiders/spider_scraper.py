import scrapy
from items import MoviesScraperItem


class ExtractMovies(scrapy.Spider):

    # This name must be unique always
    name = "extract_movies"

    # Function which will be invoked
    def start_requests(self):

        # enter the URL here
        urls = ['https://www.allocine.fr/films', ]

        for url in urls:
            yield scrapy.Request(url = url, callback = self.parse)

    # Parse function
    def parse(self, response):
        item_loader = scrapy.ItemLoader(item=MoviesScraperItem(), response=response)
        item_loader.default_input_processor = scrapy.MapCompose(remove_tags)

        item_loader.add_css("product", "h1[itemprop='name']")
        item_loader.add_css("price", "span[itemprop=price]")
        item_loader.add_css("stock", "span[itemprop=’stock’]")
        item_loader.add_css("category", "a[data-track='Breadcrumb']")

        return item_loader.load_item()