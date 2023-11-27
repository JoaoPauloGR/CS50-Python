import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    # check for iframe matches
    if iframe_matches := re.search("<iframe", s):
        pass
    else:
        return
    # if is there an iframe match, search and format the youtube link
    if matches := re.search(r"(http(?:s)?://(?:www\.)?youtube\.com/embed/[0-9a-zA-Z]+)", s):
        yt_url = matches.group(1)
        final_url = re.sub("(www\.)?youtube\.com/embed", "youtu.be", yt_url)
        final_url = re.sub("http:", "https:", final_url)
        return final_url
    else:
        return


...


if __name__ == "__main__":
    main()