import argparse

parser = argparse.ArgumentParser(description='Works out your HR zones based on the Uphill Athlete principles')
parser.add_argument('-age', help='Please provideyour age', action='store', dest='age', type=int, required=True)
parser.add_argument('-aet', help='Please provide your AeT HR', action='store', dest='aet', type=int, required=True )
parser.add_argument('-ant', help='Please provide your AnT/Lacatae threshold HR', action='store', type=int, dest='ant', required=True)
arg_results = parser.parse_args()


aet = arg_results.aet
ant = arg_results.ant
age = arg_results.age
max_hr = 220 - int(arg_results.age)

def number_change_pct(zone, aet, pct):
    res = round( zone - (aet * pct / 100) )
    return res

def pct_diff(n1, n2):
    pct_cge = round(((n1 - n2) / n2) * 100)
    return pct_cge

def aet_check(aet, ant):
    diff_pct = pct_diff(ant, aet )
    if diff_pct <= 10:
        print("Your ADS is below 10%, time to do more aerobic training in Zone 1")
    else:
        print("Your ADS is high, you still have much to gain from aerobic training in Zone2")

# Zone variables
zone_4_upper = max_hr
zone_4_lower = ant -1
zone_3_upper = ant
zone_3_lower = aet -1
zone_2_upper = aet
zone_2_lower = number_change_pct( zone_2_upper, aet, 10 ) -1
zone_1_upper = zone_2_lower
zone_1_lower = number_change_pct( zone_2_upper,aet, 20) -1
zone_reco = ( zone_1_lower -1 )
maf_aet = round( 180 - age)


print("According to the basic MAF forula your AeT should be:", maf_aet )
print("The AeT that you've submitted was:", aet)
print("There's", pct_diff(aet, maf_aet ),"% between the basic MAF formula and the AeT you submitted from your own test.")
print("The Lactate Threshold you submitted was:", ant)
print("There's a", pct_diff(ant,aet),"% diff from your AeT and your Ant")
aet_check(aet, ant)
print("Your HR zones are:")
print("Recovery should be below ", zone_reco )
print("Zone 1 =", zone_1_lower, zone_1_upper)
print("Zone 2 =", zone_2_lower, zone_2_upper)
print("Zone 3 =", zone_3_lower, zone_3_upper)
print("Zone 4 =", zone_4_lower, zone_4_upper)



