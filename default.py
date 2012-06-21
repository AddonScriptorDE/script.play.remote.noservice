import json, xbmc, xbmcplugin, xbmcgui, xbmcaddon, locale, sys, urllib, urllib2, re, os, datetime, base64

def getUrl(url,data,user,pw):
      req = urllib2.Request(url,data)
      userpass = base64.encodestring('%s:%s' % (user, pw))[:-1]
      req.add_header('Authorization', 'Basic %s' % userpass)
      response = urllib2.urlopen(req)
      link=response.read()
      response.close()
      return link

addonID = "script.play.remote.noservice"
settings = xbmcaddon.Addon(id=addonID)
translation = settings.getLocalizedString

file = xbmc.Player().getPlayingFile()
file = file.replace("\\\\","\\")
name=settings.getSetting("name")
ip=settings.getSetting("ip")
port=settings.getSetting("port")
user=settings.getSetting("user")
pw=settings.getSetting("pw")
while (ip=="" or port=="" or user=="" or pw==""):
  settings.openSettings()
  name=settings.getSetting("name")
  ip=settings.getSetting("ip")
  port=settings.getSetting("port")
  user=settings.getSetting("user")
  pw=settings.getSetting("pw")
name2=settings.getSetting("name2")
ip2=settings.getSetting("ip2")
port2=settings.getSetting("port2")
user2=settings.getSetting("user2")
pw2=settings.getSetting("pw2")
name3=settings.getSetting("name3")
ip3=settings.getSetting("ip3")
port3=settings.getSetting("port3")
user3=settings.getSetting("user3")
pw3=settings.getSetting("pw3")
dialog = xbmcgui.Dialog()
typeArray = [name+" ("+translation(30006)+")",name+" ("+translation(30009)+")"]
if name2!="":
  typeArray.append(name2+" ("+translation(30006)+")")
  typeArray.append(name2+" ("+translation(30009)+")")
if name3!="":
  typeArray.append(name3+" ("+translation(30006)+")")
  typeArray.append(name3+" ("+translation(30009)+")")
nr=dialog.select(translation(30008), typeArray)
if nr>=0:
  type = typeArray[nr]
  if type.find(name+" (")==0:
    name=name
    ip=ip
    port=port
    user=user
    pw=pw
  elif type.find(name2+" (")==0:
    name=name2
    ip=ip2
    port=port2
    user=user2
    pw=pw2
  elif type.find(name3+" (")==0:
    name=name3
    ip=ip3
    port=port3
    user=user3
    pw=pw3
  if type.find(translation(30006))>=0:
    xbmc.Player().stop()
    data = json.dumps({"jsonrpc": "2.0", "method": "Player.Open", "params": {"item": {"file": file}},  "id": 1})
    json_result = getUrl("http://"+ip+":"+port+"/jsonrpc",data,user,pw)
  elif type.find(translation(30009))>=0:
    xbmc.Player().stop()
    data = json.dumps({"jsonrpc": "2.0", "method": "Playlist.Add", "params": {"item": {"file": file}, "playlistid": 1}, "id": 1})
    json_result = getUrl("http://"+ip+":"+port+"/jsonrpc",data,user,pw)