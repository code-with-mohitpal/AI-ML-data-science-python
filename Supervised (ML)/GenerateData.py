# Cell 2: Generate synthetic customer data
np.random.seed(42)

def generate_customer_data(n_customers=5000):
    """Generate realistic customer purchase data"""
    data = pd.DataFrame({
        'customer_id': range(1, n_customers + 1),
        'tenure_days': np.random.exponential(180, n_customers).astype(int),
        'total_purchases': np.random.negative_binomial(3, 0.3, n_customers),
        'avg_order_value': np.random.gamma(2, 50, n_customers),
        'days_since_last_purchase': np.random.exponential(30, n_customers).astype(int),
        'session_count': np.random.poisson(15, n_customers),
        'avg_session_duration_min': np.random.gamma(2, 10, n_customers),
        'cart_abandonment_rate': np.random.beta(2, 5, n_customers),
        'promo_click_rate': np.random.beta(1, 4, n_customers),
        'customer_service_contacts': np.random.poisson(0.5, n_customers),
        'product_reviews_left': np.random.poisson(0.3, n_customers),
        'device_type': np.random.choice(['mobile', 'desktop', 'tablet'], n_customers, p=[0.5, 0.4, 0.1]),
        'category_preference': np.random.choice(['electronics', 'clothing', 'home', 'beauty'], n_customers)
    })
    
    # Generate target: purchase behavior
    score = (
        0.3 * (data['total_purchases'] / data['total_purchases'].max()) +
        0.2 * (data['avg_order_value'] / data['avg_order_value'].max()) -
        0.25 * (data['days_since_last_purchase'] / 100) +
        0.15 * data['promo_click_rate'] -
        0.1 * data['cart_abandonment_rate']
    )
    prob_purchase = 1 / (1 + np.exp(-score))
    data['will_purchase_next_30d'] = (np.random.random(n_customers) < prob_purchase).astype(int)
    
    # Generate sales amount
    base_sales = 50
    data['sales_amount'] = (
        base_sales +
        data['total_purchases'] * 25 +
        data['avg_order_value'] * 0.8 +
        data['session_count'] * 5 +
        np.random.normal(0, 30, n_customers)
    )
    data['sales_amount'] = data['sales_amount'].clip(0, None).astype(int)
    
    return data

df = generate_customer_data(5000)
print(f"✅ Generated {len(df)} customer records")
print(f"\nFirst 5 rows:")
df.head()
