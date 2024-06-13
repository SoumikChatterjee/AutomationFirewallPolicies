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
    grouped_data = df.groupby(['Action','Source Zone', 'Destination Zone','Application'])


    # Create a list to store the policies
    policies = []


    # Iterate through the groups
    for (act,src_zone, dest_zone,app), group in grouped_data:
        # Create a new policy
        source_ips = group['Source address'].unique()
        dest_ips = group['Destination address'].unique()
        dest_ports = group['Destination Port'].unique()
        protocol=group['IP Protocol'].unique()

        # If there are more than one protocols, I want the protocols to be concatenated with the respective Destination Port
        if len(protocol)>1:
            updated_dest_ports = []
            
            for i in range(0,len(group['Destination Port'])):
                updated_dest_ports.append(f"{group['Destination Port'].iloc[i]}-{group['IP Protocol'].iloc[i]}")
            dest_ports = list(set(updated_dest_ports))

        
        
        # Create a new policy as before
        policy = {
             'Policy Name': f"{app} {src_zone} to {dest_zone} policy",
             'Application': app,
             'Source Zone': src_zone,
             'Destination Zone': dest_zone,
             'Source IP': source_ips,
             'Destination IP': dest_ips,
             'Destination Port': dest_ports,
             'IP Protocol': protocol,  
             'Action': act
         }
        policies.append(policy)

        

        

    policies_df = pd.DataFrame(policies)
    policies_df['Source IP'] = policies_df['Source IP'].apply(lambda x: '\n'.join(sortIPAddress(x)))
    policies_df['Destination IP'] = policies_df['Destination IP'].apply(lambda x: '\n'.join(sortIPAddress(x)))
    policies_df['IP Protocol'] = policies_df['IP Protocol'].apply(lambda x: '\n'.join(sorted(x)))
    policies_df['Destination Port'] = policies_df['Destination Port'].apply(lambda x: '\n'.join([str(i) for i in np.array(sorted(x)).tolist()]))

    # Save the policies to a new CSV file
    policies_df.to_csv('policies.csv', index=False)

f()




