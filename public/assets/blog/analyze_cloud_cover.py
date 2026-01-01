#!/usr/bin/env python3
"""
Cloud Cover Analysis Script
============================

Analyzes historical cloud cover data to compare yearly trends and test
subjective feelings about weather patterns.

Usage:
    python analyze_cloud_cover.py [OPTIONS]

Options:
    --file PATH         Path to CSV file (default: cloud_data_wroclaw_2000-2025.csv)
    --target-year YEAR  Year to analyze (default: 2025)
    --output PATH       Output image path (default: cloud_cover_analysis.png)
    --help              Show this help message

CSV Format Expected:
    - date: timestamp column
    - cloud_cover: percentage (0-100)
    - cloud_cover_low: percentage (optional)
    - cloud_cover_mid: percentage (optional)
    - cloud_cover_high: percentage (optional)

Example:
    python analyze_cloud_cover.py --target-year 2024 --output results_2024.png

Author: Data-driven weather skeptic
Date: 2026-01-01
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import argparse
import sys
import warnings
warnings.filterwarnings('ignore')


def load_data(filepath):
    """Load and preprocess cloud cover data."""
    try:
        df = pd.read_csv(filepath)
        df['date'] = pd.to_datetime(df['date'])
        df['year'] = df['date'].dt.year
        df['month'] = df['date'].dt.month
        df['day'] = df['date'].dt.date
        return df
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error loading data: {e}")
        sys.exit(1)


def calculate_yearly_stats(df):
    """Calculate yearly statistics for cloud cover."""
    yearly_stats = df.groupby('year')['cloud_cover'].agg(['mean', 'median', 'std', 'count'])
    yearly_stats.columns = ['Average (%)', 'Median (%)', 'Std Dev', 'Hours']
    return yearly_stats


def calculate_cloudy_days(df, threshold=70):
    """Calculate percentage of cloudy days per year."""
    daily_avg = df.groupby(['year', 'day'])['cloud_cover'].mean().reset_index()
    daily_avg.columns = ['year', 'day', 'avg_cloud_cover']

    cloudy_days = daily_avg[daily_avg['avg_cloud_cover'] > threshold].groupby('year').size()
    total_days = daily_avg.groupby('year').size()
    cloudy_percentage = (cloudy_days / total_days * 100).round(2)

    return cloudy_days, total_days, cloudy_percentage


def calculate_clear_hours(df, threshold=30):
    """Calculate percentage of clear sky hours per year."""
    clear_hours = df[df['cloud_cover'] < threshold].groupby('year').size()
    total_hours = df.groupby('year').size()
    clear_percentage = (clear_hours / total_hours * 100).round(2)

    return clear_hours, total_hours, clear_percentage


def analyze_target_year(yearly_stats, target_year, start_year=2000):
    """Compare target year against historical averages."""
    if target_year not in yearly_stats.index:
        print(f"Error: Target year {target_year} not found in data.")
        sys.exit(1)

    avg_target = yearly_stats.loc[target_year, 'Average (%)']
    avg_historical = yearly_stats.loc[start_year:target_year-1, 'Average (%)'].mean()

    last_5_start = max(start_year, target_year - 5)
    avg_last_5 = yearly_stats.loc[last_5_start:target_year-1, 'Average (%)'].mean()

    yearly_avg = yearly_stats['Average (%)'].sort_values(ascending=False)
    rank = list(yearly_avg.index).index(target_year) + 1

    return {
        'avg_target': avg_target,
        'avg_historical': avg_historical,
        'avg_last_5': avg_last_5,
        'rank': rank,
        'total_years': len(yearly_avg)
    }


def calculate_monthly_comparison(df, target_year):
    """Compare monthly cloud cover for target year vs historical average."""
    monthly_data = df.groupby(['year', 'month'])['cloud_cover'].mean().reset_index()
    monthly_target = monthly_data[monthly_data['year'] == target_year].set_index('month')['cloud_cover']
    monthly_historical = monthly_data[monthly_data['year'] < target_year].groupby('month')['cloud_cover'].mean()

    return monthly_target, monthly_historical


def create_visualizations(yearly_stats, cloudy_percentage, monthly_target, monthly_historical,
                         target_year, avg_historical, output_path):
    """Create comprehensive visualization with 4 subplots."""
    fig, axes = plt.subplots(2, 2, figsize=(16, 12))
    fig.suptitle(f'Cloud Cover Analysis ({yearly_stats.index.min()}-{target_year})',
                 fontsize=16, fontweight='bold')

    # Plot 1: Yearly average cloud cover
    ax1 = axes[0, 0]
    years = yearly_stats.index
    avg_values = yearly_stats['Average (%)']
    colors = ['#e74c3c' if y == target_year else '#3498db' for y in years]
    ax1.bar(years, avg_values, color=colors, alpha=0.7, edgecolor='black', linewidth=0.5)
    ax1.axhline(avg_historical, color='#27ae60', linestyle='--', linewidth=2,
                label=f'Historical Avg: {avg_historical:.1f}%')
    ax1.set_xlabel('Year', fontweight='bold', fontsize=11)
    ax1.set_ylabel('Average Cloud Cover (%)', fontweight='bold', fontsize=11)
    ax1.set_title('Average Cloud Cover by Year', fontweight='bold', fontsize=12)
    ax1.legend(fontsize=10)
    ax1.grid(True, alpha=0.3, linestyle=':', linewidth=0.5)
    ax1.set_xticks(years[::2])
    ax1.set_xticklabels(years[::2], rotation=45)

    # Plot 2: Percentage of cloudy days per year
    ax2 = axes[0, 1]
    cloudy_pct_avg = cloudy_percentage.loc[2000:target_year-1].mean()
    colors2 = ['#e74c3c' if y == target_year else '#e67e22' for y in cloudy_percentage.index]
    ax2.bar(cloudy_percentage.index, cloudy_percentage.values,
            color=colors2, alpha=0.7, edgecolor='black', linewidth=0.5)
    ax2.axhline(cloudy_pct_avg, color='#27ae60', linestyle='--', linewidth=2,
                label=f'Historical Avg: {cloudy_pct_avg:.1f}%')
    ax2.set_xlabel('Year', fontweight='bold', fontsize=11)
    ax2.set_ylabel('Cloudy Days (%)', fontweight='bold', fontsize=11)
    ax2.set_title('Percentage of Cloudy Days (>70% avg) per Year', fontweight='bold', fontsize=12)
    ax2.legend(fontsize=10)
    ax2.grid(True, alpha=0.3, linestyle=':', linewidth=0.5)
    ax2.set_xticks(cloudy_percentage.index[::2])
    ax2.set_xticklabels(cloudy_percentage.index[::2], rotation=45)

    # Plot 3: Monthly comparison
    ax3 = axes[1, 0]
    month_names = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                   'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    x = np.arange(len(month_names))
    width = 0.35

    months_in_target = monthly_target.index
    bars_target = [monthly_target[m] if m in months_in_target else 0 for m in range(1, 13)]

    ax3.bar(x - width/2, monthly_historical.values, width,
            label='Historical Avg', color='#3498db', alpha=0.7, edgecolor='black', linewidth=0.5)
    ax3.bar(x + width/2, bars_target, width,
            label=str(target_year), color='#e74c3c', alpha=0.7, edgecolor='black', linewidth=0.5)
    ax3.set_xlabel('Month', fontweight='bold', fontsize=11)
    ax3.set_ylabel('Average Cloud Cover (%)', fontweight='bold', fontsize=11)
    ax3.set_title(f'Monthly Cloud Cover: {target_year} vs Historical Average',
                  fontweight='bold', fontsize=12)
    ax3.set_xticks(x)
    ax3.set_xticklabels(month_names, fontsize=10)
    ax3.legend(fontsize=10)
    ax3.grid(True, alpha=0.3, axis='y', linestyle=':', linewidth=0.5)

    # Plot 4: Trend over time
    ax4 = axes[1, 1]
    yearly_for_plot = yearly_stats.reset_index()
    ax4.plot(yearly_for_plot['year'], yearly_for_plot['Average (%)'],
             marker='o', linewidth=2, markersize=5, color='#3498db',
             markeredgecolor='black', markeredgewidth=0.5)

    # Add trend line
    z = np.polyfit(yearly_for_plot['year'], yearly_for_plot['Average (%)'], 1)
    p = np.poly1d(z)
    ax4.plot(yearly_for_plot['year'], p(yearly_for_plot['year']),
             "r--", linewidth=2, alpha=0.6, label='Trend line')

    # Highlight target year
    target_val = yearly_stats.loc[target_year, 'Average (%)']
    ax4.plot(target_year, target_val, 'ro', markersize=14,
             label=str(target_year), zorder=5, markeredgecolor='darkred', markeredgewidth=2)

    ax4.set_xlabel('Year', fontweight='bold', fontsize=11)
    ax4.set_ylabel('Average Cloud Cover (%)', fontweight='bold', fontsize=11)
    ax4.set_title('Cloud Cover Trend Over Time', fontweight='bold', fontsize=12)
    ax4.legend(fontsize=10)
    ax4.grid(True, alpha=0.3, linestyle=':', linewidth=0.5)

    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    return output_path


def print_results(df, yearly_stats, cloudy_days, cloudy_percentage, clear_percentage,
                 target_year, analysis_results, monthly_target, monthly_historical):
    """Print comprehensive analysis results."""

    print("\n" + "="*70)
    print(f"CLOUD COVER ANALYSIS RESULTS")
    print("="*70)

    print(f"\nData Period: {df['date'].min()} to {df['date'].max()}")
    print(f"Total Records: {len(df):,} hourly measurements")
    print(f"Years Analyzed: {yearly_stats.index.min()} - {yearly_stats.index.max()}")

    # Yearly statistics table
    print("\n" + "="*70)
    print("YEARLY CLOUD COVER STATISTICS")
    print("="*70)
    print(yearly_stats.to_string())

    # Target year comparison
    print("\n" + "="*70)
    print(f"HOW DOES {target_year} COMPARE?")
    print("="*70)

    avg_target = analysis_results['avg_target']
    avg_historical = analysis_results['avg_historical']
    avg_last_5 = analysis_results['avg_last_5']
    rank = analysis_results['rank']
    total_years = analysis_results['total_years']

    print(f"\n{target_year} Average Cloud Cover: {avg_target:.2f}%")
    print(f"Historical Average (2000-{target_year-1}): {avg_historical:.2f}%")
    print(f"Last 5 Years Average: {avg_last_5:.2f}%")
    print(f"\nDifference from historical: {avg_target - avg_historical:+.2f}%")
    print(f"Difference from last 5 years: {avg_target - avg_last_5:+.2f}%")
    print(f"\n{target_year} ranks #{rank} out of {total_years} years (1 = cloudiest)")

    # Cloudy days comparison
    cloudy_target = cloudy_days.get(target_year, 0)
    cloudy_pct_target = cloudy_percentage.get(target_year, 0)
    cloudy_pct_avg = cloudy_percentage.loc[2000:target_year-1].mean()

    print(f"\nCloudy days (>70% avg) in {target_year}: {cloudy_target} ({cloudy_pct_target:.1f}%)")
    print(f"Historical average: {cloudy_pct_avg:.1f}%")
    print(f"Difference: {cloudy_pct_target - cloudy_pct_avg:+.1f}%")

    # Clear sky hours
    clear_target = clear_percentage.get(target_year, 0)
    clear_avg = clear_percentage.loc[2000:target_year-1].mean()

    print(f"\nClear sky hours (<30% cloud) in {target_year}: {clear_target:.1f}%")
    print(f"Historical average: {clear_avg:.1f}%")
    print(f"Difference: {clear_target - clear_avg:+.1f}%")

    # Monthly breakdown
    print("\n" + "="*70)
    print(f"MONTHLY COMPARISON: {target_year} vs HISTORICAL AVERAGE")
    print("="*70)

    month_names = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                   'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    print(f"\n{'Month':<6} {target_year:>8}  {'Historical':>11}  {'Difference':>11}  {'Trend'}")
    print("-" * 70)

    for month in range(1, 13):
        if month in monthly_target.index:
            val_target = monthly_target[month]
            val_hist = monthly_historical[month]
            diff = val_target - val_hist
            trend = "☀️ Sunnier" if diff < -5 else "☁️ Cloudier" if diff > 5 else "≈ Similar"
            print(f"{month_names[month-1]:<6} {val_target:>7.1f}%  {val_hist:>10.1f}%  "
                  f"{diff:>10.1f}%  {trend}")

    # Summary
    print("\n" + "="*70)
    print("VERDICT")
    print("="*70)

    is_cloudier = avg_target > avg_historical
    verdict = "CLOUDIER" if is_cloudier else "SUNNIER"

    print(f"\n{target_year} was {abs(avg_target - avg_historical):.1f}% {verdict} than the historical average")
    print(f"\nRanking: #{rank} cloudiest year out of {total_years} years")

    if not is_cloudier:
        print(f"\n💡 Insight: Despite feeling cloudier, {target_year} was actually sunnier than average!")
        print("   This demonstrates recency bias and how perception differs from reality.")

    print("\n" + "="*70 + "\n")


def main():
    """Main execution function."""
    parser = argparse.ArgumentParser(
        description='Analyze cloud cover data and compare yearly trends',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python analyze_cloud_cover.py
  python analyze_cloud_cover.py --target-year 2024
  python analyze_cloud_cover.py --file my_data.csv --output results.png
        """
    )

    parser.add_argument('--file', default='cloud_data_wroclaw_2000-2025.csv',
                       help='Path to CSV file with cloud cover data')
    parser.add_argument('--target-year', type=int, default=2025,
                       help='Year to analyze (default: 2025)')
    parser.add_argument('--output', default='cloud_cover_analysis.png',
                       help='Output path for visualization (default: cloud_cover_analysis.png)')

    args = parser.parse_args()

    # Load data
    print(f"\nLoading data from {args.file}...")
    df = load_data(args.file)
    print(f"✓ Loaded {len(df):,} records")

    # Calculate statistics
    print("\nCalculating statistics...")
    yearly_stats = calculate_yearly_stats(df)
    cloudy_days, total_days, cloudy_percentage = calculate_cloudy_days(df)
    clear_hours, total_hours, clear_percentage = calculate_clear_hours(df)

    # Analyze target year
    analysis_results = analyze_target_year(yearly_stats, args.target_year)
    monthly_target, monthly_historical = calculate_monthly_comparison(df, args.target_year)

    # Create visualizations
    print(f"Creating visualizations...")
    output_path = create_visualizations(
        yearly_stats, cloudy_percentage, monthly_target, monthly_historical,
        args.target_year, analysis_results['avg_historical'], args.output
    )
    print(f"✓ Saved visualization to: {output_path}")

    # Print results
    print_results(df, yearly_stats, cloudy_days, cloudy_percentage, clear_percentage,
                 args.target_year, analysis_results, monthly_target, monthly_historical)


if __name__ == '__main__':
    main()
