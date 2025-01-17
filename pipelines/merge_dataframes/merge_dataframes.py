import pandas as pd
import numpy as np
from datetime import datetime

expected_inputs = [pd.DataFrame({
    'email': ['aa','bb','cc'],
    'event_id': ['1','2','2']
}),

pd.DataFrame({
    'id': ['1', '2'],
    'title': ['aa','bb'],
    'excerpt':['aa','bb'],
    'eventbrite_sync_description':['aa','bb'],
    'eventbrite_url':['aa','bb'],
    'eventbrite_id':['aa','bb'],
    'banner':['aa','bb']
})]

expected_output = pd.DataFrame({
    'email': ['aa','bb','cc'],
    'event_id': ['1','2','2'],
    'title': ['aa','bb','bb']
})


def run(df,df2):
    """
    This function takes care of merging both datasets, events and attendies.
    """
    print('Shape of df before merge', df.shape)
    print('Shape of df2 before merge', df2.shape)

    merged_df = pd.merge(df, df2, left_on="event_id", right_on="id").drop(['id','excerpt',
                        'eventbrite_sync_description','eventbrite_url','eventbrite_id','banner'], axis=1)

    print('Shape of merged_df', merged_df.shape)

    merged_df['starting_at'] = pd.to_datetime(merged_df['starting_at'])
    merged_df = merged_df.sort_values(['email', 'starting_at'])

    # Get first events for each email
    first_events = merged_df.groupby('email').first().reset_index()


    # Count new persons registered per event
    new_persons = first_events['event_id'].value_counts().reset_index()
    new_persons.columns = ['event_id', 'New persons registered']

    # Merge new_persons column into original dataframe
    merged_df = merged_df.merge(new_persons, on='event_id', how='left')
    return merged_df