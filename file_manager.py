import os

class FileManager:
    @staticmethod
    def write_log(data):
        # Create data folder if it doesn't exist
        if not os.path.exists('data'):
            os.makedirs('data')
        
        with open("data/traffic_history.txt", "a") as file:
            file.write(data + "\n")

    @staticmethod
    def read_history():
        try:
            with open("data/traffic_history.txt", "r") as file:
                return file.readlines()
        except FileNotFoundError:
            return ["No history found."]