# Cell 4: Find optimal clusters
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

# Select features for segmentation
seg_features = ['total_purchases', 'avg_order_value', 'days_since_last_purchase', 
                'session_count', 'cart_abandonment_rate', 'promo_click_rate']
X_seg = feature_cols[seg_features]

# Scale features
scaler_seg = StandardScaler()
X_seg_scaled = scaler_seg.fit_transform(X_seg)

# Find optimal k
inertias = []
silhouette_scores = []
K_range = range(2, 9)

for k in K_range:
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    kmeans.fit(X_seg_scaled)
    inertias.append(kmeans.inertia_)
    silhouette_scores.append(silhouette_score(X_seg_scaled, kmeans.labels_))

# Plot
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))
ax1.plot(K_range, inertias, 'bo-')
ax1.set_xlabel('Number of clusters (k)')
ax1.set_ylabel('Inertia')
ax1.set_title('Elbow Method')
ax1.grid(True)

ax2.plot(K_range, silhouette_scores, 'ro-')
ax2.set_xlabel('Number of clusters (k)')
ax2.set_ylabel('Silhouette Score')
ax2.set_title('Silhouette Method')
ax2.grid(True)

plt.tight_layout()
plt.show()

optimal_k = K_range[np.argmax(silhouette_scores)]
print(f"\n✅ Optimal number of clusters: {optimal_k}")
print(f"Best silhouette score: {max(silhouette_scores):.3f}")

# Fit final K-Means
kmeans_final = KMeans(n_clusters=optimal_k, random_state=42, n_init=10)
clusters = kmeans_final.fit_predict(X_seg_scaled)
feature_cols['Segment'] = clusters

# Analyze segments
segment_stats = df.groupby(clusters).agg({
    'total_purchases': 'mean',
    'avg_order_value': 'mean',
    'days_since_last_purchase': 'mean',
    'sales_amount': 'mean',
    'will_purchase_next_30d': 'mean'
}).round(2)

segment_stats['size'] = df.groupby(clusters).size()
segment_stats['percentage'] = (segment_stats['size'] / len(df) * 100).round(1)

print("\n📊 Segment Profiles:")
print(segment_stats)
