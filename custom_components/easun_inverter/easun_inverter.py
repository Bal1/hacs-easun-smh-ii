
import socket

class EasunInverter:
    def __init__(self, ip_address, port=502, timeout=5):
        self.ip_address = ip_address
        self.port = port
        self.timeout = timeout
        self.connection = None

    def connect(self):
        self.connection = socket.create_connection((self.ip_address, self.port), timeout=self.timeout)

    def disconnect(self):
        if self.connection:
            self.connection.close()
            self.connection = None

    def send_command(self, command):
        if not self.connection:
            raise ConnectionError("No connection established. Call connect() first.")
        self.connection.sendall((command + "\r").encode())
        response = self.connection.recv(1024).decode().strip()
        return response

    def fetch_voltage(self):
        response = self.send_command("QPGS0")
        return self._parse_voltage_response(response)

    def set_voltage(self, voltage):
        command = f"SETVOLT:{voltage}"
        return self.send_command(command)

    def _parse_voltage_response(self, response):
        if "Voltage:" in response:
            return response.split("Voltage:")[1].replace("V", "").strip()
        return "Unknown"
    