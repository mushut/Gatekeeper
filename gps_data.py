import serial

class gps_data:
    def __init__(self):
        self.serial_gps = serial.Serial('/dev/ttyAMA0')

    def read_gprmc(self):
        coordinates = []
        received = False
        chars = ''

        # Reading can start from between the commands, so one partial line is read for certainity that the
        # rest of the messages can be read as whole messages
        temp_char = b'\x00'
        
        #while int.from_bytes(self.serial_gps.read(), byteorder='big') > 127:
        #    pass

        while temp_char != '\n':
            try:
                temp_char = self.serial_gps.read().decode('utf-8')
            except UnicodeDecodeError:
                pass

        while received == False:
            try:
                chars += self.serial_gps.read().decode('utf-8')
            except UnicodeDecodeError:
                pass
           
            if chars[-1] == '\n':
                temp_string = chars
                csv_list = temp_string.split(',')

                if csv_list[0] == "$GPRMC":
                    if csv_list[3] != '' and csv_list[5] != '':
                        coordinates = self.to_coordinates(csv_list[3], csv_list[5])
                    else:
                        coordinates = [0.0, 0.0]
                    received = True

                chars = ''

        return coordinates

    def to_coordinates(self, lat_string, lng_string):
        lat = float(lat_string[:2])
        lat_smaller = float(lat_string[2:])
        lng = float(lng_string[1:3])
        lng_smaller = float(lng_string[3:])

        lat += lat_smaller / 60
        lng += lng_smaller / 60

        return [lat, lng]
