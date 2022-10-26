"""
Final Implementation of WeatherData.  Complete all the TODOs
"""


###################################
# Base Classes #
###################################
from ast import Sub


class Subject:
    
    def __init__(self):
        self.observers = []
    
    
    # Both of the following two methods take an
    # observer as an argument; that is, the observer
    # to be registered ore removed.
    def registerObserver(self, observer):
        self.observers.append(observer)
    def removeObserver(self, observer):
        self.observers.remove(observer)

    # This method is called to notify all observers
    # when the Subject's state (measuremetns) has changed.
    def notifyObservers():
        "Subject's state has been changed"

# The observer class is implemented by all observers,
# so they all have to implemented the update() method. Here
# we're following Mary and Sue's lead and
# passing the measurements to the observers.
class Observer:
    def __init__(self, data):
        self.temp = 0
        self.humidity = 0
        self.pressure = 0
        
        self.data = data
        data.registerObserver(self)
        
    def update(self, temp, humidity, pressure):
        self.temp = temp
        self.humidity = humidity
        self.pressure = pressure
        self.notifyObservers()
        self.display()


###################################
# Children Classes #
###################################

# WeatherData now implements the subject interface.
class WeatherData(Subject):

    def __init__(self):
        super().__init__()
        self.temperature = 0
        self.humidity = 0
        self.pressure = 0

    def notifyObservers(self):
        # We notify the observers when we get updated measurements
        # from the Weather Station.
        for ob in self.observers:
            ob.update(self.temperature, self.humidity, self.pressure)

    def measurementsChanged(self):
        self.notifyObservers()

    def setMeasurements(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure

        self.measurementsChanged()

    # other WeatherData methods here.

class CurrentConditionsDisplay(Observer):

    def __init__(self, weatherData):
        super().__init__(weatherData)


    def display(self):
        print("Current conditions:", self.temp,
              "F degrees and", self.humidity,"[%] humidity",
              "and pressure", self.pressure)

# : implement StatisticsDisplay class and ForecastDisplay class.


class StatisticsDisplay(Observer):
    def __init__(self, weatherData):
        super().__init__(weatherData)

        # Temperature Data
        self.min_temp = float('inf')
        self.average_temp = 0
        self.max_temp = float('-inf')


        # Humidity Data
        self.min_humidity = float('inf')
        self.average_humidity = 0
        self.max_humidity = float('-inf')

        # Pressure Data
        self.min_pressure = float('inf')
        self.average_pressure = 0
        self.max_pressure = float('-inf')
        
    def calculate_stats(self):
        
        # Claculations for Temperature Data
        self.min_temp = round(min(self.min_temp, self.temp), 2)
        self.max_temp = round(max(self.max_temp, self.temp), 2)
        self.average_temp = round((self.max_temp + self.min_temp) / 2, 2)
        
        # Claculations for Humidity Data
        self.min_humidity = round(min(self.min_humidity, self.humidity), 2)
        self.max_humidity = round(max(self.max_humidity, self.humidity), 2)
        self.average_humidity = round(
            (self.max_humidity + self.min_humidity) / 2, 2)
        
        # Claculations for Pressure Data
        self.min_pressure = round(min(self.min_pressure, self.pressure), 2)
        self.max_pressure = round(max(self.max_pressure, self.pressure), 2)
        self.average_pressure = round(
            (self.max_pressure + self.min_pressure) / 2, 2)
        
    def display_data(self):
        
        self.calculate_stats()
        
        print("Weather Statistics Today: ")
        print('-------------------------')
        print("Minimum | Average | Maximum Temperature ")
        print(self.min_temp, " | ", self.average_temp, ' | ', self.max_temp)
        print('-------------------------')
        print("Minimum | Average | Maximum Humidity ")
        print(self.min_humidity, " | ", self.average_humidity, ' | ', self.max_humidity)
        print('-------------------------')
        print("Minimum | Average | Maximum Pressure ")
        print(self.min_pressure, " | ", self.average_pressure, ' | ', self.max_pressure)


class ForecastDisplay(Observer):
        def __init__(self, weatherData):
            super().__init__(weatherData)
            self.forecast_temp = 0
            self.forecast_humidity = 0
            self.forecast_pressure = 0

        def forecast(self):
            self.forecast_temp = round(
                self.temp + 0.11 * self.humidity + 0.22 * self.pressure, 2)
            self.forecast_humidity = round(self.humidity - 0.9 * self.humidity, 2)
            self.forecast_pressure = round(
                self.pressure + 0.1 * self.temp - 0.21 * self.pressure, 2)

        def display(self):

            self.forecast()

            print("Todays forecast:")
            print("Temperature | Humidity | Pressure")
            print(self.forecast_temp, self.forecast_humidity, self.forecast_pressure)


class WeatherStation:
    def main(self):
        weather_data = WeatherData()
        current_display = CurrentConditionsDisplay(weather_data)
        stats = StatisticsDisplay(weather_data)
        forecast = ForecastDisplay(weather_data)


        weather_data.setMeasurements(80, 65,30.4)
        weather_data.setMeasurements(82, 70,29.2)
        weather_data.setMeasurements(78, 90,29.2)

        # un-register the observer
        #weather_data.removeObserver(current_display)
        #weather_data.setMeasurements(120, 100,1000)



if __name__ == "__main__":
    w = WeatherStation()
    w.main()
