"""
These module will house all functions we would be 
making use of to address the big mart dataset
"""

from sklearn.preprocessing import LabelEncoder, StandardScaler


def prepare_dataset(df):
    """
    Prepares the big martdataset for the machine learning 
    model by cleaning the dataset, performing feature 
    engineering and feature scaling.
    """
    
    # Fills the Item_Weight feature columns
    df.Item_Weight.fillna(df.Item_Weight.mean(), inplace=True)
    
    # Fills the Outlet_Size feature columns
    df.Outlet_Size.ffill(inplace=True)
    
    # Fixes the Item_Fat_Content value duplicates
    df.Item_Fat_Content.replace({
        'low fat': 'Low Fat',
        'LF': 'Low Fat',
        'reg': 'Regular'
    }, inplace=True)
    
    # Adjusting the Item_Fat_Content and Outlet_Size feature columns to numeric values
    df.Item_Fat_Content.replace({'Low Fat': 0, 'Regular': 1}, inplace=True)
    df.Outlet_Size.replace({'Small': 0, 'Medium': 1, 'High': 2}, inplace=True)

    # Setting the Grocery Store category Outlet_Type feature column to 0
    df.Outlet_Type.replace({'Grocery Store': 0}, inplace=True)
    
    # The item identifier filler
    outlet_identifier_filler = {
        v: i 
        for i, v in enumerate(sorted([
            int(val[4:]) for val in df.Outlet_Identifier.unique()
        ]))
    }
    
    # Filling the Outlet_Identifier feature column
    df.Outlet_Identifier = df.Outlet_Identifier.map(
        lambda x: outlet_identifier_filler[int(x[4:])]
    )

    # Filling the Outlet_Location_Type feature column
    df.Outlet_Location_Type = df.Outlet_Location_Type.map(
        lambda x: int(x[-1]) - 1
    )

    # Filling the Outlet_Type feature column
    df.Outlet_Type = df.Outlet_Type.map(
        lambda x: int(x[-1]) if type(x) == str else x
    )
    
    # Encoding the variables Item_Identifier, Item_Type
    df.loc[:, ['Item_Identifier', 'Item_Type']] = df[
        ['Item_Identifier', 'Item_Type']
    ].apply(LabelEncoder().fit_transform)
    
    item_mrp_scaler = StandardScaler()
    
    df.Item_MRP = item_mrp_scaler.fit_transform(
        df.Item_MRP.to_numpy().reshape(-1, 1)
    )
