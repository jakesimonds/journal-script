# process_template.py
import sys
from datetime import datetime
import requests


key = "ecf9828b39104016b5e190833230711"
base_url = "http://api.weatherapi.com/v1"
q = "04101"
aqi = "no"

url = f"{base_url}/current.json?key={key}&q={q}&aqi={aqi}"

# url = "http://api.weatherapi.com/v1/current.json?key=ecf9828b39104016b5e190833230711&q=04101&aqi=no"

response = requests.get(url)
#print(response.status_code)
data = response.json()


temp = data['current']['temp_f']



def process_template(file_path):
    with open(file_path, "r") as file:
        content = file.readlines()

    date = datetime.now()
    date_str = date.strftime("%Y-%m-%d %H:%M:%S\n")

    # Example of processing content with prompts
    # Add your logic here to customize the prompts and their handling

    with open(file_path, "w") as file:
        file.writelines(f"Current temp: {temp} \n\n")
        file.writelines(f"Time: {date_str}")
        file.writelines(content)


if __name__ == "__main__":
    process_template(sys.argv[1])
