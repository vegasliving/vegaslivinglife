Scraper Format to Las Vegas Home

base - //div[@class="col-lg-4 col-md-4 col-sm-6 col-xs-12 iq-listings-grid-card-wrap"]

title - @data-address

url - @data-url pre_url 'pre_url':'https://www.lasvegashomes.com'

description - div/div[1]/div[2]/text()

thumnail - div/div[2]/div[1]/div[1]/@data-background

longtitude - div/div[1]/div[2]/text()

latitude - div/div[1]/div[2]/text()

size - div/div[2]/div[3]/div/span[2]/text()

numberOfBeds - div/div[2]/div[3]/div/span[1]/text()

numberOfBaths - div/div[2]/div[3]/div/text()[normalize-space() !='']

detail_description - //div[@class="iq-pg-body"]/div/div/div[4]/div[2]/p/text()