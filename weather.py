from flask import Flask,request,make_response
import os,json
#import pyowm
import os

app = Flask(__name__)
#owmapikey=os.environ.get('OWMApiKey') #or provide your key here
#owm = pyowm.OWM(owmapikey)

#geting and sending response to dialogflow
@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)
    print(req)
    print("Request:")
    print(json.dumps(req, indent=4))
    
    res = processRequest(req)

    res = json.dumps(res, indent=4)
    print(res)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r

#processing the request from dialogflow
def processRequest(req):
    
    #result = req.get("result")

    speech = "Dette fungerer. Jeg er Nancy og jeg lever"    
    return {
  "fulfillmentText": "Dette er en tekst-respons",
     "simpleResponse": {
              "textToSpeech": "dette er en talerespons "
            }

        }
    
if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    print("Starting app on port %d" % port)
    app.run(debug=False, port=port, host='0.0.0.0')
