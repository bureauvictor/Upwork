# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
from itemloaders.processors import TakeFirst, MapCompose
from w3lib.html import remove_tags

def remove_emtpyspaces(value):
    return value.split()

def replace_comma(value):
    return value.replace(".", ",")

def trim_EAN(value):
    return value[-18:-5]




class FiverrItem(scrapy.Item):
    # define the fields for your item here like:
    price = scrapy.Field(input_processor = MapCompose(remove_tags, remove_emtpyspaces), output_processor = TakeFirst())
    asin = scrapy.Field(input_processor = MapCompose(remove_tags, remove_emtpyspaces), output_processor = TakeFirst())
    title = scrapy.Field(output_processor = TakeFirst())

    img = scrapy.Field(input_processor = MapCompose(remove_tags, remove_emtpyspaces), output_processor = TakeFirst())
    costeenvio  = scrapy.Field(input_processor = MapCompose(remove_tags, remove_emtpyspaces), output_processor = TakeFirst())
    asin = scrapy.Field(input_processor = MapCompose(remove_tags, remove_emtpyspaces), output_processor = TakeFirst())
    numero_valoraciones  = scrapy.Field(input_processor = MapCompose(remove_tags, remove_emtpyspaces), output_processor = TakeFirst())
    media_valoraciones  = scrapy.Field(input_processor = MapCompose(remove_tags, remove_emtpyspaces), output_processor = TakeFirst())


    pass

class YellowPagesItem(scrapy.Item):

    Name =scrapy.Field(output_processor = TakeFirst())
    Street_Address = scrapy.Field(output_processor = TakeFirst())
    Postal_Code = scrapy.Field(input_processor = MapCompose(remove_tags, remove_emtpyspaces), output_processor = TakeFirst())
    City = scrapy.Field(output_processor = TakeFirst())
    Region = scrapy.Field(output_processor = TakeFirst())
    Website = scrapy.Field(input_processor = MapCompose(remove_tags, remove_emtpyspaces), output_processor = TakeFirst())
    Email = scrapy.Field(input_processor = MapCompose(remove_tags, remove_emtpyspaces), output_processor = TakeFirst())
    Telephone = scrapy.Field(input_processor = MapCompose(remove_tags, remove_emtpyspaces), output_processor = TakeFirst())
    Logo = scrapy.Field(input_processor = MapCompose(remove_tags, remove_emtpyspaces), output_processor = TakeFirst())
    


    pass

class MilAnunciosItem(scrapy.Item):
    Modelo= scrapy.Field(output_processor = TakeFirst())
    Precio = scrapy.Field(input_processor = MapCompose(remove_tags), output_processor = TakeFirst())
    Ubicación = scrapy.Field( output_processor = TakeFirst())
    Kilometros = scrapy.Field( output_processor = TakeFirst())
    Motor = scrapy.Field(input_processor = MapCompose(remove_tags), output_processor = TakeFirst())
    Año = scrapy.Field(input_processor = MapCompose(remove_tags), output_processor = TakeFirst())
    Descripción = scrapy.Field(output_processor = TakeFirst())
    Foto = scrapy.Field(input_processor = MapCompose(remove_tags), output_processor = TakeFirst())
    url = scrapy.Field(input_processor = MapCompose(remove_tags), output_processor = TakeFirst())

pass

class EbayItem(scrapy.Item):

    Name = scrapy.Field(input_processor = MapCompose(remove_tags), output_processor = TakeFirst())
    Status = scrapy.Field(input_processor = MapCompose(remove_tags), output_processor = TakeFirst())
    Seller_Level = scrapy.Field(input_processor = MapCompose(remove_tags), output_processor = TakeFirst())
    Location = scrapy.Field(input_processor = MapCompose(remove_tags), output_processor = TakeFirst())
    Price = scrapy.Field(input_processor = MapCompose(remove_tags), output_processor = TakeFirst())
    Stars = scrapy.Field(input_processor = MapCompose(remove_tags), output_processor = TakeFirst())
    Ratings = scrapy.Field(input_processor = MapCompose(remove_tags), output_processor = TakeFirst())
    Product_url = scrapy.Field(input_processor = MapCompose(remove_tags), output_processor = TakeFirst())
    UPC = scrapy.Field(input_processor = MapCompose(remove_tags), output_processor = TakeFirst())
    Brand = scrapy.Field(input_processor = MapCompose(remove_tags), output_processor = TakeFirst())
    MPN = scrapy.Field(input_processor = MapCompose(remove_tags), output_processor = TakeFirst())
    Seller_Address = scrapy.Field(input_processor = MapCompose(remove_tags) , output_processor = TakeFirst())


pass