#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

poi = []
salary_count = 0
email_count = 0
total_payments = 0
total_payments_poi = 0
for name in enron_data:
	if enron_data[name]['poi'] is True:
		poi.append(name)
	if enron_data[name]['email_address'] != 'NaN':
		email_count += 1
	if enron_data[name]['salary'] != 'NaN':
		salary_count += 1
	if enron_data[name]['total_payments'] != 'NaN':
		total_payments += 1
	if enron_data[name]['total_payments'] == 'NaN' and enron_data[name]['poi'] is True:
		total_payments_poi += 1





# print poi
print len(poi)
# print (enron_data["SKILLING JEFFREY K"])
# print (enron_data["PRENTICE JAMES"])
# print (enron_data["COLWELL WESLEY"])
# print (enron_data["SKILLING JEFFREY K"]["exercised_stock_options"])

# vips = ["SKILLING JEFFREY K", "LAY KENNETH L", "FASTOW ANDREW S"]
# for name in vips:
# 	print "total payments for {0}: {1}".format(name, enron_data[name]["total_payments"])

print 'email_count', email_count
print 'salary_count', salary_count
print 'total_payments', total_payments
print 'total_payments_poi', total_payments_poi

