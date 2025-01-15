import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(html:str) -> str: # Take html and extract YouTube URL
    url = re.search(r"iframe .*src=\"(?:https?://)?(?:www\.)?youtube.com/embed/(.+?)\".*", html)
    try:
        return "https://youtu.be/" + str(url.group(1))
    except AttributeError:
        return None

def shorten(url:str) -> str: # Takes any youtube.com/watch/ url and shortens to youtu.be/
    pass
    # return url.replace("youtube.com/watch", "youtu.be")


if __name__ == "__main__":
    main()