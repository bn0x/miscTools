#!/usr/bin/env python

import Skype4Py
import time
import re
import altCaser

class SkypeBot(object):
  def __init__(self):
    self.skype = Skype4Py.Skype(Events=self)
    self.skype.Attach()
    self.caser = altCaser.caser()

  def AttachmentStatus(self, status):
    if status == Skype4Py.apiAttachAvailable:
      self.skype.Attach()

  def MessageStatus(self, msg, status):
    if status == "SENDING" and msg.IsEditable:
      msg.Body = self.caser.operate(msg.Body)

if __name__ == "__main__":
  bot = SkypeBot()

  while True:
    time.sleep(1.0)

