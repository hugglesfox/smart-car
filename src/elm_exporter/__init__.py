import obd

from .car import Car
from .collectors import ObdCollector

from prometheus_client import Info
from prometheus_client.core import REGISTRY


car = Car()

commands = [
    # bank A
    "ENGINE_LOAD",
    "COOLANT_TEMP",
    "SHORT_FUEL_TRIM_1",
    "LONG_FUEL_TRIM_1",
    "SHORT_FUEL_TRIM_2",
    "LONG_FUEL_TRIM_2",
    "FUEL_PRESSURE",
    "INTAKE_PRESSURE",
    "RPM",
    "SPEED",
    "TIMING_ADVANCE",
    "INTAKE_TEMP",
    "MAF",
    "THROTTLE_POS",
    "AIR_STATUS",
    "O2_B1S1",
    "O2_B1S2",
    "O2_B1S3",
    "O2_B1S4",
    "O2_B2S1",
    "O2_B2S2",
    "O2_B2S3",
    "O2_B2S4",
    "RUN_TIME",
    # bank B
    "DISTANCE_W_MIL",
    "FUEL_RAIL_PRESSURE_VAC",
    "FUEL_RAIL_PRESSURE_DIRECT",
    "O2_S1_WR_VOLTAGE",
    "O2_S2_WR_VOLTAGE",
    "O2_S3_WR_VOLTAGE",
    "O2_S4_WR_VOLTAGE",
    "O2_S5_WR_VOLTAGE",
    "O2_S6_WR_VOLTAGE",
    "O2_S7_WR_VOLTAGE",
    "O2_S8_WR_VOLTAGE",
    "COMMANDED_EGR",
    "EGR_ERROR",
    "EVAPORATIVE_PURGE",
    "FUEL_LEVEL",
    "WARMUPS_SINCE_DTC_CLEAR",
    "DISTANCE_SINCE_DTC_CLEAR",
    "EVAP_VAPOR_PRESSURE",
    "BAROMETRIC_PRESSURE",
    "O2_S1_WR_CURRENT",
    "O2_S2_WR_CURRENT",
    "O2_S3_WR_CURRENT",
    "O2_S4_WR_CURRENT",
    "O2_S5_WR_CURRENT",
    "O2_S6_WR_CURRENT",
    "O2_S7_WR_CURRENT",
    "O2_S8_WR_CURRENT",
    "CATALYST_TEMP_B1S1",
    "CATALYST_TEMP_B2S1",
    "CATALYST_TEMP_B1S2",
    "CATALYST_TEMP_B2S2",
    # bank C
    "CONTROL_MODULE_VOLTAGE",
    "ABSOLUTE_LOAD",
    "COMMANDED_EQUIV_RATIO",
    "RELATIVE_THROTTLE_POS",
    "AMBIANT_AIR_TEMP",
    "THROTTLE_POS_B",
    "THROTTLE_POS_C",
    "ACCELERATOR_POS_D",
    "ACCELERATOR_POS_E",
    "ACCELERATOR_POS_F",
    "THROTTLE_ACTUATOR",
    "RUN_TIME_MIL",
    "TIME_SINCE_DTC_CLEARED",
    "ETHANOL_PERCENT",
    "EVAP_VAPOR_PRESSURE_ABS",
    "EVAP_VAPOR_PRESSURE_ALT",
    "SHORT_O2_TRIM_B1",
    "LONG_O2_TRIM_B1",
    "SHORT_O2_TRIM_B2",
    "LONG_O2_TRIM_B2",
    "FUEL_RAIL_PRESSURE_ABS",
    "RELATIVE_ACCEL_POS",
    "HYBRID_BATTERY_REMAINING",
    "OIL_TEMP",
    "FUEL_INJECT_TIMING",
    "FUEL_RATE",
    # elm
    "ELM_VOLTAGE",
]

REGISTRY.register(ObdCollector(car, [obd.commands[cmd] for cmd in commands]))

info = {}
vin = car.query(obd.commands.VIN).value

if vin is not None:
    info["vin"] = vin.decode()

CAR_INFO = Info("car", "Static Car Information")
CAR_INFO.info(info)
