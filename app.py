

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
            column_names = column_names.tolist()
            row_data = list(df.head().values.tolist())
            print(column_names)
            print(type(column_names)) 
            tables=""
            titles=""


        

        elif request.form.get('Checkbox_action')=='Checkbox_Submit':
            print('Checkbox used')
            #The index of crosstab
            index_list = request.form.getlist("checkbox_rows")
            print(index_list)
            #The column of crosstab
            column_list = request.form.getlist("checkbox_columns")
            print(column_list)
            

           

            #Rereading the uploaded file and getting data 
            csv_file_path = session.get('uploaded_csv_file_path',None)
            print(csv_file_path)
            df = pd.read_csv(csv_file_path)
            print(df.head())
            column_names = df.columns.values
            column_names = column_names.tolist()
            row_data = list(df.head().values.tolist())
            print(column_names)
            tables=""
            titles=""

            if(len(index_list)==1 and len(column_list)==1):
                index_crosstab = [df[index_list[0]]]
                col_crosstab = df[column_list[0]]
            elif(len(index_list)==2 and len(column_list)==1):
                index_crosstab = [df[index_list[0]],df[index_list[1]]]
                col_crosstab = df[column_list[0]]

            elif(len(index_list)==1 and len(column_list)==2):
                index_crosstab = [df[index_list[0]]]
                col_crosstab = [df[column_list[0]],df[column_list[1]]]

            elif(len(index_list)==2 and len(column_list)==2):
                index_crosstab = [df[index_list[0]],df[index_list[1]]]
                col_crosstab = [df[column_list[0]],df[column_list[1]]]


            #Calling the crosstab function of pandas
            output_df = pd.crosstab(index_crosstab,col_crosstab)
            print(output_df)

            #Generating the tables for html tables
            tables = [output_df.to_html(classes='data')]
            #Generating the titles for html table
            titles = output_df.columns.values
          

        else:
            pass
            

    else:
        csv_file_path = ""
        column_names=""
        row_data=""
        tables=""
        titles=""
    
   

    return render_template('index.html',column_names=column_names, row_data=row_data, tables=tables, titles=titles,zip=zip)




#Running the app
if __name__ == '__main__':
    app.run(port=5000,debug=True)