# US Population Dashboard

This project is a **Dash and Plotly** web application that visualizes **historical US state population data** using an interactive **choropleth map** and **population trend charts**.

## Features
✅ **Interactive Choropleth Map**: Displays population distribution across US states for a selected year.
✅ **Dropdown Year Selection**: Allows users to select a year to update the map dynamically.
✅ **Population Trend Line Chart**: Clicking a state shows its population trend over time.
✅ **Live Data Processing**: Uses a dataset hosted on GitHub for real-time visualization.

## Installation
To run this project, ensure you have Python installed and follow these steps:

```sh
# Clone the repository
git clone https://github.com/YOUR_USERNAME/us-population-dashboard.git
cd us-population-dashboard

# Install dependencies
pip install dash plotly pandas numpy

# Run the application
python app.py
```

The app will be available at:
```
http://127.0.0.1:8050
```

## Dataset
The app fetches **US historical state population data** from [JoshData](https://github.com/JoshData/historical-state-population-csv). The dataset includes:
- **State** (Abbreviations converted to full names)
- **Year** (Historical records from multiple decades)
- **Population** (State population count)

## How It Works
1. **Dropdown Selection**: Choose a year from the dropdown.
2. **Interactive Map**: Hover over states to see their population.
3. **Click a State**: Displays a line chart of population trends over time.
4. **Dynamic Updates**: The map and chart update based on the user’s selection.

## File Structure
```
us-population-dashboard/
│-- app.py               # Main Dash application
│-- requirements.txt     # Required dependencies
│-- README.md            # Project documentation
```

## Future Enhancements 🚀
- Add more filtering options (e.g., regional selection).
- Deploy the app online using Heroku or GitHub Pages.
- Improve the UI with additional styling.

## License
This project is licensed under the **MIT License**.

---
Feel free to **contribute**, **suggest improvements**, or **report issues**! 🚀

