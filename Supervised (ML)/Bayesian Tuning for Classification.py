# Cell 6: Bayesian Optimization for XGBoost Classifier
import optuna

def objective_xgb_clf(trial, X_train, y_train, X_val, y_val):
    params = {
        'n_estimators': trial.suggest_int('n_estimators', 100, 500),
        'max_depth': trial.suggest_int('max_depth', 3, 10),
        'learning_rate': trial.suggest_float('learning_rate', 0.01, 0.3, log=True),
        'subsample': trial.suggest_float('subsample', 0.6, 1.0),
        'colsample_bytree': trial.suggest_float('colsample_bytree', 0.6, 1.0),
        'reg_alpha': trial.suggest_float('reg_alpha', 1e-5, 10, log=True),
        'reg_lambda': trial.suggest_float('reg_lambda', 1e-5, 10, log=True),
        'random_state': 42
    }
    
    model = XGBClassifier(**params, eval_metric='logloss', use_label_encoder=False)
    model.fit(X_train, y_train, eval_set=[(X_val, y_val)], early_stopping_rounds=20, verbose=False)
    y_pred = model.predict(X_val)
    return f1_score(y_val, y_pred, average='weighted')

# Run optimization (reduce trials for faster execution)
study_clf = optuna.create_study(direction='maximize', sampler=optuna.samplers.TPESampler(seed=42))
study_clf.optimize(lambda trial: objective_xgb_clf(trial, X_train_c_scaled, y_train_c, 
                                                    X_val_c_scaled, y_val_c), 
                   n_trials=20, show_progress_bar=True)

print(f"\n✅ Best parameters: {study_clf.best_params}")
print(f"Best F1 score: {study_clf.best_value:.4f}")
