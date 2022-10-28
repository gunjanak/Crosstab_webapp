
from pydoc_data.topics import topics
from flask import Flask, render_template, request, session,redirect
import os
from werkzeug.utils import secure_filename
import pandas as pd


Flag = 0
csv_file_path = ""
#Defining upload folder path
UPLOAD_FOLDER = os.path.join('staticFiles','uploads')
#Define allowed files
ALLOWED_EXTENSIONS = {'csv'}

app = Flask(__name__,template_folder='templates',static_folder='staticFiles')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

#Define secret key to enable session
app.secret_key = "sanaan"
column_names = ''
row_data = ''


@app.route('/',methods=("POST","GET"))
def index():
    img_file_path = ""
    if request.method =='POST':
        if request.form.get('Submit_action')=='Submit':
            #upload file flask
            uploaded_file = request.files['uploaded-file']
            print(uploaded_file.filename)
            uploaded_file.save(os.path.join(app.config['UPLOAD_FOLDER'],'upload.csv'))
            #Storing uploaded file path in flask session
            session['uploaded_csv_file_path'] = os.path.join(app.config['UPLOAD_FOLDER'],'upload.csv')
            #retriving uploaded file path from session
            csv_file_path = session.get('uploaded_csv_file_path',None)
            print(csv_file_path)
            df = pd.read_csv(csv_file_path)
            print(df.head())
            column_names = df.columns.values
            row_data = list(df.head().values.tolist())
          

        else:
            pass

    else:
        csv_file_path = ""
        column_names=""
        row_data=""
    
   

    return render_template('index.html',column_names=column_names, row_data=row_data, zip=zip)




#Running the app
#if __name__ == '__main__':
 #   app.run(port=5000,debug=True)