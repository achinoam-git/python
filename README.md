# Titanic Dashboard

An interactive web dashboard for exploring the Titanic passenger dataset. Built with [Dash](https://dash.plotly.com/) and [Plotly](https://plotly.com/python/), it lets you filter passengers by class and sex and view survival rates and age distributions.

## Features

- **Passenger class filter** — Dropdown to select 1st, 2nd, or 3rd class
- **Sex filter** — Radio buttons to filter by male or female passengers
- **Survival pie chart** — Shows the proportion of survivors vs. non-survivors for the selected group
- **Age histogram** — Displays the age distribution of passengers in the filtered subset

## Requirements

- Python 3.8+

Install dependencies:

```bash
pip install pandas plotly dash seaborn
```

| Package  | Purpose                          |
|----------|----------------------------------|
| pandas   | Data loading and filtering       |
| plotly   | Chart generation                 |
| dash     | Web dashboard framework          |
| seaborn  | Optional — loads the Titanic dataset locally |

If `seaborn` is not installed, the app falls back to downloading the dataset from GitHub.

## Usage

From the project directory, run:

```bash
python titanic_dashboard.py
```

Open your browser and go to [http://127.0.0.1:8050](http://127.0.0.1:8050). Use the dropdown and radio buttons to update the charts in real time.

Press `Ctrl+C` in the terminal to stop the server.

## Project Structure

```
python/
├── titanic_dashboard.py   # Main Dash application
└── README.md
```

## How It Works

1. The Titanic dataset is loaded via `seaborn.load_dataset('titanic')`, or from a remote CSV if seaborn is unavailable.
2. Column names are normalized so both dataset formats work (`survived`, `sex`, `age`, `pclass`).
3. A Dash callback reacts to filter changes and updates the pie chart and histogram for the selected passenger group.

## License

This project is for educational purposes as part of a data analyst course.
