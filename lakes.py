import xrviz
import xarray as xr
from xrviz.dashboard import Dashboard

data = xr.open_dataset('data/great_lakes.nc')

dash = Dashboard(data)
dash.show()