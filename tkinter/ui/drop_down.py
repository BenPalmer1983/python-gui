
import json

class DropDown:

    @staticmethod
    def load(file_path):
        try:
            with open(file_path, "r") as file:
                data = json.load(file)
                return data.get("dropdown_options", [])  # Get list or return empty list if missing
        except (FileNotFoundError, json.JSONDecodeError):
            return ["Error: No Data"]  # Handle errors
        
