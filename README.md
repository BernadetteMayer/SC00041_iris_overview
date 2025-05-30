# Iris Dataset Visualizer

This project contains a simple Python script that loads the classic **Iris dataset**, generates pairwise plots using **Seaborn**, and saves the resulting figure with a timestamped filename.

## Description

The script performs the following tasks:

- Loads the Iris dataset using `seaborn.load_dataset`.
- Creates a `PairGrid` plot with:
  - Histogram plots on the diagonal.
  - Scatter plots off the diagonal.
  - Color-coded species labels.
- Generates a timestamped filename.
- Saves the plot as a PNG image in a specified directory.

## Files

- `iris_overview.py`: Main Python script for generating the pairwise plots.
- Output files: PNG images saved with timestamped filenames (e.g., `output_250528_142301.png`).

## Example Output

Running the script will generate a plot similar to this (plot not shown here) and save it with a filename based on the current date and time.

Example filename:

output_250528_142301.png


## Usage

### Requirements

- Python 3
- Seaborn
- Matplotlib (Seaborn dependency)

You can install the required package with:

```bash
pip install seaborn

## Running the Script
Run the script using:

```bash
python3 iris_plotter.py
  ```
## License
This project is licensed under the GNU General Public License v3.0.

You are free to run, study, share, and modify this software under the terms of the license. If you distribute modified versions, they must also be licensed under the GPL.

See the LICENSE file for the full text of the license, or visit:
https://www.gnu.org/licenses/gpl-3.0.en.html
