from elvia import Elvia
import json
import asyncio
import os

# token from elvia.no/minside
meter_value_token = os.environ.get("ELVIA_METER_VALUE_TOKEN")

grid_tariff_token = os.environ.get("ELVIA_GRID_TARIFF_TOKEN")

# the metering point id of your home
metering_point_id = os.environ.get("ELVIA_METERING_POINT_ID")

elvia = Elvia(grid_tariff_token = grid_tariff_token)


elvia = Elvia(meter_value_token = meter_value_token)

async def get_meter_values():
    meter_value_client = elvia.meter_value()
    meter_values = await meter_value_client.get_meter_values(
        start_time = "2022-09-01T00:00:00",
        end_time = "2022-10-01T00:00:00",
        metering_point_ids = [metering_point_id],
        include_production = True
    )
    print(json.dumps(meter_values))
asyncio.run(get_meter_values())

import sys
sys.exit(0)

async def get_grid_tariffs():
    grid_tariff_client = elvia.grid_tariff()

    grid_tariffs = await grid_tariff_client.grid_tariffs_for_metering_points(
        range = "today",
        #start_time = "2022-08-01T00:00:00",
        #end_time = "2022-08-02T00:00:00",
        metering_point_ids = [metering_point_id]
    )
    print(json.dumps(grid_tariffs))

asyncio.run(get_grid_tariffs())



