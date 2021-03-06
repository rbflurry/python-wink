from pywink.devices.base import WinkDevice


class WinkEggtray(WinkDevice):
    """
    Represents a Wink eggminder egg tray.
    """

    def __init__(self, device_state_as_json, api_interface):
        super(WinkEggtray, self).__init__(device_state_as_json, api_interface)
        self._capability = None
        self._unit = "eggs"

    def capability(self):
        # Eggtray has no capability.
        return self._capability

    def unit(self):
        return self._unit

    def state(self):
        return self._last_reading.get("inventory")
