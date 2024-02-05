from flask import Flask,render_template,request,redirect


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

if __name__ == '__main__':
    with open('tasks.txt', 'w') as file:
        file.write('')
    app.run(debug=True)