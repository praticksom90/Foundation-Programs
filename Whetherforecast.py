import requests

def get_weather(city):
    api_key = "The API Key"  # Your API key
    base_url = "URL of the Website providing API key"

    city = city.strip()
    if not city:
        print("Please enter a valid city name.")
        return

    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        # Check if API returned weather data
        if response.status_code == 200 and 'main' in data:
            temp = data['main']['temp']
            humidity = data['main']['humidity']
            description = data['weather'][0]['description']

            print(f"\nWeather in {city}:")
            print(f"Temperature: {temp}°C")
            print(f"Humidity: {humidity}%")
            print(f"Description: {description.capitalize()}\n")

        else:
            # API returned an error
            message = data.get('message', 'Unknown error.')
            print(f"\nError fetching weather for '{city}': {message}\n")

    except requests.exceptions.RequestException as e:
        # Handles network errors
        print("Network error:", e)


def main():
    print("🌤 Robust Weather Forecast App 🌤")
    while True:
        city = input("Enter city name (or 'exit' to quit): ")
        if city.lower() == 'exit':
            print("Goodbye!")
            break
        get_weather(city)


if __name__ == "__main__":
    main()
