import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

class RatingPredictor:
    def __init__(self, learning_rate=3.3e-7, epochs=100000, reg_lambda=1000):
        """Initialize model hyperparameters."""
        self.learning_rate = learning_rate
        self.epochs = epochs
        self.reg_lambda = reg_lambda
        self.weight = 1.0
        self.bias = -185.0
        self.df = None
        self.df_clean = None

    def load_data(self, file_url=None):
        """Loads data from URL or local path."""
        if file_url is None:
            # Default Google Drive link from your notebook
            file_id = '1VfCaU5vFVWsSYrvKQF2x9iS6I7KoWEVH'
            file_url = f'https://drive.google.com/uc?id={file_id}'
        
        print("Loading data...")
        self.df = pd.read_csv(file_url)
        self.df.dropna(inplace=True)
        print(f"Data loaded. Shape: {self.df.shape}")

    def remove_outliers(self):
        """Removes outliers using IQR method."""
        if self.df is None:
            raise ValueError("Data not loaded. Call load_data() first.")

        print("Removing outliers...")
        df_temp = self.df.copy()
        for col in ['cf_rating', 'cc_rating']:
            Q1 = df_temp[col].quantile(0.25)
            Q3 = df_temp[col].quantile(0.75)
            IQR = Q3 - Q1
            lower = Q1 - 1.5 * IQR
            upper = Q3 + 1.5 * IQR
            df_temp = df_temp[(df_temp[col] >= lower) & (df_temp[col] <= upper)]
        
        self.df_clean = df_temp
        print(f"Outliers removed. New Shape: {self.df_clean.shape}")

    def visualize(self):
        """Generates plots (Scatter, KDE, Regplot)."""
        if self.df_clean is None:
            print("No clean data found. plotting raw data...")
            data_to_plot = self.df
        else:
            data_to_plot = self.df_clean

        # 1. Correlation Heatmap
        plt.figure(figsize=(6, 4))
        sns.heatmap(data_to_plot[['cc_rating', 'cf_rating']].corr(), annot=True, cmap='coolwarm')
        plt.title('Correlation Matrix')
        plt.show()

        # 2. Scatter Plot
        fig = px.scatter(data_to_plot, x='cc_rating', y='cf_rating', 
                         title='CC vs CF Ratings', color='cf_rating')
        fig.show(renderer='png')

    def train(self):
        """Runs Gradient Descent to find best Weight and Bias."""
        if self.df_clean is None:
            self.remove_outliers()

        X = self.df_clean['cc_rating'].to_numpy().flatten()
        Y = self.df_clean['cf_rating'].to_numpy().flatten()
        m = len(X)

        print(f"Training on {m} samples for {self.epochs} epochs...")
        
        for _ in range(self.epochs):
            y_pred = self.weight * X + self.bias
            error = y_pred - Y
            
            dw = np.dot(X, error) + self.reg_lambda * self.weight
            db = np.sum(error)
            
            self.weight -= (self.learning_rate / m) * dw
            self.bias -= (self.learning_rate / m) * db

        print(f"Training Complete. Model: y = ({self.weight:.4f})x + ({self.bias:.4f})")
        
        # Calculate R2 Score
        ss_res = np.sum((Y - y_pred) ** 2)
        ss_tot = np.sum((Y - np.mean(Y)) ** 2)
        r2 = 1 - (ss_res / ss_tot)
        print(f"R² Score: {r2:.4f}")

    def predict_cf(self, cc_rating):
        """Predicts Codeforces rating from Codechef rating."""
        return (cc_rating * self.weight) + self.bias

    def predict_cc(self, cf_rating):
        """Predicts Codechef rating from Codeforces rating."""
        return (cf_rating - self.bias) / self.weight

# --- Execution Block ---
if __name__ == "__main__":
    # 1. Initialize
    model = RatingPredictor()
    
    # 2. Load & Clean
    model.load_data()
    model.remove_outliers()
    
    # 3. Visualize (Optional - comment out if not needed)
    # model.visualize()
    
    # 4. Train
    model.train()
    
    # 5. Test Prediction
    test_rating = 1600
    print(f"\nPrediction: CC {test_rating} -> CF {int(model.predict_cf(test_rating))}")