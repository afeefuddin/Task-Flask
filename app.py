from flask import Flask,render_template,request,redirect,jsonify,make_response

app = Flask(__name__)


@app.route('/',methods=['POST','GET'])
def index():
    if request.method == 'POST' :
        file = open('tasks.txt','a')
        task = request.form['task']
        try:
            file.write(task+'\n')
            file.close()
            return redirect('/')
        except:
            file.close()
            return "There was an error while adding the task"
            
    else:
        file = open('tasks.txt','r')
        content = file.readlines()
        file.close()
        return render_template('index.html',tasks=content)

@app.route('/delete/<int:id>',methods=['GET'])
def delete(id):
    
    if request.method == 'GET' :
        try:
            with open('tasks.txt','r') as file:
                lines = file.readlines()
            
            if 0<=id<len(lines) :
                del lines[id]
            with open('tasks.txt','w') as file:
                file.writelines(lines)
            return redirect('/')
        except:
            return "There was an error deleting the task"
                

@app.route('/update/<int:id>', methods=['POST'])
def update(id):
    if request.method == 'POST':
        content = request.form['task']
        try:
            with open('tasks.txt', 'r') as file:
                lines = file.readlines()

            if 0 <= id < len(lines):
                lines[id] = content + '\n'

            with open('tasks.txt', 'w') as file:
                file.writelines(lines)

            return redirect('/')
        except:
            return "Error updating the task"
@app.route('/tip')
def tip():
    if request.method == 'GET':
        return jsonify({
            'tip' : 'Learn Flask today'
        })
    
@app.route('/loveCookie')
def cookie():
    if request.method=='GET':
        response =make_response('Check in dev tools🫣')
        response.set_cookie('task-flask','We love flask and you',max_age=3000)
        return response
    
@app.errorhandler(404)
def page_not_found(error):
    return "Uh oh this page doesnt exist"


if __name__ == '__main__':
    with open('tasks.txt', 'w') as file:
        file.write('')
    app.run(debug=True)