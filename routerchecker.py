#!/usr/bin/env python3
import argparse
import datetime
import sys
from concurrent.futures import ThreadPoolExecutor
import requests
from bs4 import BeautifulSoup

__title__ = "routerchecker"
__author__ = "Thurask"
__license__ = "WTFPL v2"
__copyright__ = "Copyright 2016 Thurask"
__version__ = "1.0.1"


def list_strip(alist):
    for x in alist:
        x = x.strip()
    return alist


def dateparse(datestring, format):
    stamp = datetime.datetime.strptime(datestring, format)
    return stamp.strftime("%Y %m %d")


def get_soup(url, splitter=None):
    req = requests.get(url)
    if splitter is not None:
        data = req.text.split(splitter[0])[splitter[1]]
    else:
        data = req.text
    soup = BeautifulSoup(data, "html.parser")
    return soup


def scrape_merlin():
    soup = get_soup("https://asuswrt.lostrealm.ca")
    for p in soup.findAll("p"):
        if "Stable" in p.text:
            info = p.text.replace("\xa0", "\bDate: ")
            break
    splits = info.split("Date: ")
    splits = list_strip(splits)
    return splits[1], dateparse(splits[2], "%d-%b-%Y")


def scrape_shibby():
    soup = get_soup("http://tomato.groov.pl/?page_id=12")
    for p in soup.findAll("p"):
        if p.find("strong"):
            info = p.text.replace("\u2013", "-")
            break
    splits = info.split(" - ")
    splits = list_strip(splits)
    return splits[1], dateparse(splits[0], "%Y-%m-%d")


def scrape_ddwrt():
    split = ("</head>", 1)
    soup = get_soup("https://www.dd-wrt.com/site/support/other-downloads?path=betas%2F2016%2F",
                    splitter=split)
    latest = soup.findAll("tr")[-1]
    info = latest.find("td").find("a").text
    splits = info.split("-r")
    splits = list_strip(splits)
    return "r" + splits[1], dateparse(splits[0], "%m-%d-%Y")


def scrape_openwrt():
    soup = get_soup("https://downloads.openwrt.org")
    latest = soup.findAll("li")[0]
    info = latest.text
    splits = info.split("\n")
    splits[2] = splits[2].replace("Released: ", "")
    splits = list_strip(splits)
    return splits[1], dateparse(splits[2], "%a, %d %b %Y")


def get_results():
    possibles = {"ddw": scrape_ddwrt,
                 "mer": scrape_merlin,
                 "tsh": scrape_shibby,
                 "opw": scrape_openwrt}
    results = {key: None for key in possibles.keys()}
    with ThreadPoolExecutor(max_workers=len(results.keys())) as tpe:
        for key in results:
            results[key] = tpe.submit(possibles[key]).result()
    return results


def result_printer(name, values):
    print("{0}{1}".format(name.upper(), ":" if not name.endswith(":") else ""))
    print("\t{0} released {1}\n".format(values[0], values[1]))


def main():
    print("~~~~ROUTERCHECKER {0}~~~~\n".format(__version__))
    print("GETTING VERSIONS...\n")
    results = get_results()
    result_printer("ASUSWRT MERLIN", results["mer"])
    result_printer("DD-WRT BETA", results["ddw"])
    result_printer("OPENWRT", results["opw"])
    result_printer("TOMATO (SHIBBY)", results["tsh"])


def parse_args():
    parser = argparse.ArgumentParser(
        prog="routerchecker",
        description="Router firmware update scanner",
        epilog="https://github.com/thurask/routerchecker")
    parser.add_argument(
        "-v",
        "--version",
        action="version",
        version="{0} {1}".format(parser.prog, __version__))
    parser.parse_known_args(sys.argv[1:])
    main()


if __name__ == "__main__":
    main()
