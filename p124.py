from flask import Flask,jsonify,request
app=Flask(__name__)

contacts=[ { "id" : 1, "name" :u"Purvaa" , "last_name" : u"Barot", "number":1234456789, 'done':False }, 
        { 'id':2, "name" :u"Jaini" , "last_name" : u"Solanki", "number":1234456789, 'done':False }, ]

@app.route("/add-data" , methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status" : "error",
            "message":"Please provide data"
        }, 400 )

    contact={ 'id':tasks[-1]["id"]+1, 'name':request.json["name"], 'last_name':request.json["last_name"], 'done':False , "number":request.json.get("number")}
    contacts.append(contact)
@app.route("/get-data")
def get_task():
    return jsonify({
        "data":contacts
    })

@app.route("/")
def hello():
    return "Hello"

if __name__ == "__main__":
    app.run(debug=True)        

