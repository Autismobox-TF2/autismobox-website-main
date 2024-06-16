import re
import urllib.parse
from textwrap import dedent

x_intent = "https://twitter.com/intent/tweet"
fb_sharer = "https://www.facebook.com/sharer/sharer.php"
reddit_sharer = "https://reddit.com/submit"
include = re.compile(r"blog/[1-9].*")

def on_page_markdown(markdown, **kwargs):
    page = kwargs['page']
    config = kwargs['config']
    if not include.match(page.url):
        return markdown

    page_url = config.site_url+page.url
    page_title = urllib.parse.quote(page.title+'\n')

    return markdown + dedent(f"""<br><br><br>
    [:simple-reddit:]({reddit_sharer}?url={page_url}&title={page_title}){{ .md-button }}
    [:simple-x:]({x_intent}?text={page_title}&url={page_url}){{ .md-button }}
    [:simple-facebook:]({fb_sharer}?u={page_url}){{ .md-button }}
    """)