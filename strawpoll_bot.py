import requests
import argparse
import json
from bs4 import BeautifulSoup

parser = argparse.ArgumentParser(description='Strawpoll Bot by obnoxious')
parser.add_argument('-i', '--id', help="Poll ID, can be found in the URL", default=2100485, type=int)
parser.add_argument('-c', '--choice', help="What do you want to vote for?", default=0, type=int)
args = parser.parse_args()

class bot(object):
    def __init__(self, args):
        self.session = requests.session()
        self.getRequest = self.session.get('http://strawpoll.me/%d'%args.id)
        self.bsData = BeautifulSoup(self.getRequest.content)
        for tag in self.bsData('span'):
            try:
                if "poll.title" in tag['ng-bind']:
                    self.title = tag.text
            except:
                continue
        print("[+] Got Title: %s"%self.title)
        self.options = []
        for tag in self.bsData('span'):
            try:
                if "optionText" in tag['class']:
                    self.options.append(tag.text)
            except:
                continue
        print('[+] Got %d options'%len(self.options))
        if "multi\&quot;:false," in self.getRequest.content:
            self.multi = False
            print('[+] Poll doesn\'t allow multiple votes')
        else:
            self.multi = True
            print('[+] Poll allows multiple votes')
        if "permissive\&quot;:false" in self.getRequest.content:
            self.permissive = False
            print('[+] Poll is not permissive')
        else:
            self.permissive = True
            print('[+] Poll is permissive')
        self.pc = 1
        self.votes = [args.choice]

        self.setupData = {
            "title": self.title,
            "options": self.options,
            "multi": self.multi,
            "permissive": self.permissive,
            "pc": self.pc,
            "votes": self.votes,
        }
        self.vote = self.session.patch('http://strawpoll.me/api/v2/polls/%d'%args.id,
                                        data=json.dumps(self.setupData),
                                        headers={
                                            'Host': 'strawpoll.me',
                                            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:33.0) Gecko/20100101 Firefox/33.0',
                                            'Accept': 'application/json, text/plain, */*',
                                            'Accept-Language': 'en-US,en;q=0.5',
                                            'Accept-Encoding': 'gzip, deflate',
                                            'Content-Type': 'application/json;charset=utf-8',
                                            'Referer': 'http://strawpoll.me/%d'%args.id,
                                            'Connection': 'keep-alive',
                                        })
        try:
            error = self.vote.json()['error']
            print('[!] %s'%error)
        except:
            print('[+] Sent Vote!')

if __name__ == "__main__":
    bot(args)