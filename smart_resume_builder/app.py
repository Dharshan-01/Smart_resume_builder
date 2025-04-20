from flask import Flask, request, jsonify, render_template
from openai import OpenAI
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Replace with your actual OpenAI API key
OPENAI_API_KEY = "YOUR_OPENAI_API_KEY"
client = OpenAI(api_key=OPENAI_API_KEY)

@app.route('/')
def index():
    return render_template('chatbot.html')  # Serve the HTML file

@app.route('/api/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()
        message = data['message']

        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": message}
            ]
        )
        reply = completion.choices[0].message.content

        return jsonify({'reply': reply.strip()})

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)