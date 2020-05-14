<<<<<<< HEAD
# -*- coding: utf-8 -*-
"""
Created on Thu May  7 22:35:54 2020

@author: vrjtr
"""

import glassdoor_scraper as gs
import pandas as pd
path = "C:/Users/vrjtr/Desktop/Data Science projects/ds_salary_prediction/chromedriver"

df = gs.get_jobs("data scientist", 5, False, path, 10)

=======
# -*- coding: utf-8 -*-
"""
Created on Thu May  7 22:35:54 2020

@author: vrjtr
"""

import glassdoor_scraper as gs
import pandas as pd
path = "C:/Users/vrjtr/Desktop/Data Science projects/ds_salary_prediction/chromedriver"

df = gs.get_jobs("data scientist", 5, False, path, 10)

>>>>>>> 77953ec669e3608434b710932440509c40f11139
df.to_csv("glassdoor_jobs.csv", index = False)