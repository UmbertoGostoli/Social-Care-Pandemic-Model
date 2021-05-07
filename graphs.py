# -*- coding: utf-8 -*-
"""
Created on Wed Feb 06 15:45:43 2019

@author: ug4d
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import ticker
from matplotlib.ticker import MaxNLocator
from matplotlib.backends.backend_pdf import PdfPages
from matplotlib.ticker import FormatStrFormatter
import os
from collections import OrderedDict
import pandas as pd
import sys
import pdb


def doGraphs(graphsParams, metaParams):
    
    folder = graphsParams[0]
    numRepeats = graphsParams[2]
    numScenarios = graphsParams[3]
    numPolicies = graphsParams[4]
    
    simFolder = 'Simulations_Folder/' + folder
    
    multipleRepeatsDF = []
    for repeatID in range(numRepeats):
        repFolder = simFolder + '/Rep_' + str(repeatID)
        multipleScenariosDF = []
        for scenarioID in range(numScenarios):
            scenarioFolder = repFolder + '/Scenario_' + str(scenarioID)
            multiplePoliciesDF = []
            for policyID in range(numPolicies):
                policyFolder = scenarioFolder + '/Policy_' + str(policyID)
                outputsDF = pd.read_csv(policyFolder + '/Outputs.csv', sep=',', header=0)
                
                singlePolicyGraphs(outputsDF, policyFolder, metaParams)
                
                multiplePoliciesDF.append(outputsDF)
                
            if numPolicies > 1:
                
                multiplePoliciesGraphs(multiplePoliciesDF, scenarioFolder, metaParams, numPolicies)
                
            multipleScenariosDF.append(multiplePoliciesDF)
        if numScenarios > 1:
            
            multipleScenariosGraphs(multipleScenariosDF, repFolder, metaParams, numPolicies, numScenarios)
            
        multipleRepeatsDF.append(multipleScenariosDF)
    if numRepeats > 1:
        
        multipleRepeatsGraphs(multipleRepeatsDF, simFolder, metaParams, numPolicies, numScenarios, numRepeats)
    
    
def singlePolicyGraphs(output, policyFolder, p):
    
    folder = policyFolder + '/Graphs'
    if not os.path.exists(folder):
        os.makedirs(folder)
        
    # policyYears = int((p['endYear']-p['policyStartYear']) + 1)
    
    fig, ax = plt.subplots() # Argument: figsize=(5, 3)
    p1, = ax.plot(output['day'], output['currentPop'], color="red", label = 'Total population', linewidth = 2)
    p2, = ax.plot(output['day'], output['taxPayers'], color="blue", label = 'Taxpayers', linewidth = 2)
    ax.set_ylabel('Number of people')
    handels, labels = ax.get_legend_handles_labels()
    ax.legend(loc = 'lower right')
    ax.ticklabel_format(style='sci', axis='y')
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    # ax.set_xlim(left = int(p['statsCollectFrom']), right = int(p['endYear']))
    # ax.set_xticks(range(int(p['statsCollectFrom']), int(p['endYear'])+1, 20))
    fig.tight_layout()
    path = os.path.join(folder, 'popGrowth.pdf')
    pp = PdfPages(path)
    pp.savefig(fig)
    pp.close()
    
    fig, ax = plt.subplots() # Argument: figsize=(5, 3)
    p1, = ax.plot(output['day'], output['grossDomesticProduct'], color="red", linewidth = 2)
    ax.set_ylabel('Pounds')
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    # ax.set_xlim(left = int(p['statsCollectFrom']), right = int(p['endYear']))
    # ax.set_xticks(range(int(p['statsCollectFrom']), int(p['endYear'])+1, 20))
    fig.tight_layout()
    path = os.path.join(folder, 'grossDomesticProduct.pdf')
    pp = PdfPages(path)
    pp.savefig(fig)
    pp.close()
    
    fig, ax = plt.subplots() # Argument: figsize=(5, 3)
    p1, = ax.plot(output['day'], output['averageHouseholdSize'], color="red", linewidth = 2)
    ax.set_ylabel('Average Household Size')
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    # ax.set_xlim(left = int(p['statsCollectFrom']), right = int(p['endYear']))
    # ax.set_xticks(range(int(p['statsCollectFrom']), int(p['endYear'])+1, 20))
    fig.tight_layout()
    path = os.path.join(folder, 'avgHouseholdSize.pdf')
    pp = PdfPages(path)
    pp.savefig(fig)
    pp.close()
    
    fig, ax = plt.subplots() # Argument: figsize=(5, 3)
    p1, = ax.plot(output['day'], output['marriagePropNow'], color="red", linewidth = 2)
    ax.set_ylabel('Married adult women (share)')
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    # ax.set_xlim(left = int(p['statsCollectFrom']), right = int(p['endday']))
    # ax.set_xticks(range(int(p['statsCollectFrom']), int(p['endday'])+1, 20))
    fig.tight_layout()
    path = os.path.join(folder, 'shareMarriedWomen.pdf')
    pp = PdfPages(path)
    pp.savefig(fig)
    pp.close()
    
    fig, ax = plt.subplots() # Argument: figsize=(5, 3)
    p1, = ax.plot(output['day'], output['shareSingleParents'], color="red", linewidth = 2)
    ax.set_ylabel('Single Parents (share)')
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    # ax.set_xlim(left = int(p['statsCollectFrom']), right = int(p['endday']))
    # ax.set_xticks(range(int(p['statsCollectFrom']), int(p['endday'])+1, 20))
    fig.tight_layout()
    path = os.path.join(folder, 'shareSingleParents.pdf')
    pp = PdfPages(path)
    pp.savefig(fig)
    pp.close()
    
    fig, ax = plt.subplots() # Argument: figsize=(5, 3)
    p1, = ax.plot(output['day'], output['shareFemaleSingleParent'], color="red", linewidth = 2)
    ax.set_ylabel('Female Single Parents (share)')
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    # ax.set_xlim(left = int(p['statsCollectFrom']), right = int(p['endday']))
    # ax.set_xticks(range(int(p['statsCollectFrom']), int(p['endday'])+1, 20))
    fig.tight_layout()
    path = os.path.join(folder, 'shareFemaleSingleParents.pdf')
    pp = PdfPages(path)
    pp.savefig(fig)
    pp.close()
    
    fig, ax = plt.subplots() # Argument: figsize=(5, 3)
    p1, = ax.plot(output['day'], output['totalHospitalizationCost'], color="red", linewidth = 2)
    ax.set_ylabel('Hospitalization Cost')
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    # ax.set_xlim(left = int(p['statsCollectFrom']), right = int(p['endday']))
    # ax.set_xticks(range(int(p['statsCollectFrom']), int(p['endday'])+1, 20))
    fig.tight_layout()
    path = os.path.join(folder, 'hospitalizationCost.pdf')
    pp = PdfPages(path)
    pp.savefig(fig)
    pp.close()
    
    
    
    fig, ax = plt.subplots() # Argument: figsize=(5, 3)
    p1, = ax.plot(output['day'], output['publicSocialCare'], color="red", linewidth = 2)
    ax.set_ylabel('Public Social Care (hours per week)')
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    # ax.set_xlim(left = int(p['statsCollectFrom']), right = int(p['endday']))
    # ax.set_xticks(range(int(p['statsCollectFrom']), int(p['endday'])+1, 20))
    fig.tight_layout()
    path = os.path.join(folder, 'publicSocialCare.pdf')
    pp = PdfPages(path)
    pp.savefig(fig)
    pp.close()
    
    fig, ax = plt.subplots() # Argument: figsize=(5, 3)
    p1, = ax.plot(output['day'], output['publicCareToGDP'], color="red", linewidth = 2)
    ax.set_ylabel('Share')
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    # ax.set_xlim(left = int(p['statsCollectFrom']), right = int(p['endday']))
    # ax.set_xticks(range(int(p['statsCollectFrom']), int(p['endday'])+1, 20))
    fig.tight_layout()
    path = os.path.join(folder, 'publicCareToGDP.pdf')
    pp = PdfPages(path)
    pp.savefig(fig)
    pp.close()
    
    fig, ax = plt.subplots()
    p1, = ax.plot(output['day'], output['totalInformalSocialCare'], linewidth = 2, label = 'Informal Care')
    p2, = ax.plot(output['day'], output['totalFormalSocialCare'], linewidth = 2, label = 'Formal Care')
    p3, = ax.plot(output['day'], output['totalUnmetSocialCareNeed'], linewidth = 2, label = 'Unmet Care')
    p4, = ax.plot(output['day'], output['publicSocialCare'], linewidth = 2, label = 'Public Social Care')
    # ax.set_xlim(left = p['statsCollectFrom'])
    ax.set_ylabel('Hours per week')
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    # ax.set_xlabel('day')
    handles, labels = ax.get_legend_handles_labels()
    ax.legend(loc = 'lower left')
    # ax.set_title('Total Delivered and Unmet Care')
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    # plt.xlim(p['statsCollectFrom'], p['endday'])
    # plt.ylim(0, 25)
    # plt.xticks(range(int(p['statsCollectFrom']), int(p['endday']+1), 20))
    fig.tight_layout()
    path = os.path.join(folder, 'Delivered_UnmetSocialCareChart.pdf')
    pp = PdfPages(path)
    pp.savefig(fig)
    pp.close()
    
    
    fig, ax = plt.subplots()
    p1, = ax.plot(output['day'], output['q1_infected'], linewidth = 2, label = 'Q1')
    p2, = ax.plot(output['day'], output['q2_infected'], linewidth = 2, label = 'Q2')
    p3, = ax.plot(output['day'], output['q3_infected'], linewidth = 2, label = 'Q3')
    p4, = ax.plot(output['day'], output['q4_infected'], linewidth = 2, label = 'Q4')
    p5, = ax.plot(output['day'], output['q5_infected'], linewidth = 2, label = 'Q5')
    # ax.set_xlim(left = p['statsCollectFrom'])
    ax.set_ylabel('Number of infectious')
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    # ax.set_xlabel('day')
    handles, labels = ax.get_legend_handles_labels()
    ax.legend(loc = 'upper right')
    # ax.set_title('Total Delivered and Unmet Care')
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    # plt.xlim(p['statsCollectFrom'], p['endday'])
    # plt.ylim(0, 25)
    # plt.xticks(range(int(p['statsCollectFrom']), int(p['endday']+1), 20))
    fig.tight_layout()
    path = os.path.join(folder, 'infectiousByQuintile.pdf')
    pp = PdfPages(path)
    pp.savefig(fig)
    pp.close()
    
    # Time series
    fig, ax = plt.subplots()
    p1, = ax.plot(output['day'], output['q1_hospitalized'], linewidth = 2, label = 'Q1')
    p2, = ax.plot(output['day'], output['q2_hospitalized'], linewidth = 2, label = 'Q2')
    p3, = ax.plot(output['day'], output['q3_hospitalized'], linewidth = 2, label = 'Q3')
    p4, = ax.plot(output['day'], output['q4_hospitalized'], linewidth = 2, label = 'Q4')
    p5, = ax.plot(output['day'], output['q5_hospitalized'], linewidth = 2, label = 'Q5')
    # ax.set_xlim(left = p['statsCollectFrom'])
    ax.set_ylabel('Number of hospitalized')
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    # ax.set_xlabel('day')
    handles, labels = ax.get_legend_handles_labels()
    ax.legend(loc = 'upper right')
    # ax.set_title('Total Delivered and Unmet Care')
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    # plt.xlim(p['statsCollectFrom'], p['endday'])
    # plt.ylim(0, 25)
    # plt.xticks(range(int(p['statsCollectFrom']), int(p['endday']+1), 20))
    fig.tight_layout()
    path = os.path.join(folder, 'hospitalizedByQuintile.pdf')
    pp = PdfPages(path)
    pp.savefig(fig)
    pp.close()
    
    ############    Bar charts: pandemic effects by income quintilie and age class  #########################
    
    # 1- Infected
    
    fig, ax = plt.subplots()
    objects = ('Q1', 'Q2', 'Q3', 'Q4', 'Q5')
    y_pos = np.arange(len(objects))
    outputs = []
    outputs.append(np.sum(output['infectedByClass_0']))
    outputs.append(np.sum(output['infectedByClass_1']))
    outputs.append(np.sum(output['infectedByClass_2']))
    outputs.append(np.sum(output['infectedByClass_3']))
    outputs.append(np.sum(output['infectedByClass_4']))
    ax.bar(y_pos, outputs, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    # plt.ylim(1200000, 1400000)
    ax.xaxis.set_ticks_position('none')
    # ax.set_ylabel('Total hours')
    # ax.set_title('Formal Child Care (2020-2040)')
    fig.tight_layout()
    path = os.path.join(folder, 'infectedByQuintilesBarChart.pdf')
    pp = PdfPages(path)
    pp.savefig(fig)
    pp.close()
    
    fig, ax = plt.subplots()
    objects = ('0-10', '10-20', '20-30', '30-40', '40-50', '50-60', '60-70', '70-80', '80+')
    y_pos = np.arange(len(objects))
    outputs = []
    outputs.append(np.sum(output['infectedByAge_0']))
    outputs.append(np.sum(output['infectedByAge_1']))
    outputs.append(np.sum(output['infectedByAge_2']))
    outputs.append(np.sum(output['infectedByAge_3']))
    outputs.append(np.sum(output['infectedByAge_4']))
    outputs.append(np.sum(output['infectedByAge_5']))
    outputs.append(np.sum(output['infectedByAge_6']))
    outputs.append(np.sum(output['infectedByAge_7']))
    outputs.append(np.sum(output['infectedByAge_8']))
    ax.bar(y_pos, outputs, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    # plt.ylim(1200000, 1400000)
    ax.xaxis.set_ticks_position('none')
    # ax.set_ylabel('Number')
    # ax.set_title('Formal Child Care (2020-2040)')
    fig.tight_layout()
    path = os.path.join(folder, 'infectedByAgeClassBarChart.pdf')
    pp = PdfPages(path)
    pp.savefig(fig)
    pp.close()
    
    
    # 2 - Hospitalized
    
    fig, ax = plt.subplots()
    objects = ('Q1', 'Q2', 'Q3', 'Q4', 'Q5')
    y_pos = np.arange(len(objects))
    outputs = []
    outputs.append(np.sum(output['hospitalizedByClass_0']))
    outputs.append(np.sum(output['hospitalizedByClass_1']))
    outputs.append(np.sum(output['hospitalizedByClass_2']))
    outputs.append(np.sum(output['hospitalizedByClass_3']))
    outputs.append(np.sum(output['hospitalizedByClass_4']))
    ax.bar(y_pos, outputs, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    # plt.ylim(1200000, 1400000)
    ax.xaxis.set_ticks_position('none')
    # ax.set_ylabel('Total hours')
    # ax.set_title('Formal Child Care (2020-2040)')
    fig.tight_layout()
    path = os.path.join(folder, 'hospitalizedByQuintilesBarChart.pdf')
    pp = PdfPages(path)
    pp.savefig(fig)
    pp.close()
    
    fig, ax = plt.subplots()
    objects = ('0-10', '10-20', '20-30', '30-40', '40-50', '50-60', '60-70', '70-80', '80+')
    y_pos = np.arange(len(objects))
    outputs = []
    outputs.append(np.sum(output['hospitalizedByAge_0']))
    outputs.append(np.sum(output['hospitalizedByAge_1']))
    outputs.append(np.sum(output['hospitalizedByAge_2']))
    outputs.append(np.sum(output['hospitalizedByAge_3']))
    outputs.append(np.sum(output['hospitalizedByAge_4']))
    outputs.append(np.sum(output['hospitalizedByAge_5']))
    outputs.append(np.sum(output['hospitalizedByAge_6']))
    outputs.append(np.sum(output['hospitalizedByAge_7']))
    outputs.append(np.sum(output['hospitalizedByAge_8']))
    ax.bar(y_pos, outputs, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    # plt.ylim(1200000, 1400000)
    ax.xaxis.set_ticks_position('none')
    # ax.set_ylabel('Number')
    # ax.set_title('Formal Child Care (2020-2040)')
    fig.tight_layout()
    path = os.path.join(folder, 'hospitalizedByAgeClassBarChart.pdf')
    pp = PdfPages(path)
    pp.savefig(fig)
    pp.close()
    
    # 3- Intubated
    
    fig, ax = plt.subplots()
    objects = ('Q1', 'Q2', 'Q3', 'Q4', 'Q5')
    y_pos = np.arange(len(objects))
    outputs = []
    outputs.append(np.sum(output['intubatedByClass_0']))
    outputs.append(np.sum(output['intubatedByClass_1']))
    outputs.append(np.sum(output['intubatedByClass_2']))
    outputs.append(np.sum(output['intubatedByClass_3']))
    outputs.append(np.sum(output['intubatedByClass_4']))
    ax.bar(y_pos, outputs, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    # plt.ylim(1200000, 1400000)
    ax.xaxis.set_ticks_position('none')
    # ax.set_ylabel('Total hours')
    # ax.set_title('Formal Child Care (2020-2040)')
    fig.tight_layout()
    path = os.path.join(folder, 'intubatedByQuintilesBarChart.pdf')
    pp = PdfPages(path)
    pp.savefig(fig)
    pp.close()
    
    fig, ax = plt.subplots()
    objects = ('0-10', '10-20', '20-30', '30-40', '40-50', '50-60', '60-70', '70-80', '80+')
    y_pos = np.arange(len(objects))
    outputs = []
    outputs.append(np.sum(output['intubatedByAge_0']))
    outputs.append(np.sum(output['intubatedByAge_1']))
    outputs.append(np.sum(output['intubatedByAge_2']))
    outputs.append(np.sum(output['intubatedByAge_3']))
    outputs.append(np.sum(output['intubatedByAge_4']))
    outputs.append(np.sum(output['intubatedByAge_5']))
    outputs.append(np.sum(output['intubatedByAge_6']))
    outputs.append(np.sum(output['intubatedByAge_7']))
    outputs.append(np.sum(output['intubatedByAge_8']))
    ax.bar(y_pos, outputs, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    # plt.ylim(1200000, 1400000)
    ax.xaxis.set_ticks_position('none')
    # ax.set_ylabel('Number')
    # ax.set_title('Formal Child Care (2020-2040)')
    fig.tight_layout()
    path = os.path.join(folder, 'intubatedByAgeClassBarChart.pdf')
    pp = PdfPages(path)
    pp.savefig(fig)
    pp.close()
    
    # 4 - Symptomatic
    
    fig, ax = plt.subplots()
    objects = ('Q1', 'Q2', 'Q3', 'Q4', 'Q5')
    y_pos = np.arange(len(objects))
    outputs = []
    outputs.append(np.sum(output['symptomaticByClass_0']))
    outputs.append(np.sum(output['symptomaticByClass_1']))
    outputs.append(np.sum(output['symptomaticByClass_2']))
    outputs.append(np.sum(output['symptomaticByClass_3']))
    outputs.append(np.sum(output['symptomaticByClass_4']))
    ax.bar(y_pos, outputs, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    # plt.ylim(1200000, 1400000)
    ax.xaxis.set_ticks_position('none')
    # ax.set_ylabel('Total hours')
    # ax.set_title('Formal Child Care (2020-2040)')
    fig.tight_layout()
    path = os.path.join(folder, 'symptomaticByQuintilesBarChart.pdf')
    pp = PdfPages(path)
    pp.savefig(fig)
    pp.close()
    
    fig, ax = plt.subplots()
    objects = ('0-10', '10-20', '20-30', '30-40', '40-50', '50-60', '60-70', '70-80', '80+')
    y_pos = np.arange(len(objects))
    outputs = []
    outputs.append(np.sum(output['symptomaticByAge_0']))
    outputs.append(np.sum(output['symptomaticByAge_1']))
    outputs.append(np.sum(output['symptomaticByAge_2']))
    outputs.append(np.sum(output['symptomaticByAge_3']))
    outputs.append(np.sum(output['symptomaticByAge_4']))
    outputs.append(np.sum(output['symptomaticByAge_5']))
    outputs.append(np.sum(output['symptomaticByAge_6']))
    outputs.append(np.sum(output['symptomaticByAge_7']))
    outputs.append(np.sum(output['symptomaticByAge_8']))
    ax.bar(y_pos, outputs, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    # plt.ylim(1200000, 1400000)
    ax.xaxis.set_ticks_position('none')
    # ax.set_ylabel('Number')
    # ax.set_title('Formal Child Care (2020-2040)')
    fig.tight_layout()
    path = os.path.join(folder, 'symptomaticByAgeClassBarChart.pdf')
    pp = PdfPages(path)
    pp.savefig(fig)
    pp.close()
    
    # 5 - Deaths
    
    fig, ax = plt.subplots()
    objects = ('Q1', 'Q2', 'Q3', 'Q4', 'Q5')
    y_pos = np.arange(len(objects))
    outputs = []
    outputs.append(np.sum(output['deathsByClass_0']))
    outputs.append(np.sum(output['deathsByClass_1']))
    outputs.append(np.sum(output['deathsByClass_2']))
    outputs.append(np.sum(output['deathsByClass_3']))
    outputs.append(np.sum(output['deathsByClass_4']))
    ax.bar(y_pos, outputs, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    # plt.ylim(1200000, 1400000)
    ax.xaxis.set_ticks_position('none')
    # ax.set_ylabel('Total hours')
    # ax.set_title('Formal Child Care (2020-2040)')
    fig.tight_layout()
    path = os.path.join(folder, 'deathsByQuintilesBarChart.pdf')
    pp = PdfPages(path)
    pp.savefig(fig)
    pp.close()
    
    fig, ax = plt.subplots()
    objects = ('0-10', '10-20', '20-30', '30-40', '40-50', '50-60', '60-70', '70-80', '80+')
    y_pos = np.arange(len(objects))
    outputs = []
    outputs.append(np.sum(output['deathsByAge_0']))
    outputs.append(np.sum(output['deathsByAge_1']))
    outputs.append(np.sum(output['deathsByAge_2']))
    outputs.append(np.sum(output['deathsByAge_3']))
    outputs.append(np.sum(output['deathsByAge_4']))
    outputs.append(np.sum(output['deathsByAge_5']))
    outputs.append(np.sum(output['deathsByAge_6']))
    outputs.append(np.sum(output['deathsByAge_7']))
    outputs.append(np.sum(output['deathsByAge_8']))
    ax.bar(y_pos, outputs, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    # plt.ylim(1200000, 1400000)
    ax.xaxis.set_ticks_position('none')
    # ax.set_ylabel('Number')
    # ax.set_title('Formal Child Care (2020-2040)')
    fig.tight_layout()
    path = os.path.join(folder, 'deathsByAgeClassBarChart.pdf')
    pp = PdfPages(path)
    pp.savefig(fig)
    pp.close()
    
    
    fig, ax = plt.subplots()
    p1, = ax.plot(output['day'], output['q1_hospitalized'], linewidth = 2, label = 'Q1')
    p2, = ax.plot(output['day'], output['q2_hospitalized'], linewidth = 2, label = 'Q2')
    p3, = ax.plot(output['day'], output['q3_hospitalized'], linewidth = 2, label = 'Q3')
    p4, = ax.plot(output['day'], output['q4_hospitalized'], linewidth = 2, label = 'Q4')
    p5, = ax.plot(output['day'], output['q5_hospitalized'], linewidth = 2, label = 'Q5')
    # ax.set_xlim(left = p['statsCollectFrom'])
    ax.set_ylabel('Number of hospitalized')
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    # ax.set_xlabel('day')
    handles, labels = ax.get_legend_handles_labels()
    ax.legend(loc = 'upper right')
    # ax.set_title('Total Delivered and Unmet Care')
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    # plt.xlim(p['statsCollectFrom'], p['endday'])
    # plt.ylim(0, 25)
    # plt.xticks(range(int(p['statsCollectFrom']), int(p['endday']+1), 20))
    fig.tight_layout()
    path = os.path.join(folder, 'hospitalizedByQuintile.pdf')
    pp = PdfPages(path)
    pp.savefig(fig)
    pp.close()
    
    
    
    fig, ax = plt.subplots()
    p1, = ax.plot(output['day'], output['q1_intubated'], linewidth = 2, label = 'Q1')
    p2, = ax.plot(output['day'], output['q2_intubated'], linewidth = 2, label = 'Q2')
    p3, = ax.plot(output['day'], output['q3_intubated'], linewidth = 2, label = 'Q3')
    p4, = ax.plot(output['day'], output['q4_intubated'], linewidth = 2, label = 'Q4')
    p5, = ax.plot(output['day'], output['q5_intubated'], linewidth = 2, label = 'Q5')
    # ax.set_xlim(left = p['statsCollectFrom'])
    ax.set_ylabel('Number in ICU')
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    # ax.set_xlabel('day')
    handles, labels = ax.get_legend_handles_labels()
    ax.legend(loc = 'upper right')
    # ax.set_title('Total Delivered and Unmet Care')
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    # plt.xlim(p['statsCollectFrom'], p['endday'])
    # plt.ylim(0, 25)
    # plt.xticks(range(int(p['statsCollectFrom']), int(p['endday']+1), 20))
    fig.tight_layout()
    path = os.path.join(folder, 'intubatedByQuintile.pdf')
    pp = PdfPages(path)
    pp.savefig(fig)
    pp.close()
    
    
    
    fig, ax = plt.subplots()
    p1, = ax.plot(output['day'], output['totalInformalSocialCare'], color="red", linewidth = 2)
    # ax.set_xlim(left = p['statsCollectFrom'])
    ax.set_ylabel('Hours per week')
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    # ax.set_xlabel('day')
    # handles, labels = ax.get_legend_handles_labels()
    # ax.legend(loc = 'lower left')
    # ax.set_title('Total informal care')
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    # plt.xlim(p['statsCollectFrom'], p['endday'])
    # plt.ylim(0, 25)
    # plt.xticks(range(int(p['statsCollectFrom']), int(p['endday']+1), 20))
    fig.tight_layout()
    path = os.path.join(folder, 'totalInformalCare.pdf')
    pp = PdfPages(path)
    pp.savefig(fig)
    pp.close()
    
    
    fig, ax = plt.subplots() # Argument: figsize=(5, 3)
    p1, = ax.plot(output['day'], output['totalInformalSocialCare'], color="red", linewidth = 2)
    ax.set_ylabel('Hours per week')
    # ax.set_title('Cost of out-of-work social care')
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    # ax.set_xlim(left = int(p['statsCollectFrom']), right = int(p['endday']))
    # ax.set_xticks(range(int(p['statsCollectFrom']), int(p['endday'])+1, 20))
    fig.tight_layout()
    path = os.path.join(folder, 'totalInformalSocialCare.pdf')
    pp = PdfPages(path)
    pp.savefig(fig)
    pp.close()
    
    n_groups = p['numberClasses']
    meanInformalCareReceived_1 = np.mean(output['q1_informalSocialCare'])
    meanFormalCareReceived_1 = np.mean(output['q1_formalSocialCare'])
    meanUnmetNeed_1 = np.mean(output['q1_unmetSocialCareNeed'])
    meanInformalCareReceived_2 = np.mean(output['q2_informalSocialCare'])
    meanFormalCareReceived_2 = np.mean(output['q2_formalSocialCare'])
    meanUnmetNeed_2 = np.mean(output['q2_unmetSocialCareNeed'])
    meanInformalCareReceived_3 = np.mean(output['q3_informalSocialCare'])
    meanFormalCareReceived_3 = np.mean(output['q3_formalSocialCare'])
    meanUnmetNeed_3 = np.mean(output['q3_unmetSocialCareNeed'])
    meanInformalCareReceived_4 = np.mean(output['q4_informalSocialCare'])
    meanFormalCareReceived_4 = np.mean(output['q4_formalSocialCare'])
    meanUnmetNeed_4 = np.mean(output['q4_unmetSocialCareNeed'])
    meanInformalCareReceived_5 = np.mean(output['q5_informalSocialCare'])
    meanFormalCareReceived_5 = np.mean(output['q5_formalSocialCare'])
    meanUnmetNeed_5 = np.mean(output['q5_unmetSocialCareNeed'])
    informalCare = (meanInformalCareReceived_1, meanInformalCareReceived_2, meanInformalCareReceived_3,
                    meanInformalCareReceived_4, meanInformalCareReceived_5)
    formalCare = (meanFormalCareReceived_1, meanFormalCareReceived_2, meanFormalCareReceived_3,
                  meanFormalCareReceived_4, meanFormalCareReceived_5)
    
    sumInformalFormalCare = [x + y for x, y in zip(informalCare, formalCare)]
    unmetNeeds = (meanUnmetNeed_1, meanUnmetNeed_2, meanUnmetNeed_3, meanUnmetNeed_4, meanUnmetNeed_5)
    ind = np.arange(n_groups)    # the x locations for the groups
    width = 0.4       # the width of the bars: can also be len(x) sequence
    
    fig, ax = plt.subplots()
    p1 = ax.bar(ind, informalCare, width, label = 'Informal Care')
    p2 = ax.bar(ind, formalCare, width, bottom = informalCare, label = 'Formal Care')
    p3 = ax.bar(ind, unmetNeeds, width, bottom = sumInformalFormalCare, label = 'Unmet Care Needs')
    ax.set_ylabel('Hours per week')
    ax.set_xticks(ind)
    plt.xticks(ind, ('I', 'II', 'III', 'IV', 'V'), fontsize = 12)
    handles, labels = ax.get_legend_handles_labels()
    ax.legend(loc = 'lower left')
    ax.yaxis.label.set_fontsize(12)
    # ax.set_title('Informal, Formal and Unmet Social Care Need per Recipient')
    fig.tight_layout()
    path = os.path.join(folder, 'SocialCarePerRecipientByClassStackedBarChart.pdf')
    pp = PdfPages(path)
    pp.savefig(fig)
    pp.close()
    
    fig, ax = plt.subplots() # Argument: figsize=(5, 3)
    p1, = ax.plot(output['day'], output['costPublicSocialCare'], color="red", linewidth = 2)
    ax.set_ylabel('Pounds per week')
    # ax.set_title('Cost of Public Social Care')
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    # ax.set_xlim(left = int(p['statsCollectFrom']), right = int(p['endday']))
    # ax.set_xticks(range(int(p['statsCollectFrom']), int(p['endday'])+1, 20))
    fig.tight_layout()
    path = os.path.join(folder, 'costPublicSocialCare.pdf')
    pp = PdfPages(path)
    pp.savefig(fig)
    pp.close()
    
    fig, ax = plt.subplots() # Argument: figsize=(5, 3)
    p1, = ax.plot(output['day'], output['sharePublicSocialCare'], color="red", linewidth = 2)
    ax.set_ylabel('Public Social Care (share)')
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    # ax.set_xlim(left = int(p['statsCollectFrom']), right = int(p['endday']))
    # ax.set_xticks(range(int(p['statsCollectFrom']), int(p['endday'])+1, 20))
    fig.tight_layout()
    path = os.path.join(folder, 'sharePublicSocialCare.pdf')
    pp = PdfPages(path)
    pp.savefig(fig)
    pp.close()
    
    fig, ax = plt.subplots() # Argument: figsize=(5, 3)
    p1, = ax.plot(output['day'], output['publicChildCare'], color="red", linewidth = 2)
    ax.set_ylabel('Public Child Care (hours per week)')
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    # ax.set_xlim(left = int(p['statsCollectFrom']), right = int(p['endday']))
    # ax.set_xticks(range(int(p['statsCollectFrom']), int(p['endday'])+1, 20))
    fig.tight_layout()
    path = os.path.join(folder, 'publicChildCare.pdf')
    pp = PdfPages(path)
    pp.savefig(fig)
    pp.close()
    
    fig, ax = plt.subplots() # Argument: figsize=(5, 3)
    p1, = ax.plot(output['day'], output['publicChildCare'], color="red", linewidth = 2)
    p2, = ax.plot(output['day'], output['publicSocialCare'], color="blue", linewidth = 2)
    ax.set_ylabel('Hours per week')
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    # ax.set_xlim(left = int(p['statsCollectFrom']), right = int(p['endday']))
    # ax.set_xticks(range(int(p['statsCollectFrom']), int(p['endday'])+1, 20))
    fig.tight_layout()
    path = os.path.join(folder, 'publicSocialAndChildCare.pdf')
    pp = PdfPages(path)
    pp.savefig(fig)
    pp.close()
    
    fig, ax = plt.subplots() # Argument: figsize=(5, 3)
    p1, = ax.plot(output['day'], output['sharePublicChildCare'], color="red", linewidth = 2)
    ax.set_ylabel('Public Child Care (share)')
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    # ax.set_xlim(left = int(p['statsCollectFrom']), right = int(p['endday']))
    # ax.set_xticks(range(int(p['statsCollectFrom']), int(p['endday'])+1, 20))
    fig.tight_layout()
    path = os.path.join(folder, 'sharePublicChildCare.pdf')
    pp = PdfPages(path)
    pp.savefig(fig)
    pp.close()
    
    fig, ax = plt.subplots() # Argument: figsize=(5, 3)
    p1, = ax.plot(output['day'], output['employmentRate'], color="red", linewidth = 2)
    ax.set_ylabel('Employment Rate')
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    # ax.set_xlim(left = int(p['statsCollectFrom']), right = int(p['endday']))
    # ax.set_xticks(range(int(p['statsCollectFrom']), int(p['endday'])+1, 20))
    fig.tight_layout()
    path = os.path.join(folder, 'employmentRate.pdf')
    pp = PdfPages(path)
    pp.savefig(fig)
    pp.close()
    
    fig, ax = plt.subplots() # Argument: figsize=(5, 3)
    p1, = ax.plot(output['day'], output['shareWorkingHours'], color="red", linewidth = 2)
    ax.set_ylabel('Working time (share)')
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    # ax.set_xlim(left = int(p['statsCollectFrom']), right = int(p['endday']))
    # ax.set_xticks(range(int(p['statsCollectFrom']), int(p['endday'])+1, 20))
    fig.tight_layout()
    path = os.path.join(folder, 'shareWorkingHours.pdf')
    pp = PdfPages(path)
    pp.savefig(fig)
    pp.close()
    
#    share_1 = output.loc[output['day'] == p['outputDay'], 'classShare_1'].values[0]
#    share_2 = output.loc[output['day'] == p['outputDay'], 'classShare_2'].values[0]
#    share_3 = output.loc[output['day'] == p['outputDay'], 'classShare_3'].values[0]
#    share_4 = output.loc[output['day'] == p['outputDay'], 'classShare_4'].values[0]
#    share_5 = output.loc[output['day'] == p['outputDay'], 'classShare_5'].values[0]
#    fig, ax = plt.subplots()
#    objects = ('SES I', 'SES II', 'SES III', 'SES IV', 'SES V')
#    y_pos = np.arange(len(objects))
#    shares = [share_1, share_2, share_3, share_4, share_5]
#    ax.bar(y_pos, shares, align='center', alpha=0.5)
#    ax.set_xticks(np.arange(len(objects)))
#    ax.set_xticklabels(objects)
#    ax.xaxis.set_ticks_position('none')
#    ax.set_ylabel('SES Shares')
#    # ax.set_title('Population SES Shares')
#    fig.tight_layout()
#    path = os.path.join(folder, 'sharesClasses.pdf')
#    pp = PdfPages(path)
#    pp.savefig(fig)
#    pp.close()
    
    fig, ax = plt.subplots() # Argument: figsize=(5, 3)
    p1, = ax.plot(output['day'], output['shareCareGivers'], color="red", linewidth = 2)
    ax.set_ylabel('Care Givers (share)')
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    # ax.set_xlim(left = int(p['statsCollectFrom']), right = int(p['endday']))
    # ax.set_xticks(range(int(p['statsCollectFrom']), int(p['endday'])+1, 20))
    fig.tight_layout()
    path = os.path.join(folder, 'shareCareGivers.pdf')
    pp = PdfPages(path)
    pp.savefig(fig)
    pp.close()
    
    fig, ax = plt.subplots() # Argument: figsize=(5, 3)
    p1, = ax.plot(output['day'], output['ratioFemaleMaleCarers'], color="red", linewidth = 2)
    ax.set_ylabel('Ratio female/male carers')
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    # ax.set_xlim(left = int(p['statsCollectFrom']), right = int(p['endday']))
    # ax.set_xticks(range(int(p['statsCollectFrom']), int(p['endday'])+1, 20))
    fig.tight_layout()
    path = os.path.join(folder, 'ratioFemaleMaleCarers.pdf')
    pp = PdfPages(path)
    pp.savefig(fig)
    pp.close()
    
    fig, ax = plt.subplots() # Argument: figsize=(5, 3)
    p1, = ax.plot(output['day'], output['shareMaleCarers'], label = 'Males', linewidth = 2)
    p2, = ax.plot(output['day'], output['shareFemaleCarers'], label = 'Females', linewidth = 2)
    # ax.set_title('Care Givers by Gender (share)')
    ax.set_ylabel('Shares of Population')
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    # ax.set_xlim(left = int(p['statsCollectFrom']), right = int(p['endday']))
    # ax.set_xticks(range(int(p['statsCollectFrom']), int(p['endday'])+1, 20))
    fig.tight_layout()
    path = os.path.join(folder, 'shareCareGiversByGender.pdf')
    pp = PdfPages(path)
    pp.savefig(fig)
    pp.close()
    
    fig, ax = plt.subplots() # Argument: figsize=(5, 3)
    p1, = ax.plot(output['day'], output['ratioWage'], color="red", linewidth = 2)
    ax.set_ylabel('Ratio female/male wage')
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    # ax.set_xlim(left = int(p['statsCollectFrom']), right = int(p['endday']))
    # ax.set_xticks(range(int(p['statsCollectFrom']), int(p['endday'])+1, 20))
    fig.tight_layout()
    path = os.path.join(folder, 'ratioFemaleMaleWage.pdf')
    pp = PdfPages(path)
    pp.savefig(fig)
    pp.close()
    
    fig, ax = plt.subplots() # Argument: figsize=(5, 3)
    p1, = ax.plot(output['day'], output['ratioIncome'], color="red", linewidth = 2)
    ax.set_ylabel('Ratio female/male Income')
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    # ax.set_xlim(left = int(p['statsCollectFrom']), right = int(p['endday']))
    # ax.set_xticks(range(int(p['statsCollectFrom']), int(p['endday'])+1, 20))
    fig.tight_layout()
    path = os.path.join(folder, 'ratioFemaleMaleIncome.pdf')
    pp = PdfPages(path)
    pp.savefig(fig)
    pp.close()
    
    fig, ax = plt.subplots() # Argument: figsize=(5, 3)
    p1, = ax.plot(output['day'], output['shareFamilyCarer'], color="red", linewidth = 2)
    ax.set_ylabel('Carer within family (share)')
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    # ax.set_xlim(left = int(p['statsCollectFrom']), right = int(p['endday']))
    # ax.set_xticks(range(int(p['statsCollectFrom']), int(p['endday'])+1, 20))
    fig.tight_layout()
    path = os.path.join(folder, 'shareFamilyCarer.pdf')
    pp = PdfPages(path)
    pp.savefig(fig)
    pp.close()
    
    fig, ax = plt.subplots() # Argument: figsize=(5, 3)
    p1, = ax.plot(output['day'], output['averageHoursOfCare'], color="red", linewidth = 2)
    ax.set_ylabel('Hours of care (average)')
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    # ax.set_xlim(left = int(p['statsCollectFrom']), right = int(p['endday']))
    # ax.set_xticks(range(int(p['statsCollectFrom']), int(p['endday'])+1, 20))
    fig.tight_layout()
    path = os.path.join(folder, 'averageHoursOfCare.pdf')
    pp = PdfPages(path)
    pp.savefig(fig)
    pp.close()
    
#    fig, ax = plt.subplots() # Argument: figsize=(5, 3)
#    p1, = ax.plot(output['day'], output['classShare_1'], color="red", linewidth = 2)
#    ax.set_ylabel('Share of Population')
#    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
#    # ax.set_xlim(left = int(p['statsCollectFrom']), right = int(p['endday']))
#    # ax.set_xticks(range(int(p['statsCollectFrom']), int(p['endday'])+1, 20))
#    fig.tight_layout()
#    path = os.path.join(folder, 'classShare_1.pdf')
#    pp = PdfPages(path)
#    pp.savefig(fig)
#    pp.close()
    
    fig, ax = plt.subplots() # Argument: figsize=(5, 3)
    p1, = ax.plot(output['day'], output['totalSocialCareNeed'], color="red", linewidth = 2)
    ax.set_ylabel('Social care needs (hours/week)')
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    # ax.set_xlim(left = int(p['statsCollectFrom']), right = int(p['endday']))
    # ax.set_xticks(range(int(p['statsCollectFrom']), int(p['endday'])+1, 20))
    fig.tight_layout()
    path = os.path.join(folder, 'totalSocialCareNeed.pdf')
    pp = PdfPages(path)
    pp.savefig(fig)
    pp.close()
    
    fig, ax = plt.subplots() # Argument: figsize=(5, 3)
    p1, = ax.plot(output['day'], output['mostLeastDeprivedRatio'], color="red", linewidth = 2)
    ax.set_ylabel('Q1/Q5 Ratio')
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    # ax.set_xlim(left = int(p['statsCollectFrom']), right = int(p['endday']))
    # ax.set_xticks(range(int(p['statsCollectFrom']), int(p['endday'])+1, 20))
    fig.tight_layout()
    path = os.path.join(folder, 'mostLeastDeprivedRatio.pdf')
    pp = PdfPages(path)
    pp.savefig(fig)
    pp.close()
    
    fig, ax = plt.subplots() # Argument: figsize=(5, 3)
    p1, = ax.plot(output['day'], output['informalCareRatio'], color="red", linewidth = 2)
    ax.set_ylabel('Q1/Q5 Ratio')
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    # ax.set_xlim(left = int(p['statsCollectFrom']), right = int(p['endday']))
    # ax.set_xticks(range(int(p['statsCollectFrom']), int(p['endday'])+1, 20))
    fig.tight_layout()
    path = os.path.join(folder, 'informalCareRatio.pdf')
    pp = PdfPages(path)
    pp.savefig(fig)
    pp.close()
    
    fig, ax = plt.subplots() # Argument: figsize=(5, 3)
    p1, = ax.plot(output['day'], output['careNeedRatio'], color="red", linewidth = 2)
    ax.set_ylabel('Q1/Q5 Ratio')
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    # ax.set_xlim(left = int(p['statsCollectFrom']), right = int(p['endday']))
    # ax.set_xticks(range(int(p['statsCollectFrom']), int(p['endday'])+1, 20))
    fig.tight_layout()
    path = os.path.join(folder, 'careNeedRatio.pdf')
    pp = PdfPages(path)
    pp.savefig(fig)
    pp.close()
    
    fig, ax = plt.subplots() # Argument: figsize=(5, 3)
    p1, = ax.plot(output['day'], output['hospitalizedQuintilesRatio'], color="red", linewidth = 2)
    ax.set_ylabel('Q1/Q5 Ratio')
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    # ax.set_xlim(left = int(p['statsCollectFrom']), right = int(p['endday']))
    # ax.set_xticks(range(int(p['statsCollectFrom']), int(p['endday'])+1, 20))
    fig.tight_layout()
    path = os.path.join(folder, 'hospitalizedQuintilesRatio.pdf')
    pp = PdfPages(path)
    pp.savefig(fig)
    pp.close()
    
    fig, ax = plt.subplots() # Argument: figsize=(5, 3)
    p1, = ax.plot(output['day'], output['intubatedQuintilesRatio'], color="red", linewidth = 2)
    ax.set_ylabel('Q1/Q5 Ratio')
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    # ax.set_xlim(left = int(p['statsCollectFrom']), right = int(p['endday']))
    # ax.set_xticks(range(int(p['statsCollectFrom']), int(p['endday'])+1, 20))
    fig.tight_layout()
    path = os.path.join(folder, 'intubatedQuintilesRatio.pdf')
    pp = PdfPages(path)
    pp.savefig(fig)
    pp.close()
    
    fig, ax = plt.subplots() # Argument: figsize=(5, 3)
    p1, = ax.plot(output['day'], output['deathsQuintilesRatio'], color="red", linewidth = 2)
    ax.set_ylabel('Q1/Q5 Ratio')
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    # ax.set_xlim(left = int(p['statsCollectFrom']), right = int(p['endday']))
    # ax.set_xticks(range(int(p['statsCollectFrom']), int(p['endday'])+1, 20))
    fig.tight_layout()
    path = os.path.join(folder, 'deathsQuintilesRatio.pdf')
    pp = PdfPages(path)
    pp.savefig(fig)
    pp.close()
    
    
#    fig, ax = plt.subplots() # Argument: figsize=(5, 3)
#    averageCareNeed = []
#    for i in range(int(p['startday']), int(p['endday'])+1):
#        averageCareNeed.append(output.loc[output['day'] == i, 'totalSocialCareNeed'].values[0]/output.loc[output['day'] == i, 'currentPop'].values[0])
#    p1, = ax.plot(output['day'], averageCareNeed, color="red")
#    ax.set_ylabel('Hours of social care needs')
#    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
#    ax.set_xlim(left = int(p['statsCollectFrom']), right = int(p['endday']))
#    ax.set_xticks(range(int(p['statsCollectFrom']), int(p['endday'])+1, 20))
#    fig.tight_layout()
#    path = os.path.join(folder, 'averageSocialCareNeed.pdf')
#    pp = PdfPages(path)
#    pp.savefig(fig)
#    pp.close()
    
    
    fig, ax = plt.subplots() # Argument: figsize=(5, 3)
    p1, = ax.plot(output['day'], output['totalInformalSocialCare'], label = 'Informal Care', linewidth = 2)
    p2, = ax.plot(output['day'], output['totalFormalSocialCare'], label = 'Formal Care', linewidth = 2)
    # ax.set_title('Informal and Formal Social Care')
    ax.set_ylabel('Hours per week')
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    # ax.set_xlim(left = int(p['statsCollectFrom']), right = int(p['endday']))
    # ax.set_xticks(range(int(p['statsCollectFrom']), int(p['endday'])+1, 20))
    fig.tight_layout()
    path = os.path.join(folder, 'hoursInformalFormalSocialCare.pdf')
    pp = PdfPages(path)
    pp.savefig(fig)
    pp.close()
    
    fig, ax = plt.subplots() # Argument: figsize=(5, 3)
    p1, = ax.plot(output['day'], output['totalUnmetSocialCareNeed'], color="red", linewidth = 2)
    # ax.set_title('Informal and Formal Social Care')
    ax.set_ylabel('Hours per week')
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    # ax.set_xlim(left = int(p['statsCollectFrom']), right = int(p['endday']))
    # ax.set_xticks(range(int(p['statsCollectFrom']), int(p['endday'])+1, 20))
    fig.tight_layout()
    path = os.path.join(folder, 'hoursUnmetSocialCareNeed.pdf')
    pp = PdfPages(path)
    pp.savefig(fig)
    pp.close()
    
    
    fig, ax = plt.subplots() # Argument: figsize=(5, 3)
    p1, = ax.plot(output['day'], output['share_InformalSocialCare'], color="red", linewidth = 2)
    ax.set_ylabel('Informal social care (share)')
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    # ax.set_xlim(left = int(p['statsCollectFrom']), right = int(p['endday']))
    # ax.set_xticks(range(int(p['statsCollectFrom']), int(p['endday'])+1, 20))
    fig.tight_layout()
    path = os.path.join(folder, 'shareInformalSocialCare.pdf')
    pp = PdfPages(path)
    pp.savefig(fig)
    pp.close()
    
    fig, ax = plt.subplots() # Argument: figsize=(5, 3)
    p1, = ax.plot(output['day'], output['share_UnmetSocialCareNeed'], color="red", linewidth = 2)
    ax.set_ylabel('Unmet Social Care Need (share)')
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    # ax.set_xlim(left = int(p['statsCollectFrom']), right = int(p['endday']))
    # ax.set_xticks(range(int(p['statsCollectFrom']), int(p['endday'])+1, 20))
    fig.tight_layout()
    path = os.path.join(folder, 'shareUnmetSocialCareNeed.pdf')
    pp = PdfPages(path)
    pp.savefig(fig)
    pp.close()
    
    fig, ax = plt.subplots() # Argument: figsize=(5, 3)
    p1, = ax.plot(output['day'], output['q1_socialCareNeed'], label = 'Q1', linewidth = 2)
    p2, = ax.plot(output['day'], output['q2_socialCareNeed'], label = 'Q2', linewidth = 2)
    p3, = ax.plot(output['day'], output['q3_socialCareNeed'], label = 'Q3', linewidth = 2)
    p4, = ax.plot(output['day'], output['q4_socialCareNeed'], label = 'Q4', linewidth = 2)
    p5, = ax.plot(output['day'], output['q5_socialCareNeed'], label = 'Q5', linewidth = 2)
    # ax.set_title('Social Care Needs by Income Quintiles')
    handles, labels = ax.get_legend_handles_labels()
    ax.legend(loc = 'lower right')
    ax.set_ylabel('Hours per week')
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    # ax.set_xlim(left = int(p['statsCollectFrom']), right = int(p['endday']))
    # ax.set_xticks(range(int(p['statsCollectFrom']), int(p['endday'])+1, 20))
    fig.tight_layout()
    path = os.path.join(folder, 'socialCareNeedsByQuintiles.pdf')
    pp = PdfPages(path)
    pp.savefig(fig)
    pp.close()
    
    fig, ax = plt.subplots() # Argument: figsize=(5, 3)
    p1, = ax.plot(output['day'], output['q1_unmetSocialCareNeed'], label = 'Q1', linewidth = 2)
    p2, = ax.plot(output['day'], output['q2_unmetSocialCareNeed'], label = 'Q2', linewidth = 2)
    p3, = ax.plot(output['day'], output['q3_unmetSocialCareNeed'], label = 'Q3', linewidth = 2)
    p4, = ax.plot(output['day'], output['q4_unmetSocialCareNeed'], label = 'Q4', linewidth = 2)
    p5, = ax.plot(output['day'], output['q5_unmetSocialCareNeed'], label = 'Q5', linewidth = 2)
    # ax.set_title('Social Care Needs by Income Quintiles')
    handles, labels = ax.get_legend_handles_labels()
    ax.legend(loc = 'upper left')
    ax.set_ylabel('Hours per week')
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    # ax.set_xlim(left = int(p['statsCollectFrom']), right = int(p['endday']))
    # ax.set_xticks(range(int(p['statsCollectFrom']), int(p['endday'])+1, 20))
    fig.tight_layout()
    path = os.path.join(folder, 'unmetSocialCareNeedsByQuintiles.pdf')
    pp = PdfPages(path)
    pp.savefig(fig)
    pp.close()
    
    fig, ax = plt.subplots()
    objects = ('Q1', 'Q2', 'Q3', 'Q4', 'Q5')
    y_pos = np.arange(len(objects))
    outOfWorkCare = []
    outOfWorkCare.append(np.sum(output['q1_unmetSocialCareNeed']))
    outOfWorkCare.append(np.sum(output['q2_unmetSocialCareNeed']))
    outOfWorkCare.append(np.sum(output['q3_unmetSocialCareNeed']))
    outOfWorkCare.append(np.sum(output['q4_unmetSocialCareNeed']))
    outOfWorkCare.append(np.sum(output['q5_unmetSocialCareNeed']))
    ax.bar(y_pos, outOfWorkCare, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    # plt.ylim(1200000, 1400000)
    ax.xaxis.set_ticks_position('none')
    ax.set_ylabel('Total hours')
    # ax.set_title('Formal Child Care (2020-2040)')
    fig.tight_layout()
    path = os.path.join(folder, 'unmetSocialCareByHouseholdsQuintilesBarChart.pdf')
    pp = PdfPages(path)
    pp.savefig(fig)
    pp.close()
    
    
    fig, ax = plt.subplots()
    objects = ('Q1', 'Q2', 'Q3', 'Q4', 'Q5')
    y_pos = np.arange(len(objects))
    outputs = []
    outputs.append(np.sum(output['unmetSocialCareNeed_Q1']))
    outputs.append(np.sum(output['unmetSocialCareNeed_Q2']))
    outputs.append(np.sum(output['unmetSocialCareNeed_Q3']))
    outputs.append(np.sum(output['unmetSocialCareNeed_Q4']))
    outputs.append(np.sum(output['unmetSocialCareNeed_Q5']))
    ax.bar(y_pos, outputs, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    # plt.ylim(1200000, 1400000)
    ax.xaxis.set_ticks_position('none')
    ax.set_ylabel('Total hours')
    # ax.set_title('Formal Child Care (2020-2040)')
    fig.tight_layout()
    path = os.path.join(folder, 'unmetSocialCareByAgentsQuintilesBarChart.pdf')
    pp = PdfPages(path)
    pp.savefig(fig)
    pp.close()
    
    fig, ax = plt.subplots()
    objects = ('Q1', 'Q2', 'Q3', 'Q4', 'Q5')
    y_pos = np.arange(len(objects))
    outputs = []
    outputs.append(np.sum(output['totalInformalSocialCare_Q1']))
    outputs.append(np.sum(output['totalInformalSocialCare_Q2']))
    outputs.append(np.sum(output['totalInformalSocialCare_Q3']))
    outputs.append(np.sum(output['totalInformalSocialCare_Q4']))
    outputs.append(np.sum(output['totalInformalSocialCare_Q5']))
    ax.bar(y_pos, outputs, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    # plt.ylim(1200000, 1400000)
    ax.xaxis.set_ticks_position('none')
    ax.set_ylabel('Total hours')
    # ax.set_title('Formal Child Care (2020-2040)')
    fig.tight_layout()
    path = os.path.join(folder, 'totalInformalSocialCareByAgentsQuintilesBarChart.pdf')
    pp = PdfPages(path)
    pp.savefig(fig)
    pp.close()
    
    fig, ax = plt.subplots()
    objects = ('Q1', 'Q2', 'Q3', 'Q4', 'Q5')
    y_pos = np.arange(len(objects))
    outputs = []
    outputs.append(np.sum(output['totalSocialCareNeed_Q1']))
    outputs.append(np.sum(output['totalSocialCareNeed_Q2']))
    outputs.append(np.sum(output['totalSocialCareNeed_Q3']))
    outputs.append(np.sum(output['totalSocialCareNeed_Q4']))
    outputs.append(np.sum(output['totalSocialCareNeed_Q5']))
    ax.bar(y_pos, outputs, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    # plt.ylim(1200000, 1400000)
    ax.xaxis.set_ticks_position('none')
    ax.set_ylabel('Total hours')
    # ax.set_title('Formal Child Care (2020-2040)')
    fig.tight_layout()
    path = os.path.join(folder, 'totalSocialCareNeedByAgentsQuintilesBarChart.pdf')
    pp = PdfPages(path)
    pp.savefig(fig)
    pp.close()
    
    fig, ax = plt.subplots() # Argument: figsize=(5, 3)
    p1, = ax.plot(output['day'], output['q1_outOfWorkSocialCare'], label = 'Q1', linewidth = 2)
    p2, = ax.plot(output['day'], output['q2_outOfWorkSocialCare'], label = 'Q2', linewidth = 2)
    p3, = ax.plot(output['day'], output['q3_outOfWorkSocialCare'], label = 'Q3', linewidth = 2)
    p4, = ax.plot(output['day'], output['q4_outOfWorkSocialCare'], label = 'Q4', linewidth = 2)
    p5, = ax.plot(output['day'], output['q5_outOfWorkSocialCare'], label = 'Q5', linewidth = 2)
    # ax.set_title('Social Care Needs by Income Quintiles')
    handles, labels = ax.get_legend_handles_labels()
    ax.legend(loc = 'upper left')
    ax.set_ylabel('Hours per week')
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    # ax.set_xlim(left = int(p['statsCollectFrom']), right = int(p['endday']))
    # ax.set_xticks(range(int(p['statsCollectFrom']), int(p['endday'])+1, 20))
    fig.tight_layout()
    path = os.path.join(folder, 'outOfWorkCareByQuintiles.pdf')
    pp = PdfPages(path)
    pp.savefig(fig)
    pp.close()
    
    fig, ax = plt.subplots() # Argument: figsize=(5, 3)
    p1, = ax.plot(output['day'], output['q1_formalSocialCare'], label = 'Q1', linewidth = 2)
    p2, = ax.plot(output['day'], output['q2_formalSocialCare'], label = 'Q2', linewidth = 2)
    p3, = ax.plot(output['day'], output['q3_formalSocialCare'], label = 'Q3', linewidth = 2)
    p4, = ax.plot(output['day'], output['q4_formalSocialCare'], label = 'Q4', linewidth = 2)
    p5, = ax.plot(output['day'], output['q5_formalSocialCare'], label = 'Q5', linewidth = 2)
    # ax.set_title('Social Care Needs by Income Quintiles')
    handles, labels = ax.get_legend_handles_labels()
    ax.legend(loc = 'upper left')
    ax.set_ylabel('Hours per week')
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    # ax.set_xlim(left = int(p['statsCollectFrom']), right = int(p['endday']))
    # ax.set_xticks(range(int(p['statsCollectFrom']), int(p['endday'])+1, 20))
    fig.tight_layout()
    path = os.path.join(folder, 'formalCareByQuintiles.pdf')
    pp = PdfPages(path)
    pp.savefig(fig)
    pp.close()
    
    fig, ax = plt.subplots() # Argument: figsize=(5, 3)
    p1, = ax.plot(output['day'], output['totalCostOWSC'], color="red", linewidth = 2)
    ax.set_ylabel('Pounds per week')
    # ax.set_title('Cost of out-of-work social care')
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    # ax.set_xlim(left = int(p['statsCollectFrom']), right = int(p['endday']))
    # ax.set_xticks(range(int(p['statsCollectFrom']), int(p['endday'])+1, 20))
    fig.tight_layout()
    path = os.path.join(folder, 'outOfWorkSocialCareCost.pdf')
    pp = PdfPages(path)
    pp.savefig(fig)
    pp.close()
    
    fig, ax = plt.subplots() # Argument: figsize=(5, 3)
    p1, = ax.plot(output['day'], output['susceptibles'], color="red", linewidth = 2)
    ax.set_ylabel('Number')
    # ax.set_title('Cost of out-of-work social care')
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    # ax.set_xlim(left = int(p['statsCollectFrom']), right = int(p['endday']))
    # ax.set_xticks(range(int(p['statsCollectFrom']), int(p['endday'])+1, 20))
    fig.tight_layout()
    path = os.path.join(folder, 'susceptible.pdf')
    pp = PdfPages(path)
    pp.savefig(fig)
    pp.close()
    
    fig, ax = plt.subplots() # Argument: figsize=(5, 3)
    p1, = ax.plot(output['day'], output['exposed'], label = 'Exposed', color="red", linewidth = 2)
    p2, = ax.plot(output['day'], output['infectious'], label = 'Infectious', color="blue", linewidth = 2)
    ax.set_ylabel('Number')
    handles, labels = ax.get_legend_handles_labels()
    ax.legend(loc = 'upper right')
    # ax.set_title('Cost of out-of-work social care')
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    # ax.set_xlim(left = int(p['statsCollectFrom']), right = int(p['endday']))
    # ax.set_xticks(range(int(p['statsCollectFrom']), int(p['endday'])+1, 20))
    fig.tight_layout()
    path = os.path.join(folder, 'exposedInfectious.pdf')
    pp = PdfPages(path)
    pp.savefig(fig)
    pp.close()
    
    fig, ax = plt.subplots() # Argument: figsize=(5, 3)
    p1, = ax.plot(output['day'], output['recovered'], color="red", linewidth = 2)
    ax.set_ylabel('Number')
    # ax.set_title('Cost of out-of-work social care')
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    # ax.set_xlim(left = int(p['statsCollectFrom']), right = int(p['endday']))
    # ax.set_xticks(range(int(p['statsCollectFrom']), int(p['endday'])+1, 20))
    fig.tight_layout()
    path = os.path.join(folder, 'recovered.pdf')
    pp = PdfPages(path)
    pp.savefig(fig)
    pp.close()
    
    fig, ax = plt.subplots() # Argument: figsize=(5, 3)
    p1, = ax.plot(output['day'], output['totalDeaths'], color="red", linewidth = 2)
    ax.set_ylabel('Number')
    # ax.set_title('Cost of out-of-work social care')
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    # ax.set_xlim(left = int(p['statsCollectFrom']), right = int(p['endday']))
    # ax.set_xticks(range(int(p['statsCollectFrom']), int(p['endday'])+1, 20))
    fig.tight_layout()
    path = os.path.join(folder, 'totalDeaths.pdf')
    pp = PdfPages(path)
    pp.savefig(fig)
    pp.close()
    
    fig, ax = plt.subplots() # Argument: figsize=(5, 3)
    p1, = ax.plot(output['day'], output['hospitalPopulation'], color="red", linewidth = 2)
    ax.set_ylabel('Number')
    # ax.set_title('Cost of out-of-work social care')
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    # ax.set_xlim(left = int(p['statsCollectFrom']), right = int(p['endday']))
    # ax.set_xticks(range(int(p['statsCollectFrom']), int(p['endday'])+1, 20))
    fig.tight_layout()
    path = os.path.join(folder, 'hospitalPopulation.pdf')
    pp = PdfPages(path)
    pp.savefig(fig)
    pp.close()
    
    fig, ax = plt.subplots() # Argument: figsize=(5, 3)
    p1, = ax.plot(output['day'], output['icuPopulation'], color="red", linewidth = 2)
    ax.set_ylabel('Number')
    # ax.set_title('Cost of out-of-work social care')
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    # ax.set_xlim(left = int(p['statsCollectFrom']), right = int(p['endday']))
    # ax.set_xticks(range(int(p['statsCollectFrom']), int(p['endday'])+1, 20))
    fig.tight_layout()
    path = os.path.join(folder, 'icuPopulation.pdf')
    pp = PdfPages(path)
    pp.savefig(fig)
    pp.close()
    
    fig, ax = plt.subplots() # Argument: figsize=(5, 3)
    p1, = ax.plot(output['day'], output['deaths'], color="red", linewidth = 2)
    ax.set_ylabel('Number')
    # ax.set_title('Cost of out-of-work social care')
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    # ax.set_xlim(left = int(p['statsCollectFrom']), right = int(p['endday']))
    # ax.set_xticks(range(int(p['statsCollectFrom']), int(p['endday'])+1, 20))
    fig.tight_layout()
    path = os.path.join(folder, 'deaths.pdf')
    pp = PdfPages(path)
    pp.savefig(fig)
    pp.close()
    
    fig, ax = plt.subplots() # Argument: figsize=(5, 3)
    p1, = ax.plot(output['day'], output['hospitalized'], color="red", linewidth = 2) 
    ax.set_ylabel('Number')
    # plt.ylim(0, 30)
    # ax.set_title('Cost of out-of-work social care')
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    # ax.set_xlim(left = int(p['statsCollectFrom']), right = int(p['endday']))
    # ax.set_xticks(range(int(p['statsCollectFrom']), int(p['endday'])+1, 20))
    fig.tight_layout()
    path = os.path.join(folder, 'hospitalized.pdf')
    pp = PdfPages(path)
    pp.savefig(fig)
    pp.close()
    
    fig, ax = plt.subplots() # Argument: figsize=(5, 3)
    p1, = ax.plot(output['day'], output['intubated'], color="red", linewidth = 2)
    ax.set_ylabel('Number')
    # plt.ylim(0, 20)
    # ax.set_title('Cost of out-of-work social care')
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    # ax.set_xlim(left = int(p['statsCollectFrom']), right = int(p['endday']))
    # ax.set_xticks(range(int(p['statsCollectFrom']), int(p['endday'])+1, 20))
    fig.tight_layout()
    path = os.path.join(folder, 'intubated.pdf')
    pp = PdfPages(path)
    pp.savefig(fig)
    pp.close()
    
    
    fig, ax = plt.subplots() # Argument: figsize=(5, 3)
    p1, = ax.plot(output['day'], output['newCases'], color="red", linewidth = 2)
    ax.set_ylabel('Number')
    # plt.ylim(0, 20)
    # ax.set_title('Cost of out-of-work social care')
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    # ax.set_xlim(left = int(p['statsCollectFrom']), right = int(p['endday']))
    # ax.set_xticks(range(int(p['statsCollectFrom']), int(p['endday'])+1, 20))
    fig.tight_layout()
    path = os.path.join(folder, 'newCases.pdf')
    pp = PdfPages(path)
    pp.savefig(fig)
    pp.close()
    

def multiplePoliciesGraphs(output, scenarioFolder, p, numPolicies):
    
    folder = scenarioFolder + '/Graphs'
    if not os.path.exists(folder):
        os.makedirs(folder)
    
    # Add graphs across policies (within the same run/scenario)
    
    #############################  Population   #######################################
    
    fig, ax = plt.subplots() # Argument: figsize=(5, 3)
    graph = []
    for i in range(numPolicies):
        policyLabel = 'Benchmark'
        if i != 0:
            policyLabel = 'Policy ' + str(i)
        graph.append(ax.plot(output[i]['day'], output[i]['currentPop'], label = policyLabel, linewidth = 2))
    # ax.set_title('Populations')
    ax.set_ylabel('Number of people')
    # plt.ylim(0, 7000)
    handels, labels = ax.get_legend_handles_labels()
    ax.legend(loc = 'lower left')
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    # ax.set_xlim(left = int(p['statsCollectFrom']), right = int(p['endYear']))
    # ax.set_xticks(range(int(p['statsCollectFrom']), int(p['endYear'])+1, 20))
    fig.tight_layout()
    path = os.path.join(folder, 'popGrowth_axPol.pdf')
    pp = PdfPages(path)
    pp.savefig(fig)
    pp.close()
    
    
    fig, ax = plt.subplots() # Argument: figsize=(5, 3)
    graph = []
    for i in range(numPolicies):
        policyLabel = 'Benchmark'
        if i != 0:
            policyLabel = 'Policy ' + str(i)
        graph.append(ax.plot(output[i]['day'], output[i]['cumulatedHospitalizations'], label = policyLabel, linewidth = 2))
    # ax.set_title('Populations')
    ax.set_ylabel('Number of people')
    # plt.ylim(0, 7000)
    handels, labels = ax.get_legend_handles_labels()
    ax.legend(loc = 'lower left')
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    # ax.set_xlim(left = int(p['statsCollectFrom']), right = int(p['endYear']))
    # ax.set_xticks(range(int(p['statsCollectFrom']), int(p['endYear'])+1, 20))
    fig.tight_layout()
    path = os.path.join(folder, 'cumulatedHospitalizations_axPol.pdf')
    pp = PdfPages(path)
    pp.savefig(fig)
    pp.close()
    
    fig, ax = plt.subplots() # Argument: figsize=(5, 3)
    graph = []
    for i in range(numPolicies):
        policyLabel = 'Benchmark'
        if i != 0:
            policyLabel = 'Policy ' + str(i)
        graph.append(ax.plot(output[i]['day'], output[i]['hospitalPopulation'], label = policyLabel, linewidth = 2))
    # ax.set_title('Populations')
    ax.set_ylabel('Number of people')
    # plt.ylim(0, 7000)
    handels, labels = ax.get_legend_handles_labels()
    ax.legend(loc = 'lower left')
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    # ax.set_xlim(left = int(p['statsCollectFrom']), right = int(p['endYear']))
    # ax.set_xticks(range(int(p['statsCollectFrom']), int(p['endYear'])+1, 20))
    fig.tight_layout()
    path = os.path.join(folder, 'hospitalPopulation_axPol.pdf')
    pp = PdfPages(path)
    pp.savefig(fig)
    pp.close()
    
    fig, ax = plt.subplots() # Argument: figsize=(5, 3)
    graph = []
    for i in range(numPolicies):
        policyLabel = 'Benchmark'
        if i != 0:
            policyLabel = 'Policy ' + str(i)
        graph.append(ax.plot(output[i]['day'], output[i]['cumulatedICUs'], label = policyLabel, linewidth = 2))
    # ax.set_title('Populations')
    ax.set_ylabel('Number of people')
    # plt.ylim(0, 7000)
    handels, labels = ax.get_legend_handles_labels()
    ax.legend(loc = 'lower left')
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    # ax.set_xlim(left = int(p['statsCollectFrom']), right = int(p['endYear']))
    # ax.set_xticks(range(int(p['statsCollectFrom']), int(p['endYear'])+1, 20))
    fig.tight_layout()
    path = os.path.join(folder, 'cumulatedICUs_axPol.pdf')
    pp = PdfPages(path)
    pp.savefig(fig)
    pp.close()
    
    fig, ax = plt.subplots() # Argument: figsize=(5, 3)
    graph = []
    for i in range(numPolicies):
        policyLabel = 'Benchmark'
        if i != 0:
            policyLabel = 'Policy ' + str(i)
        graph.append(ax.plot(output[i]['day'], output[i]['icuPopulation'], label = policyLabel, linewidth = 2))
    # ax.set_title('Populations')
    ax.set_ylabel('Number of people')
    # plt.ylim(0, 7000)
    handels, labels = ax.get_legend_handles_labels()
    ax.legend(loc = 'lower left')
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    # ax.set_xlim(left = int(p['statsCollectFrom']), right = int(p['endYear']))
    # ax.set_xticks(range(int(p['statsCollectFrom']), int(p['endYear'])+1, 20))
    fig.tight_layout()
    path = os.path.join(folder, 'icuPopulation_axPol.pdf')
    pp = PdfPages(path)
    pp.savefig(fig)
    pp.close()
    
    # Pandemic charts
    
    fig, ax = plt.subplots() # Argument: figsize=(5, 3)
    graph = []
    for i in range(numPolicies):
        policyLabel = 'Benchmark'
        if i != 0:
            policyLabel = 'Policy ' + str(i)
        graph.append(ax.plot(output[i]['day'], output[i]['susceptibles'], label = policyLabel, linewidth = 2))
    # ax.set_title('Populations')
    ax.set_ylabel('Number')
    ax.set_title('Total susceptible')
    handels, labels = ax.get_legend_handles_labels()
    ax.legend(loc = 'lower left')
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    # ax.set_xlim(left = int(p['statsCollectFrom']), right = int(p['endday']))
    # ax.set_xticks(range(int(p['statsCollectFrom']), int(p['endday'])+1, 20))
    fig.tight_layout()
    path = os.path.join(folder, 'susceptible_axPol.pdf')
    pp = PdfPages(path)
    pp.savefig(fig)
    pp.close()
    
    fig, ax = plt.subplots() # Argument: figsize=(5, 3)
    graph = []
    for i in range(numPolicies):
        policyLabel = 'Benchmark'
        if i != 0:
            policyLabel = 'Policy ' + str(i)
        graph.append(ax.plot(output[i]['day'], output[i]['exposed'], label = policyLabel, linewidth = 2))
    ax.set_title('Total exposed')
    ax.set_ylabel('Number')
    # ax.set_ylim(0, 300)
    # ax.set_title('Cost of out-of-work social care')
    handels, labels = ax.get_legend_handles_labels()
    ax.legend(loc = 'upper right')
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    # ax.set_xlim(left = int(p['statsCollectFrom']), right = int(p['endday']))
    # ax.set_xticks(range(int(p['statsCollectFrom']), int(p['endday'])+1, 20))
    fig.tight_layout()
    path = os.path.join(folder, 'Exposed_axPol.pdf')
    pp = PdfPages(path)
    pp.savefig(fig)
    pp.close()
    
    fig, ax = plt.subplots() # Argument: figsize=(5, 3)
    graph = []
    for i in range(numPolicies):
        policyLabel = 'Benchmark'
        if i != 0:
            policyLabel = 'Policy ' + str(i)
        graph.append(ax.plot(output[i]['day'], output[i]['infectious'], label = policyLabel, linewidth = 2))
    ax.set_title('Total Infectious')
    ax.set_ylabel('Number')
    # ax.set_title('Cost of out-of-work social care')
    handels, labels = ax.get_legend_handles_labels()
    ax.legend(loc = 'upper right')
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    # ax.set_xlim(left = int(p['statsCollectFrom']), right = int(p['endday']))
    # ax.set_xticks(range(int(p['statsCollectFrom']), int(p['endday'])+1, 20))
    fig.tight_layout()
    path = os.path.join(folder, 'Infectious_axPol.pdf')
    pp = PdfPages(path)
    pp.savefig(fig)
    pp.close()
    
    fig, ax = plt.subplots() # Argument: figsize=(5, 3)
    graph = []
    for i in range(numPolicies):
        policyLabel = 'Benchmark'
        if i != 0:
            policyLabel = 'Policy ' + str(i)
        graph.append(ax.plot(output[i]['day'], output[i]['recovered'], label = policyLabel, linewidth = 2))
    ax.set_title('Total recovered')
    ax.set_ylabel('Number')
    # ax.set_title('Cost of out-of-work social care')
    handels, labels = ax.get_legend_handles_labels()
    ax.legend(loc = 'upper left')
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    # ax.set_xlim(left = int(p['statsCollectFrom']), right = int(p['endday']))
    # ax.set_xticks(range(int(p['statsCollectFrom']), int(p['endday'])+1, 20))
    fig.tight_layout()
    path = os.path.join(folder, 'recovered_axPol.pdf')
    pp = PdfPages(path)
    pp.savefig(fig)
    pp.close()
    
    fig, ax = plt.subplots() # Argument: figsize=(5, 3)
    graph = []
    for i in range(numPolicies):
        policyLabel = 'Benchmark'
        if i != 0:
            policyLabel = 'Policy ' + str(i)
        graph.append(ax.plot(output[i]['day'], output[i]['totalDeaths'], label = policyLabel, linewidth = 2))
    ax.set_title('Total Deaths')
    ax.set_ylabel('Number')
    ax.set_title('Total deaths')
    handels, labels = ax.get_legend_handles_labels()
    ax.legend(loc = 'upper left')
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    # ax.set_ylim(0, 60)
    # ax.set_xlim(left = int(p['statsCollectFrom']), right = int(p['endday']))
    # ax.set_xticks(range(int(p['statsCollectFrom']), int(p['endday'])+1, 20))
    fig.tight_layout()
    path = os.path.join(folder, 'totalDeaths_axPol.pdf')
    pp = PdfPages(path)
    pp.savefig(fig)
    pp.close()
    
    fig, ax = plt.subplots() # Argument: figsize=(5, 3)
    graph = []
    for i in range(numPolicies):
        policyLabel = 'Benchmark'
        if i != 0:
            policyLabel = 'Policy ' + str(i)
        graph.append(ax.plot(output[i]['day'], output[i]['hospitalized'], linewidth = 2, label = policyLabel))
    ax.set_title('Hospitalized')
    ax.set_ylabel('Number')
    ax.set_ylim(0, 250)
    # ax.set_title('Cost of out-of-work social care')
    handels, labels = ax.get_legend_handles_labels()
    ax.legend(loc = 'upper right')
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    # ax.set_xlim(left = int(p['statsCollectFrom']), right = int(p['endday']))
    # ax.set_xticks(range(int(p['statsCollectFrom']), int(p['endday'])+1, 20))
    fig.tight_layout()
    path = os.path.join(folder, 'hospitalized_axPol.pdf')
    pp = PdfPages(path)
    pp.savefig(fig)
    pp.close()
    
    fig, ax = plt.subplots() # Argument: figsize=(5, 3)
    graph = []
    for i in range(numPolicies):
        policyLabel = 'Benchmark'
        if i != 0:
            policyLabel = 'Policy ' + str(i)
        graph.append(ax.plot(output[i]['day'], output[i]['newCases'], linewidth = 2, label = policyLabel))
    ax.set_title('New cases')
    ax.set_ylabel('Number')
    ax.set_ylim(0, 50)
    # ax.set_title('Cost of out-of-work social care')
    handels, labels = ax.get_legend_handles_labels()
    ax.legend(loc = 'upper right')
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    # ax.set_xlim(left = int(p['statsCollectFrom']), right = int(p['endday']))
    # ax.set_xticks(range(int(p['statsCollectFrom']), int(p['endday'])+1, 20))
    fig.tight_layout()
    path = os.path.join(folder, 'newCases_axPol.pdf')
    pp = PdfPages(path)
    pp.savefig(fig)
    pp.close()
    
    fig, ax = plt.subplots() # Argument: figsize=(5, 3)
    graph = []
    for i in range(numPolicies):
        policyLabel = 'Benchmark'
        if i != 0:
            policyLabel = 'Policy ' + str(i)
        graph.append(ax.plot(output[i]['day'], output[i]['intubated'], label = policyLabel, linewidth = 2))
    ax.set_title('Intensive Care Patients')
    ax.set_ylabel('Number')
    ax.set_ylim(0, 80)
    # ax.set_title('Cost of out-of-work social care')
    handels, labels = ax.get_legend_handles_labels()
    ax.legend(loc = 'upper right')
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    # ax.set_xlim(left = int(p['statsCollectFrom']), right = int(p['endday']))
    # ax.set_xticks(range(int(p['statsCollectFrom']), int(p['endday'])+1, 20))
    fig.tight_layout()
    path = os.path.join(folder, 'icu_axPol.pdf')
    pp = PdfPages(path)
    pp.savefig(fig)
    pp.close()
    
    ########################### Share of Umnet Care Needs    #################################
    
    fig, ax = plt.subplots() # Argument: figsize=(5, 3)
    graph = []
    for i in range(numPolicies):
        policyLabel = 'Benchmark'
        if i != 0:
            policyLabel = 'Policy ' + str(i)
        graph.append(ax.plot(output[i]['day'], output[i]['share_UnmetSocialCareNeed'], label = policyLabel, linewidth = 2))
    ax.set_title('Unmet Social Care Needs (share)')
    ax.set_ylabel('Share of Unmet Social Care')
    handels, labels = ax.get_legend_handles_labels()
    ax.legend(loc = 'upper right')
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    # ax.set_xlim(left = int(p['statsCollectFrom']), right = int(p['endYear']))
    # ax.set_xticks(range(int(p['statsCollectFrom']), int(p['endYear'])+1, 20))
    fig.tight_layout()
    path = os.path.join(folder, 'shareUnmetSocialCareNeeds_axPol.pdf')
    pp = PdfPages(path)
    pp.savefig(fig)
    pp.close()
    
    fig, ax = plt.subplots() # Argument: figsize=(5, 3)
    graph = []
    for i in range(numPolicies):
        policyLabel = 'Benchmark'
        if i != 0:
            policyLabel = 'Policy ' + str(i)
        graph.append(ax.plot(output[i]['day'], output[i]['totalUnmetSocialCareNeed'], label = policyLabel, linewidth = 2))
    # ax.set_title('Unmet Social Care Needs')
    ax.set_ylabel('Hours per day')
    # ax.set_ylim(1950, 2300)
    handels, labels = ax.get_legend_handles_labels()
    ax.legend(loc = 'upper left')
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    formatter = ticker.ScalarFormatter(useMathText=True) #scientific notation
    formatter.set_scientific(True) 
    formatter.set_powerlimits((-1,1)) 
    ax.yaxis.set_major_formatter(formatter)
    # ax.set_xlim(left = int(p['statsCollectFrom']), right = int(p['endday']))
    # ax.set_xticks(range(int(p['statsCollectFrom']), int(p['endday'])+1, 20))
    fig.tight_layout()
    path = os.path.join(folder, 'totalUnmetSocialCareNeeds_axPol.pdf')
    pp = PdfPages(path)
    pp.savefig(fig)
    pp.close()

    fig, ax = plt.subplots() # Argument: figsize=(5, 3)
    graph = []
    for i in range(numPolicies):
        policyLabel = 'Benchmark'
        if i != 0:
            policyLabel = 'Policy ' + str(i)
        graph.append(ax.plot(output[i]['day'], output[i]['totalHospitalizationCost'], label = policyLabel, linewidth = 2))
    # ax.set_title('Hospitalization Cost')
    ax.set_ylabel('Pounds per day')
    handels, labels = ax.get_legend_handles_labels()
    ax.legend(loc = 'upper left')
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    formatter = ticker.ScalarFormatter(useMathText=True) #scientific notation
    formatter.set_scientific(True) 
    formatter.set_powerlimits((-1,1)) 
    ax.yaxis.set_major_formatter(formatter)
    # ax.set_xlim(left = int(p['statsCollectFrom']), right = int(p['endday']))
    # ax.set_xticks(range(int(p['statsCollectFrom']), int(p['endday'])+1, 20))
    fig.tight_layout()
    path = os.path.join(folder, 'hospitalizationCost_axPol.pdf')
    pp = PdfPages(path)
    pp.savefig(fig)
    pp.close()
    
    fig, ax = plt.subplots() # Argument: figsize=(5, 3)
    graph = []
    for i in range(numPolicies):
        policyLabel = 'Benchmark'
        if i != 0:
            policyLabel = 'Policy ' + str(i)
        graph.append(ax.plot(output[i]['day'], output[i]['totalOWSC'], label = policyLabel, linewidth = 2))
    # ax.set_title('Out-of-Work Care')
    ax.set_ylabel('Hours per day')
    handels, labels = ax.get_legend_handles_labels()
    ax.legend(loc = 'lower left')
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    # ax.set_xlim(left = int(p['statsCollectFrom']), right = int(p['endday']))
    # ax.set_xticks(range(int(p['statsCollectFrom']), int(p['endday'])+1, 20))
    fig.tight_layout()
    path = os.path.join(folder, 'outOfWorkCare_axPol.pdf')
    pp = PdfPages(path)
    pp.savefig(fig)
    pp.close()

    fig, ax = plt.subplots() # Argument: figsize=(5, 3)
    graph = []
    for i in range(numPolicies):
        policyLabel = 'Benchmark'
        if i != 0:
            policyLabel = 'Policy ' + str(i)
        graph.append(ax.plot(output[i]['day'], output[i]['publicSocialCare'], label = policyLabel, linewidth = 2))
    # ax.set_title('Amount of Public Social Care')
    ax.set_ylabel('Hours per week')
    handels, labels = ax.get_legend_handles_labels()
    ax.legend(loc = 'upper right')
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    # ax.set_xlim(left = int(p['statsCollectFrom']), right = int(p['endday']))
    # ax.set_xticks(range(int(p['statsCollectFrom']), int(p['endday'])+1, 20))
    fig.tight_layout()
    path = os.path.join(folder, 'publicSocialCare_axPol.pdf')
    pp = PdfPages(path)
    pp.savefig(fig)
    pp.close()
    
    fig, ax = plt.subplots() # Argument: figsize=(5, 3)
    graph = []
    for i in range(numPolicies):
        policyLabel = 'Benchmark'
        if i != 0:
            policyLabel = 'Policy ' + str(i)
        graph.append(ax.plot(output[i]['day'], output[i]['totalFormalSocialCare'], label = policyLabel, linewidth = 2))
    # ax.set_title('Amount of Formal Social Care')
    ax.set_ylabel('Hours per week')
    handels, labels = ax.get_legend_handles_labels()
    ax.legend(loc = 'upper left')
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    # ax.set_xlim(left = int(p['statsCollectFrom']), right = int(p['endday']))
    # ax.set_xticks(range(int(p['statsCollectFrom']), int(p['endday'])+1, 20))
    fig.tight_layout()
    path = os.path.join(folder, 'formalSocialCare_axPol.pdf')
    pp = PdfPages(path)
    pp.savefig(fig)
    pp.close()
    
    
    fig, ax = plt.subplots() # Argument: figsize=(5, 3)
    graph = []
    for i in range(numPolicies):
        policyLabel = 'Benchmark'
        if i != 0:
            policyLabel = 'Policy ' + str(i)
        graph.append(ax.plot(output[i]['day'], output[i]['shareInformalChildCare'], label = policyLabel, linewidth = 2))
    # ax.set_title('Share Informal Child Care')
    ax.set_ylabel('Share of child care')
    plt.ylim(0.6, 1.0)
    handels, labels = ax.get_legend_handles_labels()
    ax.legend(loc = 'upper left')
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    # ax.set_xlim(left = int(p['statsCollectFrom']), right = int(p['endday']))
    # ax.set_xticks(range(int(p['statsCollectFrom']), int(p['endday'])+1, 20))
    fig.tight_layout()
    path = os.path.join(folder, 'shareInformalChildCare_axPol.pdf')
    pp = PdfPages(path)
    pp.savefig(fig)
    pp.close()
    
    fig, ax = plt.subplots() # Argument: figsize=(5, 3)
    graph = []
    for i in range(numPolicies):
        policyLabel = 'Benchmark'
        if i != 0:
            policyLabel = 'Policy ' + str(i)
        graph.append(ax.plot(output[i]['day'], output[i]['share_InformalSocialCare'], label = policyLabel, linewidth = 2))
    # ax.set_title('Share Informal Child Care')
    ax.set_ylabel('Share of social care')
    handels, labels = ax.get_legend_handles_labels()
    ax.legend(loc = 'lower left')
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    # ax.set_xlim(left = int(p['statsCollectFrom']), right = int(p['endday']))
    # ax.set_xticks(range(int(p['statsCollectFrom']), int(p['endday'])+1, 20))
    fig.tight_layout()
    path = os.path.join(folder, 'shareInformalSocialCare_axPol.pdf')
    pp = PdfPages(path)
    pp.savefig(fig)
    pp.close()
    
    
    fig, ax = plt.subplots() # Argument: figsize=(5, 3)
    graph = []
    for i in range(numPolicies):
        policyLabel = 'Benchmark'
        if i != 0:
            policyLabel = 'Policy ' + str(i)
        graph.append(ax.plot(output[i]['day'], output[i]['totalInformalChildCare'], label = policyLabel, linewidth = 2))
    # ax.set_title('Share Informal Child Care')
    ax.set_ylabel('Hours per week')
    # ax.set_ylim(2100, 2600)
    handels, labels = ax.get_legend_handles_labels()
    ax.legend(loc = 'lower left')
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    formatter = ticker.ScalarFormatter(useMathText=True) #scientific notation
    formatter.set_scientific(True) 
    formatter.set_powerlimits((-1,1)) 
    ax.yaxis.set_major_formatter(formatter)
    # ax.set_xlim(left = int(p['statsCollectFrom']), right = int(p['endday']))
    # ax.set_xticks(range(int(p['statsCollectFrom']), int(p['endday'])+1, 20))
    fig.tight_layout()
    path = os.path.join(folder, 'informalChildCare_axPol.pdf')
    pp = PdfPages(path)
    pp.savefig(fig)
    pp.close()
    
    fig, ax = plt.subplots() # Argument: figsize=(5, 3)
    graph = []
    for i in range(numPolicies):
        policyLabel = 'Benchmark'
        if i != 0:
            policyLabel = 'Policy ' + str(i)
        graph.append(ax.plot(output[i]['day'], output[i]['totalInformalSocialCare'], label = policyLabel, linewidth = 2))
    # ax.set_title('Informal social care')
    ax.set_ylabel('Hours per day')
    handels, labels = ax.get_legend_handles_labels()
    ax.legend(loc = 'lower left')
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    formatter = ticker.ScalarFormatter(useMathText=True) #scientific notation
    formatter.set_scientific(True) 
    formatter.set_powerlimits((-1,1)) 
    ax.yaxis.set_major_formatter(formatter)
    # ax.set_xlim(left = int(p['statsCollectFrom']), right = int(p['endday']))
    # ax.set_xticks(range(int(p['statsCollectFrom']), int(p['endday'])+1, 20))
    fig.tight_layout()
    path = os.path.join(folder, 'informalSocialCare_axPol.pdf')
    pp = PdfPages(path)
    pp.savefig(fig)
    pp.close()
    
    
    
    fig, ax = plt.subplots() # Argument: figsize=(5, 3)
    graph = []
    for i in range(numPolicies):
        policyLabel = 'Benchmark'
        if i != 0:
            policyLabel = 'Policy ' + str(i)
        graph.append(ax.plot(output[i]['day'], output[i]['totalSocialCareNeed'], label = policyLabel, linewidth = 2))
    # ax.set_title('Total social care need')
    ax.set_ylabel('Hours per day')
    # ax.set_ylim(5100, 5500)
    handels, labels = ax.get_legend_handles_labels()
    ax.legend(loc = 'lower left')
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    formatter = ticker.ScalarFormatter(useMathText=True) #scientific notation
    formatter.set_scientific(True) 
    formatter.set_powerlimits((-1,1)) 
    ax.yaxis.set_major_formatter(formatter)
    # ax.set_xlim(left = int(p['statsCollectFrom']), right = int(p['endday']))
    # ax.set_xticks(range(int(p['statsCollectFrom']), int(p['endday'])+1, 20))
    fig.tight_layout()
    path = os.path.join(folder, 'totalSocialCareNeed_axPol.pdf')
    pp = PdfPages(path)
    pp.savefig(fig)
    pp.close()
    
    
    fig, ax = plt.subplots() # Argument: figsize=(5, 3)
    graph = []
    for i in range(numPolicies):
        policyLabel = 'Benchmark'
        if i != 0:
            policyLabel = 'Policy ' + str(i)
        graph.append(ax.plot(output[i]['day'], output[i]['formalChildCare'], label = policyLabel, linewidth = 2))
    # ax.set_title('Formal Child Care')
    ax.set_ylabel('Hours per week')
    handels, labels = ax.get_legend_handles_labels()
    ax.legend(loc = 'upper left')
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    formatter = ticker.ScalarFormatter(useMathText=True) #scientific notation
    formatter.set_scientific(True) 
    formatter.set_powerlimits((-1,1)) 
    ax.yaxis.set_major_formatter(formatter)
    # ax.set_xlim(left = int(p['statsCollectFrom']), right = int(p['endday']))
    # ax.set_xticks(range(int(p['statsCollectFrom']), int(p['endday'])+1, 20))
    fig.tight_layout()
    path = os.path.join(folder, 'formalChildCare_axPol.pdf')
    pp = PdfPages(path)
    pp.savefig(fig)
    pp.close()
    
    fig, ax = plt.subplots() # Argument: figsize=(5, 3)
    graph = []
    for i in range(numPolicies):
        policyLabel = 'Benchmark'
        if i != 0:
            policyLabel = 'Policy ' + str(i)
        graph.append(ax.plot(output[i]['day'], output[i]['sharePublicChildCare'], label = policyLabel, linewidth = 2))
    # ax.set_title('Share of Public Child  Care')
    ax.set_ylabel('Share of child care')
    handels, labels = ax.get_legend_handles_labels()
    ax.legend(loc = 'lower right')
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    ax.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))
    # ax.set_xlim(left = int(p['statsCollectFrom']), right = int(p['endday']))
    # ax.set_xticks(range(int(p['statsCollectFrom']), int(p['endday'])+1, 20))
    fig.tight_layout()
    path = os.path.join(folder, 'sharePublicChildCare_axPol.pdf')
    pp = PdfPages(path)
    pp.savefig(fig)
    pp.close()
    
    fig, ax = plt.subplots() # Argument: figsize=(5, 3)
    graph = []
    for i in range(numPolicies):
        policyLabel = 'Benchmark'
        if i != 0:
            policyLabel = 'Policy ' + str(i)
        graph.append(ax.plot(output[i]['day'], output[i]['shareWorkingHours'], label = policyLabel, linewidth = 2))
    # ax.set_title('Share of working time')
    ax.set_ylabel('Share of total working hours')
    handels, labels = ax.get_legend_handles_labels()
    ax.legend(loc = 'lower right')
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    ax.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))
    # ax.set_xlim(left = int(p['statsCollectFrom']), right = int(p['endday']))
    # ax.set_xticks(range(int(p['statsCollectFrom']), int(p['endday'])+1, 20))
    fig.tight_layout()
    path = os.path.join(folder, 'shareWorkingTime_axPol.pdf')
    pp = PdfPages(path)
    pp.savefig(fig)
    pp.close()
    
    fig, ax = plt.subplots() # Argument: figsize=(5, 3)
    graph = []
    for i in range(numPolicies):
        policyLabel = 'Benchmark'
        if i != 0:
            policyLabel = 'Policy ' + str(i)
        graph.append(ax.plot(output[i]['day'], output[i]['employmentRate'], label = policyLabel, linewidth = 2))
    # ax.set_title('Employment Rate')
    ax.set_ylabel('Employment Rate')
    handels, labels = ax.get_legend_handles_labels()
    ax.legend(loc = 'lower right')
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    ax.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))
    # ax.set_xlim(left = int(p['statsCollectFrom']), right = int(p['endday']))
    # ax.set_xticks(range(int(p['statsCollectFrom']), int(p['endday'])+1, 20))
    fig.tight_layout()
    path = os.path.join(folder, 'employmentRate_axPol.pdf')
    pp = PdfPages(path)
    pp.savefig(fig)
    pp.close()
    
    fig, ax = plt.subplots() # Argument: figsize=(5, 3)
    graph = []
    for i in range(numPolicies):
        policyLabel = 'Benchmark'
        if i != 0:
            policyLabel = 'Policy ' + str(i)
        c1 = output[i]['costTaxFreeChildCare']
        c2 = output[i]['costPublicChildCare']
        c3 = output[i]['costPublicSocialCare']
        c4 = output[i]['costTaxFreeSocialCare']
        policyCost = [sum(x) for x in zip(c1, c2, c3, c4)]
        graph.append(ax.plot(output[i]['day'], policyCost, label = policyLabel, linewidth = 2))
    # ax.set_title('Policy Cost')
    ax.set_ylabel('Pounds per day')
    handels, labels = ax.get_legend_handles_labels()
    ax.legend(loc = 'lower right')
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    formatter = ticker.ScalarFormatter(useMathText=True) #scientific notation
    formatter.set_scientific(True) 
    formatter.set_powerlimits((-1,1)) 
    ax.yaxis.set_major_formatter(formatter)
    # ax.set_xlim(left = int(p['statsCollectFrom']), right = int(p['endday']))
    # ax.set_xticks(range(int(p['statsCollectFrom']), int(p['endday'])+1, 20))
    fig.tight_layout()
    path = os.path.join(folder, 'directPolicyCost_axPol.pdf')
    pp = PdfPages(path)
    pp.savefig(fig)
    pp.close()
   
    fig, ax = plt.subplots()
    objects = ('Benchmark', 'P1', 'P2')
    y_pos = np.arange(len(objects))
    policyOutputs = []
    for i in range(numPolicies):
        policyOutputs.append(float(np.sum(output[i]['unmetSocialCareNeed_Q1']))/float(np.sum(output[i]['unmetSocialCareNeed_Q5'])))
    width = 0.6
    ax.bar(y_pos, policyOutputs, width, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    # plt.ylim(75000000, 85000000)
    ax.xaxis.set_ticks_position('none')
    ax.set_ylabel('Q1/Q5 Ratio')
    # ax.set_title('Formal Child Care (2020-2040)')
    fig.tight_layout()
    path = os.path.join(folder, 'mostLeastDeprivedRatioBarChart.pdf')
    pp = PdfPages(path)
    pp.savefig(fig)
    pp.close()
    
    fig, ax = plt.subplots()
    objects = ('Benchmark', 'P1', 'P2')
    y_pos = np.arange(len(objects))
    policyOutputs = []
    for i in range(numPolicies):
        policyOutputs.append(float(np.sum(output[i]['totalInformalSocialCare_Q1']))/float(np.sum(output[i]['totalInformalSocialCare_Q5']))) # [-policyDays:]
    width = 0.6
    ax.bar(y_pos, policyOutputs, width, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    # plt.ylim(75000000, 85000000)
    ax.xaxis.set_ticks_position('none')
    ax.set_ylabel('Q1/Q5 Ratio')
    # ax.set_title('Formal Child Care (2020-2040)')
    fig.tight_layout()
    path = os.path.join(folder, 'informalCareRatioBarChart.pdf')
    pp = PdfPages(path)
    pp.savefig(fig)
    pp.close()
    
    fig, ax = plt.subplots()
    objects = ('Benchmark', 'P1', 'P2')
    y_pos = np.arange(len(objects))
    policyOutputs = []
    for i in range(numPolicies):
        policyOutputs.append(float(np.sum(output[i]['totalSocialCareNeed_Q1']))/float(np.sum(output[i]['totalSocialCareNeed_Q5']))) # [-policyDays:]
    width = 0.6
    ax.bar(y_pos, policyOutputs, width, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    # plt.ylim(75000000, 85000000)
    ax.xaxis.set_ticks_position('none')
    ax.set_ylabel('Q1/Q5 Ratio')
    # ax.set_title('Formal Child Care (2020-2040)')
    fig.tight_layout()
    path = os.path.join(folder, 'careNeedRatioBarChart.pdf')
    pp = PdfPages(path)
    pp.savefig(fig)
    pp.close()
    
    fig, ax = plt.subplots()
    objects = ('Benchmark', 'P1', 'P2')
    y_pos = np.arange(len(objects))
    policyOutputs = []
    for i in range(numPolicies):
        policyOutputs.append(output[i]['hospitalizedQuintilesRatio'].iloc[-1]) # [-policyDays:]
    width = 0.6
    ax.bar(y_pos, policyOutputs, width, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    # plt.ylim(75000000, 85000000)
    ax.xaxis.set_ticks_position('none')
    ax.set_ylabel('Q1/Q5 Ratio')
    # ax.set_title('Formal Child Care (2020-2040)')
    fig.tight_layout()
    path = os.path.join(folder, 'hospitalizedQuintilesRatioBarChart.pdf')
    pp = PdfPages(path)
    pp.savefig(fig)
    pp.close()
    
    fig, ax = plt.subplots()
    objects = ('Benchmark', 'P1', 'P2')
    y_pos = np.arange(len(objects))
    policyOutputs = []
    for i in range(numPolicies):
        policyOutputs.append(output[i]['intubatedQuintilesRatio'].iloc[-1]) # [-policyDays:]
    width = 0.6
    ax.bar(y_pos, policyOutputs, width, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    # plt.ylim(75000000, 85000000)
    ax.xaxis.set_ticks_position('none')
    ax.set_ylabel('Q1/Q5 Ratio')
    # ax.set_title('Formal Child Care (2020-2040)')
    fig.tight_layout()
    path = os.path.join(folder, 'intubatedQuintilesRatioBarChart.pdf')
    pp = PdfPages(path)
    pp.savefig(fig)
    pp.close()
    
    fig, ax = plt.subplots()
    objects = ('Benchmark', 'P1', 'P2')
    y_pos = np.arange(len(objects))
    policyOutputs = []
    for i in range(numPolicies):
        policyOutputs.append(output[i]['deathsQuintilesRatio'].iloc[-1]) # [-policyDays:]
    width = 0.6
    ax.bar(y_pos, policyOutputs, width, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    # plt.ylim(75000000, 85000000)
    ax.xaxis.set_ticks_position('none')
    ax.set_ylabel('Q1/Q5 Ratio')
    # ax.set_title('Formal Child Care (2020-2040)')
    fig.tight_layout()
    path = os.path.join(folder, 'deathsQuintilesRatioBarChart.pdf')
    pp = PdfPages(path)
    pp.savefig(fig)
    pp.close()
    
    
    
    # Fig. 9: Bar charts of total unmet care need by Policy
    fig, ax = plt.subplots()
    objects = ('Benchmark', 'P1', 'P2')
    y_pos = np.arange(len(objects))
    outOfWorkCare = []
    for i in range(numPolicies):
        outOfWorkCare.append(np.sum(output[i]['totalHospitalizationCost'])) # [-policyDays:]
    width = 0.6
    ax.bar(y_pos, outOfWorkCare, width, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    # plt.ylim(75000000, 85000000)
    ax.xaxis.set_ticks_position('none')
    ax.set_ylabel('Pounds')
    formatter = ticker.ScalarFormatter(useMathText=True) #scientific notation
    formatter.set_scientific(True) 
    formatter.set_powerlimits((-1,1)) 
    ax.yaxis.set_major_formatter(formatter)
    # ax.set_title('Formal Child Care (2020-2040)')
    fig.tight_layout()
    path = os.path.join(folder, 'hospitalizationCostBarChart.pdf')
    pp = PdfPages(path)
    pp.savefig(fig)
    pp.close()
    
    
    # policyYears = int(p['endYear']-p['policyStartYear']) + 1
    # Fig. 9: Bar charts of total unmet care need by Policy
    fig, ax = plt.subplots()
    objects = ('Benchmark', 'P1', 'P2')
    y_pos = np.arange(len(objects))
    outOfWorkCare = []
    for i in range(numPolicies):
        outOfWorkCare.append(np.sum(output[i]['totalSocialCareNeed']))
    width = 0.6
    ax.bar(y_pos, outOfWorkCare, width, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    # plt.ylim(1200000, 1400000)
    ax.xaxis.set_ticks_position('none')
    ax.set_ylabel('Hours per week')
    formatter = ticker.ScalarFormatter(useMathText=True) #scientific notation
    formatter.set_scientific(True) 
    formatter.set_powerlimits((-1,1)) 
    ax.yaxis.set_major_formatter(formatter)
    # ax.set_title('Formal Child Care (2020-2040)')
    fig.tight_layout()
    path = os.path.join(folder, 'totalSocialCareNeedBarChart.pdf')
    pp = PdfPages(path)
    pp.savefig(fig)
    pp.close()
    
    # policyYears = int(p['endYear']-p['policyStartYear']) + 1
    # Fig. 9: Bar charts of total unmet care need by Policy
    fig, ax = plt.subplots()
    objects = ('Benchmark', 'P1', 'P2')
    y_pos = np.arange(len(objects))
    outOfWorkCare = []
    for i in range(numPolicies):
        outOfWorkCare.append(np.sum(output[i]['totalInformalSocialCare']))
    width = 0.6
    ax.bar(y_pos, outOfWorkCare, width, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    # plt.ylim(350000, 450000)
    ax.xaxis.set_ticks_position('none')
    ax.set_ylabel('Hours per week')
    formatter = ticker.ScalarFormatter(useMathText=True) #scientific notation
    formatter.set_scientific(True) 
    formatter.set_powerlimits((-1,1)) 
    ax.yaxis.set_major_formatter(formatter)
    # ax.set_title('Formal Child Care (2020-2040)')
    fig.tight_layout()
    path = os.path.join(folder, 'totalInformalCareNeedBarChart.pdf')
    pp = PdfPages(path)
    pp.savefig(fig)
    pp.close()
    
    # policyYears = int(p['endYear']-p['policyStartYear']) + 1
    # Fig. 9: Bar charts of total unmet care need by Policy
    fig, ax = plt.subplots()
    objects = ('Benchmark', 'P1', 'P2')
    y_pos = np.arange(len(objects))
    outOfWorkCare = []
    for i in range(numPolicies):
        outOfWorkCare.append(np.sum(output[i]['totalFormalSocialCare']))
    width = 0.6
    ax.bar(y_pos, outOfWorkCare, width, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    # plt.ylim(150000, 225000)
    ax.xaxis.set_ticks_position('none')
    ax.set_ylabel('Hours per week')
    formatter = ticker.ScalarFormatter(useMathText=True) #scientific notation
    formatter.set_scientific(True) 
    formatter.set_powerlimits((-1,1)) 
    ax.yaxis.set_major_formatter(formatter)
    # ax.set_title('Formal Child Care (2020-2040)')
    fig.tight_layout()
    path = os.path.join(folder, 'totalFormalCareNeedBarChart.pdf')
    pp = PdfPages(path)
    pp.savefig(fig)
    pp.close()
    
    # policyYears = int(p['endYear']-p['policyStartYear']) + 1
    # Fig. 9: Bar charts of total unmet care need by Policy
    fig, ax = plt.subplots()
    objects = ('Benchmark', 'P1', 'P2')
    y_pos = np.arange(len(objects))
    outOfWorkCare = []
    for i in range(numPolicies):
        outOfWorkCare.append(np.sum(output[i]['formalChildCare']))
    width = 0.6
    ax.bar(y_pos, outOfWorkCare, width, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    ax.xaxis.set_ticks_position('none')
    ax.set_ylabel('Hours per week')
    formatter = ticker.ScalarFormatter(useMathText=True) #scientific notation
    formatter.set_scientific(True) 
    formatter.set_powerlimits((-1,1)) 
    ax.yaxis.set_major_formatter(formatter)
    # ax.set_title('Formal Child Care (2020-2040)')
    fig.tight_layout()
    path = os.path.join(folder, 'formalChildCareBarChart.pdf')
    pp = PdfPages(path)
    pp.savefig(fig)
    pp.close()
    
    # policyYears = int(p['endYear']-p['policyStartYear']) + 1
    # Fig. 9: Bar charts of total unmet care need by Policy
    fig, ax = plt.subplots()
    objects = ('Benchmark', 'P1', 'P2')
    y_pos = np.arange(len(objects))
    outOfWorkCare = []
    for i in range(numPolicies):
        outOfWorkCare.append(np.sum(output[i]['totalOWSC']))
    width = 0.6
    ax.bar(y_pos, outOfWorkCare, width, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    ax.xaxis.set_ticks_position('none')
    ax.set_ylabel('Hours per week')
    # ax.set_title('Out-of-Work Social Care (2020-2040)')
    fig.tight_layout()
    path = os.path.join(folder, 'outOfWorkSocialCareBarChart.pdf')
    pp = PdfPages(path)
    pp.savefig(fig)
    pp.close()

    # policyYears = int(p['endYear']-p['policyStartYear']) + 1
    # Fig. 9: Bar charts of total unmet care need by Policy
    fig, ax = plt.subplots()
    objects = ('Benchmark', 'P1', 'P2')
    y_pos = np.arange(len(objects))
    shareUnmetCareDemand = []
    for i in range(numPolicies):
        shareUnmetCareDemand.append(np.sum(output[i]['totalUnmetSocialCareNeed']))
    width = 0.6
    ax.bar(y_pos, shareUnmetCareDemand, width, align='center', alpha=0.5)
    # plt.ylim(500000, 650000)
    plt.xticks(y_pos, objects)
    ax.xaxis.set_ticks_position('none')
    ax.set_ylabel('Hours of Unmet Care')
    formatter = ticker.ScalarFormatter(useMathText=True) #scientific notation
    formatter.set_scientific(True) 
    formatter.set_powerlimits((-1,1)) 
    ax.yaxis.set_major_formatter(formatter)
    # ax.set_title('Total Unmet Social Care Need')
    fig.tight_layout()
    path = os.path.join(folder, 'TotalUnmetCareNeedBarChart.pdf')
    pp = PdfPages(path)
    pp.savefig(fig)
    pp.close()
    
    # policyYears = int(p['endYear']-p['policyStartYear']) + 1
    # Fig. 9: Bar charts of total unmet care need by Policy
    fig, ax = plt.subplots()
    objects = ('Benchmark', 'P1', 'P2')
    y_pos = np.arange(len(objects))
    shareUnmetCareDemand = []
    for i in range(numPolicies):
        shareUnmetCareDemand.append(np.sum(output[i]['publicSocialCare']))
    width = 0.6
    ax.bar(y_pos, shareUnmetCareDemand, width, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    # plt.ylim(80000, 170000)
    ax.xaxis.set_ticks_position('none')
    ax.set_ylabel('Hours of Social Care')
    formatter = ticker.ScalarFormatter(useMathText=True) #scientific notation
    formatter.set_scientific(True) 
    formatter.set_powerlimits((-1,1)) 
    ax.yaxis.set_major_formatter(formatter)
    # ax.set_title('Total Unmet Social Care Need')
    fig.tight_layout()
    path = os.path.join(folder, 'publicSocialCareBarChart.pdf')
    pp = PdfPages(path)
    pp.savefig(fig)
    pp.close()
    
    
    fig, ax = plt.subplots()
    objects = ('Benchmark', 'P1', 'P2')
    y_pos = np.arange(len(objects))
    shareUnmetCareDemand = []
    for i in range(numPolicies):
        shareUnmetCareDemand.append(np.sum(output[i]['totalHospitalized']))
    width = 0.6
    ax.bar(y_pos, shareUnmetCareDemand, width, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    # plt.ylim(80000, 170000)
    ax.xaxis.set_ticks_position('none')
    ax.set_ylabel('Number Hospitalizations')
    formatter = ticker.ScalarFormatter(useMathText=True) #scientific notation
    formatter.set_scientific(True) 
    formatter.set_powerlimits((-1,1)) 
    ax.yaxis.set_major_formatter(formatter)
    # ax.set_title('Total Unmet Social Care Need')
    fig.tight_layout()
    path = os.path.join(folder, 'totalHospitalizedBarChart.pdf')
    pp = PdfPages(path)
    pp.savefig(fig)
    pp.close()
    
    
    # policyYears = int(p['endYear']-p['policyStartYear']) + 1
    # Fig. 9: Bar charts of total unmet care need by Policy
    fig, ax = plt.subplots()
    objects = ('Benchmark', 'P1', 'P2')
    y_pos = np.arange(len(objects))
    shareUnmetCareDemand = []
    for i in range(numPolicies):
        c1 = output[i]['costTaxFreeChildCare']
        c2 = output[i]['costPublicChildCare']
        c3 = output[i]['costPublicSocialCare']
        c4 = output[i]['costTaxFreeSocialCare']
        policyCost = [sum(x) for x in zip(c1, c2, c3, c4)]
        shareUnmetCareDemand.append(np.sum(policyCost))
    width = 0.6
    ax.bar(y_pos, shareUnmetCareDemand, width, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    ax.xaxis.set_ticks_position('none')
    ax.set_ylabel('Pounds per week')
    formatter = ticker.ScalarFormatter(useMathText=True) #scientific notation
    formatter.set_scientific(True) 
    formatter.set_powerlimits((-1,1)) 
    ax.yaxis.set_major_formatter(formatter)
    # ax.set_title('Total Policy Costs (2020-2040)')
    fig.tight_layout()
    path = os.path.join(folder, 'TotalPolicyCostBarChart.pdf')
    pp = PdfPages(path)
    pp.savefig(fig)
    pp.close()

   
def multipleScenariosGraphs(output, repFolder, p, numPolicies, numScenarios):
    
    folder = repFolder + '/Graphs'
    if not os.path.exists(folder):
        os.makedirs(folder)
        
    # Add graphs across scenarios (for the same policies)
    for j in range(numPolicies):
        fig, ax = plt.subplots() # Argument: figsize=(5, 3)
        graph = []
        for i in range(numScenarios):
            graph.append(ax.plot(output[i][j]['year'], output[i][j]['currentPop'], label = 'Scenario ' + str(i+1)))
        # p2, = ax.plot(output[1][0]['year'], output[1]['currentPop'], color="blue", label = 'Policy 1')
        ax.set_title('Populations - Policy ' + str(j))
        ax.set_ylabel('Number of people')
        handels, labels = ax.get_legend_handles_labels()
        ax.legend(loc = 'lower right')
        ax.xaxis.set_major_locator(MaxNLocator(integer=True))
        ax.set_xlim(left = int(p['statsCollectFrom']), right = int(p['endYear']))
        ax.set_xticks(range(int(p['statsCollectFrom']), int(p['endYear'])+1, 20))
        fig.tight_layout()
        path = os.path.join(folder, 'popGrowth_axScen_P' + str(j) + '.pdf')
        pp = PdfPages(path)
        pp.savefig(fig)
        pp.close()
        
    
    for j in range(numPolicies):
        fig, ax = plt.subplots() # Argument: figsize=(5, 3)
        graph = []
        for i in range(numScenarios):
            graph.append(ax.plot(output[i][j]['year'], output[i][j]['share_UnmetSocialCareNeed'], label = 'Scenario ' + str(i+1)))
        # p2, = ax.plot(output[1][0]['year'], output[1]['currentPop'], color="blue", label = 'Policy 1')
        ax.set_title('Unmet Care Needs - Policy ' + str(j))
        ax.set_ylabel('Unmet Care Needs (share)')
        handels, labels = ax.get_legend_handles_labels()
        ax.legend(loc = 'lower right')
        ax.xaxis.set_major_locator(MaxNLocator(integer=True))
        ax.set_xlim(left = int(p['statsCollectFrom']), right = int(p['endYear']))
        ax.set_xticks(range(int(p['statsCollectFrom']), int(p['endYear'])+1, 20))
        fig.tight_layout()
        path = os.path.join(folder, 'shareUnmetSocialCareNeeds_axScen_P' + str(j) + '.pdf')
        pp = PdfPages(path)
        pp.savefig(fig)
        pp.close()
    
    for j in range(numPolicies):
        fig, ax = plt.subplots() # Argument: figsize=(5, 3)
        graph = []
        for i in range(numScenarios):
            graph.append(ax.plot(output[i][j]['year'], output[i][j]['totalHospitalizationCost'], label = 'Scenario ' + str(i+1)))
        # p2, = ax.plot(output[1][0]['year'], output[1]['currentPop'], color="blue", label = 'Policy 1')
        ax.set_title('Hospitalization Cost - Policy ' + str(j))
        ax.set_ylabel('Punds per year')
        handels, labels = ax.get_legend_handles_labels()
        ax.legend(loc = 'lower right')
        ax.xaxis.set_major_locator(MaxNLocator(integer=True))
        ax.set_xlim(left = int(p['statsCollectFrom']), right = int(p['endYear']))
        ax.set_xticks(range(int(p['statsCollectFrom']), int(p['endYear'])+1, 20))
        fig.tight_layout()
        path = os.path.join(folder, 'hospitalizationCost_axScen_P' + str(j) + '.pdf')
        pp = PdfPages(path)
        pp.savefig(fig)
        pp.close()
    
    for j in range(numPolicies):
        fig, ax = plt.subplots() # Argument: figsize=(5, 3)
        graph = []
        for i in range(numScenarios):
            graph.append(ax.plot(output[i][j]['year'], output[i][j]['publicCare'], label = 'Scenario ' + str(i+1)))
        # p2, = ax.plot(output[1][0]['year'], output[1]['currentPop'], color="blue", label = 'Policy 1')
        ax.set_title('Amount of Public Care - Policy ' + str(j))
        ax.set_ylabel('Hours per week')
        handels, labels = ax.get_legend_handles_labels()
        ax.legend(loc = 'lower right')
        ax.xaxis.set_major_locator(MaxNLocator(integer=True))
        ax.set_xlim(left = int(p['statsCollectFrom']), right = int(p['endYear']))
        ax.set_xticks(range(int(p['statsCollectFrom']), int(p['endYear'])+1, 20))
        fig.tight_layout()
        path = os.path.join(folder, 'publicCare_axScen_P' + str(j) + '.pdf')
        pp = PdfPages(path)
        pp.savefig(fig)
        pp.close()
    
    for j in range(numPolicies):
        fig, ax = plt.subplots() # Argument: figsize=(5, 3)
        graph = []
        for i in range(numScenarios):
            graph.append(ax.plot(output[i][j]['year'], output[i][j]['employmentRate'], label = 'Scenario ' + str(i+1)))
        # p2, = ax.plot(output[1][0]['year'], output[1]['currentPop'], color="blue", label = 'Policy 1')
        ax.set_title('Employment Rate - Policy ' + str(j))
        ax.set_ylabel('Employment Rate')
        handels, labels = ax.get_legend_handles_labels()
        ax.legend(loc = 'lower right')
        ax.xaxis.set_major_locator(MaxNLocator(integer=True))
        ax.set_xlim(left = int(p['statsCollectFrom']), right = int(p['endYear']))
        ax.set_xticks(range(int(p['statsCollectFrom']), int(p['endYear'])+1, 20))
        fig.tight_layout()
        path = os.path.join(folder, 'employmentRate_axScen_P' + str(j) + '.pdf')
        pp = PdfPages(path)
        pp.savefig(fig)
        pp.close()
    

def multipleRepeatsGraphs(output, simFolder, p, numPolicies, numScenarios, numRepeats):
   
    folder = simFolder + '/MultiRepeat_Graphs'
   
    if not os.path.exists(folder):
        os.makedirs(folder)
    
    # Add graphs across runs (for the same scenario/policy combinations)
    # For each policy scenario, take the average of year 2010-2020 for each run, and do a bar chart with error bars for each outcome of interest
    
    # Policy comparison: make charts by outcomes with bars representing the different policies
    
    
    
    for i in range(numScenarios):
        
        scenarioFolder = folder + '/Scenario ' + str(i+1)
        if not os.path.exists(scenarioFolder):
            os.makedirs(scenarioFolder)
        
        # For each scenario, two folders are created:
        # - sigle-policy graphs
        # - multiple-policy graphs (for policy comparison)
        
        # In the folder 'SinglePolicyGraphs', there are three sub-folders, one for each policy.
        folder = scenarioFolder + '/SinglePolicyGraphs'
        if not os.path.exists(folder):
            os.makedirs(folder)
        
        for j in range(numPolicies):
            
            # Policy folder
            policyFolder = folder + '/Policy_' + str(j)
            if not os.path.exists(policyFolder):
                os.makedirs(policyFolder)
                
            ## Total Informal Social Care - Time series
            
            meanValues = []
            minValues = []
            maxValues = []
            days = []
            for dayOutput in range(180+1):
                dayValues = []
                for z in range(numRepeats):
                    dayValues.append(output[z][i][j].loc[output[z][i][j]['day'] == dayOutput, 'totalInformalSocialCare'].values[0])
                mean = np.mean(dayValues)
                meanValues.append(mean)
                sd = np.std(dayValues)
                minValues.append(mean-sd)
                maxValues.append(mean+sd)
                days.append(dayOutput)
            
            fig, ax = plt.subplots() # Argument: figsize=(5, 3)
            ax.plot(days, meanValues, color="black", linewidth=2)
            ax.fill_between(days, minValues, maxValues, alpha=1, edgecolor='#3F7F4C', facecolor='#7EFF99', linewidth=0)
            ax.set_ylabel('Hours of care')
            # ax.set_title('Cost of Public Social Care')
            formatter = ticker.ScalarFormatter(useMathText=True) #scientific notation
            formatter.set_scientific(True) 
            formatter.set_powerlimits((-1,1)) 
            ax.yaxis.set_major_formatter(formatter)
            ax.xaxis.set_major_locator(MaxNLocator(integer=True))
            plt.ylim(3000.0, 6000.0)
            # ax.set_ylim([0.0, 6.0])
            # ax.set_xlim(left = int(p['statsCollectFrom']), right = int(p['endYear']))
            # ax.set_xticks(range(int(p['statsCollectFrom']), int(p['endYear'])+1, 20))
            fig.tight_layout()
            path = os.path.join(policyFolder, 'totalInformalSocialCare_Policy' + str(j) + '.pdf')
            pp = PdfPages(path)
            pp.savefig(fig)
            pp.close()
            
            # totalSocialCareNeed
            meanValues = []
            minValues = []
            maxValues = []
            days = []
            for dayOutput in range(180+1):
                dayValues = []
                for z in range(numRepeats):
                    dayValues.append(output[z][i][j].loc[output[z][i][j]['day'] == dayOutput, 'totalSocialCareNeed'].values[0])
                mean = np.mean(dayValues)
                meanValues.append(mean)
                sd = np.std(dayValues)
                minValues.append(mean-sd)
                maxValues.append(mean+sd)
                days.append(dayOutput)
            
            fig, ax = plt.subplots() # Argument: figsize=(5, 3)
            ax.plot(days, meanValues, color="black", linewidth=2)
            ax.fill_between(days, minValues, maxValues, alpha=1, edgecolor='#3F7F4C', facecolor='#7EFF99', linewidth=0)
            ax.set_ylabel('Hours of care')
            # ax.set_title('Cost of Public Social Care')
            formatter = ticker.ScalarFormatter(useMathText=True) #scientific notation
            formatter.set_scientific(True) 
            formatter.set_powerlimits((-1,1)) 
            ax.yaxis.set_major_formatter(formatter)
            ax.xaxis.set_major_locator(MaxNLocator(integer=True))
            plt.ylim(8000.0, 12000.0)
            # ax.set_xlim(left = int(p['statsCollectFrom']), right = int(p['endYear']))
            # ax.set_xticks(range(int(p['statsCollectFrom']), int(p['endYear'])+1, 20))
            fig.tight_layout()
            path = os.path.join(policyFolder, 'totalSocialCareNeed_Policy' + str(j) + '.pdf')
            pp = PdfPages(path)
            pp.savefig(fig)
            pp.close()
            
            
            # totalUnmetSocialCareNeed
            meanValues = []
            minValues = []
            maxValues = []
            days = []
            for dayOutput in range(180+1):
                dayValues = []
                for z in range(numRepeats):
                    dayValues.append(output[z][i][j].loc[output[z][i][j]['day'] == dayOutput, 'totalUnmetSocialCareNeed'].values[0])
                mean = np.mean(dayValues)
                meanValues.append(mean)
                sd = np.std(dayValues)
                minValues.append(mean-sd)
                maxValues.append(mean+sd)
                days.append(dayOutput)
            
            fig, ax = plt.subplots() # Argument: figsize=(5, 3)
            ax.plot(days, meanValues, color="black", linewidth=2)
            ax.fill_between(days, minValues, maxValues, alpha=1, edgecolor='#3F7F4C', facecolor='#7EFF99', linewidth=0)
            ax.set_ylabel('Hours of care')
            # ax.set_title('Cost of Public Social Care')
            formatter = ticker.ScalarFormatter(useMathText=True) #scientific notation
            formatter.set_scientific(True) 
            formatter.set_powerlimits((-1,1)) 
            ax.yaxis.set_major_formatter(formatter)
            ax.xaxis.set_major_locator(MaxNLocator(integer=True))
            plt.ylim(2500.0, 4500.0)
            # ax.set_xlim(left = int(p['statsCollectFrom']), right = int(p['endYear']))
            # ax.set_xticks(range(int(p['statsCollectFrom']), int(p['endYear'])+1, 20))
            fig.tight_layout()
            path = os.path.join(policyFolder, 'totalUnmetSocialCareNeed_Policy' + str(j) + '.pdf')
            pp = PdfPages(path)
            pp.savefig(fig)
            pp.close()
            
            # totalInformalSocialCare_Q1
            G1 = []; G2 = []; G3 = []; G4 = []; G5 = []
            for z in range(numRepeats):
                G1.append(np.sum(output[z][i][j]['totalInformalSocialCare_Q1']))
                G2.append(np.sum(output[z][i][j]['totalInformalSocialCare_Q2']))
                G3.append(np.sum(output[z][i][j]['totalInformalSocialCare_Q3']))
                G4.append(np.sum(output[z][i][j]['totalInformalSocialCare_Q4']))
                G5.append(np.sum(output[z][i][j]['totalInformalSocialCare_Q5']))
            meansOutput = [np.mean(G1), np.mean(G2), np.mean(G3), np.mean(G4), np.mean(G5)]
            sdOutput = [np.std(G1), np.std(G2), np.std(G3), np.std(G4), np.std(G5)]
            
            fig, ax = plt.subplots()
            objects = ['Q1', 'Q2', 'Q3', 'Q4', 'Q5']
            y_pos = np.arange(len(objects))
            ax.bar(y_pos, meansOutput, yerr=sdOutput, width = 0.6, align='center', alpha=0.5, ecolor='black', capsize=10)
            plt.xticks(y_pos, objects)
            # plt.ylim(1200000, 1400000)
            ax.xaxis.set_ticks_position('none')
            ax.set_ylabel('Total hours')
            ax.yaxis.grid(True)
            formatter = ticker.ScalarFormatter(useMathText=True) #scientific notation
            formatter.set_scientific(True) 
            formatter.set_powerlimits((-1,1)) 
            ax.yaxis.set_major_formatter(formatter)
            # ax.set_title('Formal Child Care (2020-2040)')
            fig.tight_layout()
            path = os.path.join(policyFolder, 'informalSocialCaredByQuintiles_Policy' + str(j) + '.pdf')
            pp = PdfPages(path)
            pp.savefig(fig)
            pp.close()
            
            # totalSocialCareNeed_Q1
            G1 = []; G2 = []; G3 = []; G4 = []; G5 = []
            for z in range(numRepeats):
                G1.append(np.sum(output[z][i][j]['totalSocialCareNeed_Q1']))
                G2.append(np.sum(output[z][i][j]['totalSocialCareNeed_Q2']))
                G3.append(np.sum(output[z][i][j]['totalSocialCareNeed_Q3']))
                G4.append(np.sum(output[z][i][j]['totalSocialCareNeed_Q4']))
                G5.append(np.sum(output[z][i][j]['totalSocialCareNeed_Q5']))
            meansOutput = [np.mean(G1), np.mean(G2), np.mean(G3), np.mean(G4), np.mean(G5)]
            sdOutput = [np.std(G1), np.std(G2), np.std(G3), np.std(G4), np.std(G5)]
            
            fig, ax = plt.subplots()
            objects = ['Q1', 'Q2', 'Q3', 'Q4', 'Q5']
            y_pos = np.arange(len(objects))
            ax.bar(y_pos, meansOutput, yerr=sdOutput, width = 0.6, align='center', alpha=0.5, ecolor='black', capsize=10)
            plt.xticks(y_pos, objects)
            # plt.ylim(1200000, 1400000)
            ax.xaxis.set_ticks_position('none')
            ax.set_ylabel('Total hours')
            ax.yaxis.grid(True)
            formatter = ticker.ScalarFormatter(useMathText=True) #scientific notation
            formatter.set_scientific(True) 
            formatter.set_powerlimits((-1,1)) 
            ax.yaxis.set_major_formatter(formatter)
            # ax.set_title('Formal Child Care (2020-2040)')
            fig.tight_layout()
            path = os.path.join(policyFolder, 'socialCareNeedByQuintiles_Policy' + str(j) + '.pdf')
            pp = PdfPages(path)
            pp.savefig(fig)
            pp.close()
            
            # Unmet Social Care by Quintile - Bar chart
            G1 = []; G2 = []; G3 = []; G4 = []; G5 = []
            for z in range(numRepeats):
                G1.append(np.sum(output[z][i][j]['unmetSocialCareNeed_Q1']))
                G2.append(np.sum(output[z][i][j]['unmetSocialCareNeed_Q2']))
                G3.append(np.sum(output[z][i][j]['unmetSocialCareNeed_Q3']))
                G4.append(np.sum(output[z][i][j]['unmetSocialCareNeed_Q4']))
                G5.append(np.sum(output[z][i][j]['unmetSocialCareNeed_Q5']))
            meansOutput = [np.mean(G1), np.mean(G2), np.mean(G3), np.mean(G4), np.mean(G5)]
            sdOutput = [np.std(G1), np.std(G2), np.std(G3), np.std(G4), np.std(G5)]
            
            fig, ax = plt.subplots()
            objects = ['Q1', 'Q2', 'Q3', 'Q4', 'Q5']
            y_pos = np.arange(len(objects))
            ax.bar(y_pos, meansOutput, yerr=sdOutput, width = 0.6, align='center', alpha=0.5, ecolor='black', capsize=10)
            plt.xticks(y_pos, objects)
            # plt.ylim(1200000, 1400000)
            ax.xaxis.set_ticks_position('none')
            ax.set_ylabel('Total hours')
            ax.yaxis.grid(True)
            formatter = ticker.ScalarFormatter(useMathText=True) #scientific notation
            formatter.set_scientific(True) 
            formatter.set_powerlimits((-1,1)) 
            ax.yaxis.set_major_formatter(formatter)
            # ax.set_title('Formal Child Care (2020-2040)')
            fig.tight_layout()
            path = os.path.join(policyFolder, 'unmetSocialCareByQuintiles_Policy' + str(j) + '.pdf')
            pp = PdfPages(path)
            pp.savefig(fig)
            pp.close()
       
        
            ###  Add the other single-policy charts
        
            # infectious, hospitalized, intubated, 
            meanValues = []
            minValues = []
            maxValues = []
            days = []
            for dayOutput in range(180+1):
                dayValues = []
                for z in range(numRepeats):
                    dayValues.append(output[z][i][j].loc[output[z][i][j]['day'] == dayOutput, 'infectious'].values[0])
                mean = np.mean(dayValues)
                meanValues.append(mean)
                sd = np.std(dayValues)
                minValues.append(mean-sd)
                maxValues.append(mean+sd)
                days.append(dayOutput)
            
            fig, ax = plt.subplots() # Argument: figsize=(5, 3)
            ax.plot(days, meanValues, color="black", linewidth=2)
            ax.fill_between(days, minValues, maxValues, alpha=1, edgecolor='#3F7F4C', facecolor='#7EFF99', linewidth=0)
            ax.set_ylabel('Number')
            # ax.set_title('Cost of Public Social Care')
            formatter = ticker.ScalarFormatter(useMathText=True) #scientific notation
            formatter.set_scientific(True) 
            formatter.set_powerlimits((-1,1)) 
            ax.yaxis.set_major_formatter(formatter)
            ax.xaxis.set_major_locator(MaxNLocator(integer=True))
            # ax.set_xlim(left = int(p['statsCollectFrom']), right = int(p['endYear']))
            # ax.set_xticks(range(int(p['statsCollectFrom']), int(p['endYear'])+1, 20))
            fig.tight_layout()
            path = os.path.join(policyFolder, 'infectious_Policy' + str(j) + '.pdf')
            pp = PdfPages(path)
            pp.savefig(fig)
            pp.close()
            
            meanValues = []
            minValues = []
            maxValues = []
            days = []
            for dayOutput in range(180+1):
                dayValues = []
                for z in range(numRepeats):
                    num = float(output[z][i][j].loc[output[z][i][j]['day'] == dayOutput, 'susceptibles'].values[0])
                    den = float(output[z][i][j].loc[output[z][i][j]['day'] == dayOutput, 'currentPop'].values[0])
                    dayValues.append(num/den)
                mean = np.mean(dayValues)
                meanValues.append(mean)
                sd = np.std(dayValues)
                minValues.append(mean-sd)
                maxValues.append(mean+sd)
                days.append(dayOutput)
            
            fig, ax = plt.subplots() # Argument: figsize=(5, 3)
            ax.plot(days, meanValues, color="black", linewidth=2)
            ax.fill_between(days, minValues, maxValues, alpha=1, edgecolor='#3F7F4C', facecolor='#7EFF99', linewidth=0)
            ax.set_ylabel('Share')
            # ax.set_title('Cost of Public Social Care')
            formatter = ticker.ScalarFormatter(useMathText=True) #scientific notation
            formatter.set_scientific(True) 
            formatter.set_powerlimits((-1,1)) 
            ax.yaxis.set_major_formatter(formatter)
            ax.xaxis.set_major_locator(MaxNLocator(integer=True))
            # ax.set_xlim(left = int(p['statsCollectFrom']), right = int(p['endYear']))
            # ax.set_xticks(range(int(p['statsCollectFrom']), int(p['endYear'])+1, 20))
            fig.tight_layout()
            path = os.path.join(policyFolder, 'susceptiblesShare_Policy' + str(j) + '.pdf')
            pp = PdfPages(path)
            pp.savefig(fig)
            pp.close()
            
            meanValues = []
            minValues = []
            maxValues = []
            days = []
            for dayOutput in range(180+1):
                dayValues = []
                for z in range(numRepeats):
                    dayValues.append(output[z][i][j].loc[output[z][i][j]['day'] == dayOutput, 'hospitalized'].values[0])
                mean = np.mean(dayValues)
                meanValues.append(mean)
                sd = np.std(dayValues)
                minValues.append(mean-sd)
                maxValues.append(mean+sd)
                days.append(dayOutput)
            
            fig, ax = plt.subplots() # Argument: figsize=(5, 3)
            ax.plot(days, meanValues, color="black", linewidth=2)
            ax.fill_between(days, minValues, maxValues, alpha=1, edgecolor='#3F7F4C', facecolor='#7EFF99', linewidth=0)
            ax.set_ylabel('Number')
            # ax.set_title('Cost of Public Social Care')
            formatter = ticker.ScalarFormatter(useMathText=True) #scientific notation
            formatter.set_scientific(True) 
            formatter.set_powerlimits((-1,1)) 
            ax.yaxis.set_major_formatter(formatter)
            ax.xaxis.set_major_locator(MaxNLocator(integer=True))
            # ax.set_xlim(left = int(p['statsCollectFrom']), right = int(p['endYear']))
            # ax.set_xticks(range(int(p['statsCollectFrom']), int(p['endYear'])+1, 20))
            fig.tight_layout()
            path = os.path.join(policyFolder, 'hospitalized_Policy' + str(j) + '.pdf')
            pp = PdfPages(path)
            pp.savefig(fig)
            pp.close()
            
            meanValues = []
            minValues = []
            maxValues = []
            days = []
            for dayOutput in range(180+1):
                dayValues = []
                for z in range(numRepeats):
                    dayValues.append(output[z][i][j].loc[output[z][i][j]['day'] == dayOutput, 'intubated'].values[0])
                mean = np.mean(dayValues)
                meanValues.append(mean)
                sd = np.std(dayValues)
                minValues.append(mean-sd)
                maxValues.append(mean+sd)
                days.append(dayOutput)
            
            fig, ax = plt.subplots() # Argument: figsize=(5, 3)
            ax.plot(days, meanValues, color="black", linewidth=2)
            ax.fill_between(days, minValues, maxValues, alpha=1, edgecolor='#3F7F4C', facecolor='#7EFF99', linewidth=0)
            ax.set_ylabel('Number')
            # ax.set_title('Cost of Public Social Care')
            formatter = ticker.ScalarFormatter(useMathText=True) #scientific notation
            formatter.set_scientific(True) 
            formatter.set_powerlimits((-1,1)) 
            ax.yaxis.set_major_formatter(formatter)
            ax.xaxis.set_major_locator(MaxNLocator(integer=True))
            # ax.set_xlim(left = int(p['statsCollectFrom']), right = int(p['endYear']))
            # ax.set_xticks(range(int(p['statsCollectFrom']), int(p['endYear'])+1, 20))
            fig.tight_layout()
            path = os.path.join(policyFolder, 'intubated_Policy' + str(j) + '.pdf')
            pp = PdfPages(path)
            pp.savefig(fig)
            pp.close()
            
            G1 = []; G2 = []; G3 = []; G4 = []; G5 = []
            for z in range(numRepeats):
                G1.append(np.sum(output[z][i][j]['infectedByClass_0']))
                G2.append(np.sum(output[z][i][j]['infectedByClass_1']))
                G3.append(np.sum(output[z][i][j]['infectedByClass_2']))
                G4.append(np.sum(output[z][i][j]['infectedByClass_3']))
                G5.append(np.sum(output[z][i][j]['infectedByClass_4']))
            meansOutput = [np.mean(G1), np.mean(G2), np.mean(G3), np.mean(G4), np.mean(G5)]
            sdOutput = [np.std(G1), np.std(G2), np.std(G3), np.std(G4), np.std(G5)]
            
            fig, ax = plt.subplots()
            objects = ['Q1', 'Q2', 'Q3', 'Q4', 'Q5']
            y_pos = np.arange(len(objects))
            ax.bar(y_pos, meansOutput, yerr=sdOutput, width = 0.6, align='center', alpha=0.5, ecolor='black', capsize=10)
            plt.xticks(y_pos, objects)
            # plt.ylim(1200000, 1400000)
            ax.xaxis.set_ticks_position('none')
            ax.set_ylabel('Total hours')
            ax.yaxis.grid(True)
            formatter = ticker.ScalarFormatter(useMathText=True) #scientific notation
            formatter.set_scientific(True) 
            formatter.set_powerlimits((-1,1)) 
            ax.yaxis.set_major_formatter(formatter)
            # ax.set_title('Formal Child Care (2020-2040)')
            fig.tight_layout()
            path = os.path.join(policyFolder, 'infectedByQuintiles_Policy' + str(j) + '.pdf')
            pp = PdfPages(path)
            pp.savefig(fig)
            pp.close()
            
            G1 = []; G2 = []; G3 = []; G4 = []; G5 = []
            for z in range(numRepeats):
                G1.append(np.sum(output[z][i][j]['hospitalizedByClass_0']))
                G2.append(np.sum(output[z][i][j]['hospitalizedByClass_1']))
                G3.append(np.sum(output[z][i][j]['hospitalizedByClass_2']))
                G4.append(np.sum(output[z][i][j]['hospitalizedByClass_3']))
                G5.append(np.sum(output[z][i][j]['hospitalizedByClass_4']))
            meansOutput = [np.mean(G1), np.mean(G2), np.mean(G3), np.mean(G4), np.mean(G5)]
            sdOutput = [np.std(G1), np.std(G2), np.std(G3), np.std(G4), np.std(G5)]
            
            fig, ax = plt.subplots()
            objects = ['Q1', 'Q2', 'Q3', 'Q4', 'Q5']
            y_pos = np.arange(len(objects))
            ax.bar(y_pos, meansOutput, yerr=sdOutput, width = 0.6, align='center', alpha=0.5, ecolor='black', capsize=10)
            plt.xticks(y_pos, objects)
            # plt.ylim(1200000, 1400000)
            ax.xaxis.set_ticks_position('none')
            ax.set_ylabel('Total hours')
            ax.yaxis.grid(True)
            formatter = ticker.ScalarFormatter(useMathText=True) #scientific notation
            formatter.set_scientific(True) 
            formatter.set_powerlimits((-1,1)) 
            ax.yaxis.set_major_formatter(formatter)
            # ax.set_title('Formal Child Care (2020-2040)')
            fig.tight_layout()
            path = os.path.join(policyFolder, 'hospitalizedByQuintiles_Policy' + str(j) + '.pdf')
            pp = PdfPages(path)
            pp.savefig(fig)
            pp.close()
            
            G1 = []; G2 = []; G3 = []; G4 = []; G5 = []
            for z in range(numRepeats):
                G1.append(np.sum(output[z][i][j]['intubatedByClass_0']))
                G2.append(np.sum(output[z][i][j]['intubatedByClass_1']))
                G3.append(np.sum(output[z][i][j]['intubatedByClass_2']))
                G4.append(np.sum(output[z][i][j]['intubatedByClass_3']))
                G5.append(np.sum(output[z][i][j]['intubatedByClass_4']))
            meansOutput = [np.mean(G1), np.mean(G2), np.mean(G3), np.mean(G4), np.mean(G5)]
            sdOutput = [np.std(G1), np.std(G2), np.std(G3), np.std(G4), np.std(G5)]
            
            fig, ax = plt.subplots()
            objects = ['Q1', 'Q2', 'Q3', 'Q4', 'Q5']
            y_pos = np.arange(len(objects))
            ax.bar(y_pos, meansOutput, yerr=sdOutput, width = 0.6, align='center', alpha=0.5, ecolor='black', capsize=10)
            plt.xticks(y_pos, objects)
            # plt.ylim(1200000, 1400000)
            ax.xaxis.set_ticks_position('none')
            ax.set_ylabel('Total hours')
            ax.yaxis.grid(True)
            formatter = ticker.ScalarFormatter(useMathText=True) #scientific notation
            formatter.set_scientific(True) 
            formatter.set_powerlimits((-1,1)) 
            ax.yaxis.set_major_formatter(formatter)
            # ax.set_title('Formal Child Care (2020-2040)')
            fig.tight_layout()
            path = os.path.join(policyFolder, 'intubatedByQuintiles_Policy' + str(j) + '.pdf')
            pp = PdfPages(path)
            pp.savefig(fig)
            pp.close()
            
        
        #####     Policies comparison charts    ###################
        
        folder = scenarioFolder + '/PoliciesComparisonGraphs'
        if not os.path.exists(folder):
            os.makedirs(folder)
        
        policies = ['Benchmark', 'Policy 1', 'Policy 2'] # , 'Policy 2', 'Policy 3', 'Policy 4']
        
        
        # Total unmet social care need - Time series
        meanValues_P = []
        minValues_P = []
        maxValues_P = []
        for j in range(numPolicies):
            meanValues = []
            minValues = []
            maxValues = []
            days = []
            for dayOutput in range(180+1):
                dayValues = []
                for z in range(numRepeats):
                    dayValues.append(output[z][i][j].loc[output[z][i][j]['day'] == dayOutput, 'totalInformalSocialCare'].values[0])
                mean = np.mean(dayValues)
                meanValues.append(mean)
                sd = np.std(dayValues)
                minValues.append(mean-sd)
                maxValues.append(mean+sd)
                days.append(dayOutput)
            meanValues_P.append(meanValues)
            minValues_P.append(minValues)
            maxValues_P.append(maxValues)
            
        fig, ax = plt.subplots() # Argument: figsize=(5, 3)
        colors = ["green", "blue", "red"]
        for j in range(numPolicies):
            policyLabel = 'Benchmark'
            if j != 0:
                policyLabel = 'Policy ' + str(j)
            ax.plot(days, meanValues_P[j], color=colors[j], label = policyLabel, linewidth=2)
            ax.fill_between(days, minValues_P[j], maxValues_P[j], alpha = 0.5, edgecolor='lightgrey', facecolor='lightgrey', linewidth=0)
                            # edgecolor='#3F7F4C', facecolor='#7EFF99'
        ax.set_ylabel('Total Hours')
        # ax.set_title('Cost of Public Social Care')
        formatter = ticker.ScalarFormatter(useMathText=True) #scientific notation
        formatter.set_scientific(True) 
        formatter.set_powerlimits((-1,1)) 
        ax.yaxis.set_major_formatter(formatter)
        handels, labels = ax.get_legend_handles_labels()
        ax.legend(loc = 'upper left')
        ax.xaxis.set_major_locator(MaxNLocator(integer=True))
        # ax.set_xlim(left = int(p['statsCollectFrom']), right = int(p['endYear']))
        # ax.set_xticks(range(int(p['statsCollectFrom']), int(p['endYear'])+1, 20))
        fig.tight_layout()
        path = os.path.join(folder, 'totalInformalSocialCare_TS.pdf')
        pp = PdfPages(path)
        pp.savefig(fig)
        pp.close()
        
        # Total unmet social care need - Time series
        meanValues_P = []
        minValues_P = []
        maxValues_P = []
        for j in range(numPolicies):
            meanValues = []
            minValues = []
            maxValues = []
            days = []
            for dayOutput in range(180+1):
                dayValues = []
                for z in range(numRepeats):
                    dayValues.append(output[z][i][j].loc[output[z][i][j]['day'] == dayOutput, 'totalUnmetSocialCareNeed'].values[0])
                mean = np.mean(dayValues)
                meanValues.append(mean)
                sd = np.std(dayValues)
                minValues.append(mean-sd)
                maxValues.append(mean+sd)
                days.append(dayOutput)
            meanValues_P.append(meanValues)
            minValues_P.append(minValues)
            maxValues_P.append(maxValues)
            
        fig, ax = plt.subplots() # Argument: figsize=(5, 3)
        colors = ["green", "blue", "red"]
        for j in range(numPolicies):
            policyLabel = 'Benchmark'
            if j != 0:
                policyLabel = 'Policy ' + str(j)
            ax.plot(days, meanValues_P[j], color=colors[j], label = policyLabel, linewidth=2)
            ax.fill_between(days, minValues_P[j], maxValues_P[j], alpha = 0.5, edgecolor='lightgrey', facecolor='lightgrey', linewidth=0)
                            # edgecolor='#3F7F4C', facecolor='#7EFF99'
        ax.set_ylabel('Total Hours')
        # ax.set_title('Cost of Public Social Care')
        formatter = ticker.ScalarFormatter(useMathText=True) #scientific notation
        formatter.set_scientific(True) 
        formatter.set_powerlimits((-1,1)) 
        ax.yaxis.set_major_formatter(formatter)
        handels, labels = ax.get_legend_handles_labels()
        ax.legend(loc = 'upper left')
        ax.xaxis.set_major_locator(MaxNLocator(integer=True))
        # ax.set_xlim(left = int(p['statsCollectFrom']), right = int(p['endYear']))
        # ax.set_xticks(range(int(p['statsCollectFrom']), int(p['endYear'])+1, 20))
        fig.tight_layout()
        path = os.path.join(folder, 'totalUnmetSocialCareNeed_TS.pdf')
        pp = PdfPages(path)
        pp.savefig(fig)
        pp.close()
        
        
        meansOutput = []
        sdOutput = []
        for j in range(numPolicies):
            values = []
            for z in range(numRepeats):
                values.append(np.sum(output[z][i][j]['totalInformalSocialCare']))
            meansOutput.append(np.mean(values))
            sdOutput.append(np.std(values))
        fig, ax = plt.subplots()
        x_pos = np.arange(len(policies))
        ax.bar(x_pos, meansOutput, yerr=sdOutput, width = 0.6, align='center', alpha=0.5, ecolor='black', capsize=10)
        ax.set_ylabel('Total Hours')
        ax.set_xticks(x_pos)
        ax.set_xticklabels(policies)
        formatter = ticker.ScalarFormatter(useMathText=True) #scientific notation
        formatter.set_scientific(True) 
        formatter.set_powerlimits((-1,1)) 
        ax.yaxis.set_major_formatter(formatter)
        # ax.set_title('Unmet Social Care Needs (mean 2025-2035)')
        ax.yaxis.grid(True)
        fig.tight_layout()
        path = os.path.join(folder, 'totalInformalSocialCare_BC.pdf')
        pp = PdfPages(path)
        pp.savefig(fig)
        pp.close()
        
        meansOutput = []
        sdOutput = []
        for j in range(numPolicies):
            values = []
            for z in range(numRepeats):
                values.append(np.sum(output[z][i][j]['totalUnmetSocialCareNeed']))
            meansOutput.append(np.mean(values))
            sdOutput.append(np.std(values))
        fig, ax = plt.subplots()
        x_pos = np.arange(len(policies))
        ax.bar(x_pos, meansOutput, yerr=sdOutput, width = 0.6, align='center', alpha=0.5, ecolor='black', capsize=10)
        ax.set_ylabel('Total Hours')
        ax.set_xticks(x_pos)
        ax.set_xticklabels(policies)
        formatter = ticker.ScalarFormatter(useMathText=True) #scientific notation
        formatter.set_scientific(True) 
        formatter.set_powerlimits((-1,1)) 
        ax.yaxis.set_major_formatter(formatter)
        # ax.set_title('Unmet Social Care Needs (mean 2025-2035)')
        ax.yaxis.grid(True)
        fig.tight_layout()
        path = os.path.join(folder, 'totalUnmetSocialCareNeed_BC.pdf')
        pp = PdfPages(path)
        pp.savefig(fig)
        pp.close()
        
        ##  Most-least deprived ratio bar chart
        
        meansOutput = []
        sdOutput = []
        for j in range(numPolicies):
            values = []
            for z in range(numRepeats):
                values.append(np.mean(output[z][i][j]['mostLeastDeprivedRatio']))
            meansOutput.append(np.mean(values))
            sdOutput.append(np.std(values))
        fig, ax = plt.subplots()
        x_pos = np.arange(len(policies))
        ax.bar(x_pos, meansOutput, yerr=sdOutput, width = 0.6, align='center', alpha=0.5, ecolor='black', capsize=10)
        ax.set_ylabel('Q1/Q5 Ratio')
        ax.set_xticks(x_pos)
        ax.set_xticklabels(policies)
        formatter = ticker.ScalarFormatter(useMathText=True) #scientific notation
        formatter.set_scientific(True) 
        formatter.set_powerlimits((-1,1)) 
        ax.yaxis.set_major_formatter(formatter)
        # ax.set_title('Unmet Social Care Needs (mean 2025-2035)')
        ax.yaxis.grid(True)
        fig.tight_layout()
        path = os.path.join(folder, 'mostLeastDeprivedRatio_BC.pdf')
        pp = PdfPages(path)
        pp.savefig(fig)
        pp.close()
        
        
        ###  Add other multiple-policy graphs....
        
        meanValues_P = []
        minValues_P = []
        maxValues_P = []
        for j in range(numPolicies):
            meanValues = []
            minValues = []
            maxValues = []
            days = []
            for dayOutput in range(180+1):
                dayValues = []
                for z in range(numRepeats):
                    dayValues.append(output[z][i][j].loc[output[z][i][j]['day'] == dayOutput, 'hospitalized'].values[0])
                mean = np.mean(dayValues)
                meanValues.append(mean)
                sd = np.std(dayValues)
                minValues.append(mean-sd)
                maxValues.append(mean+sd)
                days.append(dayOutput)
            meanValues_P.append(meanValues)
            minValues_P.append(minValues)
            maxValues_P.append(maxValues)
            
        fig, ax = plt.subplots() # Argument: figsize=(5, 3)
        colors = ["green", "blue", "red"]
        for j in range(numPolicies):
            policyLabel = 'Benchmark'
            if j != 0:
                policyLabel = 'Policy ' + str(j)
            ax.plot(days, meanValues_P[j], color=colors[j], label = policyLabel, linewidth=2)
            ax.fill_between(days, minValues_P[j], maxValues_P[j], alpha = 0.5, edgecolor='lightgrey', facecolor='lightgrey', linewidth=0)
                            # edgecolor='#3F7F4C', facecolor='#7EFF99'
        ax.set_ylabel('Number')
        # ax.set_title('Cost of Public Social Care')
        formatter = ticker.ScalarFormatter(useMathText=True) #scientific notation
        formatter.set_scientific(True) 
        formatter.set_powerlimits((-1,1)) 
        ax.yaxis.set_major_formatter(formatter)
        handels, labels = ax.get_legend_handles_labels()
        ax.legend(loc = 'upper left')
        ax.xaxis.set_major_locator(MaxNLocator(integer=True))
        # ax.set_xlim(left = int(p['statsCollectFrom']), right = int(p['endYear']))
        # ax.set_xticks(range(int(p['statsCollectFrom']), int(p['endYear'])+1, 20))
        fig.tight_layout()
        path = os.path.join(folder, 'hospitalized_TS.pdf')
        pp = PdfPages(path)
        pp.savefig(fig)
        pp.close()
        
        meanValues_P = []
        minValues_P = []
        maxValues_P = []
        for j in range(numPolicies):
            meanValues = []
            minValues = []
            maxValues = []
            days = []
            for dayOutput in range(180+1):
                dayValues = []
                for z in range(numRepeats):
                    dayValues.append(output[z][i][j].loc[output[z][i][j]['day'] == dayOutput, 'intubated'].values[0])
                mean = np.mean(dayValues)
                meanValues.append(mean)
                sd = np.std(dayValues)
                minValues.append(mean-sd)
                maxValues.append(mean+sd)
                days.append(dayOutput)
            meanValues_P.append(meanValues)
            minValues_P.append(minValues)
            maxValues_P.append(maxValues)
            
        fig, ax = plt.subplots() # Argument: figsize=(5, 3)
        colors = ["green", "blue", "red"]
        for j in range(numPolicies):
            policyLabel = 'Benchmark'
            if j != 0:
                policyLabel = 'Policy ' + str(j)
            ax.plot(days, meanValues_P[j], color=colors[j], label = policyLabel, linewidth=2)
            ax.fill_between(days, minValues_P[j], maxValues_P[j], alpha = 0.5, edgecolor='lightgrey', facecolor='lightgrey', linewidth=0)
                            # edgecolor='#3F7F4C', facecolor='#7EFF99'
        ax.set_ylabel('Number')
        # ax.set_title('Cost of Public Social Care')
        formatter = ticker.ScalarFormatter(useMathText=True) #scientific notation
        formatter.set_scientific(True) 
        formatter.set_powerlimits((-1,1)) 
        ax.yaxis.set_major_formatter(formatter)
        handels, labels = ax.get_legend_handles_labels()
        ax.legend(loc = 'upper left')
        ax.xaxis.set_major_locator(MaxNLocator(integer=True))
        # ax.set_xlim(left = int(p['statsCollectFrom']), right = int(p['endYear']))
        # ax.set_xticks(range(int(p['statsCollectFrom']), int(p['endYear'])+1, 20))
        fig.tight_layout()
        path = os.path.join(folder, 'intubated_TS.pdf')
        pp = PdfPages(path)
        pp.savefig(fig)
        pp.close()
        
        meansOutput = []
        sdOutput = []
        for j in range(numPolicies):
            values = []
            for z in range(numRepeats):
                values.append(np.sum(output[z][i][j]['hospitalized']))
            meansOutput.append(np.mean(values))
            sdOutput.append(np.std(values))
        fig, ax = plt.subplots()
        x_pos = np.arange(len(policies))
        ax.bar(x_pos, meansOutput, yerr=sdOutput, width = 0.6, align='center', alpha=0.5, ecolor='black', capsize=10)
        ax.set_ylabel('Total days')
        ax.set_xticks(x_pos)
        ax.set_xticklabels(policies)
        formatter = ticker.ScalarFormatter(useMathText=True) #scientific notation
        formatter.set_scientific(True) 
        formatter.set_powerlimits((-1,1)) 
        ax.yaxis.set_major_formatter(formatter)
        # ax.set_title('Unmet Social Care Needs (mean 2025-2035)')
        ax.yaxis.grid(True)
        fig.tight_layout()
        path = os.path.join(folder, 'hospitalized_BC.pdf')
        pp = PdfPages(path)
        pp.savefig(fig)
        pp.close()
        
        
        meansOutput = []
        sdOutput = []
        for j in range(numPolicies):
            values = []
            for z in range(numRepeats):
                values.append(np.sum(output[z][i][j]['intubated']))
            meansOutput.append(np.mean(values))
            sdOutput.append(np.std(values))
        fig, ax = plt.subplots()
        x_pos = np.arange(len(policies))
        ax.bar(x_pos, meansOutput, yerr=sdOutput, width = 0.6, align='center', alpha=0.5, ecolor='black', capsize=10)
        ax.set_ylabel('Total days')
        ax.set_xticks(x_pos)
        ax.set_xticklabels(policies)
        formatter = ticker.ScalarFormatter(useMathText=True) #scientific notation
        formatter.set_scientific(True) 
        formatter.set_powerlimits((-1,1)) 
        ax.yaxis.set_major_formatter(formatter)
        # ax.set_title('Unmet Social Care Needs (mean 2025-2035)')
        ax.yaxis.grid(True)
        fig.tight_layout()
        path = os.path.join(folder, 'intubated_BC.pdf')
        pp = PdfPages(path)
        pp.savefig(fig)
        pp.close()
       
        
        meansOutput = []
        sdOutput = []
        for j in range(numPolicies):
            values = []
            for z in range(numRepeats):
                values.append(np.mean(output[z][i][j]['hospitalizedQuintilesRatio']))
            meansOutput.append(np.mean(values))
            sdOutput.append(np.std(values))
        fig, ax = plt.subplots()
        x_pos = np.arange(len(policies))
        ax.bar(x_pos, meansOutput, yerr=sdOutput, width = 0.6, align='center', alpha=0.5, ecolor='black', capsize=10)
        ax.set_ylabel('Q1/Q5 Ratio')
        ax.set_xticks(x_pos)
        ax.set_xticklabels(policies)
        formatter = ticker.ScalarFormatter(useMathText=True) #scientific notation
        formatter.set_scientific(True) 
        formatter.set_powerlimits((-1,1)) 
        ax.yaxis.set_major_formatter(formatter)
        # ax.set_title('Unmet Social Care Needs (mean 2025-2035)')
        ax.yaxis.grid(True)
        fig.tight_layout()
        path = os.path.join(folder, 'hospitalizedQuintilesRatio_BC.pdf')
        pp = PdfPages(path)
        pp.savefig(fig)
        pp.close()
        
        
        
        
        
        # pdb.set_trace()
        ## Plots and Bar charts with error bars for:
        ## 1 - Total deaths
        ## 2 - Total Hospitalized
        ## 3 - Total unmet care
        ## 4 - Total informal care
    
        meanValues_P = []
        minValues_P = []
        maxValues_P = []
        
        for j in range(numPolicies):
            meanValues = []
            minValues = []
            maxValues = []
            days = []
            for dayOutput in range(180+1):
                dayValues = []
                for z in range(numRepeats):
                    dayValues.append(output[z][i][j].loc[output[z][i][j]['day'] == dayOutput, 'totalHospitalized'].values[0])
                mean = np.mean(dayValues)
                meanValues.append(mean)
                sd = np.std(dayValues)
                minValues.append(mean-sd)
                maxValues.append(mean+sd)
                days.append(dayOutput)
            meanValues_P.append(meanValues)
            minValues_P.append(minValues)
            maxValues_P.append(maxValues)
            
        # Create charts
        fig, ax = plt.subplots() # Argument: figsize=(5, 3)
        for j in range(numPolicies):
            ax.plot(days, meanValues[j], color="black", linewidth=2)
            ax.fill_between(days, minValues[j], maxValues[j], alpha=1, edgecolor='#3F7F4C', facecolor='#7EFF99', linewidth=0)
        ax.set_ylabel('Hospitalizations')
        # ax.set_title('Cost of Public Social Care')
        formatter = ticker.ScalarFormatter(useMathText=True) #scientific notation
        formatter.set_scientific(True) 
        formatter.set_powerlimits((-1,1)) 
        ax.yaxis.set_major_formatter(formatter)
        ax.xaxis.set_major_locator(MaxNLocator(integer=True))
        ax.set_xlim(left = int(p['statsCollectFrom']), right = int(p['endYear']))
        ax.set_xticks(range(int(p['statsCollectFrom']), int(p['endYear'])+1, 20))
        fig.tight_layout()
        path = os.path.join(folder, 'totalHospitalized_Policies.pdf')
        pp = PdfPages(path)
        pp.savefig(fig)
        pp.close()
        
    
        meanValues_P = []
        minValues_P = []
        maxValues_P = []
        
        for j in range(numPolicies):
            meanValues = []
            minValues = []
            maxValues = []
            days = []
            for dayOutput in range(180+1):
                dayValues = []
                for z in range(numRepeats):
                    dayValues.append(output[z][i][j].loc[output[z][i][j]['day'] == dayOutput, 'hospitalPopulation'].values[0])
                mean = np.mean(dayValues)
                meanValues.append(mean)
                sd = np.std(dayValues)
                minValues.append(mean-sd)
                maxValues.append(mean+sd)
                days.append(dayOutput)
            meanValues_P.append(meanValues)
            minValues_P.append(minValues)
            maxValues_P.append(maxValues)
            
        # Create charts
        fig, ax = plt.subplots() # Argument: figsize=(5, 3)
        for j in range(numPolicies):
            ax.plot(days, meanValues[j], color="black", linewidth=2)
            ax.fill_between(days, minValues[j], maxValues[j], alpha=1, edgecolor='#3F7F4C', facecolor='#7EFF99', linewidth=0)
        ax.set_ylabel('Hospital Population')
        # ax.set_title('Cost of Public Social Care')
        formatter = ticker.ScalarFormatter(useMathText=True) #scientific notation
        formatter.set_scientific(True) 
        formatter.set_powerlimits((-1,1)) 
        ax.yaxis.set_major_formatter(formatter)
        ax.xaxis.set_major_locator(MaxNLocator(integer=True))
        ax.set_xlim(left = int(p['statsCollectFrom']), right = int(p['endYear']))
        ax.set_xticks(range(int(p['statsCollectFrom']), int(p['endYear'])+1, 20))
        fig.tight_layout()
        path = os.path.join(folder, 'hospitalPopulation_Policies.pdf')
        pp = PdfPages(path)
        pp.savefig(fig)
        pp.close()
        
        meanValues_P = []
        minValues_P = []
        maxValues_P = []
        
        for j in range(numPolicies):
            meanValues = []
            minValues = []
            maxValues = []
            days = []
            for dayOutput in range(180+1):
                dayValues = []
                for z in range(numRepeats):
                    dayValues.append(output[z][i][j].loc[output[z][i][j]['day'] == dayOutput, 'totalInformalSocialCare'].values[0])
                mean = np.mean(dayValues)
                meanValues.append(mean)
                sd = np.std(dayValues)
                minValues.append(mean-sd)
                maxValues.append(mean+sd)
                days.append(dayOutput)
            meanValues_P.append(meanValues)
            minValues_P.append(minValues)
            maxValues_P.append(maxValues)
            
        # Create charts
        fig, ax = plt.subplots() # Argument: figsize=(5, 3)
        for j in range(numPolicies):
            ax.plot(days, meanValues[j], color="black", linewidth=2)
            ax.fill_between(days, minValues[j], maxValues[j], alpha=1, edgecolor='#3F7F4C', facecolor='#7EFF99', linewidth=0)
        ax.set_ylabel('Hours of care')
        # ax.set_title('Cost of Public Social Care')
        formatter = ticker.ScalarFormatter(useMathText=True) #scientific notation
        formatter.set_scientific(True) 
        formatter.set_powerlimits((-1,1)) 
        ax.yaxis.set_major_formatter(formatter)
        ax.xaxis.set_major_locator(MaxNLocator(integer=True))
        ax.set_xlim(left = int(p['statsCollectFrom']), right = int(p['endYear']))
        ax.set_xticks(range(int(p['statsCollectFrom']), int(p['endYear'])+1, 20))
        fig.tight_layout()
        path = os.path.join(folder, 'totalInformalSocialCare_Policies.pdf')
        pp = PdfPages(path)
        pp.savefig(fig)
        pp.close()
        
        
        meansOutput = []
        sdOutput = []
        for j in range(numPolicies):
            values = []
            for z in range(numRepeats):
                values.append(sum(output[z][i][j]['totalUnmetSocialCareNeed']))
            meansOutput.append(np.mean(values))
            sdOutput.append(np.std(values))
        fig, ax = plt.subplots()
        x_pos = np.arange(len(policies))
        ax.bar(x_pos, meansOutput, yerr=sdOutput, align='center', alpha=0.5, ecolor='black', capsize=10)
        ax.set_ylabel('Hours')
        ax.set_xticks(x_pos)
        ax.set_xticklabels(policies)
        formatter = ticker.ScalarFormatter(useMathText=True) #scientific notation
        formatter.set_scientific(True) 
        formatter.set_powerlimits((-1,1)) 
        ax.yaxis.set_major_formatter(formatter)
        # ax.set_title('Unmet Social Care Needs (mean 2025-2035)')
        ax.yaxis.grid(True)
        fig.tight_layout()
        path = os.path.join(scenarioFolder, 'totalUnmetSocialCareNeedBarChart_P.pdf')
        pp = PdfPages(path)
        pp.savefig(fig)
        pp.close()
        
        meansOutput = []
        sdOutput = []
        for j in range(numPolicies):
            values = []
            for z in range(numRepeats):
                values.append(sum(output[z][i][j]['totalInformalSocialCare']))
            meansOutput.append(np.mean(values))
            sdOutput.append(np.std(values))
        fig, ax = plt.subplots()
        x_pos = np.arange(len(policies))
        ax.bar(x_pos, meansOutput, yerr=sdOutput, align='center', alpha=0.5, ecolor='black', capsize=10)
        ax.set_ylabel('Hours of care')
        ax.set_xticks(x_pos)
        ax.set_xticklabels(policies)
        formatter = ticker.ScalarFormatter(useMathText=True) #scientific notation
        formatter.set_scientific(True) 
        formatter.set_powerlimits((-1,1)) 
        ax.yaxis.set_major_formatter(formatter)
        # ax.set_title('Unmet Social Care Needs (mean 2025-2035)')
        ax.yaxis.grid(True)
        fig.tight_layout()
        path = os.path.join(scenarioFolder, 'totalInformalSocialCareBarChart_P.pdf')
        pp = PdfPages(path)
        pp.savefig(fig)
        pp.close()
        
        
        meansOutput = []
        sdOutput = []
        for j in range(numPolicies):
            values = []
            for z in range(numRepeats):
                values.append(sum(output[z][i][j]['totalHospitalized']))
            meansOutput.append(np.mean(values))
            sdOutput.append(np.std(values))
        fig, ax = plt.subplots()
        x_pos = np.arange(len(policies))
        ax.bar(x_pos, meansOutput, yerr=sdOutput, align='center', alpha=0.5, ecolor='black', capsize=10)
        ax.set_ylabel('Hospitalizations')
        ax.set_xticks(x_pos)
        ax.set_xticklabels(policies)
        formatter = ticker.ScalarFormatter(useMathText=True) #scientific notation
        formatter.set_scientific(True) 
        formatter.set_powerlimits((-1,1)) 
        ax.yaxis.set_major_formatter(formatter)
        # ax.set_title('Unmet Social Care Needs (mean 2025-2035)')
        ax.yaxis.grid(True)
        fig.tight_layout()
        path = os.path.join(scenarioFolder, 'totalHospitalizedBarChart_P.pdf')
        pp = PdfPages(path)
        pp.savefig(fig)
        pp.close()
        
        ###  Bar charts
        
        meansOutput = []
        sdOutput = []
        for j in range(numPolicies):
            values = []
            for z in range(numRepeats):
                values.append(np.mean(output[z][i][j]['mostLeastDeprivedRatio']))
            meansOutput.append(np.mean(values))
            sdOutput.append(np.std(values))
        fig, ax = plt.subplots()
        x_pos = np.arange(len(policies))
        ax.bar(x_pos, meansOutput, yerr=sdOutput, align='center', alpha=0.5, ecolor='black', capsize=10)
        ax.set_ylabel('Q1/Q5 Ratio')
        ax.set_xticks(x_pos)
        ax.set_xticklabels(policies)
        formatter = ticker.ScalarFormatter(useMathText=True) #scientific notation
        formatter.set_scientific(True) 
        formatter.set_powerlimits((-1,1)) 
        ax.yaxis.set_major_formatter(formatter)
        # ax.set_title('Unmet Social Care Needs (mean 2025-2035)')
        ax.yaxis.grid(True)
        fig.tight_layout()
        path = os.path.join(folder, 'mostLeastDeprivedRatio_Policies.pdf')
        pp = PdfPages(path)
        pp.savefig(fig)
        pp.close()
        
        meansOutput = []
        sdOutput = []
        for j in range(numPolicies):
            values = []
            for z in range(numRepeats):
                values.append(np.mean(output[z][i][j]['informalCareRatio']))
            meansOutput.append(np.mean(values))
            sdOutput.append(np.std(values))
        fig, ax = plt.subplots()
        x_pos = np.arange(len(policies))
        ax.bar(x_pos, meansOutput, yerr=sdOutput, align='center', alpha=0.5, ecolor='black', capsize=10)
        ax.set_ylabel('Q1/Q5 Ratio')
        ax.set_xticks(x_pos)
        ax.set_xticklabels(policies)
        formatter = ticker.ScalarFormatter(useMathText=True) #scientific notation
        formatter.set_scientific(True) 
        formatter.set_powerlimits((-1,1)) 
        ax.yaxis.set_major_formatter(formatter)
        # ax.set_title('Unmet Social Care Needs (mean 2025-2035)')
        ax.yaxis.grid(True)
        fig.tight_layout()
        path = os.path.join(folder, 'informalCareRatio_Policies.pdf')
        pp = PdfPages(path)
        pp.savefig(fig)
        pp.close()
        
        meansOutput = []
        sdOutput = []
        for j in range(numPolicies):
            values = []
            for z in range(numRepeats):
                values.append(np.mean(output[z][i][j]['careNeedRatio']))
            meansOutput.append(np.mean(values))
            sdOutput.append(np.std(values))
        fig, ax = plt.subplots()
        x_pos = np.arange(len(policies))
        ax.bar(x_pos, meansOutput, yerr=sdOutput, align='center', alpha=0.5, ecolor='black', capsize=10)
        ax.set_ylabel('Q1/Q5 Ratio')
        ax.set_xticks(x_pos)
        ax.set_xticklabels(policies)
        formatter = ticker.ScalarFormatter(useMathText=True) #scientific notation
        formatter.set_scientific(True) 
        formatter.set_powerlimits((-1,1)) 
        ax.yaxis.set_major_formatter(formatter)
        # ax.set_title('Unmet Social Care Needs (mean 2025-2035)')
        ax.yaxis.grid(True)
        fig.tight_layout()
        path = os.path.join(folder, 'careNeedRatio_Policies.pdf')
        pp = PdfPages(path)
        pp.savefig(fig)
        pp.close()
      
        meansOutput = []
        sdOutput = []
        for j in range(numPolicies):
            values = []
            for z in range(numRepeats):
                values.append(np.mean(output[z][i][j]['hospitalizedQuintilesRatio']))
            meansOutput.append(np.mean(values))
            sdOutput.append(np.std(values))
        fig, ax = plt.subplots()
        x_pos = np.arange(len(policies))
        ax.bar(x_pos, meansOutput, yerr=sdOutput, align='center', alpha=0.5, ecolor='black', capsize=10)
        ax.set_ylabel('Q1/Q5 Ratio')
        ax.set_xticks(x_pos)
        ax.set_xticklabels(policies)
        formatter = ticker.ScalarFormatter(useMathText=True) #scientific notation
        formatter.set_scientific(True) 
        formatter.set_powerlimits((-1,1)) 
        ax.yaxis.set_major_formatter(formatter)
        # ax.set_title('Unmet Social Care Needs (mean 2025-2035)')
        ax.yaxis.grid(True)
        fig.tight_layout()
        path = os.path.join(folder, 'hospitalizedQuintilesRatio_Policies.pdf')
        pp = PdfPages(path)
        pp.savefig(fig)
        pp.close()
        
        meansOutput = []
        sdOutput = []
        for j in range(numPolicies):
            values = []
            for z in range(numRepeats):
                values.append(np.mean(output[z][i][j]['intubatedQuintilesRatio']))
            meansOutput.append(np.mean(values))
            sdOutput.append(np.std(values))
        fig, ax = plt.subplots()
        x_pos = np.arange(len(policies))
        ax.bar(x_pos, meansOutput, yerr=sdOutput, align='center', alpha=0.5, ecolor='black', capsize=10)
        ax.set_ylabel('Q1/Q5 Ratio')
        ax.set_xticks(x_pos)
        ax.set_xticklabels(policies)
        formatter = ticker.ScalarFormatter(useMathText=True) #scientific notation
        formatter.set_scientific(True) 
        formatter.set_powerlimits((-1,1)) 
        ax.yaxis.set_major_formatter(formatter)
        # ax.set_title('Unmet Social Care Needs (mean 2025-2035)')
        ax.yaxis.grid(True)
        fig.tight_layout()
        path = os.path.join(folder, 'intubatedQuintilesRatio_Policies.pdf')
        pp = PdfPages(path)
        pp.savefig(fig)
        pp.close()
        
        meansOutput = []
        sdOutput = []
        for j in range(numPolicies):
            values = []
            for z in range(numRepeats):
                values.append(np.mean(output[z][i][j]['deathsQuintilesRatio']))
            meansOutput.append(np.mean(values))
            sdOutput.append(np.std(values))
        fig, ax = plt.subplots()
        x_pos = np.arange(len(policies))
        ax.bar(x_pos, meansOutput, yerr=sdOutput, align='center', alpha=0.5, ecolor='black', capsize=10)
        ax.set_ylabel('Q1/Q5 Ratio')
        ax.set_xticks(x_pos)
        ax.set_xticklabels(policies)
        formatter = ticker.ScalarFormatter(useMathText=True) #scientific notation
        formatter.set_scientific(True) 
        formatter.set_powerlimits((-1,1)) 
        ax.yaxis.set_major_formatter(formatter)
        # ax.set_title('Unmet Social Care Needs (mean 2025-2035)')
        ax.yaxis.grid(True)
        fig.tight_layout()
        path = os.path.join(folder, 'deathsQuintilesRatio_Policies.pdf')
        pp = PdfPages(path)
        pp.savefig(fig)
        pp.close()
        
        
        meansOutput = []
        sdOutput = []
        for j in range(numPolicies):
            values = []
            for z in range(numRepeats):
                values.append(sum(output[z][i][j]['totalUnmetSocialCareNeed']))
            meansOutput.append(np.mean(values))
            sdOutput.append(np.std(values))
        fig, ax = plt.subplots()
        x_pos = np.arange(len(policies))
        ax.bar(x_pos, meansOutput, yerr=sdOutput, align='center', alpha=0.5, ecolor='black', capsize=10)
        ax.set_ylabel('Hours')
        ax.set_xticks(x_pos)
        ax.set_xticklabels(policies)
        formatter = ticker.ScalarFormatter(useMathText=True) #scientific notation
        formatter.set_scientific(True) 
        formatter.set_powerlimits((-1,1)) 
        ax.yaxis.set_major_formatter(formatter)
        # ax.set_title('Unmet Social Care Needs (mean 2025-2035)')
        ax.yaxis.grid(True)
        fig.tight_layout()
        path = os.path.join(folder, 'hoursUnmetSocialCareNeed_Policies.pdf')
        pp = PdfPages(path)
        pp.savefig(fig)
        pp.close()
        
        
        # Single historical pplot with standard errors
        for j in range(numPolicies):
            meanValues = []
            minValues = []
            maxValues = []
            days = []
            for dayOutput in range(180+1):
                dayValues = []
                for z in range(numRepeats):
                    dayValues.append(output[z][i][j].loc[output[z][i][j]['day'] == dayOutput, 'share_UnmetSocialCareNeed'].values[0])
                mean = np.mean(dayValues)
                meanValues.append(mean)
                sd = np.std(dayValues)
                minValues.append(mean-sd)
                maxValues.append(mean+sd)
                days.append(dayOutput)
            # Create charts
            fig, ax = plt.subplots() # Argument: figsize=(5, 3)
            ax.plot(days, meanValues, color="black", linewidth=2)
            ax.fill_between(days, minValues, maxValues, alpha=1, color='#3F7F4C', facecolor='#7EFF99', linewidth=0)
            ax.set_ylabel('Share')
            ax.xaxis.set_major_locator(MaxNLocator(integer=True))
            ax.set_xlim(left = int(p['statsCollectFrom']), right = int(p['endYear']))
            ax.set_xticks(range(int(p['statsCollectFrom']), int(p['endYear'])+1, 20))
            fig.tight_layout()
            path = os.path.join(folder, 'shareUnmetSocialCareNeed_' + str(j) + '.pdf')
            pp = PdfPages(path)
            pp.savefig(fig)
            pp.close()
            
            meanValues = []
            minValues = []
            maxValues = []
            days = []
            for dayOutput in range(180+1):
                dayValues = []
                for z in range(numRepeats):
                    dayValues.append(output[z][i][j].loc[output[z][i][j]['day'] == dayOutput, 'mostLeastDeprivedRatio'].values[0])
                mean = np.mean(dayValues)
                meanValues.append(mean)
                sd = np.std(dayValues)
                minValues.append(mean-sd)
                maxValues.append(mean+sd)
                days.append(dayOutput)
            # Create charts
            fig, ax = plt.subplots() # Argument: figsize=(5, 3)
            ax.plot(days, meanValues, color="black", linewidth=2)
            ax.fill_between(days, minValues, maxValues, alpha=1, color='#3F7F4C', facecolor='#7EFF99', linewidth=0)
            ax.set_ylabel('Q1/Q5 Ratio')
            ax.xaxis.set_major_locator(MaxNLocator(integer=True))
            ax.set_xlim(left = int(p['statsCollectFrom']), right = int(p['endYear']))
            ax.set_xticks(range(int(p['statsCollectFrom']), int(p['endYear'])+1, 20))
            fig.tight_layout()
            path = os.path.join(folder, 'mostLeastDeprivedRatio_' + str(j) + '.pdf')
            pp = PdfPages(path)
            pp.savefig(fig)
            pp.close()
            
            meanValues = []
            minValues = []
            maxValues = []
            days = []
            for dayOutput in range(180+1):
                dayValues = []
                for z in range(numRepeats):
                    dayValues.append(output[z][i][j].loc[output[z][i][j]['day'] == dayOutput, 'informalCareRatio'].values[0])
                mean = np.mean(dayValues)
                meanValues.append(mean)
                sd = np.std(dayValues)
                minValues.append(mean-sd)
                maxValues.append(mean+sd)
                days.append(dayOutput)
            # Create charts
            fig, ax = plt.subplots() # Argument: figsize=(5, 3)
            ax.plot(days, meanValues, color="black", linewidth=2)
            ax.fill_between(days, minValues, maxValues, alpha=1, color='#3F7F4C', facecolor='#7EFF99', linewidth=0)
            ax.set_ylabel('Q1/Q5 Ratio')
            ax.xaxis.set_major_locator(MaxNLocator(integer=True))
            ax.set_xlim(left = int(p['statsCollectFrom']), right = int(p['endYear']))
            ax.set_xticks(range(int(p['statsCollectFrom']), int(p['endYear'])+1, 20))
            fig.tight_layout()
            path = os.path.join(folder, 'informalCareRatio_' + str(j) + '.pdf')
            pp = PdfPages(path)
            pp.savefig(fig)
            pp.close()
            
            meanValues = []
            minValues = []
            maxValues = []
            days = []
            for dayOutput in range(180+1):
                dayValues = []
                for z in range(numRepeats):
                    dayValues.append(output[z][i][j].loc[output[z][i][j]['day'] == dayOutput, 'careNeedRatio'].values[0])
                mean = np.mean(dayValues)
                meanValues.append(mean)
                sd = np.std(dayValues)
                minValues.append(mean-sd)
                maxValues.append(mean+sd)
                days.append(dayOutput)
            # Create charts
            fig, ax = plt.subplots() # Argument: figsize=(5, 3)
            ax.plot(days, meanValues, color="black", linewidth=2)
            ax.fill_between(days, minValues, maxValues, alpha=1, color='#3F7F4C', facecolor='#7EFF99', linewidth=0)
            ax.set_ylabel('Q1/Q5 Ratio')
            ax.xaxis.set_major_locator(MaxNLocator(integer=True))
            ax.set_xlim(left = int(p['statsCollectFrom']), right = int(p['endYear']))
            ax.set_xticks(range(int(p['statsCollectFrom']), int(p['endYear'])+1, 20))
            fig.tight_layout()
            path = os.path.join(folder, 'careNeedRatio_' + str(j) + '.pdf')
            pp = PdfPages(path)
            pp.savefig(fig)
            pp.close()
       
            meanValues = []
            minValues = []
            maxValues = []
            days = []
            for dayOutput in range(180+1):
                dayValues = []
                for z in range(numRepeats):
                    dayValues.append(output[z][i][j].loc[output[z][i][j]['day'] == dayOutput, 'hospitalizedQuintilesRatio'].values[0])
                mean = np.mean(dayValues)
                meanValues.append(mean)
                sd = np.std(dayValues)
                minValues.append(mean-sd)
                maxValues.append(mean+sd)
                days.append(dayOutput)
            # Create charts
            fig, ax = plt.subplots() # Argument: figsize=(5, 3)
            ax.plot(days, meanValues, color="black", linewidth=2)
            ax.fill_between(days, minValues, maxValues, alpha=1, color='#3F7F4C', facecolor='#7EFF99', linewidth=0)
            ax.set_ylabel('Q1/Q5 Ratio')
            ax.xaxis.set_major_locator(MaxNLocator(integer=True))
            ax.set_xlim(left = int(p['statsCollectFrom']), right = int(p['endYear']))
            ax.set_xticks(range(int(p['statsCollectFrom']), int(p['endYear'])+1, 20))
            fig.tight_layout()
            path = os.path.join(folder, 'hospitalizedQuintilesRatio_' + str(j) + '.pdf')
            pp = PdfPages(path)
            pp.savefig(fig)
            pp.close()
            
            meanValues = []
            minValues = []
            maxValues = []
            days = []
            for dayOutput in range(180+1):
                dayValues = []
                for z in range(numRepeats):
                    dayValues.append(output[z][i][j].loc[output[z][i][j]['day'] == dayOutput, 'intubatedQuintilesRatio'].values[0])
                mean = np.mean(dayValues)
                meanValues.append(mean)
                sd = np.std(dayValues)
                minValues.append(mean-sd)
                maxValues.append(mean+sd)
                days.append(dayOutput)
            # Create charts
            fig, ax = plt.subplots() # Argument: figsize=(5, 3)
            ax.plot(days, meanValues, color="black", linewidth=2)
            ax.fill_between(days, minValues, maxValues, alpha=1, color='#3F7F4C', facecolor='#7EFF99', linewidth=0)
            ax.set_ylabel('Q1/Q5 Ratio')
            ax.xaxis.set_major_locator(MaxNLocator(integer=True))
            ax.set_xlim(left = int(p['statsCollectFrom']), right = int(p['endYear']))
            ax.set_xticks(range(int(p['statsCollectFrom']), int(p['endYear'])+1, 20))
            fig.tight_layout()
            path = os.path.join(folder, 'intubatedQuintilesRatio_' + str(j) + '.pdf')
            pp = PdfPages(path)
            pp.savefig(fig)
            pp.close()
            
            meanValues = []
            minValues = []
            maxValues = []
            days = []
            for dayOutput in range(180+1):
                dayValues = []
                for z in range(numRepeats):
                    dayValues.append(output[z][i][j].loc[output[z][i][j]['day'] == dayOutput, 'deathsQuintilesRatio'].values[0])
                mean = np.mean(dayValues)
                meanValues.append(mean)
                sd = np.std(dayValues)
                minValues.append(mean-sd)
                maxValues.append(mean+sd)
                days.append(dayOutput)
            # Create charts
            fig, ax = plt.subplots() # Argument: figsize=(5, 3)
            ax.plot(days, meanValues, color="black", linewidth=2)
            ax.fill_between(days, minValues, maxValues, alpha=1, color='#3F7F4C', facecolor='#7EFF99', linewidth=0)
            ax.set_ylabel('Q1/Q5 Ratio')
            ax.xaxis.set_major_locator(MaxNLocator(integer=True))
            ax.set_xlim(left = int(p['statsCollectFrom']), right = int(p['endYear']))
            ax.set_xticks(range(int(p['statsCollectFrom']), int(p['endYear'])+1, 20))
            fig.tight_layout()
            path = os.path.join(folder, 'deathsQuintilesRatio_' + str(j) + '.pdf')
            pp = PdfPages(path)
            pp.savefig(fig)
            pp.close()

        # Bar charts with error bars
        meansOutput = []
        sdOutput = []
        for j in range(numPolicies):
            values = []
            for z in range(numRepeats):
                s1 = sum(output[z][i][j]['totalInformalSocialCare'])
                s2 = sum(output[z][i][j]['totalFormalSocialCare'])
                s3 = sum(output[z][i][j]['publicSocialCare'])
                values.append(s1+s2+s3)
            meansOutput.append(np.mean(values))
            sdOutput.append(np.std(values))
        fig, ax = plt.subplots()
        x_pos = np.arange(len(policies))
        ax.bar(x_pos, meansOutput, yerr=sdOutput, align='center', alpha=0.5, ecolor='black', capsize=10)
        ax.set_ylabel('Hours')
        ax.set_xticks(x_pos)
        ax.set_xticklabels(policies)
        formatter = ticker.ScalarFormatter(useMathText=True) #scientific notation
        formatter.set_scientific(True) 
        formatter.set_powerlimits((-1,1)) 
        ax.yaxis.set_major_formatter(formatter)
        # ax.set_title('Unmet Social Care Needs (mean 2025-2035)')
        ax.yaxis.grid(True)
        fig.tight_layout()
        path = os.path.join(folder, 'totalCareDelivered.pdf')
        pp = PdfPages(path)
        pp.savefig(fig)
        pp.close()

    
    for i in range(numScenarios):
        
        scenarioFolder = folder + '/Scenario ' + str(i+1)
        if not os.path.exists(scenarioFolder):
            os.makedirs(scenarioFolder)
        
        # Share of Unmet Social Care: mean and sd across the n repeats for the 5 policies.
        meansOutput = []
        sdOutput = []
        for j in range(numPolicies):
            values = []
            for z in range(numRepeats):
                policyWindow = []
                for yearOutput in range(2025, 2036, 1):
                    policyWindow.append(output[z][i][j].loc[output[z][i][j]['year'] == yearOutput, 'share_UnmetSocialCareNeed'].values[0])
                values.append(np.mean(policyWindow))
            meansOutput.append(np.mean(values))
            sdOutput.append(np.std(values))
        fig, ax = plt.subplots()
        x_pos = np.arange(len(policies))
        ax.bar(x_pos, meansOutput, yerr=sdOutput, align='center', alpha=0.5, ecolor='black', capsize=10)
        ax.set_ylabel('Share of Unmet Social Care')
        ax.set_xticks(x_pos)
        ax.set_xticklabels(policies)
        ax.set_title('Shares of Unmet Social Care (mean 2025-2035)')
        ax.yaxis.grid(True)
    
        fig.tight_layout()
        path = os.path.join(scenarioFolder, 'shareUnmetSocialCareNeed.pdf')
        pp = PdfPages(path)
        pp.savefig(fig)
        pp.close()
        
        # Hours of Unmet Social Care: mean and sd across the n repeats for the 5 policies.
        meansOutput = []
        sdOutput = []
        for j in range(numPolicies):
            values = []
            for z in range(numRepeats):
                policyWindow = []
                for yearOutput in range(2025, 2036, 1):
                    policyWindow.append(output[z][i][j].loc[output[z][i][j]['year'] == yearOutput, 'totalUnmetSocialCareNeed'].values[0])
                values.append(np.mean(policyWindow))
            meansOutput.append(np.mean(values))
            sdOutput.append(np.std(values))
        fig, ax = plt.subplots()
        x_pos = np.arange(len(policies))
        ax.bar(x_pos, meansOutput, yerr=sdOutput, align='center', alpha=0.5, ecolor='black', capsize=10)
        ax.set_ylabel('Hours per week')
        ax.set_xticks(x_pos)
        ax.set_xticklabels(policies)
        ax.set_title('Unmet Social Care Needs (mean 2025-2035)')
        ax.yaxis.grid(True)
    
        fig.tight_layout()
        path = os.path.join(scenarioFolder, 'hoursUnmetSocialCareNeed.pdf')
        pp = PdfPages(path)
        pp.savefig(fig)
        pp.close()
        
        # Direct policy cost (total)
        meansOutput = []
        sdOutput = []
        for j in range(numPolicies):
            values = []
            for z in range(numRepeats):
                policyWindow = []
                for yearOutput in range(2025, 2036, 1):
                    tfc = output[z][i][j].loc[output[z][i][j]['year'] == yearOutput, 'costTaxFreeChildCare'].values[0]
                    pc = output[z][i][j].loc[output[z][i][j]['year'] == yearOutput, 'costPublicChildCare'].values[0]
                    ps = output[z][i][j].loc[output[z][i][j]['year'] == yearOutput, 'costPublicSocialCare'].values[0]
                    tfs = output[z][i][j].loc[output[z][i][j]['year'] == yearOutput, 'costTaxFreeSocialCare'].values[0]
                    policyWindow.append(tfc+pc+ps+tfs)
                values.append(np.mean(policyWindow))
            meansOutput.append(np.mean(values))
            sdOutput.append(np.std(values))
        fig, ax = plt.subplots()
        x_pos = np.arange(len(policies))
        ax.bar(x_pos, meansOutput, yerr=sdOutput, align='center', alpha=0.5, ecolor='black', capsize=10)
        ax.set_ylabel('Pounds per week')
        ax.set_xticks(x_pos)
        ax.set_xticklabels(policies)
        ax.set_title('Direct Policy Cost (mean 2025-2035)')
        ax.yaxis.grid(True)
    
        fig.tight_layout()
        path = os.path.join(scenarioFolder, 'directPolicyCost.pdf')
        pp = PdfPages(path)
        pp.savefig(fig)
        pp.close()
        
        # ICERD
        newPolicies = policies[1:]
        meansOutput = []
        sdOutput = []
        for j in range(1, numPolicies):
            values = []
            for z in range(numRepeats):
                policyWindow = []
                for yearOutput in range(2025, 2036, 1):
                    tfc = output[z][i][j].loc[output[z][i][j]['year'] == yearOutput, 'costTaxFreeChildCare'].values[0]
                    pc = output[z][i][j].loc[output[z][i][j]['year'] == yearOutput, 'costPublicChildCare'].values[0]
                    ps = output[z][i][j].loc[output[z][i][j]['year'] == yearOutput, 'costPublicSocialCare'].values[0]
                    tfs = output[z][i][j].loc[output[z][i][j]['year'] == yearOutput, 'costTaxFreeSocialCare'].values[0]
                    policyCost = tfc+pc+ps+tfs
                    tfc = output[z][i][j].loc[output[z][i][0]['year'] == yearOutput, 'costTaxFreeChildCare'].values[0]
                    pc = output[z][i][j].loc[output[z][i][0]['year'] == yearOutput, 'costPublicChildCare'].values[0]
                    ps = output[z][i][j].loc[output[z][i][0]['year'] == yearOutput, 'costPublicSocialCare'].values[0]
                    tfs = output[z][i][j].loc[output[z][i][0]['year'] == yearOutput, 'costTaxFreeSocialCare'].values[0]
                    benchmarkCost = tfc+pc+ps+tfs
                    deltaCost = policyCost-benchmarkCost
                    hourUnmetCarePolicy = output[z][i][j].loc[output[z][i][j]['year'] == yearOutput, 'totalUnmetSocialCareNeed'].values[0]
                    hourUnmetCareBenchmark = output[z][i][j].loc[output[z][i][0]['year'] == yearOutput, 'totalUnmetSocialCareNeed'].values[0]
                    deltaCare = hourUnmetCareBenchmark-hourUnmetCarePolicy
                    policyWindow.append(deltaCost/deltaCare)
                values.append(np.mean(policyWindow))
            meansOutput.append(np.mean(values))
            sdOutput.append(np.std(values))
        fig, ax = plt.subplots()
        x_pos = np.arange(len(newPolicies))
        ax.bar(x_pos, meansOutput, yerr=sdOutput, align='center', alpha=0.5, ecolor='black', capsize=10)
        ax.set_ylabel('Pounds per hour')
        ax.set_xticks(x_pos)
        ax.set_xticklabels(newPolicies)
        ax.set_title('Direct Cost ICER (mean 2025-2035)')
        ax.yaxis.grid(True)
    
        fig.tight_layout()
        path = os.path.join(scenarioFolder, 'directICER.pdf')
        pp = PdfPages(path)
        pp.savefig(fig)
        pp.close()
        
        # Hospitalization cost
        meansOutput = []
        sdOutput = []
        for j in range(numPolicies):
            values = []
            for z in range(numRepeats):
                policyWindow = []
                for yearOutput in range(2025, 2036, 1):
                    policyWindow.append(output[z][i][j].loc[output[z][i][j]['year'] == yearOutput, 'totalHospitalizationCost'].values[0]/52.0)
                values.append(np.mean(policyWindow))
            meansOutput.append(np.mean(values))
            sdOutput.append(np.std(values))
        fig, ax = plt.subplots()
        x_pos = np.arange(len(policies))
        ax.bar(x_pos, meansOutput, yerr=sdOutput, align='center', alpha=0.5, ecolor='black', capsize=10)
        ax.set_ylabel('Pounds per week')
        ax.set_xticks(x_pos)
        ax.set_xticklabels(policies)
        ax.set_title('Hospitalization Costs (mean 2025-2035)')
        ax.yaxis.grid(True)
    
        fig.tight_layout()
        path = os.path.join(scenarioFolder, 'hospitalizationCosts.pdf')
        pp = PdfPages(path)
        pp.savefig(fig)
        pp.close()
        
        
        ############    Bar charts: pandemic effects by income quintilie and age class  #########################

    for i in range(numScenarios):
        
        folder = simFolder + '/MultipleRepeatsGraphs/' + '/Scenario_' + str(i+1)
        if not os.path.exists(folder):
            os.makedirs(folder)

        for j in range(numPolicies):
            
            policyFolder = folder + '/Policy_' + str(j+1)
            if not os.path.exists(folder):
                os.makedirs(folder)
                
            # Hours of unmet care need
            
            groups = ['Q1', 'Q2', 'Q3', 'Q4', 'Q5']
            outputsByGroup_0 = []
            outputsByGroup_1 = []
            outputsByGroup_2 = []
            outputsByGroup_3 = []
            outputsByGroup_4 = []
            for z in range(numRepeats):
                outputsByGroup_0.append(np.sum(output[z][i][j]['unmetSocialCareNeed_Q1']))
                outputsByGroup_1.append(np.sum(output[z][i][j]['unmetSocialCareNeed_Q2']))
                outputsByGroup_2.append(np.sum(output[z][i][j]['unmetSocialCareNeed_Q3']))
                outputsByGroup_3.append(np.sum(output[z][i][j]['unmetSocialCareNeed_Q4']))
                outputsByGroup_4.append(np.sum(output[z][i][j]['unmetSocialCareNeed_Q5']))
            meansOutput = [np.mean(outputsByGroup_0), np.mean(outputsByGroup_1), np.mean(outputsByGroup_2), np.mean(outputsByGroup_3), np.mean(outputsByGroup_4)]
            sdOutput = [np.std(outputsByGroup_0), np.std(outputsByGroup_1), np.std(outputsByGroup_2), np.std(outputsByGroup_3), np.std(outputsByGroup_4)]
            fig, ax = plt.subplots()
            x_pos = np.arange(len(groups))
            ax.bar(x_pos, meansOutput, yerr=sdOutput, align='center', alpha=0.5, ecolor='black', capsize=10)
            ax.set_ylabel('Total hours')
            ax.set_xticks(x_pos)
            ax.set_xticklabels(policies)
            # ax.set_title('Hospitalization Costs (mean 2025-2035)')
            ax.yaxis.grid(True)
            fig.tight_layout()
            path = os.path.join(policyFolder, 'totalUnmetCareNeedBarChart.pdf')
            pp = PdfPages(path)
            pp.savefig(fig)
            pp.close()
            
            groups = ['Q1', 'Q2', 'Q3', 'Q4', 'Q5']
            outputsByGroup_0 = []
            outputsByGroup_1 = []
            outputsByGroup_2 = []
            outputsByGroup_3 = []
            outputsByGroup_4 = []
            for z in range(numRepeats):
                outputsByGroup_0.append(np.sum(output[z][i][j]['totalInformalSocialCare_Q1']))
                outputsByGroup_1.append(np.sum(output[z][i][j]['totalInformalSocialCare_Q2']))
                outputsByGroup_2.append(np.sum(output[z][i][j]['totalInformalSocialCare_Q3']))
                outputsByGroup_3.append(np.sum(output[z][i][j]['totalInformalSocialCare_Q4']))
                outputsByGroup_4.append(np.sum(output[z][i][j]['totalInformalSocialCare_Q5']))
            meansOutput = [np.mean(outputsByGroup_0), np.mean(outputsByGroup_1), np.mean(outputsByGroup_2), np.mean(outputsByGroup_3), np.mean(outputsByGroup_4)]
            sdOutput = [np.std(outputsByGroup_0), np.std(outputsByGroup_1), np.std(outputsByGroup_2), np.std(outputsByGroup_3), np.std(outputsByGroup_4)]
            fig, ax = plt.subplots()
            x_pos = np.arange(len(groups))
            ax.bar(x_pos, meansOutput, yerr=sdOutput, align='center', alpha=0.5, ecolor='black', capsize=10)
            ax.set_ylabel('Total hours')
            ax.set_xticks(x_pos)
            ax.set_xticklabels(policies)
            # ax.set_title('Hospitalization Costs (mean 2025-2035)')
            ax.yaxis.grid(True)
            fig.tight_layout()
            path = os.path.join(policyFolder, 'totalInformalSocialCareBarChart.pdf')
            pp = PdfPages(path)
            pp.savefig(fig)
            pp.close()
            
            groups = ['Q1', 'Q2', 'Q3', 'Q4', 'Q5']
            outputsByGroup_0 = []
            outputsByGroup_1 = []
            outputsByGroup_2 = []
            outputsByGroup_3 = []
            outputsByGroup_4 = []
            for z in range(numRepeats):
                outputsByGroup_0.append(np.sum(output[z][i][j]['totalSocialCareNeed_Q1']))
                outputsByGroup_1.append(np.sum(output[z][i][j]['totalSocialCareNeed_Q2']))
                outputsByGroup_2.append(np.sum(output[z][i][j]['totalSocialCareNeed_Q3']))
                outputsByGroup_3.append(np.sum(output[z][i][j]['totalSocialCareNeed_Q4']))
                outputsByGroup_4.append(np.sum(output[z][i][j]['totalSocialCareNeed_Q5']))
            meansOutput = [np.mean(outputsByGroup_0), np.mean(outputsByGroup_1), np.mean(outputsByGroup_2), np.mean(outputsByGroup_3), np.mean(outputsByGroup_4)]
            sdOutput = [np.std(outputsByGroup_0), np.std(outputsByGroup_1), np.std(outputsByGroup_2), np.std(outputsByGroup_3), np.std(outputsByGroup_4)]
            fig, ax = plt.subplots()
            x_pos = np.arange(len(groups))
            ax.bar(x_pos, meansOutput, yerr=sdOutput, align='center', alpha=0.5, ecolor='black', capsize=10)
            ax.set_ylabel('Total hours')
            ax.set_xticks(x_pos)
            ax.set_xticklabels(policies)
            # ax.set_title('Hospitalization Costs (mean 2025-2035)')
            ax.yaxis.grid(True)
            fig.tight_layout()
            path = os.path.join(policyFolder, 'totalSocialCareNeedBarChart.pdf')
            pp = PdfPages(path)
            pp.savefig(fig)
            pp.close()
            
            
            # Infected
            
            groups = ['Q1', 'Q2', 'Q3', 'Q4', 'Q5']
            outputsByGroup_0 = []
            outputsByGroup_1 = []
            outputsByGroup_2 = []
            outputsByGroup_3 = []
            outputsByGroup_4 = []
            for z in range(numRepeats):
                outputsByGroup_0.append(np.sum(output[z][i][j]['infectedByClass_0']))
                outputsByGroup_1.append(np.sum(output[z][i][j]['infectedByClass_1']))
                outputsByGroup_2.append(np.sum(output[z][i][j]['infectedByClass_2']))
                outputsByGroup_3.append(np.sum(output[z][i][j]['infectedByClass_3']))
                outputsByGroup_4.append(np.sum(output[z][i][j]['infectedByClass_4']))
            meansOutput = [np.mean(outputsByGroup_0), np.mean(outputsByGroup_1), np.mean(outputsByGroup_2), np.mean(outputsByGroup_3), np.mean(outputsByGroup_4)]
            sdOutput = [np.std(outputsByGroup_0), np.std(outputsByGroup_1), np.std(outputsByGroup_2), np.std(outputsByGroup_3), np.std(outputsByGroup_4)]
            fig, ax = plt.subplots()
            x_pos = np.arange(len(groups))
            ax.bar(x_pos, meansOutput, yerr=sdOutput, align='center', alpha=0.5, ecolor='black', capsize=10)
            ax.set_ylabel('Number Infected')
            ax.set_xticks(x_pos)
            ax.set_xticklabels(policies)
            # ax.set_title('Hospitalization Costs (mean 2025-2035)')
            ax.yaxis.grid(True)
            fig.tight_layout()
            path = os.path.join(policyFolder, 'infectedByQuintilesBarChart.pdf')
            pp = PdfPages(path)
            pp.savefig(fig)
            pp.close()
        
            groups = ['0-10', '10-20', '20-30', '30-40', '40-50', '50-60', '60-70', '70-80', '80+']
            outputsByGroup_0 = []
            outputsByGroup_1 = []
            outputsByGroup_2 = []
            outputsByGroup_3 = []
            outputsByGroup_4 = []
            outputsByGroup_5 = []
            outputsByGroup_6 = []
            outputsByGroup_7 = []
            outputsByGroup_8 = []
            for z in range(numRepeats):
                outputsByGroup_0.append(np.sum(output[z][i][j]['infectedByAge_0']))
                outputsByGroup_1.append(np.sum(output[z][i][j]['infectedByAge_1']))
                outputsByGroup_2.append(np.sum(output[z][i][j]['infectedByAge_2']))
                outputsByGroup_3.append(np.sum(output[z][i][j]['infectedByAge_3']))
                outputsByGroup_4.append(np.sum(output[z][i][j]['infectedByAge_4']))
                outputsByGroup_5.append(np.sum(output[z][i][j]['infectedByAge_5']))
                outputsByGroup_6.append(np.sum(output[z][i][j]['infectedByAge_6']))
                outputsByGroup_7.append(np.sum(output[z][i][j]['infectedByAge_7']))
                outputsByGroup_8.append(np.sum(output[z][i][j]['infectedByAge_8']))
            meansOutput = [np.mean(outputsByGroup_0), np.mean(outputsByGroup_1), np.mean(outputsByGroup_2), np.mean(outputsByGroup_3), np.mean(outputsByGroup_4),
                           np.mean(outputsByGroup_5), np.mean(outputsByGroup_6), np.mean(outputsByGroup_7), np.mean(outputsByGroup_8)]
            sdOutput = [np.std(outputsByGroup_0), np.std(outputsByGroup_1), np.std(outputsByGroup_2), np.std(outputsByGroup_3), np.std(outputsByGroup_4),
                        np.std(outputsByGroup_5), np.std(outputsByGroup_6), np.std(outputsByGroup_7), np.std(outputsByGroup_8)]
            fig, ax = plt.subplots()
            x_pos = np.arange(len(groups))
            ax.bar(x_pos, meansOutput, yerr=sdOutput, align='center', alpha=0.5, ecolor='black', capsize=10)
            ax.set_ylabel('Number Infected')
            ax.set_xticks(x_pos)
            ax.set_xticklabels(policies)
            # ax.set_title('Hospitalization Costs (mean 2025-2035)')
            ax.yaxis.grid(True)
            fig.tight_layout()
            path = os.path.join(policyFolder, 'infectedByAgeBarChart.pdf')
            pp = PdfPages(path)
            pp.savefig(fig)
            pp.close()
        
       
            # 2 - Hospitalized
            
            groups = ['Q1', 'Q2', 'Q3', 'Q4', 'Q5']
            outputsByGroup_0 = []
            outputsByGroup_1 = []
            outputsByGroup_2 = []
            outputsByGroup_3 = []
            outputsByGroup_4 = []
            for z in range(numRepeats):
                outputsByGroup_0.append(np.sum(output[z][i][j]['hospitalizedByClass_0']))
                outputsByGroup_1.append(np.sum(output[z][i][j]['hospitalizedByClass_1']))
                outputsByGroup_2.append(np.sum(output[z][i][j]['hospitalizedByClass_2']))
                outputsByGroup_3.append(np.sum(output[z][i][j]['hospitalizedByClass_3']))
                outputsByGroup_4.append(np.sum(output[z][i][j]['hospitalizedByClass_4']))
            meansOutput = [np.mean(outputsByGroup_0), np.mean(outputsByGroup_1), np.mean(outputsByGroup_2), np.mean(outputsByGroup_3), np.mean(outputsByGroup_4)]
            sdOutput = [np.std(outputsByGroup_0), np.std(outputsByGroup_1), np.std(outputsByGroup_2), np.std(outputsByGroup_3), np.std(outputsByGroup_4)]
            fig, ax = plt.subplots()
            x_pos = np.arange(len(groups))
            ax.bar(x_pos, meansOutput, yerr=sdOutput, align='center', alpha=0.5, ecolor='black', capsize=10)
            ax.set_ylabel('Number hospitalized')
            ax.set_xticks(x_pos)
            ax.set_xticklabels(policies)
            # ax.set_title('Hospitalization Costs (mean 2025-2035)')
            ax.yaxis.grid(True)
            fig.tight_layout()
            path = os.path.join(policyFolder, 'hospitalizedByQuintilesBarChart.pdf')
            pp = PdfPages(path)
            pp.savefig(fig)
            pp.close()
        
            groups = ['0-10', '10-20', '20-30', '30-40', '40-50', '50-60', '60-70', '70-80', '80+']
            outputsByGroup_0 = []
            outputsByGroup_1 = []
            outputsByGroup_2 = []
            outputsByGroup_3 = []
            outputsByGroup_4 = []
            outputsByGroup_5 = []
            outputsByGroup_6 = []
            outputsByGroup_7 = []
            outputsByGroup_8 = []
            for z in range(numRepeats):
                outputsByGroup_0.append(np.sum(output[z][i][j]['hospitalizedByAge_0']))
                outputsByGroup_1.append(np.sum(output[z][i][j]['hospitalizedByAge_1']))
                outputsByGroup_2.append(np.sum(output[z][i][j]['hospitalizedByAge_2']))
                outputsByGroup_3.append(np.sum(output[z][i][j]['hospitalizedByAge_3']))
                outputsByGroup_4.append(np.sum(output[z][i][j]['hospitalizedByAge_4']))
                outputsByGroup_5.append(np.sum(output[z][i][j]['hospitalizedByAge_5']))
                outputsByGroup_6.append(np.sum(output[z][i][j]['hospitalizedByAge_6']))
                outputsByGroup_7.append(np.sum(output[z][i][j]['hospitalizedByAge_7']))
                outputsByGroup_8.append(np.sum(output[z][i][j]['hospitalizedByAge_8']))
            meansOutput = [np.mean(outputsByGroup_0), np.mean(outputsByGroup_1), np.mean(outputsByGroup_2), np.mean(outputsByGroup_3), np.mean(outputsByGroup_4),
                           np.mean(outputsByGroup_5), np.mean(outputsByGroup_6), np.mean(outputsByGroup_7), np.mean(outputsByGroup_8)]
            sdOutput = [np.std(outputsByGroup_0), np.std(outputsByGroup_1), np.std(outputsByGroup_2), np.std(outputsByGroup_3), np.std(outputsByGroup_4),
                        np.std(outputsByGroup_5), np.std(outputsByGroup_6), np.std(outputsByGroup_7), np.std(outputsByGroup_8)]
            fig, ax = plt.subplots()
            x_pos = np.arange(len(groups))
            ax.bar(x_pos, meansOutput, yerr=sdOutput, align='center', alpha=0.5, ecolor='black', capsize=10)
            ax.set_ylabel('Number hospitalized')
            ax.set_xticks(x_pos)
            ax.set_xticklabels(policies)
            # ax.set_title('Hospitalization Costs (mean 2025-2035)')
            ax.yaxis.grid(True)
            fig.tight_layout()
            path = os.path.join(policyFolder, 'hospitalizedByAgeBarChart.pdf')
            pp = PdfPages(path)
            pp.savefig(fig)
            pp.close()
        
            # 3- Intubated
            
            groups = ['Q1', 'Q2', 'Q3', 'Q4', 'Q5']
            outputsByGroup_0 = []
            outputsByGroup_1 = []
            outputsByGroup_2 = []
            outputsByGroup_3 = []
            outputsByGroup_4 = []
            for z in range(numRepeats):
                outputsByGroup_0.append(np.sum(output[z][i][j]['intubatedByClass_0']))
                outputsByGroup_1.append(np.sum(output[z][i][j]['intubatedByClass_1']))
                outputsByGroup_2.append(np.sum(output[z][i][j]['intubatedByClass_2']))
                outputsByGroup_3.append(np.sum(output[z][i][j]['intubatedByClass_3']))
                outputsByGroup_4.append(np.sum(output[z][i][j]['intubatedByClass_4']))
            meansOutput = [np.mean(outputsByGroup_0), np.mean(outputsByGroup_1), np.mean(outputsByGroup_2), np.mean(outputsByGroup_3), np.mean(outputsByGroup_4)]
            sdOutput = [np.std(outputsByGroup_0), np.std(outputsByGroup_1), np.std(outputsByGroup_2), np.std(outputsByGroup_3), np.std(outputsByGroup_4)]
            fig, ax = plt.subplots()
            x_pos = np.arange(len(groups))
            ax.bar(x_pos, meansOutput, yerr=sdOutput, align='center', alpha=0.5, ecolor='black', capsize=10)
            ax.set_ylabel('Number intubated')
            ax.set_xticks(x_pos)
            ax.set_xticklabels(policies)
            # ax.set_title('Hospitalization Costs (mean 2025-2035)')
            ax.yaxis.grid(True)
            fig.tight_layout()
            path = os.path.join(policyFolder, 'intubatedByQuintilesBarChart.pdf')
            pp = PdfPages(path)
            pp.savefig(fig)
            pp.close()
        
            groups = ['0-10', '10-20', '20-30', '30-40', '40-50', '50-60', '60-70', '70-80', '80+']
            outputsByGroup_0 = []
            outputsByGroup_1 = []
            outputsByGroup_2 = []
            outputsByGroup_3 = []
            outputsByGroup_4 = []
            outputsByGroup_5 = []
            outputsByGroup_6 = []
            outputsByGroup_7 = []
            outputsByGroup_8 = []
            for z in range(numRepeats):
                outputsByGroup_0.append(np.sum(output[z][i][j]['intubatedByAge_0']))
                outputsByGroup_1.append(np.sum(output[z][i][j]['intubatedByAge_1']))
                outputsByGroup_2.append(np.sum(output[z][i][j]['intubatedByAge_2']))
                outputsByGroup_3.append(np.sum(output[z][i][j]['intubatedByAge_3']))
                outputsByGroup_4.append(np.sum(output[z][i][j]['intubatedByAge_4']))
                outputsByGroup_5.append(np.sum(output[z][i][j]['intubatedByAge_5']))
                outputsByGroup_6.append(np.sum(output[z][i][j]['intubatedByAge_6']))
                outputsByGroup_7.append(np.sum(output[z][i][j]['intubatedByAge_7']))
                outputsByGroup_8.append(np.sum(output[z][i][j]['intubatedByAge_8']))
            meansOutput = [np.mean(outputsByGroup_0), np.mean(outputsByGroup_1), np.mean(outputsByGroup_2), np.mean(outputsByGroup_3), np.mean(outputsByGroup_4),
                           np.mean(outputsByGroup_5), np.mean(outputsByGroup_6), np.mean(outputsByGroup_7), np.mean(outputsByGroup_8)]
            sdOutput = [np.std(outputsByGroup_0), np.std(outputsByGroup_1), np.std(outputsByGroup_2), np.std(outputsByGroup_3), np.std(outputsByGroup_4),
                        np.std(outputsByGroup_5), np.std(outputsByGroup_6), np.std(outputsByGroup_7), np.std(outputsByGroup_8)]
            fig, ax = plt.subplots()
            x_pos = np.arange(len(groups))
            ax.bar(x_pos, meansOutput, yerr=sdOutput, align='center', alpha=0.5, ecolor='black', capsize=10)
            ax.set_ylabel('Number intubated')
            ax.set_xticks(x_pos)
            ax.set_xticklabels(policies)
            # ax.set_title('Hospitalization Costs (mean 2025-2035)')
            ax.yaxis.grid(True)
            fig.tight_layout()
            path = os.path.join(policyFolder, 'intubatedByAgeBarChart.pdf')
            pp = PdfPages(path)
            pp.savefig(fig)
            pp.close()
        
            # 4 - Symptomatic
            
            groups = ['Q1', 'Q2', 'Q3', 'Q4', 'Q5']
            outputsByGroup_0 = []
            outputsByGroup_1 = []
            outputsByGroup_2 = []
            outputsByGroup_3 = []
            outputsByGroup_4 = []
            for z in range(numRepeats):
                outputsByGroup_0.append(np.sum(output[z][i][j]['symptomaticByClass_0']))
                outputsByGroup_1.append(np.sum(output[z][i][j]['symptomaticByClass_1']))
                outputsByGroup_2.append(np.sum(output[z][i][j]['symptomaticByClass_2']))
                outputsByGroup_3.append(np.sum(output[z][i][j]['symptomaticByClass_3']))
                outputsByGroup_4.append(np.sum(output[z][i][j]['symptomaticByClass_4']))
            meansOutput = [np.mean(outputsByGroup_0), np.mean(outputsByGroup_1), np.mean(outputsByGroup_2), np.mean(outputsByGroup_3), np.mean(outputsByGroup_4)]
            sdOutput = [np.std(outputsByGroup_0), np.std(outputsByGroup_1), np.std(outputsByGroup_2), np.std(outputsByGroup_3), np.std(outputsByGroup_4)]
            fig, ax = plt.subplots()
            x_pos = np.arange(len(groups))
            ax.bar(x_pos, meansOutput, yerr=sdOutput, align='center', alpha=0.5, ecolor='black', capsize=10)
            ax.set_ylabel('Number symptomatic')
            ax.set_xticks(x_pos)
            ax.set_xticklabels(policies)
            # ax.set_title('Hospitalization Costs (mean 2025-2035)')
            ax.yaxis.grid(True)
            fig.tight_layout()
            path = os.path.join(policyFolder, 'symptomaticByQuintilesBarChart.pdf')
            pp = PdfPages(path)
            pp.savefig(fig)
            pp.close()
        
            groups = ['0-10', '10-20', '20-30', '30-40', '40-50', '50-60', '60-70', '70-80', '80+']
            outputsByGroup_0 = []
            outputsByGroup_1 = []
            outputsByGroup_2 = []
            outputsByGroup_3 = []
            outputsByGroup_4 = []
            outputsByGroup_5 = []
            outputsByGroup_6 = []
            outputsByGroup_7 = []
            outputsByGroup_8 = []
            for z in range(numRepeats):
                outputsByGroup_0.append(np.sum(output[z][i][j]['symptomaticByAge_0']))
                outputsByGroup_1.append(np.sum(output[z][i][j]['symptomaticByAge_1']))
                outputsByGroup_2.append(np.sum(output[z][i][j]['symptomaticByAge_2']))
                outputsByGroup_3.append(np.sum(output[z][i][j]['symptomaticByAge_3']))
                outputsByGroup_4.append(np.sum(output[z][i][j]['symptomaticByAge_4']))
                outputsByGroup_5.append(np.sum(output[z][i][j]['symptomaticByAge_5']))
                outputsByGroup_6.append(np.sum(output[z][i][j]['symptomaticByAge_6']))
                outputsByGroup_7.append(np.sum(output[z][i][j]['symptomaticByAge_7']))
                outputsByGroup_8.append(np.sum(output[z][i][j]['symptomaticByAge_8']))
            meansOutput = [np.mean(outputsByGroup_0), np.mean(outputsByGroup_1), np.mean(outputsByGroup_2), np.mean(outputsByGroup_3), np.mean(outputsByGroup_4),
                           np.mean(outputsByGroup_5), np.mean(outputsByGroup_6), np.mean(outputsByGroup_7), np.mean(outputsByGroup_8)]
            sdOutput = [np.std(outputsByGroup_0), np.std(outputsByGroup_1), np.std(outputsByGroup_2), np.std(outputsByGroup_3), np.std(outputsByGroup_4),
                        np.std(outputsByGroup_5), np.std(outputsByGroup_6), np.std(outputsByGroup_7), np.std(outputsByGroup_8)]
            fig, ax = plt.subplots()
            x_pos = np.arange(len(groups))
            ax.bar(x_pos, meansOutput, yerr=sdOutput, align='center', alpha=0.5, ecolor='black', capsize=10)
            ax.set_ylabel('Number symptomatic')
            ax.set_xticks(x_pos)
            ax.set_xticklabels(policies)
            # ax.set_title('Hospitalization Costs (mean 2025-2035)')
            ax.yaxis.grid(True)
            fig.tight_layout()
            path = os.path.join(policyFolder, 'symptomaticByAgeBarChart.pdf')
            pp = PdfPages(path)
            pp.savefig(fig)
            pp.close()
            
            # Deaths
            
            groups = ['Q1', 'Q2', 'Q3', 'Q4', 'Q5']
            outputsByGroup_0 = []
            outputsByGroup_1 = []
            outputsByGroup_2 = []
            outputsByGroup_3 = []
            outputsByGroup_4 = []
            for z in range(numRepeats):
                outputsByGroup_0.append(np.sum(output[z][i][j]['deathsByClass_0']))
                outputsByGroup_1.append(np.sum(output[z][i][j]['deathsByClass_1']))
                outputsByGroup_2.append(np.sum(output[z][i][j]['deathsByClass_2']))
                outputsByGroup_3.append(np.sum(output[z][i][j]['deathsByClass_3']))
                outputsByGroup_4.append(np.sum(output[z][i][j]['deathsByClass_4']))
            meansOutput = [np.mean(outputsByGroup_0), np.mean(outputsByGroup_1), np.mean(outputsByGroup_2), np.mean(outputsByGroup_3), np.mean(outputsByGroup_4)]
            sdOutput = [np.std(outputsByGroup_0), np.std(outputsByGroup_1), np.std(outputsByGroup_2), np.std(outputsByGroup_3), np.std(outputsByGroup_4)]
            fig, ax = plt.subplots()
            x_pos = np.arange(len(groups))
            ax.bar(x_pos, meansOutput, yerr=sdOutput, align='center', alpha=0.5, ecolor='black', capsize=10)
            ax.set_ylabel('Number deaths')
            ax.set_xticks(x_pos)
            ax.set_xticklabels(policies)
            # ax.set_title('Hospitalization Costs (mean 2025-2035)')
            ax.yaxis.grid(True)
            fig.tight_layout()
            path = os.path.join(policyFolder, 'deathsByQuintilesBarChart.pdf')
            pp = PdfPages(path)
            pp.savefig(fig)
            pp.close()
        
            groups = ['0-10', '10-20', '20-30', '30-40', '40-50', '50-60', '60-70', '70-80', '80+']
            outputsByGroup_0 = []
            outputsByGroup_1 = []
            outputsByGroup_2 = []
            outputsByGroup_3 = []
            outputsByGroup_4 = []
            outputsByGroup_5 = []
            outputsByGroup_6 = []
            outputsByGroup_7 = []
            outputsByGroup_8 = []
            for z in range(numRepeats):
                outputsByGroup_0.append(np.sum(output[z][i][j]['deathsByAge_0']))
                outputsByGroup_1.append(np.sum(output[z][i][j]['deathsByAge_1']))
                outputsByGroup_2.append(np.sum(output[z][i][j]['deathsByAge_2']))
                outputsByGroup_3.append(np.sum(output[z][i][j]['deathsByAge_3']))
                outputsByGroup_4.append(np.sum(output[z][i][j]['deathsByAge_4']))
                outputsByGroup_5.append(np.sum(output[z][i][j]['deathsByAge_5']))
                outputsByGroup_6.append(np.sum(output[z][i][j]['deathsByAge_6']))
                outputsByGroup_7.append(np.sum(output[z][i][j]['deathsByAge_7']))
                outputsByGroup_8.append(np.sum(output[z][i][j]['deathsByAge_8']))
            meansOutput = [np.mean(outputsByGroup_0), np.mean(outputsByGroup_1), np.mean(outputsByGroup_2), np.mean(outputsByGroup_3), np.mean(outputsByGroup_4),
                           np.mean(outputsByGroup_5), np.mean(outputsByGroup_6), np.mean(outputsByGroup_7), np.mean(outputsByGroup_8)]
            sdOutput = [np.std(outputsByGroup_0), np.std(outputsByGroup_1), np.std(outputsByGroup_2), np.std(outputsByGroup_3), np.std(outputsByGroup_4),
                        np.std(outputsByGroup_5), np.std(outputsByGroup_6), np.std(outputsByGroup_7), np.std(outputsByGroup_8)]
            fig, ax = plt.subplots()
            x_pos = np.arange(len(groups))
            ax.bar(x_pos, meansOutput, yerr=sdOutput, align='center', alpha=0.5, ecolor='black', capsize=10)
            ax.set_ylabel('Number deaths')
            ax.set_xticks(x_pos)
            ax.set_xticklabels(policies)
            # ax.set_title('Hospitalization Costs (mean 2025-2035)')
            ax.yaxis.grid(True)
            fig.tight_layout()
            path = os.path.join(policyFolder, 'deathsByAgeBarChart.pdf')
            pp = PdfPages(path)
            pp.savefig(fig)
            pp.close()
        
        
    for i in range(numScenarios):  
        
        # Total public budget costs
        meansOutput = []
        sdOutput = []
        for j in range(numPolicies):
            values = []
            for z in range(numRepeats):
                policyWindow = []
                for yearOutput in range(2025, 2036, 1):
                    tfc = output[z][i][j].loc[output[z][i][j]['year'] == yearOutput, 'costTaxFreeChildCare'].values[0]
                    pc = output[z][i][j].loc[output[z][i][j]['year'] == yearOutput, 'costPublicChildCare'].values[0]
                    ps = output[z][i][j].loc[output[z][i][j]['year'] == yearOutput, 'costPublicSocialCare'].values[0]
                    tfs = output[z][i][j].loc[output[z][i][j]['year'] == yearOutput, 'costTaxFreeSocialCare'].values[0]
                    hc = output[z][i][j].loc[output[z][i][j]['year'] == yearOutput, 'totalHospitalizationCost'].values[0]/52.0
                    policyWindow.append(tfc+pc+ps+tfs+hc)
                values.append(np.mean(policyWindow))
            meansOutput.append(np.mean(values))
            sdOutput.append(np.std(values))
        fig, ax = plt.subplots()
        x_pos = np.arange(len(policies))
        ax.bar(x_pos, meansOutput, yerr=sdOutput, align='center', alpha=0.5, ecolor='black', capsize=10)
        ax.set_ylabel('Pounds per week')
        ax.set_xticks(x_pos)
        ax.set_xticklabels(policies)
        ax.set_title('Public Budget Policy Cost (mean 2025-2035)')
        ax.yaxis.grid(True)
    
        fig.tight_layout()
        path = os.path.join(scenarioFolder, 'dpublicBudgetPolicyCost.pdf')
        pp = PdfPages(path)
        pp.savefig(fig)
        pp.close()
        
        # ICERB
        newPolicies = policies[1:]
        meansOutput = []
        sdOutput = []
        for j in range(1, numPolicies):
            values = []
            for z in range(numRepeats):
                policyWindow = []
                for yearOutput in range(2025, 2036, 1):
                    tfc = output[z][i][j].loc[output[z][i][j]['year'] == yearOutput, 'costTaxFreeChildCare'].values[0]
                    pc = output[z][i][j].loc[output[z][i][j]['year'] == yearOutput, 'costPublicChildCare'].values[0]
                    ps = output[z][i][j].loc[output[z][i][j]['year'] == yearOutput, 'costPublicSocialCare'].values[0]
                    tfs = output[z][i][j].loc[output[z][i][j]['year'] == yearOutput, 'costTaxFreeSocialCare'].values[0]
                    hc = output[z][i][j].loc[output[z][i][j]['year'] == yearOutput, 'totalHospitalizationCost'].values[0]/52.0
                    policyCost = tfc+pc+ps+tfs+hc
                    tfc = output[z][i][j].loc[output[z][i][0]['year'] == yearOutput, 'costTaxFreeChildCare'].values[0]
                    pc = output[z][i][j].loc[output[z][i][0]['year'] == yearOutput, 'costPublicChildCare'].values[0]
                    ps = output[z][i][j].loc[output[z][i][0]['year'] == yearOutput, 'costPublicSocialCare'].values[0]
                    tfs = output[z][i][j].loc[output[z][i][0]['year'] == yearOutput, 'costTaxFreeSocialCare'].values[0]
                    hc = output[z][i][j].loc[output[z][i][0]['year'] == yearOutput, 'totalHospitalizationCost'].values[0]/52.0
                    benchmarkCost = tfc+pc+ps+tfs+hc
                    deltaCost = policyCost-benchmarkCost
                    hourUnmetCarePolicy = output[z][i][j].loc[output[z][i][j]['year'] == yearOutput, 'totalUnmetSocialCareNeed'].values[0]
                    hourUnmetCareBenchmark = output[z][i][j].loc[output[z][i][0]['year'] == yearOutput, 'totalUnmetSocialCareNeed'].values[0]
                    deltaCare = hourUnmetCareBenchmark-hourUnmetCarePolicy
                    policyWindow.append(deltaCost/deltaCare)
                values.append(np.mean(policyWindow))
            meansOutput.append(np.mean(values))
            sdOutput.append(np.std(values))
        fig, ax = plt.subplots()
        x_pos = np.arange(len(newPolicies))
        ax.bar(x_pos, meansOutput, yerr=sdOutput, align='center', alpha=0.5, ecolor='black', capsize=10)
        ax.set_ylabel('Pounds per hour')
        ax.set_xticks(x_pos)
        ax.set_xticklabels(newPolicies)
        ax.set_title('Budget Cost ICER (mean 2025-2035)')
        ax.yaxis.grid(True)
    
        fig.tight_layout()
        path = os.path.join(scenarioFolder, 'budgetCostICER.pdf')
        pp = PdfPages(path)
        pp.savefig(fig)
        pp.close()
        
        # Cost of working hours care
        meansOutput = []
        sdOutput = []
        for j in range(numPolicies):
            values = []
            for z in range(numRepeats):
                policyWindow = []
                for yearOutput in range(2025, 2036, 1):
                    policyWindow.append(output[z][i][j].loc[output[z][i][j]['year'] == yearOutput, 'totalCostOWSC'].values[0])
                values.append(np.mean(policyWindow))
            meansOutput.append(np.mean(values))
            sdOutput.append(np.std(values))
        fig, ax = plt.subplots()
        x_pos = np.arange(len(policies))
        ax.bar(x_pos, meansOutput, yerr=sdOutput, align='center', alpha=0.5, ecolor='black', capsize=10)
        ax.set_ylabel('Pounds per week')
        ax.set_xticks(x_pos)
        ax.set_xticklabels(policies)
        ax.set_title('Working Hours Care Costs (mean 2025-2035)')
        ax.yaxis.grid(True)
    
        fig.tight_layout()
        path = os.path.join(scenarioFolder, 'workingHoursCareCosts.pdf')
        pp = PdfPages(path)
        pp.savefig(fig)
        pp.close()
        
        # Total Policy Costs
        meansOutput = []
        sdOutput = []
        for j in range(numPolicies):
            values = []
            for z in range(numRepeats):
                policyWindow = []
                for yearOutput in range(2025, 2036, 1):
                    tfc = output[z][i][j].loc[output[z][i][j]['year'] == yearOutput, 'costTaxFreeChildCare'].values[0]
                    pc = output[z][i][j].loc[output[z][i][j]['year'] == yearOutput, 'costPublicChildCare'].values[0]
                    ps = output[z][i][j].loc[output[z][i][j]['year'] == yearOutput, 'costPublicSocialCare'].values[0]
                    tfs = output[z][i][j].loc[output[z][i][j]['year'] == yearOutput, 'costTaxFreeSocialCare'].values[0]
                    hc = output[z][i][j].loc[output[z][i][j]['year'] == yearOutput, 'totalHospitalizationCost'].values[0]/52.0
                    ows = output[z][i][j].loc[output[z][i][j]['year'] == yearOutput, 'totalCostOWSC'].values[0]
                    policyWindow.append(tfc+pc+ps+tfs+hc+ows)
                values.append(np.mean(policyWindow))
            meansOutput.append(np.mean(values))
            sdOutput.append(np.std(values))
        fig, ax = plt.subplots()
        x_pos = np.arange(len(policies))
        ax.bar(x_pos, meansOutput, yerr=sdOutput, align='center', alpha=0.5, ecolor='black', capsize=10)
        ax.set_ylabel('Pounds per week')
        ax.set_xticks(x_pos)
        ax.set_xticklabels(policies)
        ax.set_title('Total Policy Cost (mean 2025-2035)')
        ax.yaxis.grid(True)
    
        fig.tight_layout()
        path = os.path.join(scenarioFolder, 'totalPolicyCost.pdf')
        pp = PdfPages(path)
        pp.savefig(fig)
        pp.close()
        
        # ICERT
        newPolicies = policies[1:]
        meansOutput = []
        sdOutput = []
        for j in range(1, numPolicies):
            values = []
            for z in range(numRepeats):
                policyWindow = []
                for yearOutput in range(2025, 2036, 1):
                    tfc = output[z][i][j].loc[output[z][i][j]['year'] == yearOutput, 'costTaxFreeChildCare'].values[0]
                    pc = output[z][i][j].loc[output[z][i][j]['year'] == yearOutput, 'costPublicChildCare'].values[0]
                    ps = output[z][i][j].loc[output[z][i][j]['year'] == yearOutput, 'costPublicSocialCare'].values[0]
                    tfs = output[z][i][j].loc[output[z][i][j]['year'] == yearOutput, 'costTaxFreeSocialCare'].values[0]
                    hc = output[z][i][j].loc[output[z][i][j]['year'] == yearOutput, 'totalHospitalizationCost'].values[0]/52.0
                    ows = output[z][i][j].loc[output[z][i][j]['year'] == yearOutput, 'totalCostOWSC'].values[0]
                    policyCost = tfc+pc+ps+tfs+hc+ows
                    tfc = output[z][i][j].loc[output[z][i][0]['year'] == yearOutput, 'costTaxFreeChildCare'].values[0]
                    pc = output[z][i][j].loc[output[z][i][0]['year'] == yearOutput, 'costPublicChildCare'].values[0]
                    ps = output[z][i][j].loc[output[z][i][0]['year'] == yearOutput, 'costPublicSocialCare'].values[0]
                    tfs = output[z][i][j].loc[output[z][i][0]['year'] == yearOutput, 'costTaxFreeSocialCare'].values[0]
                    hc = output[z][i][j].loc[output[z][i][0]['year'] == yearOutput, 'totalHospitalizationCost'].values[0]/52.0
                    ows = output[z][i][j].loc[output[z][i][0]['year'] == yearOutput, 'totalCostOWSC'].values[0]
                    benchmarkCost = tfc+pc+ps+tfs+hc+ows
                    deltaCost = policyCost-benchmarkCost
                    hourUnmetCarePolicy = output[z][i][j].loc[output[z][i][j]['year'] == yearOutput, 'totalUnmetSocialCareNeed'].values[0]
                    hourUnmetCareBenchmark = output[z][i][j].loc[output[z][i][0]['year'] == yearOutput, 'totalUnmetSocialCareNeed'].values[0]
                    deltaCare = hourUnmetCareBenchmark-hourUnmetCarePolicy
                    policyWindow.append(deltaCost/deltaCare)
                values.append(np.mean(policyWindow))
            meansOutput.append(np.mean(values))
            sdOutput.append(np.std(values))
        fig, ax = plt.subplots()
        x_pos = np.arange(len(newPolicies))
        ax.bar(x_pos, meansOutput, yerr=sdOutput, align='center', alpha=0.5, ecolor='black', capsize=10)
        ax.set_ylabel('Pounds per hour')
        ax.set_xticks(x_pos)
        ax.set_xticklabels(newPolicies)
        ax.set_title('Total Cost ICER (mean 2025-2035)')
        ax.yaxis.grid(True)
    
        fig.tight_layout()
        path = os.path.join(scenarioFolder, 'totalCostICER.pdf')
        pp = PdfPages(path)
        pp.savefig(fig)
        pp.close()
        
    
#    for j in range(numPolicies):
#        for i in range(numScenarios):
#            fig, ax = plt.subplots() # Argument: figsize=(5, 3)
#            graph = []
#            for z in range(numRepeats):
#                graph.append(ax.plot(output[z][i][j]['year'], output[z][i][j]['currentPop'], label = 'Run ' + str(z+1)))
#            ax.set_title('Populations - ' + 'Scenario ' + str(i+1) + '/Policy ' + str(j))
#            ax.set_ylabel('Number of people')
#            handels, labels = ax.get_legend_handles_labels()
#            ax.legend(loc = 'lower right')
#            ax.xaxis.set_major_locator(MaxNLocator(integer=True))
#            ax.set_xlim(left = int(p['statsCollectFrom']), right = int(p['endYear']))
#            ax.set_xticks(range(int(p['statsCollectFrom']), int(p['endYear'])+1, 20))
#            fig.tight_layout()
#            path = os.path.join(folder, 'popGrowth_axRep_S' + str(i+1) + '_P' + str(j) + '.pdf')
#            pp = PdfPages(path)
#            pp.savefig(fig)
#            pp.close()
#            
#    for j in range(numPolicies):
#        for i in range(numScenarios):
#            fig, ax = plt.subplots() # Argument: figsize=(5, 3)
#            graph = []
#            for z in range(numRepeats):
#                graph.append(ax.plot(output[z][i][j]['year'], output[z][i][j]['share_UnmetSocialCareNeed'], label = 'Run ' + str(z+1)))
#            ax.set_title('Unmet Care Needs - ' + 'Scenario ' + str(i+1) + '/Policy ' + str(j))
#            ax.set_ylabel('Unmet Care Needs (share)')
#            handels, labels = ax.get_legend_handles_labels()
#            ax.legend(loc = 'lower right')
#            ax.xaxis.set_major_locator(MaxNLocator(integer=True))
#            ax.set_xlim(left = int(p['statsCollectFrom']), right = int(p['endYear']))
#            ax.set_xticks(range(int(p['statsCollectFrom']), int(p['endYear'])+1, 20))
#            fig.tight_layout()
#            path = os.path.join(folder, 'shareUnmetSocialCareNeeds_axRep_S' + str(i+1) + '_P' + str(j) + '.pdf')
#            pp = PdfPages(path)
#            pp.savefig(fig)
#            pp.close()



mP = pd.read_csv('metaParameters.csv', sep=',', header=0)
numberRows = mP.shape[0]
keys = list(mP.columns.values)
values = []
for column in mP:
    colValues = []
    for i in range(numberRows):
        if pd.isnull(mP.loc[i, column]):
            break
        colValues.append(mP[column][i])
    values.append(colValues)
metaParams = OrderedDict(zip(keys, values))
for key, value in metaParams.iteritems():
    if len(value) < 2:
        metaParams[key] = value[0]
        
graphsParams = pd.read_csv('graphsParams.csv', sep=',', header=0)
dummy = list(graphsParams['doGraphs'])
for i in range(len(dummy)):
    if dummy[i] == 1:
        doGraphs(graphsParams.loc[i], metaParams)

        

