import requests
import json                                              
api_add = 'https://api.openweathermap.org/data/3.0/onecall'          
    

params = {
    'appid' : 'd7db31508de6b5a51eff1e86b8a07dca',
    'lat' : 30.19679,
    'lon' : 71.47824,
    'dt' : 1643803200                             
}

output_response = requests.get(api_add, params=params)   

if output_response.status_code == 200:                   

    output_data = output_response.json()  
    

    formatted_json = json.dumps(output_data, indent=4)

                        
    lines = formatted_json.split('\n')                   

    file_add = 'C:/Users/DELLL/Desktop/h/api_data.json'    
    with open(file_add,'w') as file:                    
        file.write( formatted_json)                      
    print('Your data is save successfully!')
else:
    print("API request failed with status code:", output_response.status_code)










