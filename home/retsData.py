import csv

csvfile = 'static/listingData/listings.csv'

with open(csvfile) as f:
	reader = csv.reader(f, skipinitialspace=True)
	header = next(reader)
	listings = [dict(zip(header, map(str, row))) for row in reader]
	for key in listings[0].items():
		print(key)
	# for listing in listings:
	# 	# for key, value in listing.items():
	# 	# 	print(key, value)





# # fieldnames = ("Area","Association Features Available", "Association Fee 1", "Association Fee 1 MQYN",
# # 	"Association Fee Includes","Association Name","Association Phone","Baths Full","Baths Half","Baths Total",
# # 	"Bedrooms Total Possible Num","Beds Total","Building Description","Close Price","Construction Description",
# # 	"Community Name","Current Price","Directions","Dryer Included","Dryer Utilities","Financing Considered",
# # 	"Flooring Description","Garage Description","House Faces","Last List Price","List Agent MUI","List Agent Full Name",
# # 	"List Office Name","List Office Phone","List Price","Matrix Unique ID","Matrix Modified DT","MLS Number","MLS","MLS Photo Count",
# # 	"Postal Code","Property Condition","Property Sub Type","Public Address","Public Remarks","Selling Agent MUI",
# # 	"Selling Agent Full Name","Selling Agent Direct Work Phone","Street Name","Street Number","Subdivision Name","Sq Ft Total")
