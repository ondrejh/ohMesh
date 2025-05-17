#!/usr/bin/python3

from bs4 import BeautifulSoup
import os

with open("../www/heltec_v3_mobile_build.html", "r", encoding="utf-8") as f:
    html = f.read()

soup = BeautifulSoup(html, "html.parser")

galerie = soup.find_all("a", attrs={"data-lightbox": True})

obrazky = []

for a in galerie:
    href = a.get("href")
    href = os.path.join("../www", href)
    img = a.find("img")
    alt = img.get("alt", "") if img else ""

    obrazky.append([href, alt])

obrazky.sort(key=lambda pair: pair[0])

with open("images_from_html.md", 'w') as f:
    for img in obrazky:
        line = "![{}]({})".format(img[1], img[0])
        print(line)
        f.write("{}\n".format(line))
