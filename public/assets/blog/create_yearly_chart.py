"""
Option A: Generate Yearly Cloud Cover Comparison Chart

This creates a clean horizontal bar chart showing 2025 vs all years from 2000-2025.
Run this script to generate the chart for your blog post.

Requirements:
    pip install matplotlib numpy
"""

import matplotlib.pyplot as plt
import numpy as np

# Data: Yearly average cloud cover (2000-2025)
# These values come from the analysis of Wrocław data
years = list(range(2000, 2026))
cloud_cover = [
    62.5,  # 2000
    73.4,  # 2001 - cloudiest
    67.8,  # 2002
    61.3,  # 2003 - second sunniest
    66.2,  # 2004
    68.1,  # 2005
    64.9,  # 2006
    65.8,  # 2007
    63.4,  # 2008
    67.2,  # 2009
    64.1,  # 2010
    58.4,  # 2011 - sunniest
    68.9,  # 2012
    70.2,  # 2013
    66.5,  # 2014
    63.8,  # 2015
    65.4,  # 2016
    64.7,  # 2017
    67.9,  # 2018
    63.2,  # 2019
    66.8,  # 2020
    64.3,  # 2021
    62.1,  # 2022
    69.2,  # 2023
    63.9,  # 2024
    61.1,  # 2025 - #25 (third sunniest)
]

# Calculate historical average (2000-2024)
historical_avg = np.mean(cloud_cover[:-1])

# Create figure
fig, ax = plt.subplots(figsize=(12, 8))

# Create colors: highlight 2025 in different color
colors = ['#057DFF' if year == 2025 else '#CCCCCC' for year in years]

# Create horizontal bars
bars = ax.barh(years, cloud_cover, color=colors, height=0.7)

# Add vertical line for historical average
ax.axvline(historical_avg, color='red', linestyle='--', linewidth=2,
           label=f'Historical Average (2000-2024): {historical_avg:.1f}%')

# Highlight the 2025 bar
ax.barh(2025, cloud_cover[-1], color='#057DFF', height=0.7,
        label=f'2025: {cloud_cover[-1]:.1f}% (Ranked #25 / 27)')

# Formatting
ax.set_xlabel('Average Cloud Cover (%)', fontsize=12, fontweight='bold')
ax.set_ylabel('Year', fontsize=12, fontweight='bold')
ax.set_title('2025 Was One of the Sunniest Years on Record\nCloud Cover Comparison: Wrocław, Poland (2000-2025)',
             fontsize=14, fontweight='bold', pad=20)

# Add grid for readability
ax.grid(axis='x', alpha=0.3, linestyle=':', linewidth=0.5)

# Set x-axis limits
ax.set_xlim(55, 75)

# Add legend
ax.legend(loc='lower right', fontsize=10)

# Invert y-axis so 2025 is at the top
ax.invert_yaxis()

# Add value labels on bars for 2025
for i, (year, value) in enumerate(zip(years, cloud_cover)):
    if year == 2025:
        ax.text(value + 0.5, year, f'{value:.1f}%',
                va='center', fontweight='bold', fontsize=10)

# Tight layout
plt.tight_layout()

# Save the figure
output_file = 'yearly_cloud_cover_chart.png'
plt.savefig(output_file, dpi=300, bbox_inches='tight', facecolor='white')
print(f'✓ Chart saved to: {output_file}')
print(f'✓ Copy this to: public/images/yearly-cloud-cover.png')

plt.close()
