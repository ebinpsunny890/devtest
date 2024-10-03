from flask import Flask, jsonify
app = Flask(__name__)

@app.route(&#39;/api/hello&#39;, methods=[&#39;GET&#39;])
def hello():
return jsonify(message=&quot;Hello, World!&quot;)

if __name__ == &#39;__main__&#39;:
app.run(debug=True)
