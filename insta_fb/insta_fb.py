from  dotenv import load_dotenv
import requests
import json
import time
import csv
import os

from constants import INSTA_BRIGHTDATA_URL, NUM_OF_INSTA_POSTS, GET_INSTA_SNAPSHOT, SNAP_SHOT_FORMAT, FB_BRIGHTDATA_URL, FB_URL, NUM_OF_FB_POSTS



class bright_data:

    def __init__(self):
        print("Bright data initialized")

    def search_insta_keyword(self,keyword_input):
        self.keyword_input = keyword_input
        url = INSTA_BRIGHTDATA_URL
        load_dotenv(override=True)

        headers = {
            "Authorization": "Bearer "+ os.getenv("BRIGHTDATA_APIKEY"),
            "Content-Type": "application/json"
        }

        data = [
            {
                "keyword": self.keyword_input,
                "num_of_posts": NUM_OF_INSTA_POSTS,
                "start_date": "",
                "end_date": ""
            }
        ]


        try:
            response = requests.post(url, headers=headers, json=data)
            response_str = response.content.decode('utf-8')
            # Parse the string to a dictionary
            response_dict = json.loads(response_str)

            time.sleep(3)
            # Access the 'status' field
            snapshot_id = response_dict.get("snapshot_id")
          
            # Convert the byte string to a string
            return snapshot_id

    
        except:
            return "API credentials might be wrong. pls check if it got expired or not"
        
    def search_fb_profile_url(self,profile_url):
        self.profile_url = profile_url
        print(self.profile_url )
        load_dotenv(override=True)

        headers = {
            "Authorization": "Bearer "+ os.getenv("BRIGHTDATA_APIKEY"),
            
            "Content-Type": "application/json"
        }

        data = [
            {
                "url": FB_URL + self.profile_url+ "/",
                "num_of_posts": NUM_OF_FB_POSTS,
                "start_date": "",
                "end_date": ""
            }
        ]

        print(data )

        try:
            response = requests.post(FB_BRIGHTDATA_URL, headers=headers,json=data)
            print(response.content)
            response_str = response.content.decode('utf-8')

            
            # Parse the string to a dictionary
            response_dict = json.loads(response_str)

            time.sleep(3)
            # Access the 'status' field
            snapshot_id = response_dict.get("snapshot_id")
          
            # Convert the byte string to a string
            return snapshot_id

    
        except:
            return "API credentials might be wrong. pls check if it got expired or not"
        
    def get_insta_fb_snapshot_initial_status(self,snapshot_id):
        self.snapshot_id = snapshot_id
        url = GET_INSTA_SNAPSHOT+snapshot_id+SNAP_SHOT_FORMAT

        load_dotenv(override=True)

        headers = {
            "Authorization": "Bearer "+ os.getenv("BRIGHTDATA_APIKEY"),
            "Content-Type": "application/json"
        }

        print(url)

        response = requests.get(url, headers=headers)
        # Convert the byte string to a string
        response_str = response.content.decode('utf-8')

        # Parse the string to a dictionary
        response_dict = json.loads(response_str)
                # Access the 'status' field
        status = response_dict.get("status")
        return status
       
        
    def get_insta_snapshot(self,snapshot_id):
        self.snapshot_id = snapshot_id
        url = GET_INSTA_SNAPSHOT+snapshot_id+SNAP_SHOT_FORMAT

        print(url)

        load_dotenv(override=True)

        headers = {
            "Authorization": "Bearer "+ os.getenv("BRIGHTDATA_APIKEY"),
            "Content-Type": "application/json"
        }

        status = "running"

        try:
            time.sleep(20)
            while(status=="running"):
                
                response = requests.get(url, headers=headers)
                # Convert the byte string to a string
                response_str = response.content.decode('utf-8')

                # Parse the string to a dictionary
                response_dict = json.loads(response_str)
                # Access the 'status' field
                status = response_dict.get("status")
        except:
            print("loop ended")


        if status!="failed":
            print(f"status = {status}")

            print(response.content)

            # Simulating the response content for demonstration purposes
            # Replace `response.content` with your actual response content
            content = response.content.decode('utf-8')  # Decode the content from bytes to string
            lines = content.splitlines()  # Split the content into lines

            # Create a CSV reader to parse the lines
            reader = csv.reader(lines)

            # Extract the header (first line)
            header = next(reader)

            # Open a new file to write the parsed data
            with open('insta_output.csv', 'w', newline='', encoding='utf-8') as csvfile:
                # Create a CSV writer object
                writer = csv.writer(csvfile)
                
                # Write the header row to the CSV file
                writer.writerow(header)
                
                # Process and write each row
                for row in reader:
                    parsed_row = []
                    for value in row:
                        # Try to parse fields that may contain JSON data
                        try:
                            parsed_value = json.loads(value)
                            # Convert back to string if it's a complex object like a dict or list
                            if isinstance(parsed_value, (dict, list)):
                                parsed_value = json.dumps(parsed_value)
                        except (json.JSONDecodeError, TypeError):
                            # If it's not JSON, keep the original value
                            parsed_value = value
                        parsed_row.append(parsed_value)
                    
                    # Write the parsed row to the CSV file
                    writer.writerow(parsed_row)

            print("Data has been successfully written to output.csv")

        else:
            print("snap shot failed")


    def get_fb_snapshot(self,snapshot_id):
        self.snapshot_id = snapshot_id
        url = GET_INSTA_SNAPSHOT+snapshot_id+SNAP_SHOT_FORMAT

        print(url)

        load_dotenv(override=True)

        headers = {
                "Authorization": "Bearer "+ os.getenv("BRIGHTDATA_APIKEY"),
                "Content-Type": "application/json"
            }

        status = "running"

        try:
            time.sleep(20)
            while(status=="running"):
                 
                response = requests.get(url, headers=headers)
                # Convert the byte string to a string
                response_str = response.content.decode('utf-8')

                # Parse the string to a dictionary
                response_dict = json.loads(response_str)
                # Access the 'status' field
                status = response_dict.get("status")
        except:
            print("loop ended")


        if status!="failed":
            print(f"status = {status}")
            print(response.content)

            # Simulating the response content for demonstration purposes
            # Replace `response.content` with your actual response content
            content = response.content.decode('utf-8')  # Decode the content from bytes to string
            lines = content.splitlines()  # Split the content into lines

            # Create a CSV reader to parse the lines
            reader = csv.reader(lines)
            # Extract the header (first line)
            header = next(reader)
            # Open a new file to write the parsed data
            with open('fb_output.csv', 'w', newline='', encoding='utf-8') as csvfile:
            # Create a CSV writer object
                writer = csv.writer(csvfile)
                 
                # Write the header row to the CSV file
                writer.writerow(header)
                  
                # Process and write each row
                for row in reader:
                    parsed_row = []
                    for value in row:
                    # Try to parse fields that may contain JSON data
                        try:
                            parsed_value = json.loads(value)
                            # Convert back to string if it's a complex object like a dict or list
                            if isinstance(parsed_value, (dict, list)):
                                parsed_value = json.dumps(parsed_value)
                        except (json.JSONDecodeError, TypeError):
                                # If it's not JSON, keep the original value
                            parsed_value = value
                            parsed_row.append(parsed_value)
                        
                        # Write the parsed row to the CSV file
                    writer.writerow(parsed_row)

            print("Data has been successfully written to output.csv")

        else:
            print("snap shot failed")