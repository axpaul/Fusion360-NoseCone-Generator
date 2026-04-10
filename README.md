# Fusion 360 Nose Cone Generator

A Python-based script for Autodesk Fusion 360 designed to automatically generate precise 2D nose cone profiles based on custom parameters. This tool is ideal for amateur rocketry, aerospace design, and aerodynamic research.

## Features

- **Integrated User Interface**: A single dialog box to configure all parameters at once.
- **Full Parameter Control**: Adjustable length, diameter, and precision (number of points).
- **Supports Multiple Aerodynamic Profiles**: Choose from the most common nose cone geometries, mathematically validated and ready for revolution.

### Supported Profiles Gallery

<table>
  <tr>
    <td align="center">
      <img src="https://raw.githubusercontent.com/axpaul/Fusion360-NoseCone-Generator/main/Ogive_Tangent_150mm.png" width="200px"/><br/>
      <b>Tangent Ogive</b>
    </td>
    <td align="center">
      <img src="https://raw.githubusercontent.com/axpaul/Fusion360-NoseCone-Generator/main/Ogive_Von%20Karman_150mm.png" width="200px"/><br/>
      <b>Von Kármán</b>
    </td>
  </tr>
  <tr>
    <td align="center">
      <img src="https://raw.githubusercontent.com/axpaul/Fusion360-NoseCone-Generator/main/Ogive_Conic_150mm.png" width="200px"/><br/>
      <b>Conic</b>
    </td>
    <td align="center">
      <img src="https://raw.githubusercontent.com/axpaul/Fusion360-NoseCone-Generator/main/Ogive_Elliptical_150mm.png" width="200px"/><br/>
      <b>Elliptical</b>
    </td>
  </tr>
</table>

## Installation

1. Download the `OgiveGenerator.py` file from this repository.
2. In **Autodesk Fusion 360**, navigate to the **Utilities** tab > **Add-ins** > **Scripts and Add-ins**.
3. Click the **Scripts** tab and then the **Create** button.
4. Name it `OgiveGenerator`.
5. An editor window will open. Replace the default code with the content of `OgiveGenerator.py`.
6. Save and return to Fusion 360.
7. Select the script and click **Run**.

## Usage

1. Launch the script.
2. Select the **Nose Cone Type** from the dropdown menu.
3. Enter the **Length** and **Base Diameter** (in mm).
4. Set the **Precision** (number of points).
5. Click **OK**. A closed sketch will be created at the origin.
6. Use the **Revolve** tool in Fusion 360 with the X-axis as the axis of revolution.

## License

This work is licensed under a GNU General Public License v3.0
