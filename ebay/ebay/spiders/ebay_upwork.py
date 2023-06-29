import scrapy
from ebay.items import EbayItem
from scrapy.loader import ItemLoader



class EbaySpider(scrapy.Spider):
    
    name = "ebay"
    allowed_domains = ["ebay.es"]
    start_urls = ["https://www.ebay.es"]

    # Allow a custom parameter (-a flag in the scrapy command)
    def __init__(self, search="alfombrillas de goma BMW X3"):
        self.search_string = search

    def parse(self, response):
        # Extract the trksid to build a search request  
        trksid = response.css("input[type='hidden'][name='_trksid']").xpath("@value").extract()[0]       
        
        # Build the url and start the requests
        yield scrapy.Request("http://www.ebay.es/sch/i.html?_from=R40&_trksid=" + trksid +
                             "&_nkw=" + self.search_string.replace(' ','+') + "&_ipg=200", 
                             callback=self.parse_link)

    # Parse the search results
    def parse_link(self, response):
        # Extract the list of products 
        results = response.xpath('//div/div/ul/li[contains(@class, "s-item" )]')
        # Extract info for each product
        for product in results:
                   
            #We introduce the class to make it easier to manage our results
            l = ItemLoader(item=EbayItem(),selector = product)

            name = l.add_xpath('Name', './/*[@class="s-item__title"]//text()')
            # Sponsored or New Listing links have a different class
            if name == None:
                l.add_xpath('Name','.//*[@class="s-item__title s-item__title--has-tags"]/text()')          
                if name == None:
                    l.add_xpath('Name','.//*[@class="s-item__title s-item__title--has-tags"]//text()')       
            if name == 'New Listing':
                l.add_xpath('Name','.//*[@class="s-item__title"]//text()')

            # If this get a None result
            if name == None:
                name = "ERROR"

            l.add_xpath('Price','.//*[@class="s-item__price"]/text()')
            l.add_xpath('Status','.//*[@class="SECONDARY_INFO"]/text()')
            l.add_xpath('Seller_Level','//span[@class="s-item__etrs-text"]/text()')
            l.add_xpath('Location','//span[@class="s-item__location s-item__itemLocation"]/text()')
            l.add_xpath('Product_url','.//a[@class="s-item__link"]/@href')
            l.add_xpath('Stars','//span[@class="clipped"]/text()')
            l.add_xpath('Ratings','.//span[@class="s-item__seller-info-text"]/text()')
            product_url = product.xpath('.//a[@class="s-item__link"]/@href').extract_first()
            
            # Go to the product details page
            yield scrapy.Request(product_url, meta={'l':l}, callback=self.parse_product_details)
            
        # Get the next page
        next_page_url = response.xpath('//a[@aria-label="Ir a la página de búsqueda siguiente"]/@href').get()

        # The last page do not have a valid url and ends with '#'
        if next_page_url == None or str(next_page_url).endswith("#"):
            self.log("eBay products collected successfully !!!")
        else:
            print('\n'+'-'*40)
            print('Next page: {}'.format(next_page_url))
            yield scrapy.Request(next_page_url, callback=self.parse_link)


    #Parse details page for each product
    def parse_product_details(self, response):
        string = ''
        l = response.meta['l']
        UPC= response.xpath('//h2[@itemprop="gtin13"]/text()').extract_first()
        Price = response.xpath("//span[@itemprop='price']//span/text()").extract_first()
        #Processing the data to conver a list into a string
        Seller_Address = response.xpath("//div[@class='ux-section ux-section--nameAndAddress']//div[@class='ux-section__item']//span[@class='ux-textspans']/text()").getall()
        for item in Seller_Address:
            string += " " + item
        l.add_value('Price', Price)
        l.add_value('UPC', UPC)
        l.add_value('Seller_Address', string)

        yield l.load_item()






