###############################################
# To download metocean time series
# Matthew Zhang
# 07 Nov 2019
###############################################

import cdsapi

# variable: either 'wind' or 'wave', case insensitive, or specify a list to download
# area: example '80/-50/-25/0', # North, West, South, East. Default: global


def ERA5(year_start, year_end, variable, area):
    if variable.lower() == 'wind':
        varlist = ['100m_u_component_of_wind',
                   '100m_v_component_of_wind',
                   '10m_u_component_of_wind',
                   '10m_v_component_of_wind'
                   ]
        name = 'wind'
    elif variable.lower() == 'wave':
        varlist = ['mean_wave_direction',
                   'mean_wave_period',
                   'peak_wave_period',
                   'significant_height_of_combined_wind_waves_and_swell'
                   ]
        name = 'wave'
    elif isinstance(variable, list):
        varlist = variable
        name = ''
    else:
        raise Exception("Variable to download is not specified correctly, "
                        "either 'wind' or 'wave' or a user-defined list")

    c = cdsapi.Client()
    for year in range(year_start, year_end+1):
        print("Getting year "+str(year))
        c.retrieve(
            'reanalysis-era5-single-levels',
            {
                'product_type': 'reanalysis',
                'format': 'netcdf',
                'variable': varlist,
                'year': [str(year)],
                'month': [str(month).zfill(2) for month in range(1, 13)],
                'day': ['01', '02', '03', '04', '05', '06', '07', '08', '09',
                        '10', '11', '12', '13', '14', '15', '16', '17', '18',
                        '19', '20', '21', '22', '23', '24', '25', '26', '27',
                        '28', '29', '30', '31'
                        ],
                'time': ['00:00', '01:00', '02:00', '03:00', '04:00', '05:00',
                         '06:00', '07:00', '08:00', '09:00', '10:00', '11:00',
                         '12:00', '13:00', '14:00', '15:00', '16:00', '17:00',
                         '18:00', '19:00', '20:00', '21:00', '22:00', '23:00'
                         ],
                'area': area
            },
            str(year)+'_ERA5'+name+'.nc')
