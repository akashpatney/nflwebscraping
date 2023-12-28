from scrapy import Spider
from scrapy import Selector
from nfldatacollection.items import PlayerItem

class PasserSpider(Spider):
    name = "nfl_passer"
    allowed_domains = ["nfl.com"]
    start_urls = ["https://www.nfl.com/stats/player-stats/"]

    def parse(self, response):
        players = Selector(response).xpath("//*[@id='main-content']/section[3]/div/div/div/div/table/tbody/tr")

        for player in players:
            item = PlayerItem()
            item['name'] = player.xpath("td/div/div/a/text()").extract_first()
            item['passing_yards'] = player.xpath("td[2]/text()").extract_first()
            yield item

