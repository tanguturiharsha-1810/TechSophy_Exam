# Personal Finance Analyzer

A Python-based tool for analyzing, visualizing, and generating insights from messy personal finance transaction data. The project includes anomaly detection, clustering, recommendations, and optional AI-powered insights using Google Gemini.

## Features
- **Data Ingestion & Cleaning:** Handles messy CSVs, missing values, and inconsistent categories.
- **Visualization:** Plots spending by category and monthly trends using Matplotlib and Seaborn.
- **Analysis:**
  - Anomaly detection with Isolation Forest
  - Spending clustering with KMeans
- **Recommendations:** Actionable tips based on your spending patterns.
- **AI Insights (Optional):** Uses Google Gemini API for advanced, AI-generated financial suggestions.

## Project Structure
```
├── Analysis.py           # Anomaly detection & clustering
├── Visualize.py          # Visualization functions
├── ingestion.py          # Data loading & cleaning
├── recommendation.py     # Rule-based recommendations
├── gemini_analysis.py    # Gemini AI integration
├── Main.py               # Main script to run everything
├── data/
│   └── messy_transactions_1200.csv  # Sample data
```

## Requirements
- Python 3.8+
- pandas
- numpy
- scikit-learn
- matplotlib
- seaborn
- python-dotenv (for .env support)
- google-generativeai (for Gemini AI, optional)

Install dependencies:
```bash
pip install pandas numpy scikit-learn matplotlib seaborn python-dotenv google-generativeai
```

## Usage
1. **Prepare your data:** Place your CSV file in the `data/` folder. Default is `messy_transactions_1200.csv`.
2. **(Optional) Set up Gemini API:**
   - Get your Gemini API key from Google.
   - Create a `.env` file in the project root:
     ```
     api_key=YOUR_GEMINI_API_KEY
     ```
3. **Run the main script:**
   ```bash
   python Main.py
   ```
4. **View Results:**
   - Visualizations will pop up.
   - Recommendations and (if API key is set) Gemini AI insights will print in the terminal.

## Customization
- To use a different CSV, change the filename in `Main.py`:
  ```python
  df = load_and_clean_data("data/your_file.csv")
  ```
- You can modify thresholds and logic in `recommendation.py` for personalized tips.

## Notes
- The project is modular; you can use individual scripts for specific tasks.
- If you do not provide a Gemini API key, the AI insights section will be skipped.

## License
MIT License

---
*Developed for TechSophy Exam Project, July 2025.*
