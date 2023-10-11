# Project Title: Salary Trend Prediction using Linear Regression

# Description:

This project focuses on predicting salary trends for the upcoming year using a Linear Regression model.
It leverages data from Kaggle for historical salary trends and incorporates economic indicators such as inflation rate and GDP from AlphaVantage.
The integrated dataset is stored in a PostgreSQL database for seamless analysis.

# Key Features:
- Data Acquisition: Utilized Kaggle API to extract comprehensive job market data and AlphaVantage for economic indicators.
- Linear Regression Model: Implemented to predict future salary trends based on historical data and economic indicators.
- FastAPI Web Interface: Provided a user-friendly interface for customized insights, allowing users to input specific job titles for targeted analysis.
- Database management using PostgreSQL for storing and updating project data.
- Visual representation of salary trends through matplotlib.

# Project Structure:
- `data_extraction.py`: Contains scripts for acquiring and integrating data from Kaggle and AlphaVantage.
- `linear_regression_model.py`: Includes the implementation of the Linear Regression model for salary predictions.
- `web_interface.py`: Implements the FastAPI web interface for user interaction with the data.
- `database_setup.py`: Sets up the PostgreSQL database and handles data integration.

# Usage:
1. Clone the repository: `git clone https://github.com/NafayMalik/salary-trend-prediction.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Run the project: `python api.py`

# Future Enhancements:
- Explore additional economic indicators for a more comprehensive analysis.
- Consider incorporating advanced machine learning models for improved accuracy.

# Contributing:
Contributions are welcome! Feel free to open issues or submit pull requests for enhancements or bug fixes.

3 License:
This project is licensed under the MIT License - see the `LICENSE` file for details.
