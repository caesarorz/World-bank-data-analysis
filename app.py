from generate.api import URL, FetchFilterAPI
from generate.df import GenerateDataFrame

male_employeer_ind = 'SL.EMP.MPYR.MA.ZS'
female_employeer_ind = 'SL.EMP.MPYR.FE.ZS'
total_employeer_ind = 'SL.EMP.MPYR.ZS'
exports_high_income_ind = 'TX.VAL.MRCH.HI.ZS'
imports_high_income_ind = 'TM.VAL.MRCH.HI.ZS'
exports_east_asia_pacific_ind = 'TX.VAL.MRCH.R1.ZS'
imports_east_asia_pacific_ind = 'TM.VAL.MRCH.R1.ZS'
exports_eu_centralasia_ind = 'TX.VAL.MRCH.R2.ZS'
imports_eu_centralasia_ind  = 'TM.VAL.MRCH.R2.ZS'
imports_latin_caribe_ind  = 'TM.VAL.MRCH.R3.ZS'
exports_latin_caribe_ind  = 'TX.VAL.MRCH.R3.ZS'
exports_south_asia_ind  = 'TX.VAL.MRCH.R5.ZS'
imports_south_asia_ind  = 'TM.VAL.MRCH.R5.ZS'


def genDf(*args, **kwags):
    list_ind = []
    for indicator in args:
        s1 = URL()
        s1.setIndicator(indicator)
        s1.setCountry('cr')
        s1.setUrl()

        g1 = FetchFilterAPI()
        g1.setURL(s1.getURLIndicatorByCountry())
        g1.fetchAPI()
        g1.setIndicatorName()
        info = g1.generateInfo()

        df1 = GenerateDataFrame()
        df1.set_df_one_indicator(info)
        list_ind.append(df1.get_df_one_indicator())

    return list_ind


print(genDf(male_employeer_ind, female_employeer_ind))

