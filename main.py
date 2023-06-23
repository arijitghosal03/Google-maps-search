from flask import Flask, render_template, request, jsonify
import googlemaps

app = Flask(__name__)
gmaps = googlemaps.Client(key= 'AIzaSyDzCkAHtwyy-gZvoZWVrPzXq4oTjH8jlCc')


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/autocomplete', methods=['GET'])
def autocomplete():
    input_text = request.args.get('input')

    # Call the Places Autocomplete API
    result = gmaps.places_autocomplete(input_text)

    # Extract the place predictions from the API response
    predictions = [item['description'] for item in result]

    return jsonify(predictions)


if __name__ == '__main__':
    app.run()
