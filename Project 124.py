from flask import Flask, jsonify, request

app = Flask(__name__)

contacts = [
    {
        "Contact" : 9130292849,
        "Name" : "Lily",
        "done" : False,
        "id" : 1,
    },

    {
        "Contact" : 934019865,
        "Name" : "Bobby",
        "done" : False,
        "id" : 2,        
    }    
]
@app.route("/post-contacts", methods=["POST"])

def add_contact():
    if not request.json:
        return jsonify({
            "status": "error",
            "message" : "please provide data!"
        }, 400)

    contact = {
        'id' : contacts[-1]['id']+1,
        'tilte' : request.json['title'],
        'description' : request.json.get('description', "empty")
    }

    contacts.append(contact)
    return jsonify({
        "status" : "success",
        "message" : "task added successfully",
    })

@app.route("/get-contacts", methods = ["GET"])

def get_contact():
    return jsonify({
        "contact" : contacts
    })

if  (__name__ == "__main__"):
    app.run(debug = True)