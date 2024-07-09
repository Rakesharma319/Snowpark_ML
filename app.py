# install using pip3 install snowflake-snowpark-python

from snowflake.snowpark import Session
import getpass
import pandas as pd
import json

accountname = getpass.getpass("NBWVVHD-TN65519") # ORGNAME-ACCOUNTNAME (separated by minus sign)
username = getpass.getpass("RAKESHARMA786")    # SNOWFLAKE-USERNAME
password = getpass.getpass("Rakesharma@786")    # SNOWFLAKE-PASSWORD

# connection parameter
# just account name and user/pwd
connection_param = {
    "account": accountname,
    "user": username,
    "password": password,
    "role": "ACCOUNTADMIN"
}

# print connection params
print("The Parameter :",connection_param)

# creating a session object
session = Session.builder.configs(connection_param).create()

# print values from session object to test
print("\n\t Current Account Name: ",session.get_current_account())
print("\t Current Database Name: ",session.get_current_database())
print("\t Current Schema Name: ",session.get_current_schema())
print("\t Current Role Name: ",session.get_current_role())
print("\t Current Warehouse Name: ",session.get_current_warehouse())
print("\t Fully Qualified Schema Name: ",session.get_fully_qualified_current_schema(),"\n")

print("Session Object Type:", type(session))


# closing the session
session.close()
