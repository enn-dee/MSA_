import requests

url = "http://api.aladhan.com/v1/calendar/2017/4?latitude=51.508515&longitude=-0.1254872&method=2http://api.aladhan.com/v1/calendar/2019?latitude=51.508515&longitude=-0.1254872&method=2"

response = requests.get(url)

while True:
    
    if response.status_code == 200:
        try:
            
            getIqamah = input("****Enter Prayer name to know iqamah timing or Type exit to leave***\n")
            getIqamah= getIqamah.capitalize()
            
            if getIqamah.lower() =="exit":
                print("Exiting...")
                break;
            else:
                response_json = response.json()
                data = response_json['data']
               
                try:
                    timings = data[0]['timings']
                    
                    if getIqamah in timings:
                        iqamah_time = timings[getIqamah]
                        print(f"{getIqamah} Iqamah timing: {iqamah_time}")
                    else:
                        print(f"Prayer name '{getIqamah}' not found in the timings.")    
                except KeyError:
                    print(f"{getIqamah} Not found")
                
        except requests.exceptions.JSONDecodeError:
            print("Error: The response is not in JSON format")
            print("Raw response content:", response.text)
