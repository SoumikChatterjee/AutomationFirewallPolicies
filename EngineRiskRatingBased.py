import pandas as pd
import numpy as np
from functools import cmp_to_key
def sortIPAddress(ip_addresses):
    sorted_ip_addresses = sorted(ip_addresses, key=lambda ip: [int(num) for num in ip.split('.')])
    return sorted_ip_addresses


def f():
 # Read the firewall logs file
    df = pd.read_csv('log.csv')


    # Group the data based on Application, Source Zone, and Destination Zone
    grouped_data = df.groupby(['Source User','Risk of app', 'Rule','Application','Category of app','Action'])


    # Create a list to store the policies
    policies = []


    # Iterate through the groups
    for (src_usr,risk,rule,app,cat_of_app,act), group in grouped_data:
        # Create a new policy
        source_ips = group['Source address'].unique()
        dest_ips = group['Destination address'].unique()
        dest_ports = group['Destination Port'].astype(str) + "-" + group['IP Protocol'].astype(str)
        dest_ports =dest_ports.unique()
        nat = group['NAT Destination Port'].astype(str) + "-" + group['IP Protocol'].astype(str)
        nat=nat.unique()
        
        nat_src_ip=group['NAT Source IP'].unique()
        nat_dest_ip=group['NAT Destination IP'].unique()
        src_zone=group['Source Zone'].unique()
        dest_zone=group['Destination Zone'].unique()
        gen_time=group['Generate Time'].unique()
        # protocol=group['IP Protocol'].unique()
        
        
        # Create a new policy as before
        policy = {
             'Policy Name': app,
             'User':src_usr,
             'Rule':rule,
            #  'Date & Time':gen_time,
             'Application': app,
             'Source Zone': src_zone,
             'Destination Zone': dest_zone,
             'Source IP': source_ips,
             'Destination IP': dest_ips,
             'Destination Port': dest_ports,
             'NAT Source IP':nat_src_ip,
             'NAT Destination IP':nat_dest_ip,
             'NAT Destination Port':nat,
             'Category of App':cat_of_app,
             'Risk Rating': risk,
             'Action': act
         }
        policies.append(policy)

        

        

    policies_df = pd.DataFrame(policies)
    policies_df['Source IP'] = policies_df['Source IP'].apply(lambda x: '\n'.join(sortIPAddress(x)))
    policies_df['Destination IP'] = policies_df['Destination IP'].apply(lambda x: '\n'.join(sortIPAddress(x)))
    policies_df['Destination Port'] = policies_df['Destination Port'].apply(lambda x: '\n'.join([str(i) for i in np.array(sorted(x)).tolist()]))

    policies_df['NAT Source IP'] = policies_df['NAT Source IP'].apply(lambda x: '\n'.join(sortIPAddress(x)))
    policies_df['NAT Destination IP'] = policies_df['NAT Destination IP'].apply(lambda x: '\n'.join(sortIPAddress(x)))
    policies_df['NAT Destination Port'] = policies_df['NAT Destination Port'].apply(lambda x: '\n'.join([str(i) for i in np.array(sorted(x)).tolist()]))

    policies_df['Source Zone']=policies_df['Source Zone'].apply(lambda x: '\n'.join([str(i) for i in np.array(x).tolist()]))
    policies_df['Destination Zone']=policies_df['Destination Zone'].apply(lambda x: '\n'.join([str(i) for i in np.array(x).tolist()]))
    # Save the policies to a new CSV file
    policies_df.to_csv('policies.csv', index=False)

f()




