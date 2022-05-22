import scrapy
import re
import pandas as pd


class QuotesSpider(scrapy.Spider):
    name = "dialogues"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.scripts = pd.read_csv("../data/scripts.csv")
        self.start_urls = self.scripts.script_link.tolist()
        self.labels = [
            "ross",
            "rachel",
            "joey",
            "chandler",
            "monica",
            "phoebe",
        ]

    def parse(self, response):
        pars = response.css("p *::text").getall()
        for index, par in enumerate(pars):

            try:
                p = par.split(':', 1)
                person = re.sub('\s+', ' ', p[0]).strip().lower()
                if person not in self.labels:
                    continue
                dialogue = re.sub('\s+', ' ', p[1]).strip()
                print(dialogue, p[1])

            except:
                continue

            yield {
                "person": person,
                "dialogue": dialogue,
            }
