# -*- coding: utf-8 -*-

from scrapy.cmdline import execute
from scrapy.utils.project import get_project_settings

settings = get_project_settings()
settings.update({})

execute(['scrapy', 'crawl', 'xc'], settings=settings)
