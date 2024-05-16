# Correlations Between Air Quality & Several Factors
![Air Quality Image](https://github.com/heidthecamp/CU-VIRT-AI-PT-03-2024-U-LOLC-PROJECT-1/assets/161158238/b3524d86-41ee-4252-9cb2-507c0617d2cf)
_By Team Hephaestus_


## Overview
Team Hephaestus conducted a thorough analysis of various metrics to
evaluate their impacts on local air quality, with particular attention
paid to walkability and vehicle density. The hypothesis is that areas with higher pedestrian - walkability may exhibit better air quality due to reduced reliance on motorized transportation, which can contribute to emissions. On the flip side, regions with increased vehicle presence could see elevated pollution levels resulting from
exhaust emissions. The following presentation will involve statistical analysis and modeling to establish correlations between these factors and show the air quality recorded in different regions.
We are looking to see how several metrics affect air quality of an area.



## Dataset

We will be using data from [data.gov](https://data.gov/).

[FIPS to County](https://transition.fcc.gov/oet/info/maps/census/fips/fips.txt)

[Air Now.org](https://docs.airnowapi.org) 

[Air Quality Index](https://www.epa.gov/sites/default/files/2021-06/documents/national_walkability_index_methodology_and_user_guide_june2021.pdf)

[SMART LOCATION DATABASE TECHNICAL DOCUMENTATION AND USER GUIDE](https://www.epa.gov/system/files/documents/2023-10/epa_sld_3.0_technicaldocumentationuserguide_may2021_0.pdf)

[EV Charging Stations](https://developer.nrel.gov/)


## Outputs

### Charging Station Density

The following maps and charts show the charging station density and the car
registraion percentage.  
We were hoping to see how the density of charging stations might affect the
percnetage of EV registraions in an area.

_EV Charging Stations_
![EV Charging Stations](https://github.com/heidthecamp/CU-VIRT-AI-PT-03-2024-U-LOLC-PROJECT-1/assets/161158238/e3537aa2-2641-4818-953d-92dc30b39d4e)

_NYC Heat Map_
![NYC Heat map](https://github.com/heidthecamp/CU-VIRT-AI-PT-03-2024-U-LOLC-PROJECT-1/assets/161158238/98e8f0aa-335c-4968-b87d-8cffb1ffa9e0)

_Percent of vehicles registered by Borough_
![vehicles registered by Borough](https://github.com/heidthecamp/CU-VIRT-AI-PT-03-2024-U-LOLC-PROJECT-1/assets/161158238/8768278c-5204-439c-a9cb-7d11c853866e)

_Fuel Type 2022-2024_
![FuelType 2022-2024](https://github.com/heidthecamp/CU-VIRT-AI-PT-03-2024-U-LOLC-PROJECT-1/assets/161158238/02738179-6bdf-4403-9cc9-911b8b096a76)

#### Conclusion

What is evident by these maps and the vehicle registation percentages is that as
of 2022-2024 EV ownership percentage of a borough in NYC is not highly reflective.
It seems that charging density and population denisty might be more closely
corrolated. This would require further investigation.

### Vehicle Registration

_Registration by Borough_
![Registration by borough over time](https://github.com/heidthecamp/CU-VIRT-AI-PT-03-2024-U-LOLC-PROJECT-1/assets/161158238/9a4e3835-f398-475c-991b-24503849d4ba)

_Vehicle Reg & Air Quality_
![Vehicle Reg   Air Quality](https://github.com/heidthecamp/CU-VIRT-AI-PT-03-2024-U-LOLC-PROJECT-1/assets/161158238/60fd3a18-aa3f-45ed-89a6-2e064fe37251)

_Heat Map #2_
![Heatmap](https://github.com/heidthecamp/CU-VIRT-AI-PT-03-2024-U-LOLC-PROJECT-1/assets/161158238/1b35f818-6f50-4fd4-b967-2c3ded8440bd)

_Fuel Type against Particulate Matter 2.5µm_
![Fuel Type against AQI](https://github.com/heidthecamp/CU-VIRT-AI-PT-03-2024-U-LOLC-PROJECT-1/assets/161158238/b899f42f-bdfe-4842-9285-eb94eeda1926)

#### Conclusion

We can see see from the vehicle registration that it is a fairly steady rate of
increase, which indicates that there is steady growth of vehicle population over
the observed years.  
We can also see that the air quality in NYC stays fairly consistent over the
course of the observed years, other than August 2023 in which the wild fires
from Canada can be attributed.  
Lastly we can see that the air quality versus the different fuel type
registrations seems to be loosely correlated at best. It surprised us that gas
vehicle registrations had a slight negative correlation (an increase in PM2.5)
where had a slightly negative correlation (a decrease in PM2.5).  The spread of
the trends not seem to be seemed to be wide enough for us to question how well
that correlation holds.

<!-- Removing due to no longer using unemployment because year's didn't match with the rest of the data 
_Bronx Unemployment 2018-2022_
![Bronx Unemployment](https
![2018-2022](https://github.com/heidthecamp/CU-VIRT-AI-PT-03-2024-U-LOLC-PROJECT-1/assets/161158238/0a1912a6-dba3-4bf8-99ea-8a8a18bdc206)

_2018-2022 Fuel_
![2018-2022](https://github.com/heidthecamp/CU-VIRT-AI-PT-03-2024-U-LOLC-PROJECT-1/assets/161158238/3872723a-9475-44b4-b8fc-6fedf02d655e) -->

### Walkability and Transit

_Public Transit_
![Public Transit](https://github.com/heidthecamp/CU-VIRT-AI-PT-03-2024-U-LOLC-PROJECT-1/assets/161158238/26ac5ad6-936c-4722-b810-538d57aa46a3)

_Miles Traveled_
![Miles Traveled](https://github.com/heidthecamp/CU-VIRT-AI-PT-03-2024-U-LOLC-PROJECT-1/assets/161158238/588c7098-6078-4c80-9082-192a425d7873)

_Energy Used_
![Energy Used](https://github.com/heidthecamp/CU-VIRT-AI-PT-03-2024-U-LOLC-PROJECT-1/assets/161158238/00bda8f5-578a-4d08-97b5-dbc1ad90e59d)

#### Conclusion

We were not able to match walkability on air quality as we had initially planned
on since the air quality index was for the entire city and not just a single
borough. How ever we were still able to pull out some interesting trends.

## Group Members
Timothy Heidcamp 

Duane Anglin

Matilda Wang

Christian Leon

Aniel Rios

Wassam Qayyum




