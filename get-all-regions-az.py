################################################################################
#
# This Python program will list all AWS regions and availability zones
#
# 1) install Python interpreter
# 2) install aws CLI
# 3) install aws boto3 package if needed
#    pip3 install boto3
# 4) setup your aws credentials
#    aws configure
# 5) run this application
#    python get-all-az.py
#
################################################################################
import boto3

ec2 = boto3.client("ec2")

# Retrieves all regions/endpoints that work with EC2
aws_regions = ec2.describe_regions()

total_region_cnt = 0;
total_az_cnt = 0;

# Get a list of regions and then instantiate a new ec2 client for each region in
# order to get list of AZs for the region
for region in aws_regions['Regions']: 
    curr_region_name = region['RegionName']
    ec2_region = boto3.client('ec2', region_name=curr_region_name)
    curr_region = [{'Name': 'region-name', 'Values': [curr_region_name]}]
    print ("\nCurrent Region is " + curr_region_name)
    aws_azs = ec2_region.describe_availability_zones(Filters=curr_region)

    total_region_cnt += 1
    for az in aws_azs['AvailabilityZones']:
        zone = az['ZoneName']
        total_az_cnt += 1
        print(zone)

print("\nTotal number of regions = " + str(total_region_cnt))
print("Total number of AZs     = " + str(total_az_cnt))


################################################################################
# Output:
# 
# Current Region is eu-north-1
# eu-north-1a
# eu-north-1b
# eu-north-1c
# 
# Current Region is ap-south-1
# ap-south-1a
# ap-south-1b
# ap-south-1c
# 
# Current Region is eu-west-3
# eu-west-3a
# eu-west-3b
# eu-west-3c
# 
# Current Region is eu-west-2
# eu-west-2a
# eu-west-2b
# eu-west-2c
# 
# Current Region is eu-west-1
# eu-west-1a
# eu-west-1b
# eu-west-1c
# 
# Current Region is ap-northeast-2
# ap-northeast-2a
# ap-northeast-2b
# ap-northeast-2c
# 
# Current Region is ap-northeast-1
# ap-northeast-1a
# ap-northeast-1c
# ap-northeast-1d
# 
# Current Region is sa-east-1
# sa-east-1a
# sa-east-1b
# sa-east-1c
# 
# Current Region is ca-central-1
# ca-central-1a
# ca-central-1b
# ca-central-1d
# 
# Current Region is ap-southeast-1
# ap-southeast-1a
# ap-southeast-1b
# ap-southeast-1c
# 
# Current Region is ap-southeast-2
# ap-southeast-2a
# ap-southeast-2b
# ap-southeast-2c
# 
# Current Region is eu-central-1
# eu-central-1a
# eu-central-1b
# eu-central-1c
# 
# Current Region is us-east-1
# us-east-1a
# us-east-1b
# us-east-1c
# us-east-1d
# us-east-1e
# us-east-1f
# 
# Current Region is us-east-2
# us-east-2a
# us-east-2b
# us-east-2c
# 
# Current Region is us-west-1
# us-west-1a
# us-west-1c
# 
# Current Region is us-west-2
# us-west-2a
# us-west-2b
# us-west-2c
# us-west-2d
# 
# Total number of regions = 16
# Total number of AZs     = 51
# 
