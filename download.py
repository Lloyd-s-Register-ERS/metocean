# To download metocean time series
# Matthew Zhang
# 07 Nov 2019


# varList = ['100m_u_component_of_wind', \
#               '100m_v_component_of_wind', \
#              '10m_u_component_of_wind', \
#               '10m_v_component_of_wind'

import cdsapi
import sys

def ERA5(year_start, year_end, varList, output):
    
    c = cdsapi.Client()

    varList = ['mean_wave_direction', \
               'mean_wave_period', \
               'peak_wave_period', \
               'significant_height_of_combined_wind_waves_and_swell']

    year_start = int(sys.argv[1])

    if len(sys.argv)>2:

        year_end = int(sys.argv[2])
                 
    for year in range(year_start,year_end+1):
        print("Getting year "+str(year))
        c.retrieve(
            'reanalysis-era5-single-levels',
            {
                'product_type':'reanalysis',
                'format':'netcdf',
                'variable':varList,
                'year':[str(year)],
                'month':[str(month).zfill(2) for month in range(1,13)],
                'day':[
                    '01','02','03',
                    '04','05','06',
                    '07','08','09',
                    '10','11','12',
                    '13','14','15',
                    '16','17','18',
                    '19','20','21',
                    '22','23','24',
                    '25','26','27',
                    '28','29','30',
                    '31'
                ],
                'time':[
                    '00:00','01:00','02:00',
                    '03:00','04:00','05:00',
                    '06:00','07:00','08:00',
                    '09:00','10:00','11:00',
                    '12:00','13:00','14:00',
                    '15:00','16:00','17:00',
                    '18:00','19:00','20:00',
                    '21:00','22:00','23:00'
                ],
                'area': "36/129/31/137"
            },
            str(year)+'_ERA5_wave_data.nc')
