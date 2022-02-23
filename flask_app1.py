#!/usr/bin/env python

from flask import Flask, json, render_template, request
import os

#create instance of Flask app
app = Flask(__name__)

## 1a:

#flask is calling a function called route to all the info in the json file
@app.route("/all")

def nobel():
    #referencing a path where the data is located
    json_url = os.path.join(app.static_folder,"","nobel.json")
    data_json = json.load(open(json_url))
    
    return render_template('index.html',html_page_text=data_json)

## 1b:

#flask route for year using GET
@app.route("/year/<year>", methods=['GET'])

def add_year(year):
    json_url = os.path.join(app.static_folder,"","nobel.json")
    data_json = json.load(open(json_url))
    #convert passed data into a variable
    data = data_json["prizes"]
    if request.method == 'GET':
        data_json = json.load(open(json_url))
        data = data_json["prizes"]
        year = request.view_args['year']
        output_data = [x for x in data if x['year']==year]
        
        #render template is always looking in template folder
        return render_template('index.html', html_page_text=output_data)

## 1c:  

@app.route("/add", methods=['POST'])
def form():
    form_url = os.path.join("templates","form.html")
    #send_file lets you send the contents in a form to a client
    return send_file(form_url)

#now write logic to get POSTed data from the form




if __name__ == "__main__":
    app.run(debug=True)

## 2: What kind of API did you build? What types of APIs are there? Why are APIs important?

## - The API that I built is a Web API. There are many types of APIs: Open APIs  - aka external/public have relaxed security measures allowing for developers and external users to access the data easily.
## Partner APIs promote communication between a company and its exeternal users. This type of API uses more securoty to grant data access to specific buisness partners
## Internal APIs aka private are hidden from external parties and enhance communication within an company. It has security measures to measure employee identification
## Composite APIs are robust and imporves data service performance and provides an all-in-one solution. It integrates multiple systems and combines all data needed to execute one operation

# Question: Can web-based APIs fall into any of the above API types or is it its own seperate thing?