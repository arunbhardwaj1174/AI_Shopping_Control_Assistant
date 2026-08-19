# AI Shopping Control Assistant

This project is a Python desktop application that predicts whether a planned purchase may cause regret. The app uses a simple machine learning model, a local SQLite database, and a custom GUI built with `customtkinter`.

## Project Structure

- `app.py` - main entry point for the application
- `requirements.txt` - Python dependencies
- `data/` - CSV datasets and saved prediction history
- `models/` - trained model artifacts and trainer script
- `src/` - application source code
  - `gui/` - GUI screens, frames, and database helper
  - `ml/` - prediction logic and decision rules
  - `utils/` - helper modules for validation, charting, and file handling
- `assets/` - UI theme settings and static assets

## Setup in VS Code

1. Open the `AI_Shopping_Control_Assistant` folder in VS Code.
2. Create and activate a virtual environment:
   - PowerShell:
     ```powershell
     python -m venv .venv
     .venv\Scripts\Activate.ps1
     ```
   - Command Prompt:
     ```cmd
     python -m venv .venv
     .venv\Scripts\activate.bat
     ```
3. Install dependencies:
   ```powershell
   pip install -r requirements.txt
   ```
4. Train the models once:
   ```powershell
   python models/model_trainer.py
   ```
5. Run the application:
   ```powershell
   python app.py
   ```

## Notes

- The app saves recent purchase predictions to a local SQLite database at `src/gui/database/purchase_history.db`.
- Predictions are also appended to `data/saved_predictions.csv`.
- If the model files are missing, the app automatically trains logistic regression and decision tree models from `data/training_data.csv`.

## Optional

- Use the VS Code Run view to launch `app.py`.
- If the GUI appears too small, resize the window, or adjust the layout in `src/gui/main_window.py`.
