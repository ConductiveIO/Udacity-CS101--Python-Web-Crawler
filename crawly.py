# Webcrawler built while studying the Udacity CS101 course.
# 9.10.2012 | Robby Grodin | grodin.robby@gmail.com

def get_page(url):
        try:
            f = urllib.urlopen(url)
            page = f.read()
            f.close()
            return page
        except:
            return ""
        return ""
def get_next_target(page):
        start_link = page.find('<a href=')
        if start_link == -1:
            return None, 0
        start_quote = page.find('"', start_link)
        end_quote = page.find('"', start_quote + 1)
        url = page[start_quote + 1:end_quote]
        return url, end_quote
