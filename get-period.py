from elvia import Elvia
import json
import asyncio
import os
import sys

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
        start_time = sys.argv[1],
        end_time =   sys.argv[2],
        metering_point_ids = [metering_point_id],
        include_production = True
    )
    print(json.dumps(meter_values))
asyncio.run(get_meter_values())

