import xrviz
import xarray as xr
from xrviz.dashboard import Dashboard

ds = xr.open_dataset('data/great_lakes.nc')

dash = Dashboard(ds)
dash.show()