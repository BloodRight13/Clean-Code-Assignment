# Task 1

def WeatherDataFetcher(city):
    
    # Simulated function to fetch weather data for a given city
    # Simulated data based on city
    
    print(f"Fetching weather data for {city}...")
    
    weather_data = {
        "New York": {"temperature": 70, "condition": "Sunny", "humidity": 50, "city": "New York"},
        "London": {"temperature": 60, "condition": "Cloudy", "humidity": 65, "city": "London"},
        "Tokyo": {"temperature": 75, "condition": "Rainy", "humidity": 70, "city": "Tokyo"}
    }
    return weather_data.get(city, {})

def DataParser(data):  # Function to parse weather data
    if not data:
        return "Weather data not available"
    city = data["city"]
    temperature = data["temperature"]
    condition = data["condition"]
    humidity = data["humidity"]
    return f"Weather in {city}: {temperature} degrees, {condition}, Humidity: {humidity}%"

def detailed_weather_forcast(city):  # Function to provide a detailed weather forecast for a city
    data = WeatherDataFetcher(city)
    return DataParser(data)

def display_weather(city):  # Function to display the basic weather forecast for a city
    data = WeatherDataFetcher(city)
    if not data:
        print(f"Weather data not available for {city}")
    else:
        weather_report = DataParser(data)
        print(weather_report)

def UserInterface(): 
    while True:
        city = input("Enter the city to get the weather forecast or 'exit' to quit: ")
        if city.lower() == 'exit':
            break
        
        detailed = input("Do you want a detailed forecast? (yes/no): no").lower()
        if detailed == 'yes':
            forecast = detailed_weather_forcast(city)
        else:
            forecast = display_weather(city)
        print(forecast)

if __name__ == "__main__":
    UserInterface()