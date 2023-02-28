## extracing MRMS grib2 files
## 1. see what data are there
## 2. extract that data
## 3. crop to CPF and ETF
## 4. conver to csv

import xarray as xr
ds = xr.open_dataset('E:/MRMS_test/RadarOnly_QPE_01H_00.00_20210601-000000.grib2', engine='cfgrib')

