from __future__ import print_function

import urllib, json
import os
import subprocess
import socket 

from notebook import notebookapp
from telegram import Bot

# subprocess library allows you to run the jupyterlab server in the background
# subprocess.Popen("jupyter lab --ip=0.0.0.0 --port=80")
subprocess.Popen("jupyter lab --ip=0.0.0.0")

#change these
bot = Bot(os.environ["MYBOT_TELE_KEY"]) # set your environment variables
my_tele_id = 12345678 # your telegram account id - used as a target for your bot to send the url to
#end changes

def get_ip():
    # get external ip address
    pub_ip = json.loads(urllib.urlopen("http://ip.jsontest.com/").read())
    return pub_ip["ip"]

def get_local_ip():
    # get local ip address instead - in case of problems with firewall. 
    return socket.gethostbyname(socket.gethostname()) 

def form_url():
    # form the url to access jupyter
    try:
        my_ip = get_ip()
    except:
        try:
            my_ip = get_local_ip()
        except:
            return "You did not have internet. If you still get this telegram message that means something is weird with your ip configuration"
    servers = list(notebookapp.list_running_servers())
    if len(servers) > 0:
        urls = []
        for idx, server, in enumerate(servers):
            urltosend = "".join(["http://", my_ip, ":", str(server["port"]), "/?token=", str(server["token"])])
            urls.append(urltosend)
    else:
        return  "Something went wrong."
    return "Your jupyter instances are at " + "\n ".join(urls)

bot.sendMessage(my_tele_id, form_url())
bot.sendMessage(my_tele_id, "Also, my local IP is {}. Just in case the server is blocking ports from the internet, which is probably a good idea.".format(get_local_ip()))