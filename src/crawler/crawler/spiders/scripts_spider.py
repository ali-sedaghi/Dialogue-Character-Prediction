import scrapy
import re

class ScriptsSpider(scrapy.Spider):
    name = "scripts"
    start_urls = ["https://www.oocities.org/friends_greatestsitcom/script.htm"]


    def parse(self, response):
        tables = response.css("table.linearoundtable")
        for index, table in enumerate(tables):
            season_num = 10 - index
            rows = table.css("tr:nth-child(n+3)")

            for row in rows:
                episode_num = row.css("td:first-child::text").get()
                link = row.css("td:nth-child(2) a")[0]
                script_link = link.attrib["href"]
                script_title = re.sub('\s+', ' ', link.css("*::text").get())

                yield {
                    "season_num": season_num,
                    "episode_num": episode_num,
                    "script_link": script_link,
                    "script_title": script_title,
                }

