# API INTEGRATION AND DATA VISUALIZATION

*COMPANY* : CODTECH IT SOLUTIONS

*NAME* : BHAVYA SRI DINDUKURTHI

*INTERN ID* : CT04DN375

*DOMAIN* : PYTHON PROGRAMMING

*DURATION* : 4 WEEKS

*MENTOR* : NEELA SANTOSH


 **Project Overview: Visualizing Weather Forecasts with Python**

In this project, we built a simple but powerful weather forecasting tool using Python. The idea was to tap into real-time weather data using the OpenWeatherMap API and then bring that data to life through graphs that show temperature and humidity trends over five days. Instead of checking weather apps manually, this script fetches data for a chosen city and visually presents it in a clean, easy-to-understand format.

---

### The Tools Used in the Project

## Python 

We chose Python because it’s incredibly beginner-friendly and flexible. It’s widely used in data science, web development etc. In our case, it acted as the main engine that connected all the different parts of the project together.

## Requests – The Web Connector

To pull live weather data, we used the `requests` library. It sends a request like: “Hey, what’s the weather in Hyderabad for the next five days?” and the server replies with detailed weather data in a format our program can understand.

#### 🔹 Pandas – The Data Organizer

Once we had the raw data, we needed to make sense of it. That’s where `pandas` came in. It helped us turn the messy JSON (JavaScript Object Notation) response into a clean table (DataFrame) that was easier to work with. We could then filter, sort, and convert the data however we wanted—especially date and time information, which was key for our plots.

#### 🔹 Matplotlib and Seaborn – The Graph Ploteers

With our data cleaned up and organized, we needed to display it in a way that’s visually meaningful. `matplotlib` and `seaborn` did exactly that. `matplotlib` is great for building detailed plots, and `seaborn` makes those plots look more attractive right out of the box. Together, they helped us show temperature and humidity on a timeline, making trends easy to spot.

#### 🔹 OpenWeatherMap API – The Data Source

Everything hinges on the OpenWeatherMap API, which is an online service that provides free and paid access to weather data. By signing up, we received an API key that allowed us to make authorized requests. The API gave us a 5-day forecast broken down into 3-hour chunks—perfect for creating detailed, time-based visualizations.


## Where We Coded: Platforms and Editors 

To write and run this script, we can use editors like **VS Code** or **Jupyter Notebook**.

* **VS Code** is a great all-round editor with features like auto-completion, a built-in terminal, and error highlighting. It’s excellent for writing longer scripts. I have particullarly used VS code because it is easy to use 
             
* **Jupyter Notebook**, on the other hand, is perfect for data analysis. You can write your code in cells, see the output immediately, and even visualize graphs right inside the notebook.

Both are free and highly customizable, and they let you focus on building without getting in your way.


### Real-Life Applications

* **News and Media**: Weather channels and websites can use tools like this to automatically update and visualize forecasts for different regions.
* **Tourism & Travel**: Apps can show this kind of forecast to help users plan their trips—maybe avoid hiking when it’s going to rain . 
* **Agriculture**: Farmers can rely on this kind of data to plan watering schedules or harvesting, especially if they're using smart devices.
* **Smart Homes and IoT Devices**: Imagine your AC adjusting automatically based on tomorrow’s forecast. This data can feed directly into smart systems to optimize energy usage.
* **Emergency Planning**: For regions vulnerable to extreme weather, seeing visual trends early can help authorities prepare alerts or evacuation plans in advance.

  Absolutely! Here's a humanized, conversational rewrite of your paragraph that keeps your original message but makes it flow more naturally:


Right now, in May 2025, we’re seeing something unusual—heavy rainfall in cities where it’s typically supposed to be hot and sunny. In short, *May isn’t May-ing*! With such unpredictable weather, a project like this becomes especially useful. It allows us to get a glimpse of the upcoming weather patterns ahead of time, helping us plan our days better.

Of course, weather forecasting isn’t always perfect. These predictions are made based on past patterns and current data, and sometimes nature just has its own plans. So yes, there can be inaccuracies at times. But even with that margin of error, having access to this kind of tool can really help individuals and organizations make more informed decisions—whether it’s about travel, events, or just deciding whether or not to carry an umbrella.


