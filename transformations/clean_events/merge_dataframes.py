import pandas as pd
import numpy as np
from datetime import datetime

def run(df3):
    """
    This function takes care of merging both datasets, events and attendies.
    """


    df3 = pd.merge(df, df2, left_on="event_id", right_on="id").drop(['id','excerpt',
                    'eventbrite_sync_description','eventbrite_url','eventbrite_id','banner'], axis=1)