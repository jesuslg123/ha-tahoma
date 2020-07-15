"""Constants for the TaHoma integration."""

DOMAIN = "tahoma"

# Used to map the Somfy uiClass to the Home Assistant platform
TAHOMA_TYPES = {
    "Light": "light",
    "ExteriorScreen": "cover",
    "Pergola": "cover",
    "RollerShutter": "cover",
    "Window": "cover",
    "HeatingSystem": "climate",
    "TemperatureSensor": "sensor",
    "LightSensor": "sensor",
    "DoorLock": "lock",
    "OnOff": "switch",
    "AirFlowSensor": "binary_sensor",  # widgetName, uiClass is AirSensor (sensor)
    "WaterDetectionSensor": "binary_sensor",  # widgetName, uiClass is HumiditySensor (sensor)
    "HumiditySensor": "sensor",
    "GarageDoor": "cover",
    "CarButtonSensor": "binary_sensor",
    "ContactSensor": "binary_sensor",
    "RainSensor": "binary_sensor",
    "SmokeSensor": "binary_sensor",
    "OccupancySensor": "binary_sensor",
    "MotionSensor": "binary_sensor",
    "WindowHandle": "binary_sensor",
    "ExteriorVenetianBlind": "cover",
    "Awning": "cover",
    "Gate": "cover",
    "Curtain": "cover",
    "Generic": "cover",
    "SwingingShutter": "cover",
    "ElectricitySensor": "sensor",
    "AirSensor": "sensor",
    "Siren": "switch",
    "WindSensor": "sensor",
    "SunSensor": "sensor",
    "AdjustableSlatsRollerShutter": None,
    "Alarm": None,
    "Ballast": None,
    "Camera": None,
    "CircuitBreaker": None,
    "ConfigurationComponent": None,
    "ConsumptionSensor": "sensor",
    "Dock": None,
    "EvoHome": None,
    "ExteriorHeatingSystem": None,
    "GasSensor": "sensor",
    "GenericSensor": "sensor",
    "GroupConfiguration": None,
    "HeatPumpSystem": None,
    "HitachiHeatingSystem": None,
    "IRBlasterController": None,
    "IntrusionSensor": "sensor",
    "MusicPlayer": None,
    "NetworkComponent": None,
    "Oven": None,
    "Pod": None,
    "ProtocolGateway": None,
    "RemoteController": None,
    "Screen": "cover",
    "Shutter": "cover",
    "SunIntensitySensor": "sensor",
    "SwimmingPool": None,
    "ThermalEnergySensor": "sensor",
    "ThirdPartyGateway": "cover",
    "VenetianBlind": "cover",
    "VentilationSystem": None,
    "WashingMachine": None,
    "WaterHeatingSystem": None,
    "WaterSensor": "sensor",
    "WeatherSensor": "sensor",
    "Wifi": None,
}

CORE_ON_OFF_STATE = "core:OnOffState"

COMMAND_OFF = "off"
COMMAND_ON = "on"
