from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

languages = [{'name':'Java'},{'name':'Python'}]

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/test',methods=['GET'])
def test():
    return jsonify({'message': 'It works!'})  
    
@app.route('/lang',methods=['GET'])
def lang():
    return jsonify({"languages": languages})    

@app.route('/lang/<string:name>',methods=['GET'])
def return_one(name):
    langs = [lang for lang in languages if lang['name'] == name]
    return jsonify({"language":langs[0]})

@app.route('/lang',methods=['POST'])
def add_one():
    lang = {'name': request.json['name']}
    languages.append(lang)
    return jsonify({"languages": languages})    


if __name__ == '__main__':
    app.run(debug=True)


