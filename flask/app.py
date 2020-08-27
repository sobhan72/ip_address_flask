import flask

app=flask.Flask(__name__)
i = 0
@app.route('/')
#show your ip addres and count of ip
def index():
    global i
    ip_addr = flask.request.remote_addr
    i+=1
    return "this is your ip addr :" +ip_addr +"  " "count:" + str(i)

if __name__=='main':
    app.run()