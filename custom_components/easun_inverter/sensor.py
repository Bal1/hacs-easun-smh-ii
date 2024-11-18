
from homeassistant.helpers.entity import Entity

class EasunInverterSensor(Entity):
    def __init__(self, inverter, name):
        self._inverter = inverter
        self._name = name
        self._state = None

    @property
    def name(self):
        return self._name

    @property
    def state(self):
        return self._state

    def update(self):
        try:
            self._inverter.connect()
            self._state = self._inverter.fetch_voltage()
        except Exception as e:
            self._state = f"Error: {e}"
        finally:
            self._inverter.disconnect()
    