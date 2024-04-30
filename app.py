from flask import Flask, render_template, request, jsonify
import requests

RASA_API_URL = "http://localhost:5002/api"

app= Flask(__name__)

@app.route('/')
def index():
    return render_template ('index.html')

@app.route('/api', method=['POST'])
def webhook():
    user_message = request.json['message']
    print("User Message:", user_message)
    
    # Send user message to Tasa and get bot's response
    rasa_response = request.post(RASA_API_URL, json={'messsage': user_message})
    rasa_response_json = rasa_response.json()
    
    print("Rasa Response:", rasa_response_json)
    
    bot_response = rasa_response_json[0]['text'] if rasa_response else 'Sorry I didn\'t understand that.'
    
    return jsonify({'response': bot_response})
   

if __name__ == "__main__":
    app.run(debug = True, port= 3000)