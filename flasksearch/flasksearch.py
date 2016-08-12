import csv, os
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

file_path = os.path.join(os.path.dirname(__file__), "clubs.csv")

rowdata = []

#imports latest clublist
def clublist_as_lists():
    with open(file_path, newline='') as f:
        clublist = csv.reader(f, delimiter=',', quotechar='|') #reads clublist via reader
        for row in clublist: #goes through every iteration of clublist
            rowdata.append(row) #adds row to rowdata



clublist_as_lists()


@app.route('/')
def database():
    return render_template('index.html', rowdata=rowdata)

@app.route('/search', methods=['POST', 'GET'])
def search():
    search_result = []

    if request.method == 'POST':
        inputa = str(request.form['search'])
        for cars in rowdata:
            if inputa.lower() in map(str.lower, cars): #Add additional row to table if addition found and normalizes for string case
                search_result.append(cars)
        if search_result == []: #This basically says that if the array is empty to say that no result could be found
            search_result = ["noresult"]
    return render_template('search.html', search_result=search_result)

if __name__ == '__main__':
    app.run(debug=True)
