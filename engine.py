from utils.config import MIN_GREEN, MAX_GREEN, THRESHOLD
from utils.file_manager import FileManager

class SmartEngine:
    def __init__(self, junction_obj):
        self.junction = junction_obj

    def process(self):
        print(f"--- Processing Junction: {self.junction.name} ---")
        
        for lane in self.junction.lanes:
            count = self.junction.sensors[lane].get_vehicle_count()
            
            # Smart Logic: Dynamic Timing
            green_time = MAX_GREEN if count > THRESHOLD else MIN_GREEN
            
            status = f"Lane {lane}: {count} cars detected. Green Time: {green_time}s"
            print(status)
            
            # Save to file
            FileManager.write_log(status)