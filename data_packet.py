import datetime
import json

# Gets location from gps module and index for simulated data.
# Index is from 0 to 59 (lcm of 15 and 20 data points from simulations is 60).
class data_packet:
    def __init__(self, gps_coordinates, index_simulation):
        self.gps = gps_coordinates
        self.index = index_simulation
        self.sims = self.get_sims()
        self.time = self.add_time()
        self.data = {"gps_coordinates" : self.gps,
                     "sim1_coordinates" : self.sims[0],
                     "sim2_coordinates" : self.sims[1],
                     "date_and_time" : self.time}

    def get_sims(self):
        sim1 = []
        sim2 = []

        with open('/home/fleetmaster/Gatekeeper/simulation1_data.txt', 'r') as file_sim1:
            i = 0
            for line in file_sim1:
                # Convert index values of 0-59 to i values 0-14 with modulo
                if i == (self.index % 15):
                    csv_coord1 = line.split(',')
                    sim1.append(float(csv_coord1[0]))
                    sim1.append(float(csv_coord1[1]))
                    break
                else:
                    i += 1

        with open('/home/fleetmaster/Gatekeeper/simulation2_data.txt', 'r') as file_sim2:
            i = 0
            for line in file_sim2:
                # Convert index values of 0-59 to i values 0-19 with modulo
                if i == (self.index % 20):
                    csv_coord2 = line.split(',')
                    sim2.append(float(csv_coord2[0]))
                    sim2.append(float(csv_coord2[1]))
                    break
                else:
                    i += 1

        return [sim1, sim2]

    # Date and time as an integer list (year, month, day, hour, minute, second)
    def add_time(self):
        now = datetime.datetime.now()

        time_str = str(now.year) + "-"
        time_str += str(now.month) + "-"
        time_str += str(now.day) + "T"
        time_str += str(now.hour) + ":"
        time_str += str(now.minute) + ":"
        time_str += str(now.second)

        return time_str

    def return_json(self):
        data_json = json.dumps(self.data, sort_keys=True, indent=4)

        return data_json

    def return_log_data(self):
        data_log = "Log: "
        data_log += self.time + " - "
        data_log += str(self.gps[0]) + "," + str(self.gps[1]) + " - "
        data_log += str(self.index) + " - "
        data_log += str(self.sims[0]) + "," + str(self.sims[1]) + "\n"

        return data_log
