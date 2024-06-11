import matplotlib
matplotlib.use('Agg')
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import UploadFileForm
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            data_analysis = handle_uploaded_file(request.FILES['file'])
            return render(request, 'dataapp/results.html', data_analysis)
    else:
        form = UploadFileForm()
    return render(request, 'dataapp/upload.html', {'form': form})

def handle_uploaded_file(f):
    # Save the uploaded file to a temporary location
    with open('temp.csv', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    
    # Process the file
    data = pd.read_csv('temp.csv')
    
    # Perform data analysis
    data_analysis = {
        "head": data.head().to_html(),
        "description": data.describe().to_html(),
        "missing_values": data.isnull().sum().reset_index().to_html(),
    }
    
    # Ensure the static directory exists
    static_dir = os.path.join(os.path.dirname(__file__), '..', 'static')
    if not os.path.exists(static_dir):
        os.makedirs(static_dir)
    
    # Generate plots
    plt.figure()
    data.hist(figsize=(10, 10))
    plot_path = os.path.join(static_dir, 'histograms.png')
    plt.savefig(plot_path)
    plt.close()  # Close the plot to free memory

    # data for India
    india = data[data['Country']=="India"]
    # Create a figure with subplots
    fig, axs = plt.subplots(3, 1, figsize=(10, 18))

    # Plot CO2 emissions in the first subplot
    axs[0].bar(india['Year'], india['Emissions.Type.CO2'], color='blue', label='CO2')
    axs[0].set_xlabel('Year')
    axs[0].set_ylabel('Emissions in kilo-tons')
    axs[0].set_title('India: Yearly CO2 Emissions')
    axs[0].legend()

    # Plot N2O emissions in the second subplot
    axs[1].bar(india['Year'], india['Emissions.Type.N2O'], color='green', label='N2O')
    axs[1].set_xlabel('Year')
    axs[1].set_ylabel('Emissions in kilo-tons')
    axs[1].set_title('India: Yearly N2O Emissions')
    axs[1].legend()

    # Plot CH4 emissions in the third subplot
    axs[2].bar(india['Year'], india['Emissions.Type.CH4'], color='red', label='CH4')
    axs[2].set_xlabel('Year')
    axs[2].set_ylabel('Emissions in kilo-tons')
    axs[2].set_title('India: Yearly CH4 Emissions')
    axs[2].legend()

    # Adjust layout to prevent overlap
    plt.tight_layout()

    # Save the plot
    india_plot_path = os.path.join(static_dir, 'india_emissions.png')
    plt.savefig(india_plot_path)
    plt.close()

    sum_co2 = india['Emissions.Type.CO2'].sum()
    sum_n2o = india['Emissions.Type.N2O'].sum()
    sum_ch4 = india['Emissions.Type.CH4'].sum()

    # Data for the pie chart
    sums = [sum_co2, sum_n2o, sum_ch4]
    labels = ['CO2','N2O','CH4']

    # Plotting the pie chart
    plt.figure(figsize=(4,4))
    plt.pie(sums, labels=labels, autopct='%1.1f%%', startangle=140, colors=['skyblue', 'green', 'orange'])
    plt.title('Total Emissions by Type')
    pie_plot_path = os.path.join(static_dir, 'pie_chart.png')
    plt.savefig(pie_plot_path)
    plt.close()

    # Sample data
    sum_pi = india['Emissions.Sector.Power Industry'].sum()
    sum_b = india['Emissions.Sector.Buildings'].sum()
    sum_tr = india['Emissions.Sector.Transport'].sum()
    sum_ot = india['Emissions.Sector.Other sectors'].sum()
    vals = [sum_pi, sum_b, sum_tr, sum_ot]
    labels = ['Power Sector', 'Construction', 'Transport', 'Other']

    # Create a figure with subplots
    fig, axs = plt.subplots(1, 2, figsize=(15, 6))

    # Plot the bar chart in the first subplot
    axs[0].bar(labels, vals, color=['skyblue', 'green', 'orange', 'purple'])
    axs[0].set_xlabel('Sector')
    axs[0].set_ylabel('Total Emissions')
    axs[0].set_title('Total Emissions by Sector')

    # Plot the pie chart in the second subplot
    axs[1].pie(vals, labels=labels, autopct='%1.1f%%', startangle=140, colors=['skyblue', 'green', 'orange', 'purple'])
    axs[1].set_title('Emissions Distribution by Sector')

    # Adjust layout to prevent overlap
    plt.tight_layout()

    # Save the plot
    sector_plot_path = os.path.join(static_dir, 'sector_emissions.png')
    plt.savefig(sector_plot_path)
    plt.close()

    #india vs World
    w_sum_co2 = data['Emissions.Type.CO2'].sum()
    w_sum_n2o = data['Emissions.Type.N2O'].sum()
    w_sum_ch4 = data['Emissions.Type.CH4'].sum()
    w_total = w_sum_co2+w_sum_n2o+w_sum_ch4 - sum(sums)
    # Data for the pie chart
    comp = [w_total,sum(sums)]
    labels = ['World','India']

    # Plotting the pie chart
    plt.figure(figsize=(4,4))
    plt.pie(comp, labels=labels, autopct='%1.1f%%', startangle=140, colors=['skyblue','orange'])
    plt.title('Total Emissions(1970-2010): India vs World')
    comp_plot_path = os.path.join(static_dir, 'comp_chart.png')
    plt.savefig(comp_plot_path)
    plt.close()

    return data_analysis
