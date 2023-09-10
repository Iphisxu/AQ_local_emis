
progdir = 'D:/data/Project_Anqing/'
datadir = progdir + 'Local_emis_2021/create_emis/'

# local emis
emisdir   = datadir + 'step0_original/'
emisfile1  = emisdir + 'AQ_2021_standard.xlsx'
emisfile2  = emisdir + 'AQ_2021_inventory.xlsx'
# emispoint = emisdir + 'point_source.xlsx'
# emisarea  = emisdir + 'area_source.xlsx'

# sector mapping file
secmap = datadir + 'SectorMapping.xlsx'

# local emis netcdf
emis_nc_dir = datadir + 'step1_preliminary/meic_category/sum/'
local_ind_file = emis_nc_dir + 'Industry.nc'
local_pow_file = emis_nc_dir + 'Power.nc'
local_tra_file = emis_nc_dir + 'Transportation.nc'
local_res_file = emis_nc_dir + 'Residential.nc'
local_agr_file = emis_nc_dir + 'Agriculture.nc'

# meic emis
meicdir = datadir + 'MEIC_AQ/'
meic_ind_file = meicdir + 'emis.CN3AH_135X138.ind.ncf'
meic_pow_file = meicdir + 'emis.CN3AH_135X138.pow.ncf'
meic_res_file = meicdir + 'emis.CN3AH_135X138.res.ncf'
meic_tra_file = meicdir + 'emis.CN3AH_135X138.tra.ncf'
meic_agr_file = meicdir + 'emis.CN3AH_135X138.agr.ncf'
meic_shp_file = meicdir + 'emis.CN3AH_135X138.shp.ncf'

# allocated emis
allocated_dir = datadir + 'step2_allocated/'
lex_ind_file = allocated_dir + 'ind.nc'
lex_pow_file = allocated_dir + 'pow.nc'
lex_tra_file = allocated_dir + 'tra.nc'
lex_res_file = allocated_dir + 'res.nc'
lex_agr_file = allocated_dir + 'agr.nc'

# =============================================================

# for TEST_SIM
timestart = '2023-06-11T00'
timeend   = '2023-06-16T23'

mcip_file   = progdir + 'TEST_SIM/AQ_test_mcip.nc'
meic_ncfile = progdir + 'TEST_SIM/AQ_test_meic.nc'
lex_ncfile  = progdir + 'TEST_SIM/AQ_test_lex.nc'

# shapefile
shphz   = progdir + 'shapefile/杭州市/杭州市.shp'
shpAQ = progdir + 'shapefile/萧山区/萧山区.shp'
shpmap   = progdir + 'shapefile/杭州市各区/杭州市各区.shp'