# O.weather

[![Version](https://img.shields.io/badge/Version-1.09-blue.svg)](https://github.com/Superjulien/O.weather/) [![Python](https://img.shields.io/badge/Python_3-14354C?&logo=python&logoColor=white.svg)](https://www.python.org/)

O.weather is a simple Python script that allows you to fetch real-time weather information and display it either as an ASCII table or in plain text format. It uses the OpenWeatherMap API to retrieve weather data.

## Features

- Fetches and displays current weather conditions, including status, humidity, sunrise and sunset times, wind speed, and temperatures.
- Provides a detailed weather forecast for the upcoming day at the time you specify.

## Installation

Before you begin, make sure you have the following installed:

- Python 3.x
- The `pyowm` library

You can install the `pyowm` library using the following command:

```bash
pip install pyowm
```

1. Clone this repository to your local machine or download the ZIP file and extract it.
2. Navigate to the project directory:

```bash
cd O.weather/
```

## Configuration

1. Open the `o.weather.py` file in your preferred text editor.
2. Customize the values of the following variables according to your preferences:

- `CITY`: Replace this variable with the name of the city for which you want to obtain weather information.

- `API_KEY`: Replace this variable with your OpenWeatherMap API key. You can obtain an API key by signing up at [OpenWeatherMap](https://openweathermap.org/api) (free registration available).

- `HOURS_TO_ADD`: Set the number of hours to add to the current time to get weather forecasts for the desired time.

- `HOURS_TO_ADD_TWO`: Set the number of hours to add to the current time to get weather forecasts for another desired time.

- `UNITS`: Choose between 'celsius' or 'fahrenheit' for your preferred temperature unit.

- `LANG`: Choose the language in which you want to receive weather information (e.g., 'EN' for English).

## Usage

To use the script, you need to execute `o.weather.py` using Python. Here's how it works:

```bash
python3 o.weather.py
```

## Command-Line Options

The script supports the following command-line options:

- `-a` or `--ascii`: Use this option to generate a weather report in ASCII table format.

- `-v` or `--version`: Use this option to display the script's version number.

## How It Works

The script operates by following these steps:

1. It retrieves the current time.

2. It uses the OpenWeatherMap API to obtain current weather information for the configured city.

3. It adjusts the current time by adding the number of hours specified in `HOURS_TO_ADD` and `HOURS_TO_ADD_TWO` to obtain two future moments.

4. It fetches weather forecasts for these two future moments using the OpenWeatherMap API.

5. It then displays the weather information either as an ASCII table or in plain text format, depending on the command-line options.

## Examples

1. Display a weather report in plain text format for the configured city:

```bash
python3 o.weather.py
```

2. Generate a weather report in ASCII table format for the configured city:

```bash
python3 o.weather.py -a
```

3. Display the script's version:

```bash
python3 o.weather.py -v
```

## Sponsoring

This software is provided to you free of charge, with the hope that if you find it valuable, you'll consider making a donation to a charitable organization of your choice :

- SPA (Society for the Protection of Animals): The SPA is one of the oldest and most recognized organizations in France for the protection of domestic animals. It provides shelters, veterinary care, and works towards responsible adoption.

  [![SPA](https://img.shields.io/badge/Sponsoring-SPA-red.svg)](https://www.la-spa.fr/)

- French Popular Aid: This organization aims to fight against poverty and exclusion by providing food aid, clothing, and organizing recreational activities for disadvantaged individuals.

  [![SPF](https://img.shields.io/badge/Sponsoring-Secours%20Populaire%20Français-red.svg)](https://www.secourspopulaire.fr)

- Doctors Without Borders (MSF): MSF provides emergency medical assistance to populations in danger around the world, particularly in conflict zones and humanitarian crises.

  [![MSF](https://img.shields.io/badge/Sponsoring-Médecins%20Sans%20Frontières-red.svg)](https://www.msf.fr)

- Restaurants of the Heart : Restaurants of the Heart provides meals, emergency accommodation, and social services to the underprivileged.

  [![RDC](https://img.shields.io/badge/Sponsoring-Restaurants%20du%20Cœur-red.svg)](https://www.restosducoeur.org)

- French Red Cross: The Red Cross offers humanitarian aid, emergency relief, first aid training, as well as social and medical activities for vulnerable individuals.

   [![CRF](https://img.shields.io/badge/Sponsoring-Croix%20Rouge%20Française-red.svg)](https://www.croix-rouge.fr)

Every small gesture matters and contributes to making a real difference.

## Support
For support email : 

[![Gmail: superjulien](https://img.shields.io/badge/Gmail-Contact%20Me-purple.svg)](mailto:contact.superjulien@gmail.com) [![Tutanota: superjulien](https://img.shields.io/badge/Tutanota-Contact%20Me-green.svg)](mailto:contacts.superjulien@tutanota.com)
