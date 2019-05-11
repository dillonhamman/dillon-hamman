"""
record_api.py: This program is a restful api that contains 3 GET methods
    and one POST method. The GET methods can return the sorted records in
    json by age, lastname or gender(followed by last name).
"""
# import flask for api
# import jsonify, and request to obtain POST request and json output
from flask import Flask
from flask import jsonify, request
# import Recorder_Sorter.py to obtain Global lists and read_post function
from Record_Sorter import*

app = Flask(__name__)


@app.route('/', methods=['GET'])
def main():
    """Main funciton returns all the current records in the list
    and uses GENDER as the example"""
    return jsonify(GENDER)


@app.route('/records/gender', methods=['GET'])
def api_gender():
    """First GET method returns the GENDER sorted list in json"""
    return jsonify(GENDER)


@app.route('/records/age', methods=['GET'])
def api_birthdate():
    """Second GET method returns the DOB sorted list in json"""
    return jsonify(DOB)


@app.route('/records/lastname', methods=['GET'])
def api_name():
    """Last GET method returns the LASTNAME sorted list in json"""
    return jsonify(LASTNAME)


@app.route('/add', methods=['POST'])
def add_record():
    new_record_string = request.json['record']
    # add to the 3 lists stored in new_record_string
    read_post(new_record_string)


if __name__ == '__main__':
    app.run(debug=True)
