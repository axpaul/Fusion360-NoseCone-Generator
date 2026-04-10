# Fusion 360 Nose Cone Generator

A Python-based script for Autodesk Fusion 360 designed to automatically generate precise 2D nose cone profiles based on custom parameters. This tool is ideal for amateur rocketry, aerospace design, and aerodynamic research.

## Features

- **Integrated User Interface**: A single dialog box to configure all parameters at once.
- **5 Supported Profile Types**:
  - **Tangent**: Standard profile for a smooth transition to the body tube.
  - **Parabolic**: Excellent performance for subsonic flight.
  - **Von Kármán (Haack Series)** : Mathematically optimized for minimum drag at supersonic speeds.
  - **Conic**: Simple straight-line geometry.
  - **Elliptical**: Rounded nose, popular for subsonic sport rocketry.
- **Full Parameter Control**: Adjustable length, diameter, and precision (number of points).
- **Ready for Revolution**: Generates a closed profile that can be immediately used with the Fusion 360 "Revolve" tool.

## Installation

1. Download the `OgiveGenerator.py` file from this repository.
2. In **Autodesk Fusion 360**, navigate to the **Utilities** tab > **Add-ins** > **Scripts and Add-ins**.
3. Click the **Scripts** tab and then the **Create** button.
4. Name it `OgiveGenerator`.
5. An editor window will open (VS Code or similar). Replace the default code with the content of `OgiveGenerator.py`.
6. Save the file and return to Fusion 360.
7. Select the script in the list and click **Run**.

## Usage

1. Launch the script.
2. Select the **Nose Cone Type** from the dropdown menu.
3. Enter the **Length** and **Base Diameter** (in mm).
4. Set the **Precision** (number of points). *Recommendation: Use 50+ points for Von Kármán profiles.*
5. Click **OK**. A sketch will be created at the origin of the active component.
6. Use the **Revolve** tool in Fusion 360, selecting the generated profile and the X-axis as the axis of revolution.

## Technical Details

The script implements standard aerodynamic equations for nose cone design as documented in aerospace literature and [Wikipedia](https://en.wikipedia.org/wiki/Nose_cone_design).

## License

This project is licensed under the GNU General Public License v3.0 - see the LICENSE file for details.
