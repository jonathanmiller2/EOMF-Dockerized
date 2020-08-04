get_modis_raw_data:
Sending tasks to queue:
Monitoring tasks
Progress: 0 Finished: 0 Errors: 0 Retry: 0 Started 0 Pending 36 
Progress: 0 Finished: 0 Errors: 0 Retry: 0 Started 0 Pending 36 
Progress: 16 Finished: 6 Errors: 0 Retry: 0 Started 0 Pending 30 
Progress: 100 Finished: 36 Errors: 0 Retry: 0 Started 0 Pending 0 
Processing data
iam in PROCESS DATA ******************
data:
dataset:
mod09a1
[93m*********************i entered gap fill code***********************[0m
MOD09A1
data confirmed as mod09a1
[94m******************this is relation_dict *********[0m
[('ndvi', 'gf_ndvi'), ('evi', 'gf_evi'), ('lswi', 'gf_lswi'), ('lswi2105', 'gf_lswi2105'), ('ndsi', 'gf_ndsi'), ('ndwi1200', 'gf_ndwi1200')]
 -------------*************i am in gap fill algorithm: *************------------------
bad_obs:***
[]
year:	2009->
	day:	1->
		this day is a bad observation
	day:	105->
		 this observation is good
		1. as length of bad observations is:	1[0m
[1m			There is no initial value[0m
[4m				 i cannot fill previous because there is no initial value for  for these bad obs[0m
		year:  2009day:  105value: good_observation[0m
		setting/changing initial good obs to: year:  2009day:  105value: good_observation[0m
	day:	113->
		 this observation is good
		1. as length of bad observations is:	0[0m
[94m[93m			 part where the max obs > 4 i should leave them ****[0m
		year:  2009day:  113value: good_observation[0m
		setting/changing initial good obs to: year:  2009day:  113value: good_observation[0m
	day:	121->
		this day is a bad observation
	day:	129->
		 this observation is good
		1. as length of bad observations is:	1[0m
[1m			2. as length of bad observations is:	1[0m
[92m				 Doing gap fill for	year:	2009	day:	121[0m
[95m~~~~~~~~~~~~~~~~~~~~~Filling GAP fill values USING set_gf method~~~~~~~~~~~~~~~~~~~~~~~[0m
[93mstart:	num_bad_obs:1	pos:1	gf_key:gf_applied	gf_value:	Yes[0m
**working/producing gap fills**
******************************************************************************************************************
[91m		ini:  -0.275862068966	end:  -3.0	result:  -1.63793103448	key:  ndvi	value:  gf_ndvi[0m
		 iam in the EVI exempt part
		result:  None	gf_key:  NA
[91m		ini:  -1.30882352941	end:  -0.769230769231	result:  -1.03902714932	key:  lswi	value:  gf_lswi[0m
[91m		ini:  -3.21052631579	end:  -0.8	result:  -2.00526315789	key:  lswi2105	value:  gf_lswi2105[0m
[91m		ini:  -0.794285714286	end:  0.333333333333	result:  -0.230476190477	key:  ndsi	value:  gf_ndsi[0m
[91m		ini:  -0.5	end:  -1.10714285714	result:  -0.80357142857	key:  ndwi1200	value:  gf_ndwi1200[0m
******************************************************************************************************************
		year:  2009day:  129value: good_observation[0m
		setting/changing initial good obs to: year:  2009day:  129value: good_observation[0m
	day:	137->
		this day is a bad observation
	day:	145->
		this day is a bad observation
	day:	153->
		 this observation is good
		1. as length of bad observations is:	2[0m
[1m			2. as length of bad observations is:	2[0m
[92m				 Doing gap fill for	year:	2009	day:	137[0m
[95m~~~~~~~~~~~~~~~~~~~~~Filling GAP fill values USING set_gf method~~~~~~~~~~~~~~~~~~~~~~~[0m
[93mstart:	num_bad_obs:2	pos:1	gf_key:gf_applied	gf_value:	Yes[0m
**working/producing gap fills**
******************************************************************************************************************
[91m		ini:  -3.0	end:  -1.05714285714	result:  -2.35238095238	key:  ndvi	value:  gf_ndvi[0m
		 iam in the EVI exempt part
		result:  None	gf_key:  NA
[91m		ini:  -0.769230769231	end:  -0.99416909621	result:  -0.844210211557	key:  lswi	value:  gf_lswi[0m
[91m		ini:  -0.8	end:  -0.993788819876	result:  -0.864596273292	key:  lswi2105	value:  gf_lswi2105[0m
[91m		ini:  0.333333333333	end:  -0.879120879121	result:  -0.0708180708183	key:  ndsi	value:  gf_ndsi[0m
[91m		ini:  -1.10714285714	end:  -1.04	result:  -1.08476190476	key:  ndwi1200	value:  gf_ndwi1200[0m
******************************************************************************************************************
[92m				 Doing gap fill for	year:	2009	day:	145[0m
[95m~~~~~~~~~~~~~~~~~~~~~Filling GAP fill values USING set_gf method~~~~~~~~~~~~~~~~~~~~~~~[0m
[93mstart:	num_bad_obs:2	pos:2	gf_key:gf_applied	gf_value:	Yes[0m
**working/producing gap fills**
******************************************************************************************************************
[91m		ini:  -3.0	end:  -1.05714285714	result:  -1.70476190476	key:  ndvi	value:  gf_ndvi[0m
		 iam in the EVI exempt part
		result:  None	gf_key:  NA
[91m		ini:  -0.769230769231	end:  -0.99416909621	result:  -0.919189653884	key:  lswi	value:  gf_lswi[0m
[91m		ini:  -0.8	end:  -0.993788819876	result:  -0.929192546584	key:  lswi2105	value:  gf_lswi2105[0m
[91m		ini:  0.333333333333	end:  -0.879120879121	result:  -0.47496947497	key:  ndsi	value:  gf_ndsi[0m
[91m		ini:  -1.10714285714	end:  -1.04	result:  -1.06238095238	key:  ndwi1200	value:  gf_ndwi1200[0m
******************************************************************************************************************
		year:  2009day:  153value: good_observation[0m
		setting/changing initial good obs to: year:  2009day:  153value: good_observation[0m
	day:	161->
		 this observation is good
		1. as length of bad observations is:	0[0m
[94m[93m			 part where the max obs > 4 i should leave them ****[0m
		year:  2009day:  161value: good_observation[0m
		setting/changing initial good obs to: year:  2009day:  161value: good_observation[0m
	day:	169->
		this day is a bad observation
	day:	17->
		 this observation is good
		1. as length of bad observations is:	1[0m
[1m			2. as length of bad observations is:	1[0m
[92m				 Doing gap fill for	year:	2009	day:	169[0m
[95m~~~~~~~~~~~~~~~~~~~~~Filling GAP fill values USING set_gf method~~~~~~~~~~~~~~~~~~~~~~~[0m
[93mstart:	num_bad_obs:1	pos:1	gf_key:gf_applied	gf_value:	Yes[0m
**working/producing gap fills**
******************************************************************************************************************
[91m		ini:  0.0191082802548	end:  -0.0299003322259	result:  -0.00539602598555	key:  ndvi	value:  gf_ndvi[0m
		 iam in the EVI exempt part
		result:  None	gf_key:  NA
[91m		ini:  2.63636363636	end:  -0.00567536889898	result:  1.31534413373	key:  lswi	value:  gf_lswi[0m
[91m		ini:  2.07692307692	end:  0.0774907749077	result:  1.07720692591	key:  lswi2105	value:  gf_lswi2105[0m
[91m		ini:  -0.756097560976	end:  0.0722513089005	result:  -0.341923126038	key:  ndsi	value:  gf_ndsi[0m
[91m		ini:  -0.111111111111	end:  0.0	result:  -0.0555555555555	key:  ndwi1200	value:  gf_ndwi1200[0m
******************************************************************************************************************
		year:  2009day:  17value: good_observation[0m
		setting/changing initial good obs to: year:  2009day:  17value: good_observation[0m
	day:	177->
		 this observation is good
		1. as length of bad observations is:	0[0m
[94m[93m			 part where the max obs > 4 i should leave them ****[0m
		year:  2009day:  177value: good_observation[0m
		setting/changing initial good obs to: year:  2009day:  177value: good_observation[0m
	day:	185->
		this day is a bad observation
	day:	193->
		this day is a bad observation
	day:	201->
		this day is a bad observation
	day:	209->
		 this observation is good
		1. as length of bad observations is:	3[0m
[1m			2. as length of bad observations is:	3[0m
[92m				 Doing gap fill for	year:	2009	day:	185[0m
[95m~~~~~~~~~~~~~~~~~~~~~Filling GAP fill values USING set_gf method~~~~~~~~~~~~~~~~~~~~~~~[0m
[93mstart:	num_bad_obs:3	pos:1	gf_key:gf_applied	gf_value:	Yes[0m
**working/producing gap fills**
******************************************************************************************************************
[91m		ini:  -0.00104058272633	end:  0.0843373493976	result:  0.0203039003047	key:  ndvi	value:  gf_ndvi[0m
		 iam in the EVI exempt part
		result:  None	gf_key:  NA
[91m		ini:  -0.00723888314374	end:  -46.0	result:  -11.5054291624	key:  lswi	value:  gf_lswi[0m
[91m		ini:  0.15523465704	end:  -46.0	result:  -11.3835740072	key:  lswi2105	value:  gf_lswi2105[0m
[91m		ini:  0.0356435643564	end:  -0.132530120482	result:  -0.0063998568532	key:  ndsi	value:  gf_ndsi[0m
[91m		ini:  0.144219308701	end:  -0.379310344828	result:  0.0133368953187	key:  ndwi1200	value:  gf_ndwi1200[0m
******************************************************************************************************************
[92m				 Doing gap fill for	year:	2009	day:	193[0m
[95m~~~~~~~~~~~~~~~~~~~~~Filling GAP fill values USING set_gf method~~~~~~~~~~~~~~~~~~~~~~~[0m
[93mstart:	num_bad_obs:3	pos:2	gf_key:gf_applied	gf_value:	Yes[0m
**working/producing gap fills**
******************************************************************************************************************
[91m		ini:  -0.00104058272633	end:  0.0843373493976	result:  0.0416483833356	key:  ndvi	value:  gf_ndvi[0m
		 iam in the EVI exempt part
		result:  0.0237623762376	gf_key:  NA
[91m		ini:  -0.00723888314374	end:  -46.0	result:  -23.0036194416	key:  lswi	value:  gf_lswi[0m
[91m		ini:  0.15523465704	end:  -46.0	result:  -22.9223826715	key:  lswi2105	value:  gf_lswi2105[0m
[91m		ini:  0.0356435643564	end:  -0.132530120482	result:  -0.0484432780628	key:  ndsi	value:  gf_ndsi[0m
[91m		ini:  0.144219308701	end:  -0.379310344828	result:  -0.117545518064	key:  ndwi1200	value:  gf_ndwi1200[0m
******************************************************************************************************************
[92m				 Doing gap fill for	year:	2009	day:	201[0m
[95m~~~~~~~~~~~~~~~~~~~~~Filling GAP fill values USING set_gf method~~~~~~~~~~~~~~~~~~~~~~~[0m
[93mstart:	num_bad_obs:3	pos:3	gf_key:gf_applied	gf_value:	Yes[0m
**working/producing gap fills**
******************************************************************************************************************
[91m		ini:  -0.00104058272633	end:  0.0843373493976	result:  0.0629928663666	key:  ndvi	value:  gf_ndvi[0m
		 iam in the EVI exempt part
		result:  -0.0106132751994	gf_key:  NA
[91m		ini:  -0.00723888314374	end:  -46.0	result:  -34.5018097208	key:  lswi	value:  gf_lswi[0m
[91m		ini:  0.15523465704	end:  -46.0	result:  -34.4611913357	key:  lswi2105	value:  gf_lswi2105[0m
[91m		ini:  0.0356435643564	end:  -0.132530120482	result:  -0.0904866992724	key:  ndsi	value:  gf_ndsi[0m
[91m		ini:  0.144219308701	end:  -0.379310344828	result:  -0.248427931446	key:  ndwi1200	value:  gf_ndwi1200[0m
******************************************************************************************************************
		year:  2009day:  209value: good_observation[0m
		setting/changing initial good obs to: year:  2009day:  209value: good_observation[0m
	day:	217->
		this day is a bad observation
	day:	225->
		this day is a bad observation
	day:	233->
		this day is a bad observation
	day:	241->
		this day is a bad observation
	day:	249->
		this day is a bad observation
	day:	25->
		this day is a bad observation
	day:	257->
		this day is a bad observation
	day:	265->
		this day is a bad observation
	day:	273->
		this day is a bad observation
	day:	281->
		this day is a bad observation
	day:	289->
		this day is a bad observation
	day:	297->
		this day is a bad observation
	day:	305->
		this day is a bad observation
	day:	313->
		this day is a bad observation
	day:	321->
		this day is a bad observation
	day:	329->
		this day is a bad observation
	day:	33->
		 this observation is good
		1. as length of bad observations is:	16[0m
[94m[93m			 part where the max obs > 4 i should leave them ****[0m
values left : gf i set to NA:	year:	2009	day:	217
values left : gf i set to NA:	year:	2009	day:	225
values left : gf i set to NA:	year:	2009	day:	233
values left : gf i set to NA:	year:	2009	day:	241
values left : gf i set to NA:	year:	2009	day:	249
values left : gf i set to NA:	year:	2009	day:	25
values left : gf i set to NA:	year:	2009	day:	257
values left : gf i set to NA:	year:	2009	day:	265
values left : gf i set to NA:	year:	2009	day:	273
values left : gf i set to NA:	year:	2009	day:	281
values left : gf i set to NA:	year:	2009	day:	289
values left : gf i set to NA:	year:	2009	day:	297
values left : gf i set to NA:	year:	2009	day:	305
values left : gf i set to NA:	year:	2009	day:	313
values left : gf i set to NA:	year:	2009	day:	321
values left : gf i set to NA:	year:	2009	day:	329
		year:  2009day:  33value: good_observation[0m
		setting/changing initial good obs to: year:  2009day:  33value: good_observation[0m
	day:	337->
		 this observation is good
		1. as length of bad observations is:	0[0m
[94m[93m			 part where the max obs > 4 i should leave them ****[0m
		year:  2009day:  337value: good_observation[0m
		setting/changing initial good obs to: year:  2009day:  337value: good_observation[0m
	day:	345->
		 this observation is good
		1. as length of bad observations is:	0[0m
[94m[93m			 part where the max obs > 4 i should leave them ****[0m
		year:  2009day:  345value: good_observation[0m
		setting/changing initial good obs to: year:  2009day:  345value: good_observation[0m
	day:	353->
		this day is a bad observation
	day:	361->
		this day is a bad observation
	day:	41->
		 this observation is good
		1. as length of bad observations is:	2[0m
[1m			2. as length of bad observations is:	2[0m
[92m				 Doing gap fill for	year:	2009	day:	353[0m
[95m~~~~~~~~~~~~~~~~~~~~~Filling GAP fill values USING set_gf method~~~~~~~~~~~~~~~~~~~~~~~[0m
[93mstart:	num_bad_obs:2	pos:1	gf_key:gf_applied	gf_value:	Yes[0m
**working/producing gap fills**
******************************************************************************************************************
[91m		ini:  -0.5	end:  -0.0212765957447	result:  -0.340425531915	key:  ndvi	value:  gf_ndvi[0m
		 iam in the EVI exempt part
		result:  0.00094679038061	gf_key:  NA
[91m		ini:  -1.16541353383	end:  -1.30463576159	result:  -1.21182094308	key:  lswi	value:  gf_lswi[0m
[91m		ini:  -1.23913043478	end:  -1.68656716418	result:  -1.38827601125	key:  lswi2105	value:  gf_lswi2105[0m
[91m		ini:  -0.93288590604	end:  -0.560538116592	result:  -0.808769976224	key:  ndsi	value:  gf_ndsi[0m
[91m		ini:  0.466666666667	end:  -0.626016260163	result:  0.10243902439	key:  ndwi1200	value:  gf_ndwi1200[0m
******************************************************************************************************************
[92m				 Doing gap fill for	year:	2009	day:	361[0m
[95m~~~~~~~~~~~~~~~~~~~~~Filling GAP fill values USING set_gf method~~~~~~~~~~~~~~~~~~~~~~~[0m
[93mstart:	num_bad_obs:2	pos:2	gf_key:gf_applied	gf_value:	Yes[0m
**working/producing gap fills**
******************************************************************************************************************
[91m		ini:  -0.5	end:  -0.0212765957447	result:  -0.18085106383	key:  ndvi	value:  gf_ndvi[0m
		 iam in the EVI exempt part
		result:  0.00506072874494	gf_key:  NA
[91m		ini:  -1.16541353383	end:  -1.30463576159	result:  -1.25822835234	key:  lswi	value:  gf_lswi[0m
[91m		ini:  -1.23913043478	end:  -1.68656716418	result:  -1.53742158771	key:  lswi2105	value:  gf_lswi2105[0m
[91m		ini:  -0.93288590604	end:  -0.560538116592	result:  -0.684654046408	key:  ndsi	value:  gf_ndsi[0m
[91m		ini:  0.466666666667	end:  -0.626016260163	result:  -0.261788617886	key:  ndwi1200	value:  gf_ndwi1200[0m
******************************************************************************************************************
		year:  2009day:  41value: good_observation[0m
		setting/changing initial good obs to: year:  2009day:  41value: good_observation[0m
	day:	49->
		this day is a bad observation
	day:	57->
		this day is a bad observation
	day:	65->
		this day is a bad observation
	day:	73->
		data in this is none
	day:	81->
		 this observation is good
		1. as length of bad observations is:	0[0m
[1m			There is no initial value[0m
		year:  2009day:  81value: good_observation[0m
		setting/changing initial good obs to: year:  2009day:  81value: good_observation[0m
	day:	89->
		this day is a bad observation
	day:	9->
		this day is a bad observation
	day:	97->
		 this observation is good
		1. as length of bad observations is:	2[0m
[1m			2. as length of bad observations is:	2[0m
[92m				 Doing gap fill for	year:	2009	day:	89[0m
[95m~~~~~~~~~~~~~~~~~~~~~Filling GAP fill values USING set_gf method~~~~~~~~~~~~~~~~~~~~~~~[0m
[93mstart:	num_bad_obs:2	pos:1	gf_key:gf_applied	gf_value:	Yes[0m
**working/producing gap fills**
******************************************************************************************************************
[91m		ini:  0.470588235294	end:  0.75	result:  0.563725490196	key:  ndvi	value:  gf_ndvi[0m
		 iam in the EVI exempt part
		result:  -0.00595632031767	gf_key:  NA
[91m		ini:  -2.0	end:  -1.19444444444	result:  -1.73148148148	key:  lswi	value:  gf_lswi[0m
[91m		ini:  -26.0	end:  -1.21538461538	result:  -17.7384615385	key:  lswi2105	value:  gf_lswi2105[0m
[91m		ini:  -0.048951048951	end:  -0.0533333333333	result:  -0.0504118104118	key:  ndsi	value:  gf_ndsi[0m
[91m		ini:  -0.6	end:  -0.86	result:  -0.686666666667	key:  ndwi1200	value:  gf_ndwi1200[0m
******************************************************************************************************************
[92m				 Doing gap fill for	year:	2009	day:	9[0m
[95m~~~~~~~~~~~~~~~~~~~~~Filling GAP fill values USING set_gf method~~~~~~~~~~~~~~~~~~~~~~~[0m
[93mstart:	num_bad_obs:2	pos:2	gf_key:gf_applied	gf_value:	Yes[0m
**working/producing gap fills**
******************************************************************************************************************
[91m		ini:  0.470588235294	end:  0.75	result:  0.656862745098	key:  ndvi	value:  gf_ndvi[0m
		 iam in the EVI exempt part
		result:  -0.0344027831465	gf_key:  NA
[91m		ini:  -2.0	end:  -1.19444444444	result:  -1.46296296296	key:  lswi	value:  gf_lswi[0m
[91m		ini:  -26.0	end:  -1.21538461538	result:  -9.47692307692	key:  lswi2105	value:  gf_lswi2105[0m
[91m		ini:  -0.048951048951	end:  -0.0533333333333	result:  -0.0518725718725	key:  ndsi	value:  gf_ndsi[0m
[91m		ini:  -0.6	end:  -0.86	result:  -0.773333333333	key:  ndwi1200	value:  gf_ndwi1200[0m
******************************************************************************************************************
		year:  2009day:  97value: good_observation[0m
		setting/changing initial good obs to: year:  2009day:  97value: good_observation[0m
year:	2010->
	day:	1->
		this day is a bad observation
	day:	105->
		this day is a bad observation
	day:	113->
		 this observation is good
		1. as length of bad observations is:	2[0m
[1m			2. as length of bad observations is:	2[0m
[92m				 Doing gap fill for	year:	2010	day:	1[0m
[95m~~~~~~~~~~~~~~~~~~~~~Filling GAP fill values USING set_gf method~~~~~~~~~~~~~~~~~~~~~~~[0m
[93mstart:	num_bad_obs:2	pos:1	gf_key:gf_applied	gf_value:	Yes[0m
**working/producing gap fills**
******************************************************************************************************************
[91m		ini:  0.75	end:  -1.75	result:  -0.0833333333333	key:  ndvi	value:  gf_ndvi[0m
		 iam in the EVI exempt part
		result:  -0.0262231482147	gf_key:  NA
[91m		ini:  -1.19444444444	end:  -0.895652173913	result:  -1.09484702093	key:  lswi	value:  gf_lswi[0m
[91m		ini:  -1.21538461538	end:  -0.885167464115	result:  -1.10531223163	key:  lswi2105	value:  gf_lswi2105[0m
[91m		ini:  -0.0533333333333	end:  -0.981818181818	result:  -0.362828282828	key:  ndsi	value:  gf_ndsi[0m
[91m		ini:  -0.86	end:  -0.0769230769231	result:  -0.598974358974	key:  ndwi1200	value:  gf_ndwi1200[0m
******************************************************************************************************************
[92m				 Doing gap fill for	year:	2010	day:	105[0m
[95m~~~~~~~~~~~~~~~~~~~~~Filling GAP fill values USING set_gf method~~~~~~~~~~~~~~~~~~~~~~~[0m
[93mstart:	num_bad_obs:2	pos:2	gf_key:gf_applied	gf_value:	Yes[0m
**working/producing gap fills**
******************************************************************************************************************
[91m		ini:  0.75	end:  -1.75	result:  -0.916666666667	key:  ndvi	value:  gf_ndvi[0m
		 iam in the EVI exempt part
		result:  -0.00028990549081	gf_key:  NA
[91m		ini:  -1.19444444444	end:  -0.895652173913	result:  -0.995249597422	key:  lswi	value:  gf_lswi[0m
[91m		ini:  -1.21538461538	end:  -0.885167464115	result:  -0.99523984787	key:  lswi2105	value:  gf_lswi2105[0m
[91m		ini:  -0.0533333333333	end:  -0.981818181818	result:  -0.672323232323	key:  ndsi	value:  gf_ndsi[0m
[91m		ini:  -0.86	end:  -0.0769230769231	result:  -0.337948717949	key:  ndwi1200	value:  gf_ndwi1200[0m
******************************************************************************************************************
		year:  2010day:  113value: good_observation[0m
		setting/changing initial good obs to: year:  2010day:  113value: good_observation[0m
	day:	121->
		 this observation is good
		1. as length of bad observations is:	0[0m
[94m[93m			 part where the max obs > 4 i should leave them ****[0m
		year:  2010day:  121value: good_observation[0m
		setting/changing initial good obs to: year:  2010day:  121value: good_observation[0m
	day:	129->
		this day is a bad observation
	day:	137->
		this day is a bad observation
	day:	145->
		this day is a bad observation
	day:	153->
		this day is a bad observation
	day:	161->
		data in this is none
	day:	169->
		this day is a bad observation
	day:	17->
		 this observation is good
		1. as length of bad observations is:	1[0m
[1m			There is no initial value[0m
[4m				 i cannot fill previous because there is no initial value for  for these bad obs[0m
		year:  2010day:  17value: good_observation[0m
		setting/changing initial good obs to: year:  2010day:  17value: good_observation[0m
	day:	177->
		this day is a bad observation
	day:	185->
		 this observation is good
		1. as length of bad observations is:	1[0m
[1m			2. as length of bad observations is:	1[0m
[92m				 Doing gap fill for	year:	2010	day:	177[0m
[95m~~~~~~~~~~~~~~~~~~~~~Filling GAP fill values USING set_gf method~~~~~~~~~~~~~~~~~~~~~~~[0m
[93mstart:	num_bad_obs:1	pos:1	gf_key:gf_applied	gf_value:	Yes[0m
**working/producing gap fills**
******************************************************************************************************************
[91m		ini:  -1.03921568627	end:  0.029702970297	result:  -0.504756357986	key:  ndvi	value:  gf_ndvi[0m
		 iam in the EVI exempt part
		result:  None	gf_key:  NA
[91m		ini:  -1.04651162791	end:  -2.33333333333	result:  -1.68992248062	key:  lswi	value:  gf_lswi[0m
[91m		ini:  -0.999930247968	end:  -2.18181818182	result:  -1.59087421489	key:  lswi2105	value:  gf_lswi2105[0m
[91m		ini:  0.640816326531	end:  -0.733333333333	result:  -0.046258503401	key:  ndsi	value:  gf_ndsi[0m
[91m		ini:  -0.970149253731	end:  -0.262411347518	result:  -0.616280300625	key:  ndwi1200	value:  gf_ndwi1200[0m
******************************************************************************************************************
		year:  2010day:  185value: good_observation[0m
		setting/changing initial good obs to: year:  2010day:  185value: good_observation[0m
	day:	193->
		this day is a bad observation
	day:	201->
		this day is a bad observation
	day:	209->
		this day is a bad observation
	day:	217->
		this day is a bad observation
	day:	225->
		this day is a bad observation
	day:	233->
		 this observation is good
		1. as length of bad observations is:	5[0m
[94m[93m			 part where the max obs > 4 i should leave them ****[0m
values left : gf i set to NA:	year:	2010	day:	193
values left : gf i set to NA:	year:	2010	day:	201
values left : gf i set to NA:	year:	2010	day:	209
values left : gf i set to NA:	year:	2010	day:	217
values left : gf i set to NA:	year:	2010	day:	225
		year:  2010day:  233value: good_observation[0m
		setting/changing initial good obs to: year:  2010day:  233value: good_observation[0m
	day:	241->
		this day is a bad observation
	day:	249->
		this day is a bad observation
	day:	25->
		this day is a bad observation
	day:	257->
		this day is a bad observation
	day:	265->
		this day is a bad observation
	day:	273->
		this day is a bad observation
	day:	281->
		this day is a bad observation
	day:	289->
		 this observation is good
		1. as length of bad observations is:	7[0m
[94m[93m			 part where the max obs > 4 i should leave them ****[0m
values left : gf i set to NA:	year:	2010	day:	241
values left : gf i set to NA:	year:	2010	day:	249
values left : gf i set to NA:	year:	2010	day:	25
values left : gf i set to NA:	year:	2010	day:	257
values left : gf i set to NA:	year:	2010	day:	265
values left : gf i set to NA:	year:	2010	day:	273
values left : gf i set to NA:	year:	2010	day:	281
		year:  2010day:  289value: good_observation[0m
		setting/changing initial good obs to: year:  2010day:  289value: good_observation[0m
	day:	297->
		this day is a bad observation
	day:	305->
		this day is a bad observation
	day:	313->
		this day is a bad observation
	day:	321->
		this day is a bad observation
	day:	329->
		this day is a bad observation
	day:	33->
		this day is a bad observation
	day:	337->
		this day is a bad observation
	day:	345->
		this day is a bad observation
	day:	353->
		 this observation is good
		1. as length of bad observations is:	8[0m
[94m[93m			 part where the max obs > 4 i should leave them ****[0m
values left : gf i set to NA:	year:	2010	day:	297
values left : gf i set to NA:	year:	2010	day:	305
values left : gf i set to NA:	year:	2010	day:	313
values left : gf i set to NA:	year:	2010	day:	321
values left : gf i set to NA:	year:	2010	day:	329
values left : gf i set to NA:	year:	2010	day:	33
values left : gf i set to NA:	year:	2010	day:	337
values left : gf i set to NA:	year:	2010	day:	345
		year:  2010day:  353value: good_observation[0m
		setting/changing initial good obs to: year:  2010day:  353value: good_observation[0m
	day:	361->
		this day is a bad observation
	day:	41->
		 this observation is good
		1. as length of bad observations is:	1[0m
[1m			2. as length of bad observations is:	1[0m
[92m				 Doing gap fill for	year:	2010	day:	361[0m
[95m~~~~~~~~~~~~~~~~~~~~~Filling GAP fill values USING set_gf method~~~~~~~~~~~~~~~~~~~~~~~[0m
[93mstart:	num_bad_obs:1	pos:1	gf_key:gf_applied	gf_value:	Yes[0m
**working/producing gap fills**
******************************************************************************************************************
[91m		ini:  -1.63157894737	end:  15.0	result:  6.68421052631	key:  ndvi	value:  gf_ndvi[0m
		 iam in the EVI exempt part
		result:  None	gf_key:  NA
[91m		ini:  -1.07407407407	end:  -1.29090909091	result:  -1.18249158249	key:  lswi	value:  gf_lswi[0m
[91m		ini:  -1.18181818182	end:  -1.32	result:  -1.25090909091	key:  lswi2105	value:  gf_lswi2105[0m
[91m		ini:  0.00296735905045	end:  0.16	result:  0.0814836795252	key:  ndsi	value:  gf_ndsi[0m
[91m		ini:  -1.11650485437	end:  -0.783783783784	result:  -0.950144319077	key:  ndwi1200	value:  gf_ndwi1200[0m
******************************************************************************************************************
		year:  2010day:  41value: good_observation[0m
		setting/changing initial good obs to: year:  2010day:  41value: good_observation[0m
	day:	49->
		 this observation is good
		1. as length of bad observations is:	0[0m
[94m[93m			 part where the max obs > 4 i should leave them ****[0m
		year:  2010day:  49value: good_observation[0m
		setting/changing initial good obs to: year:  2010day:  49value: good_observation[0m
	day:	57->
		this day is a bad observation
	day:	65->
		 this observation is good
		1. as length of bad observations is:	1[0m
[1m			2. as length of bad observations is:	1[0m
[92m				 Doing gap fill for	year:	2010	day:	57[0m
[95m~~~~~~~~~~~~~~~~~~~~~Filling GAP fill values USING set_gf method~~~~~~~~~~~~~~~~~~~~~~~[0m
[93mstart:	num_bad_obs:1	pos:1	gf_key:gf_applied	gf_value:	Yes[0m
**working/producing gap fills**
******************************************************************************************************************
[91m		ini:  -0.00560747663551	end:  -0.0143396226415	result:  -0.00997354963851	key:  ndvi	value:  gf_ndvi[0m
[91m		ini:  -0.00170116246102	end:  -0.00565981531129	result:  -0.00368048888616	key:  evi	value:  gf_evi[0m
[91m		ini:  0.00188323917137	end:  0.0227094753328	result:  0.0122963572521	key:  lswi	value:  gf_lswi[0m
[91m		ini:  0.0924024640657	end:  0.0883333333333	result:  0.0903678986995	key:  lswi2105	value:  gf_lswi2105[0m
[91m		ini:  0.0535714285714	end:  0.0776053215078	result:  0.0655883750396	key:  ndsi	value:  gf_ndsi[0m
[91m		ini:  0.0802030456853	end:  0.0600649350649	result:  0.0701339903751	key:  ndwi1200	value:  gf_ndwi1200[0m
******************************************************************************************************************
		year:  2010day:  65value: good_observation[0m
		setting/changing initial good obs to: year:  2010day:  65value: good_observation[0m
	day:	73->
		 this observation is good
		1. as length of bad observations is:	0[0m
[94m[93m			 part where the max obs > 4 i should leave them ****[0m
		year:  2010day:  73value: good_observation[0m
		setting/changing initial good obs to: year:  2010day:  73value: good_observation[0m
	day:	81->
		 this observation is good
		1. as length of bad observations is:	0[0m
[94m[93m			 part where the max obs > 4 i should leave them ****[0m
		year:  2010day:  81value: good_observation[0m
		setting/changing initial good obs to: year:  2010day:  81value: good_observation[0m
	day:	89->
		this day is a bad observation
	day:	9->
		this day is a bad observation
	day:	97->
		 this observation is good
		1. as length of bad observations is:	2[0m
[1m			2. as length of bad observations is:	2[0m
[92m				 Doing gap fill for	year:	2010	day:	89[0m
[95m~~~~~~~~~~~~~~~~~~~~~Filling GAP fill values USING set_gf method~~~~~~~~~~~~~~~~~~~~~~~[0m
[93mstart:	num_bad_obs:2	pos:1	gf_key:gf_applied	gf_value:	Yes[0m
**working/producing gap fills**
******************************************************************************************************************
[91m		ini:  -0.75	end:  -5.8	result:  -2.43333333333	key:  ndvi	value:  gf_ndvi[0m
		 iam in the EVI exempt part
		result:  -0.000553709856035	gf_key:  NA
[91m		ini:  -1.12765957447	end:  -0.351351351351	result:  -0.868890166764	key:  lswi	value:  gf_lswi[0m
[91m		ini:  -0.9997907585	end:  -1.00083740405	result:  -1.00013964035	key:  lswi2105	value:  gf_lswi2105[0m
[91m		ini:  -0.234567901235	end:  -1.5	result:  -0.656378600823	key:  ndsi	value:  gf_ndsi[0m
[91m		ini:  -0.9997907585	end:  -1.00083740405	result:  -1.00013964035	key:  ndwi1200	value:  gf_ndwi1200[0m
******************************************************************************************************************
[92m				 Doing gap fill for	year:	2010	day:	9[0m
[95m~~~~~~~~~~~~~~~~~~~~~Filling GAP fill values USING set_gf method~~~~~~~~~~~~~~~~~~~~~~~[0m
[93mstart:	num_bad_obs:2	pos:2	gf_key:gf_applied	gf_value:	Yes[0m
**working/producing gap fills**
******************************************************************************************************************
[91m		ini:  -0.75	end:  -5.8	result:  -4.11666666667	key:  ndvi	value:  gf_ndvi[0m
		 iam in the EVI exempt part
		result:  0.0159404888417	gf_key:  NA
[91m		ini:  -1.12765957447	end:  -0.351351351351	result:  -0.610120759057	key:  lswi	value:  gf_lswi[0m
[91m		ini:  -0.9997907585	end:  -1.00083740405	result:  -1.0004885222	key:  lswi2105	value:  gf_lswi2105[0m
[91m		ini:  -0.234567901235	end:  -1.5	result:  -1.07818930041	key:  ndsi	value:  gf_ndsi[0m
[91m		ini:  -0.9997907585	end:  -1.00083740405	result:  -1.0004885222	key:  ndwi1200	value:  gf_ndwi1200[0m
******************************************************************************************************************
		year:  2010day:  97value: good_observation[0m
		setting/changing initial good obs to: year:  2010day:  97value: good_observation[0m
year:	2011->
	day:	1->
		this day is a bad observation
	day:	105->
		 this observation is good
		1. as length of bad observations is:	1[0m
[1m			2. as length of bad observations is:	1[0m
[92m				 Doing gap fill for	year:	2011	day:	1[0m
[95m~~~~~~~~~~~~~~~~~~~~~Filling GAP fill values USING set_gf method~~~~~~~~~~~~~~~~~~~~~~~[0m
[93mstart:	num_bad_obs:1	pos:1	gf_key:gf_applied	gf_value:	Yes[0m
**working/producing gap fills**
******************************************************************************************************************
[91m		ini:  -5.8	end:  0.269230769231	result:  -2.76538461538	key:  ndvi	value:  gf_ndvi[0m
		 iam in the EVI exempt part
		result:  None	gf_key:  NA
[91m		ini:  -0.351351351351	end:  -2.34693877551	result:  -1.34914506343	key:  lswi	value:  gf_lswi[0m
[91m		ini:  -1.00083740405	end:  -2.22222222222	result:  -1.61152981314	key:  lswi2105	value:  gf_lswi2105[0m
[91m		ini:  -1.5	end:  -0.131034482759	result:  -0.815517241379	key:  ndsi	value:  gf_ndsi[0m
[91m		ini:  -1.00083740405	end:  0.0153846153846	result:  -0.492726394333	key:  ndwi1200	value:  gf_ndwi1200[0m
******************************************************************************************************************
		year:  2011day:  105value: good_observation[0m
		setting/changing initial good obs to: year:  2011day:  105value: good_observation[0m
	day:	113->
		this day is a bad observation
	day:	121->
		 this observation is good
		1. as length of bad observations is:	1[0m
[1m			2. as length of bad observations is:	1[0m
[92m				 Doing gap fill for	year:	2011	day:	113[0m
[95m~~~~~~~~~~~~~~~~~~~~~Filling GAP fill values USING set_gf method~~~~~~~~~~~~~~~~~~~~~~~[0m
[93mstart:	num_bad_obs:1	pos:1	gf_key:gf_applied	gf_value:	Yes[0m
**working/producing gap fills**
******************************************************************************************************************
[91m		ini:  0.269230769231	end:  0.129032258065	result:  0.199131513648	key:  ndvi	value:  gf_ndvi[0m
		 iam in the EVI exempt part
		result:  None	gf_key:  NA
[91m		ini:  -2.34693877551	end:  -3.12121212121	result:  -2.73407544836	key:  lswi	value:  gf_lswi[0m
[91m		ini:  -2.22222222222	end:  -4.04347826087	result:  -3.13285024154	key:  lswi2105	value:  gf_lswi2105[0m
[91m		ini:  -0.131034482759	end:  -0.0461538461538	result:  -0.0885941644564	key:  ndsi	value:  gf_ndsi[0m
[91m		ini:  0.0153846153846	end:  -0.270833333333	result:  -0.127724358974	key:  ndwi1200	value:  gf_ndwi1200[0m
******************************************************************************************************************
		year:  2011day:  121value: good_observation[0m
		setting/changing initial good obs to: year:  2011day:  121value: good_observation[0m
	day:	129->
		this day is a bad observation
	day:	137->
		this day is a bad observation
	day:	145->
		this day is a bad observation
	day:	153->
		this day is a bad observation
	day:	161->
		this day is a bad observation
	day:	169->
		this day is a bad observation
	day:	17->
		 this observation is good
		1. as length of bad observations is:	6[0m
[94m[93m			 part where the max obs > 4 i should leave them ****[0m
values left : gf i set to NA:	year:	2011	day:	129
values left : gf i set to NA:	year:	2011	day:	137
values left : gf i set to NA:	year:	2011	day:	145
values left : gf i set to NA:	year:	2011	day:	153
values left : gf i set to NA:	year:	2011	day:	161
values left : gf i set to NA:	year:	2011	day:	169
		year:  2011day:  17value: good_observation[0m
		setting/changing initial good obs to: year:  2011day:  17value: good_observation[0m
	day:	177->
		this day is a bad observation
	day:	185->
		 this observation is good
		1. as length of bad observations is:	1[0m
[1m			2. as length of bad observations is:	1[0m
[92m				 Doing gap fill for	year:	2011	day:	177[0m
[95m~~~~~~~~~~~~~~~~~~~~~Filling GAP fill values USING set_gf method~~~~~~~~~~~~~~~~~~~~~~~[0m
[93mstart:	num_bad_obs:1	pos:1	gf_key:gf_applied	gf_value:	Yes[0m
**working/producing gap fills**
******************************************************************************************************************
[91m		ini:  -1.375	end:  -0.0869565217391	result:  -0.73097826087	key:  ndvi	value:  gf_ndvi[0m
		 iam in the EVI exempt part
		result:  None	gf_key:  NA
[91m		ini:  -0.969230769231	end:  -1.15441176471	result:  -1.06182126697	key:  lswi	value:  gf_lswi[0m
[91m		ini:  -0.962848297214	end:  -1.20638820639	result:  -1.0846182518	key:  lswi2105	value:  gf_lswi2105[0m
[91m		ini:  -0.741496598639	end:  -0.736296296296	result:  -0.738896447467	key:  ndsi	value:  gf_ndsi[0m
[91m		ini:  -0.944444444444	end:  0.787234042553	result:  -0.0786052009455	key:  ndwi1200	value:  gf_ndwi1200[0m
******************************************************************************************************************
		year:  2011day:  185value: good_observation[0m
		setting/changing initial good obs to: year:  2011day:  185value: good_observation[0m
	day:	193->
		this day is a bad observation
	day:	201->
		 this observation is good
		1. as length of bad observations is:	1[0m
[1m			2. as length of bad observations is:	1[0m
[92m				 Doing gap fill for	year:	2011	day:	193[0m
[95m~~~~~~~~~~~~~~~~~~~~~Filling GAP fill values USING set_gf method~~~~~~~~~~~~~~~~~~~~~~~[0m
[93mstart:	num_bad_obs:1	pos:1	gf_key:gf_applied	gf_value:	Yes[0m
**working/producing gap fills**
******************************************************************************************************************
[91m		ini:  -0.0869565217391	end:  -1.04	result:  -0.56347826087	key:  ndvi	value:  gf_ndvi[0m
		 iam in the EVI exempt part
		result:  0.0120727382479	gf_key:  NA
[91m		ini:  -1.15441176471	end:  -1.016	result:  -1.08520588235	key:  lswi	value:  gf_lswi[0m
[91m		ini:  -1.20638820639	end:  -1.01290322581	result:  -1.1096457161	key:  lswi2105	value:  gf_lswi2105[0m
[91m		ini:  -0.736296296296	end:  0.16	result:  -0.288148148148	key:  ndsi	value:  gf_ndsi[0m
[91m		ini:  0.787234042553	end:  -0.939393939394	result:  -0.0760799484205	key:  ndwi1200	value:  gf_ndwi1200[0m
******************************************************************************************************************
		year:  2011day:  201value: good_observation[0m
		setting/changing initial good obs to: year:  2011day:  201value: good_observation[0m
	day:	209->
		this day is a bad observation
	day:	217->
		 this observation is good
		1. as length of bad observations is:	1[0m
[1m			2. as length of bad observations is:	1[0m
[92m				 Doing gap fill for	year:	2011	day:	209[0m
[95m~~~~~~~~~~~~~~~~~~~~~Filling GAP fill values USING set_gf method~~~~~~~~~~~~~~~~~~~~~~~[0m
[93mstart:	num_bad_obs:1	pos:1	gf_key:gf_applied	gf_value:	Yes[0m
**working/producing gap fills**
******************************************************************************************************************
[91m		ini:  -1.04	end:  -0.5	result:  -0.77	key:  ndvi	value:  gf_ndvi[0m
		 iam in the EVI exempt part
		result:  -0.00404647667495	gf_key:  NA
[91m		ini:  -1.016	end:  -1.07079646018	result:  -1.04339823009	key:  lswi	value:  gf_lswi[0m
[91m		ini:  -1.01290322581	end:  -1.22222222222	result:  -1.11756272401	key:  lswi2105	value:  gf_lswi2105[0m
[91m		ini:  0.16	end:  -0.509677419355	result:  -0.174838709678	key:  ndsi	value:  gf_ndsi[0m
[91m		ini:  -0.939393939394	end:  -0.910112359551	result:  -0.924753149472	key:  ndwi1200	value:  gf_ndwi1200[0m
******************************************************************************************************************
		year:  2011day:  217value: good_observation[0m
		setting/changing initial good obs to: year:  2011day:  217value: good_observation[0m
	day:	225->
		this day is a bad observation
	day:	233->
		this day is a bad observation
	day:	241->
		this day is a bad observation
	day:	249->
		this day is a bad observation
	day:	25->
		this day is a bad observation
	day:	257->
		this day is a bad observation
	day:	265->
		this day is a bad observation
	day:	273->
		this day is a bad observation
	day:	281->
		 this observation is good
		1. as length of bad observations is:	8[0m
[94m[93m			 part where the max obs > 4 i should leave them ****[0m
values left : gf i set to NA:	year:	2011	day:	225
values left : gf i set to NA:	year:	2011	day:	233
values left : gf i set to NA:	year:	2011	day:	241
values left : gf i set to NA:	year:	2011	day:	249
values left : gf i set to NA:	year:	2011	day:	25
values left : gf i set to NA:	year:	2011	day:	257
values left : gf i set to NA:	year:	2011	day:	265
values left : gf i set to NA:	year:	2011	day:	273
		year:  2011day:  281value: good_observation[0m
		setting/changing initial good obs to: year:  2011day:  281value: good_observation[0m
	day:	289->
		this day is a bad observation
	day:	297->
		this day is a bad observation
	day:	305->
		this day is a bad observation
	day:	313->
		 this observation is good
		1. as length of bad observations is:	3[0m
[1m			2. as length of bad observations is:	3[0m
[92m				 Doing gap fill for	year:	2011	day:	289[0m
[95m~~~~~~~~~~~~~~~~~~~~~Filling GAP fill values USING set_gf method~~~~~~~~~~~~~~~~~~~~~~~[0m
[93mstart:	num_bad_obs:3	pos:1	gf_key:gf_applied	gf_value:	Yes[0m
**working/producing gap fills**
******************************************************************************************************************
[91m		ini:  -1.93333333333	end:  -1.76923076923	result:  -1.8923076923	key:  ndvi	value:  gf_ndvi[0m
		 iam in the EVI exempt part
		result:  0.0154734887559	gf_key:  NA
[91m		ini:  -1.17073170732	end:  -3.0	result:  -1.62804878049	key:  lswi	value:  gf_lswi[0m
[91m		ini:  -1.19444444444	end:  -1.3125	result:  -1.22395833333	key:  lswi2105	value:  gf_lswi2105[0m
[91m		ini:  0.127450980392	end:  0.814814814815	result:  0.299291938998	key:  ndsi	value:  gf_ndsi[0m
[91m		ini:  -1.18918918919	end:  -0.411764705882	result:  -0.994833068363	key:  ndwi1200	value:  gf_ndwi1200[0m
******************************************************************************************************************
[92m				 Doing gap fill for	year:	2011	day:	297[0m
[95m~~~~~~~~~~~~~~~~~~~~~Filling GAP fill values USING set_gf method~~~~~~~~~~~~~~~~~~~~~~~[0m
[93mstart:	num_bad_obs:3	pos:2	gf_key:gf_applied	gf_value:	Yes[0m
**working/producing gap fills**
******************************************************************************************************************
[91m		ini:  -1.93333333333	end:  -1.76923076923	result:  -1.85128205128	key:  ndvi	value:  gf_ndvi[0m
		 iam in the EVI exempt part
		result:  -0.0138652549316	gf_key:  NA
[91m		ini:  -1.17073170732	end:  -3.0	result:  -2.08536585366	key:  lswi	value:  gf_lswi[0m
[91m		ini:  -1.19444444444	end:  -1.3125	result:  -1.25347222222	key:  lswi2105	value:  gf_lswi2105[0m
[91m		ini:  0.127450980392	end:  0.814814814815	result:  0.471132897603	key:  ndsi	value:  gf_ndsi[0m
[91m		ini:  -1.18918918919	end:  -0.411764705882	result:  -0.800476947536	key:  ndwi1200	value:  gf_ndwi1200[0m
******************************************************************************************************************
[92m				 Doing gap fill for	year:	2011	day:	305[0m
[95m~~~~~~~~~~~~~~~~~~~~~Filling GAP fill values USING set_gf method~~~~~~~~~~~~~~~~~~~~~~~[0m
[93mstart:	num_bad_obs:3	pos:3	gf_key:gf_applied	gf_value:	Yes[0m
**working/producing gap fills**
******************************************************************************************************************
[91m		ini:  -1.93333333333	end:  -1.76923076923	result:  -1.81025641026	key:  ndvi	value:  gf_ndvi[0m
		 iam in the EVI exempt part
		result:  -0.00683332384261	gf_key:  NA
[91m		ini:  -1.17073170732	end:  -3.0	result:  -2.54268292683	key:  lswi	value:  gf_lswi[0m
[91m		ini:  -1.19444444444	end:  -1.3125	result:  -1.28298611111	key:  lswi2105	value:  gf_lswi2105[0m
[91m		ini:  0.127450980392	end:  0.814814814815	result:  0.642973856209	key:  ndsi	value:  gf_ndsi[0m
[91m		ini:  -1.18918918919	end:  -0.411764705882	result:  -0.606120826709	key:  ndwi1200	value:  gf_ndwi1200[0m
******************************************************************************************************************
		year:  2011day:  313value: good_observation[0m
		setting/changing initial good obs to: year:  2011day:  313value: good_observation[0m
	day:	321->
		this day is a bad observation
	day:	329->
		this day is a bad observation
	day:	33->
		 this observation is good
		1. as length of bad observations is:	2[0m
[1m			2. as length of bad observations is:	2[0m
[92m				 Doing gap fill for	year:	2011	day:	321[0m
[95m~~~~~~~~~~~~~~~~~~~~~Filling GAP fill values USING set_gf method~~~~~~~~~~~~~~~~~~~~~~~[0m
[93mstart:	num_bad_obs:2	pos:1	gf_key:gf_applied	gf_value:	Yes[0m
**working/producing gap fills**
******************************************************************************************************************
[91m		ini:  -1.76923076923	end:  2.5	result:  -0.346153846153	key:  ndvi	value:  gf_ndvi[0m
		 iam in the EVI exempt part
		result:  0.00364675135234	gf_key:  NA
[91m		ini:  -3.0	end:  -1.13249211356	result:  -2.37749737119	key:  lswi	value:  gf_lswi[0m
[91m		ini:  -1.3125	end:  -1.21538461538	result:  -1.28012820513	key:  lswi2105	value:  gf_lswi2105[0m
[91m		ini:  0.814814814815	end:  -0.307543520309	result:  0.440695369774	key:  ndsi	value:  gf_ndsi[0m
[91m		ini:  -0.411764705882	end:  -0.0869565217391	result:  -0.303495311168	key:  ndwi1200	value:  gf_ndwi1200[0m
******************************************************************************************************************
[92m				 Doing gap fill for	year:	2011	day:	329[0m
[95m~~~~~~~~~~~~~~~~~~~~~Filling GAP fill values USING set_gf method~~~~~~~~~~~~~~~~~~~~~~~[0m
[93mstart:	num_bad_obs:2	pos:2	gf_key:gf_applied	gf_value:	Yes[0m
**working/producing gap fills**
******************************************************************************************************************
[91m		ini:  -1.76923076923	end:  2.5	result:  1.07692307692	key:  ndvi	value:  gf_ndvi[0m
		 iam in the EVI exempt part
		result:  None	gf_key:  NA
[91m		ini:  -3.0	end:  -1.13249211356	result:  -1.75499474237	key:  lswi	value:  gf_lswi[0m
[91m		ini:  -1.3125	end:  -1.21538461538	result:  -1.24775641025	key:  lswi2105	value:  gf_lswi2105[0m
[91m		ini:  0.814814814815	end:  -0.307543520309	result:  0.0665759247323	key:  ndsi	value:  gf_ndsi[0m
[91m		ini:  -0.411764705882	end:  -0.0869565217391	result:  -0.195225916453	key:  ndwi1200	value:  gf_ndwi1200[0m
******************************************************************************************************************
		year:  2011day:  33value: good_observation[0m
		setting/changing initial good obs to: year:  2011day:  33value: good_observation[0m
	day:	337->
		 this observation is good
		1. as length of bad observations is:	0[0m
[94m[93m			 part where the max obs > 4 i should leave them ****[0m
		year:  2011day:  337value: good_observation[0m
		setting/changing initial good obs to: year:  2011day:  337value: good_observation[0m
	day:	345->
		this day is a bad observation
	day:	353->
		this day is a bad observation
	day:	361->
		 this observation is good
		1. as length of bad observations is:	2[0m
[1m			2. as length of bad observations is:	2[0m
[92m				 Doing gap fill for	year:	2011	day:	345[0m
[95m~~~~~~~~~~~~~~~~~~~~~Filling GAP fill values USING set_gf method~~~~~~~~~~~~~~~~~~~~~~~[0m
[93mstart:	num_bad_obs:2	pos:1	gf_key:gf_applied	gf_value:	Yes[0m
**working/producing gap fills**
******************************************************************************************************************
[91m		ini:  -0.391304347826	end:  7.0	result:  2.07246376812	key:  ndvi	value:  gf_ndvi[0m
		 iam in the EVI exempt part
		result:  0.00507260161055	gf_key:  NA
[91m		ini:  -0.75	end:  -1.57142857143	result:  -1.02380952381	key:  lswi	value:  gf_lswi[0m
[91m		ini:  0.12	end:  0.411764705882	result:  0.217254901961	key:  lswi2105	value:  gf_lswi2105[0m
[91m		ini:  0.0710900473934	end:  0.490566037736	result:  0.210915377508	key:  ndsi	value:  gf_ndsi[0m
[91m		ini:  -0.65	end:  -7.0	result:  -2.76666666667	key:  ndwi1200	value:  gf_ndwi1200[0m
******************************************************************************************************************
[92m				 Doing gap fill for	year:	2011	day:	353[0m
[95m~~~~~~~~~~~~~~~~~~~~~Filling GAP fill values USING set_gf method~~~~~~~~~~~~~~~~~~~~~~~[0m
[93mstart:	num_bad_obs:2	pos:2	gf_key:gf_applied	gf_value:	Yes[0m
**working/producing gap fills**
******************************************************************************************************************
[91m		ini:  -0.391304347826	end:  7.0	result:  4.53623188406	key:  ndvi	value:  gf_ndvi[0m
		 iam in the EVI exempt part
		result:  -0.0288811238679	gf_key:  NA
[91m		ini:  -0.75	end:  -1.57142857143	result:  -1.29761904762	key:  lswi	value:  gf_lswi[0m
[91m		ini:  0.12	end:  0.411764705882	result:  0.314509803921	key:  lswi2105	value:  gf_lswi2105[0m
[91m		ini:  0.0710900473934	end:  0.490566037736	result:  0.350740707622	key:  ndsi	value:  gf_ndsi[0m
[91m		ini:  -0.65	end:  -7.0	result:  -4.88333333333	key:  ndwi1200	value:  gf_ndwi1200[0m
******************************************************************************************************************
		year:  2011day:  361value: good_observation[0m
		setting/changing initial good obs to: year:  2011day:  361value: good_observation[0m
	day:	41->
		this day is a bad observation
	day:	49->
		this day is a bad observation
	day:	57->
		this day is a bad observation
	day:	65->
		this day is a bad observation
	day:	73->
		this day is a bad observation
	day:	81->
		this day is a bad observation
	day:	89->
		this day is a bad observation
	day:	9->
		this day is a bad observation
	day:	97->
		 this observation is good
		1. as length of bad observations is:	8[0m
[94m[93m			 part where the max obs > 4 i should leave them ****[0m
values left : gf i set to NA:	year:	2011	day:	41
values left : gf i set to NA:	year:	2011	day:	49
values left : gf i set to NA:	year:	2011	day:	57
values left : gf i set to NA:	year:	2011	day:	65
values left : gf i set to NA:	year:	2011	day:	73
values left : gf i set to NA:	year:	2011	day:	81
values left : gf i set to NA:	year:	2011	day:	89
values left : gf i set to NA:	year:	2011	day:	9
		year:  2011day:  97value: good_observation[0m
		setting/changing initial good obs to: year:  2011day:  97value: good_observation[0m
saving data
i entered main and returning just none:
{'metadata': {'lon': 109.688242, 'dataset': 'mod09a1', 'tile': u'h28v08', 'lat': 0.820435, 'years': [2009, 2010, 2011], 'col': 1161, 'row': 1101}, 'filename': 'mod09a1_lat_0.820435_lon_109.688242_years_2009,2010,2011.csv'}
