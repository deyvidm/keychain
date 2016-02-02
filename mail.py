#!/usr/bin/python

import smtplib

fromaddr = "cron@grr.la"
toaddrs  = "cron@grr.la"

msg = ("From: %s\r\nTo: %s\r\n\r\n"
       % (fromaddr, ", ".join(toaddrs)))

server = smtplib.SMTP('localhost')
server.set_debuglevel(1)
server.sendmail(fromaddr, toaddrs, msg)
server.quit()
