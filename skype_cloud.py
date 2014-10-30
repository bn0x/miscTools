import requests
import sys

class cloud(object):
    def __init__(self):
        self.oldRes = []
        self.originalRequest = requests.get('http://gibson.tgqx.at/api/%s'%sys.argv[1]).json()
        for result in self.originalRequest:
            print('[!] Original: %s'%result['public'])
            self.oldRes.append(result['public'])
        while True:
            for result in requests.get('http://gibson.tgqx.at/api/%s'%sys.argv[1]).json():
                if result['public'] not in self.oldRes:
                    print("[+] New IP: %s"%result['public'])
                    self.oldRes.append(result['public'])

if __name__ == "__main__":
    cloud()