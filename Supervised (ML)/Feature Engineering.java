# Cell 3: Prepare features
def prepare_features(df, target_cols=None):
    df_clean = df.copy()
    
    # Encode categorical variables
    le_device = LabelEncoder()
    le_category = LabelEncoder()
    
    df_clean['device_type_encoded'] = le_device.fit_transform(df_clean['device_type'])
    df_clean['category_encoded'] = le_category.fit_transform(df_clean['category_preference'])
    
    # Create additional features
    df_clean['purchase_frequency_score'] = df_clean['total_purchases'] / (df_clean['tenure_days'] / 30)
    df_clean['monetary_score'] = df_clean['total_purchases'] * df_clean['avg_order_value']
    df_clean['engagement_score'] = df_clean['session_count'] * df_clean['avg_session_duration_min']
    df_clean['recency_risk'] = np.where(df_clean['days_since_last_purchase'] > 60, 1, 0)
    
    # Drop original categorical and ID columns
    cols_to_drop = ['customer_id', 'device_type', 'category_preference']
    if target_cols:
        cols_to_drop.extend(target_cols)
    
    features = df_clean.drop(columns=cols_to_drop, errors='ignore')
    
    return features, df_clean

feature_cols, df_with_features = prepare_features(df, ['will_purchase_next_30d', 'sales_amount'])
print(f"✅ Features shape: {feature_cols.shape}")
print(f"\nFeatures created: {feature_cols.columns.tolist()}")
