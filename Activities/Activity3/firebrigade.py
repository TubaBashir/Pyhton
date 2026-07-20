import time
from datetime import datetime

class FireStation:
    def __init__(self, station_id, location, total_trucks):
        self.station_id = station_id
        self.location = location
        self.total_trucks = total_trucks
        self.available_trucks = total_trucks

    def dispatch_trucks(self, count):
        if self.available_trucks >= count:
            self.available_trucks -= count
            return True
        return False

    def return_trucks(self, count):
        if self.available_trucks + count <= self.total_trucks:
            self.available_trucks += count
        else:
            self.available_trucks = self.total_trucks


class IncidentCommand:
    def __init__(self):
        self.active_incidents = {}
        self.incident_counter = 1

    def report_incident(self, location, severity_level, station):
        """
        Severity Levels: 
        1 - Minor (1 Truck needed)
        2 - Medium (2 Trucks needed)
        3 - Major / Working Fire (3+ Trucks needed)
        """
        required_trucks = severity_level
        incident_id = f"INC-{self.incident_counter:04d}"
        
        print(f"\n🚨 [{datetime.now().strftime('%H:%M:%S')}] EMERGENCY REPORTED at {location} (Severity Level: {severity_level})")
        
        # Check resources and dispatch
        if station.dispatch_trucks(required_trucks):
            self.active_incidents[incident_id] = {
                "location": location,
                "severity": severity_level,
                "station_id": station.station_id,
                "trucks_dispatched": required_trucks,
                "status": "RESPONDING"
            }
            print(f"🚒 CODE RED: {required_trucks} fire engine(s) dispatched from Station {station.station_id}.")
            print(f"📋 Incident {incident_id} logged. Status: RESPONDING.")
            self.incident_counter += 1
            return incident_id
        else:
            print(f"❌ RESOURCE ERROR: Station {station.station_id} has insufficient trucks for this incident!")
            print(f"⚠️ Requesting mutual aid from neighboring departments...")
            return None

    def resolve_incident(self, incident_id, station):
        if incident_id in self.active_incidents:
            incident = self.active_incidents[incident_id]
            trucks_to_return = incident["trucks_dispatched"]
            station.return_trucks(trucks_to_return)
            
            incident["status"] = "ALL CLEAR"
            print(f"\n🟢 [{datetime.now().strftime('%H:%M:%S')}] Incident {incident_id} at {incident['location']} resolved.")
            print(f"🔄 {trucks_to_return} fire engine(s) returned to Station {station.station_id}. Available now: {station.available_trucks}")
            del self.active_incidents[incident_id]
        else:
            print("\n❌ Error: Incident ID not found.")


# --- Simulation Run ---
if __name__ == "__main__":
    # 1. Initialize a Fire Station (Station 1, Sector 4, 5 total trucks)
    hq_station = FireStation(station_id=1, location="Sector 4 Downtown", total_trucks=5)
    dispatcher = IncidentCommand()
    
    print(f"🔥 Fire Brigade System Online. Station {hq_station.station_id} has {hq_station.available_trucks} trucks available.")

    # 2. Simulate Incoming Emergency Calls
    inc1 = dispatcher.report_incident("123 Maple Street (House Fire)", severity_level=2, station=hq_station)
    time.sleep(1) # Simulating time passage
    
    inc2 = dispatcher.report_incident("Commercial Plaza (Kitchen Smoke)", severity_level=1, station=hq_station)
    time.sleep(1)

    # 3. Clear incidents as fire crews put out the fires
    dispatcher.resolve_incident(inc1, hq_station)
    dispatcher.resolve_incident(inc2, hq_station)
