# Cell 5: Prepare data for classification
X_class = feature_cols.drop(['sales_amount', 'will_purchase_next_30d'], axis=1, errors='ignore')
y_class = df_with_features['will_purchase_next_30d']

# Split data
X_train_c, X_test_c, y_train_c, y_test_c = train_test_split(
    X_class, y_class, test_size=0.2, random_state=42, stratify=y_class
)
X_train_c, X_val_c, y_train_c, y_val_c = train_test_split(
    X_train_c, y_train_c, test_size=0.2, random_state=42, stratify=y_train_c
)

# Scale features
scaler_class = StandardScaler()
X_train_c_scaled = scaler_class.fit_transform(X_train_c)
X_val_c_scaled = scaler_class.transform(X_val_c)
X_test_c_scaled = scaler_class.transform(X_test_c)

print(f"✅ Classification data ready")
print(f"Training: {X_train_c.shape}, Validation: {X_val_c.shape}, Test: {X_test_c.shape}")
print(f"Class distribution:\n{y_class.value_counts()}")
