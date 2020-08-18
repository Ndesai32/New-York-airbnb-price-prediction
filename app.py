from flask import Flask, request, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('AB_NYC_Airbnb.pkl', 'rb'))


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/prediction', methods=['POST'])
def predict():
    if request.method == 'POST':

        # Neighbourhood_Group

        neighbourhood_group = request.form.get("neighbourhood_group", False)

        if (neighbourhood_group == 'Bronx'):
            Bronx = 1,
            Brooklyn = 0,
            Manhattan = 0,
            Queens = 0,
            Staten_Island = 0

        elif (neighbourhood_group == 'Brooklyn'):
            Bronx = 0,
            Brooklyn = 1,
            Manhattan = 0,
            Queens = 0,
            Staten_Island = 0

        elif (neighbourhood_group == 'Manhattan'):
            Bronx = 0,
            Brooklyn = 0,
            Manhattan = 1,
            Queens = 0,
            Staten_Island = 0

        elif (neighbourhood_group == 'Queens'):
            Bronx = 0,
            Brooklyn = 0,
            Manhattan = 0,
            Queens = 1,
            Staten_Island = 0

        elif (neighbourhood_group == 'Staten_Island'):
            Bronx = 0,
            Brooklyn = 0,
            Manhattan = 0,
            Queens = 0,
            Staten_Island = 1

        else:
            Bronx = 0,
            Brooklyn = 0,
            Manhattan = 0,
            Queens = 0,
            Staten_Island = 0

        # print(Bronx,
        # Brooklyn,
        # Manhattan,
        # Queens,
        # Staten_Island)

        # Latitude

        latitude = int(request.form.get("latitude", False))

        # Print(Latitude)

        # Longitude

        longitude = int(request.form.get("longitude", False))

        # Print(Longitude)

        # Room_Type

        room_types = request.form.get("room_types", False)
        if (room_types == 'Entire_home_apt'):
            Entire_home_apt = 1,
            Private_room = 0,
            Shared_room = 0

        elif (room_types == 'Private_room'):
            Entire_home_apt = 0,
            Private_room = 1,
            Shared_room = 0

        elif (room_types == 'Shared_room'):
            Entire_home_apt = 0,
            Private_room = 0,
            Shared_room = 1

        else:
            Entire_room_apt = 0,
            Private_room = 0,
            Shared_room = 0

            # print(Entire_room/apt,
            # Private_room,
            # Shared_room)

        # Minimum_Nights

        minimum_nights = int(request.form.get("minimum_nights", False))

        # print(Minimum_nights)

        # Number of reviews

        number_of_reviews = int(request.form.get("number_of_reviews", False))

        # print(number_of_nights)

        # availability

        availability_365 = int(request.form.get("availability_365", False))

        # print(Availability_365)

        prediction = model.predict([[
            neighbourhood_group,
            latitude,
            longitude,
            room_types,
            minimum_nights,
            number_of_reviews,
            availability_365
        ]])

        output = round(prediction[0], 2)

        return render_template('index.html', prediction_text="Your Airbnb House price is $ {}".format(output))

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
