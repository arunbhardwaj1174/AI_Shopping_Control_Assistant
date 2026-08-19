# AI Shopping Control Assistant - Project Design

## Overview

The AI Shopping Control Assistant is a desktop application designed to help users make informed purchasing decisions by predicting the likelihood of purchase regret based on several factors.

## Architecture

### Components

1. **GUI Layer** (`src/gui/`)
   - `main_window.py`: Main application window
   - `input_frame.py`: User input interface
   - `result_frame.py`: Prediction result display
   - `dashboard.py`: Analytics dashboard

2. **Machine Learning Layer** (`src/gui/ml/`)
   - `predictor.py`: Core prediction engine
   - `decision_rules.py`: Rule-based decision logic
   - `regret_classifier.py`: Model training utilities

3. **Data Layer** (`src/gui/database/`)
   - `db.py`: SQLite database management

4. **Utilities** (`src/gui/utils/`)
   - `data_loader.py`: Data loading functions
   - `file_handler.py`: File I/O operations
   - `validation.py`: Input validation
   - `charts.py`: Chart generation

5. **Assets** (`assets/`)
   - Theme configuration
   - Static images (logo, shopping icon)

6. **Reporting** (`reports/`)
   - `report_generator.py`: Generate prediction summaries
   - `user_report_manager.py`: Manage user-specific reports

## Data Flow

1. User enters purchase details via GUI
2. Input validation layer processes inputs
3. Prediction engine generates predictions
4. Results displayed in result frame
5. Data stored in database and CSV
6. Dashboard updated with new statistics

## Models

- **Logistic Regression**: Primary prediction model
- **Decision Tree**: Ensemble backup model
- **Decision Rules**: Rule-based scoring system

## Database Schema

```sql
CREATE TABLE purchase_history (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cost REAL NOT NULL,
    savings REAL NOT NULL,
    previous_purchase INTEGER NOT NULL,
    days_since_last_purchase INTEGER NOT NULL,
    prediction INTEGER NOT NULL,
    probability REAL NOT NULL,
    model_name TEXT NOT NULL,
    advice TEXT NOT NULL,
    created_at TEXT NOT NULL
)
```

## File Structure

```
AI_Shopping_Control_Assistant/
├── app.py                          # Entry point
├── requirements.txt                # Dependencies
├── data/
│   ├── training_data.csv           # ML training data
│   ├── shopping_history.csv        # User history
│   └── saved_predictions.csv       # Prediction history
├── models/
│   ├── model_trainer.py            # Model training script
│   ├── logistic_regression_model.pkl
│   └── decision_tree_model.pkl
├── src/
│   └── gui/
│       ├── main_window.py
│       ├── input_frame.py
│       ├── result_frame.py
│       ├── dashboard.py
│       ├── database/db.py
│       ├── ml/
│       │   ├── predictor.py
│       │   ├── regret_classifier.py
│       │   └── decision_rules.py
│       └── utils/
│           ├── data_loader.py
│           ├── file_handler.py
│           ├── validation.py
│           └── charts.py
├── assets/
│   ├── theme.py
│   ├── logo.png
│   └── shopping.png
├── reports/
│   ├── report_generator.py
│   └── user_report_manager.py
├── tests/
│   ├── test_model.py
│   ├── test_gui.py
│   └── test_database.py
└── docs/
    ├── project_design.md
    ├── flowchart.png
    └── architecture_diagram.png

## Key Features

1. **Real-time Predictions**: ML-based purchase regret prediction
2. **Purchase History**: SQLite database for tracking decisions
3. **Analytics Dashboard**: Visual representation of prediction patterns
4. **Validation**: Input validation for data integrity
5. **Reporting**: Generate prediction reports and user analytics

## Technologies

- **GUI**: customtkinter (modern Tkinter alternative)
- **ML**: scikit-learn (LogisticRegression, DecisionTreeClassifier)
- **Database**: SQLite3
- **Data Processing**: pandas, numpy
- **Visualization**: matplotlib
- **Testing**: unittest

## Setup & Execution

1. Install dependencies: `pip install -r requirements.txt`
2. Train models: `python models/model_trainer.py`
3. Run app: `python app.py`

## Future Enhancements

- Add deep learning models (TensorFlow/Keras)
- Implement cloud-based data sync
- Add mobile app version
- Integrate payment APIs
- Add product recommendation engine
- Implement user authentication
