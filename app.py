from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# In-memory dictionary to store mood-based lines
mood_lines = {
    'happy': ["Keep smiling!", "Today is a great day!", "Happiness is a choice."],
    'sad': ["This too shall pass.", "Stay strong!", "It's okay to feel sad sometimes."],
    'depressed': ["You are not alone.", "Things will get better.", "Keep going, one step at a time."],
    'love': ["Love is a beautiful journey.", "Cherish every moment.", "Love yourself first."],
    # Add more categories and lines as needed
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get-line', methods=['POST'])
def get_line():
    user_mood = request.json.get('mood').lower()
    lines = mood_lines.get(user_mood, ["Keep going, you're doing great!"])
    selected_line = random.choice(lines)
    return jsonify({"line": selected_line})

if __name__ == '__main__':
    app.run(debug=True)
