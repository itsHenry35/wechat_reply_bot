from flask import Flask, render_template, request
import itchat
chatroom = '测试群聊'
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
 
@app.route('/submit', methods=['post'])
def submit():
    msg = request.form.get('message')
    print(msg)
    msgafter= msg
    print(msgafter)
    result = itchat.search_chatrooms(chatroom)
    uuid = result[0]["UserName"]
    print(uuid)
    result = str(itchat.send(msgafter, uuid))
    return result

@app.route('/login')
def login():
    QR = itchat.auto_login()
    return "Good Job~"
 
if __name__ == '__main__':
    app.run(host="::" , port=int("8080"))
