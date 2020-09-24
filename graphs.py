# -*- coding: utf-8 -*-
"""
Created on Wed Feb 06 15:45:43 2019

@author: ug4d
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from matplotlib.backends.backend_pdf import PdfPages
import os
from collections import OrderedDict
import pandas as pd
import sys


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
    
    fig, ax = plt.subplots() # Argument: figsize=(5, 3)
    p1, = ax.plot(output['day'], output['classShare_1'], color="red", linewidth = 2)
    ax.set_ylabel('Share of Population')
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    # ax.set_xlim(left = int(p['statsCollectFrom']), right = int(p['endday']))
    # ax.set_xticks(range(int(p['statsCollectFrom']), int(p['endday'])+1, 20))
    fig.tight_layout()
    path = os.path.join(folder, 'classShare_1.pdf')
    pp = PdfPages(path)
    pp.savefig(fig)
    pp.close()
    
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
    # ax.set_title('Cost of out-of-work social care')
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
    ax.legend(loc = 'lower right')
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    ax.set_ylim(0, 50)
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
    ax.set_title('Unmet Social Care Needs (hours)')
    ax.set_ylabel('Hours per week')
    handels, labels = ax.get_legend_handles_labels()
    ax.legend(loc = 'upper right')
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
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
    ax.legend(loc = 'lower left')
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
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
    ax.legend(loc = 'upper right')
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
    ax.legend(loc = 'upper right')
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
    handels, labels = ax.get_legend_handles_labels()
    ax.legend(loc = 'lower right')
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
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
    # ax.set_title('Share Informal Child Care')
    ax.set_ylabel('Hours per week')
    handels, labels = ax.get_legend_handles_labels()
    ax.legend(loc = 'upper right')
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
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
        graph.append(ax.plot(output[i]['day'], output[i]['formalChildCare'], label = policyLabel, linewidth = 2))
    # ax.set_title('Formal Child Care')
    ax.set_ylabel('Hours per week')
    handels, labels = ax.get_legend_handles_labels()
    ax.legend(loc = 'lower left')
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
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
    # ax.set_xlim(left = int(p['statsCollectFrom']), right = int(p['endday']))
    # ax.set_xticks(range(int(p['statsCollectFrom']), int(p['endday'])+1, 20))
    fig.tight_layout()
    path = os.path.join(folder, 'directPolicyCost_axPol.pdf')
    pp = PdfPages(path)
    pp.savefig(fig)
    pp.close()
   
    
    
    policyDays = int(p['pandemicPeriod']-p['policyStartDay']) + 1
    # Fig. 9: Bar charts of total unmet care need by Policy
    fig, ax = plt.subplots()
    objects = ('Benchmark', 'P1')
    y_pos = np.arange(len(objects))
    outOfWorkCare = []
    for i in range(numPolicies):
        outOfWorkCare.append(np.sum(output[i]['totalHospitalizationCost'])) # [-policyDays:]
    width = 0.4
    ax.bar(y_pos, outOfWorkCare, width, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    # plt.ylim(75000000, 85000000)
    ax.xaxis.set_ticks_position('none')
    ax.set_ylabel('Pounds')
    # ax.set_title('Formal Child Care (2020-2040)')
    fig.tight_layout()
    path = os.path.join(folder, 'hospitalizationCostBarChart.pdf')
    pp = PdfPages(path)
    pp.savefig(fig)
    pp.close()
    
    
    # policyYears = int(p['endYear']-p['policyStartYear']) + 1
    # Fig. 9: Bar charts of total unmet care need by Policy
    fig, ax = plt.subplots()
    objects = ('Benchmark', 'P1')
    y_pos = np.arange(len(objects))
    outOfWorkCare = []
    for i in range(numPolicies):
        outOfWorkCare.append(np.sum(output[i]['totalSocialCareNeed']))
    ax.bar(y_pos, outOfWorkCare, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    # plt.ylim(1200000, 1400000)
    ax.xaxis.set_ticks_position('none')
    ax.set_ylabel('Hours per week')
    # ax.set_title('Formal Child Care (2020-2040)')
    fig.tight_layout()
    path = os.path.join(folder, 'totalSocialCareNeedBarChart.pdf')
    pp = PdfPages(path)
    pp.savefig(fig)
    pp.close()
    
    # policyYears = int(p['endYear']-p['policyStartYear']) + 1
    # Fig. 9: Bar charts of total unmet care need by Policy
    fig, ax = plt.subplots()
    objects = ('Benchmark', 'P1')
    y_pos = np.arange(len(objects))
    outOfWorkCare = []
    for i in range(numPolicies):
        outOfWorkCare.append(np.sum(output[i]['totalInformalSocialCare']))
    ax.bar(y_pos, outOfWorkCare, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    # plt.ylim(350000, 450000)
    ax.xaxis.set_ticks_position('none')
    ax.set_ylabel('Hours per week')
    # ax.set_title('Formal Child Care (2020-2040)')
    fig.tight_layout()
    path = os.path.join(folder, 'totalInformalCareNeedBarChart.pdf')
    pp = PdfPages(path)
    pp.savefig(fig)
    pp.close()
    
    # policyYears = int(p['endYear']-p['policyStartYear']) + 1
    # Fig. 9: Bar charts of total unmet care need by Policy
    fig, ax = plt.subplots()
    objects = ('Benchmark', 'P1')
    y_pos = np.arange(len(objects))
    outOfWorkCare = []
    for i in range(numPolicies):
        outOfWorkCare.append(np.sum(output[i]['totalFormalSocialCare']))
    ax.bar(y_pos, outOfWorkCare, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    # plt.ylim(150000, 225000)
    ax.xaxis.set_ticks_position('none')
    ax.set_ylabel('Hours per week')
    # ax.set_title('Formal Child Care (2020-2040)')
    fig.tight_layout()
    path = os.path.join(folder, 'totalFormalCareNeedBarChart.pdf')
    pp = PdfPages(path)
    pp.savefig(fig)
    pp.close()
    
    # policyYears = int(p['endYear']-p['policyStartYear']) + 1
    # Fig. 9: Bar charts of total unmet care need by Policy
    fig, ax = plt.subplots()
    objects = ('Benchmark', 'P1')
    y_pos = np.arange(len(objects))
    outOfWorkCare = []
    for i in range(numPolicies):
        outOfWorkCare.append(np.sum(output[i]['formalChildCare']))
    ax.bar(y_pos, outOfWorkCare, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    ax.xaxis.set_ticks_position('none')
    ax.set_ylabel('Hours per week')
    # ax.set_title('Formal Child Care (2020-2040)')
    fig.tight_layout()
    path = os.path.join(folder, 'formal Child CareBarChart.pdf')
    pp = PdfPages(path)
    pp.savefig(fig)
    pp.close()
    
    
    
    # policyYears = int(p['endYear']-p['policyStartYear']) + 1
    # Fig. 9: Bar charts of total unmet care need by Policy
    fig, ax = plt.subplots()
    objects = ('Benchmark', 'P1')
    y_pos = np.arange(len(objects))
    outOfWorkCare = []
    for i in range(numPolicies):
        outOfWorkCare.append(np.sum(output[i]['totalOWSC']))
    ax.bar(y_pos, outOfWorkCare, align='center', alpha=0.5)
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
    objects = ('Benchmark', 'P1')
    y_pos = np.arange(len(objects))
    shareUnmetCareDemand = []
    for i in range(numPolicies):
        shareUnmetCareDemand.append(np.sum(output[i]['totalUnmetSocialCareNeed']))
    ax.bar(y_pos, shareUnmetCareDemand, align='center', alpha=0.5)
    # plt.ylim(500000, 650000)
    plt.xticks(y_pos, objects)
    ax.xaxis.set_ticks_position('none')
    ax.set_ylabel('Hours of Unmet Care')
    # ax.set_title('Total Unmet Social Care Need')
    fig.tight_layout()
    path = os.path.join(folder, 'TotalUnmetCareNeedBarChart.pdf')
    pp = PdfPages(path)
    pp.savefig(fig)
    pp.close()
    
    # policyYears = int(p['endYear']-p['policyStartYear']) + 1
    # Fig. 9: Bar charts of total unmet care need by Policy
    fig, ax = plt.subplots()
    objects = ('Benchmark', 'P1')
    y_pos = np.arange(len(objects))
    shareUnmetCareDemand = []
    for i in range(numPolicies):
        shareUnmetCareDemand.append(np.sum(output[i]['publicSocialCare']))
    ax.bar(y_pos, shareUnmetCareDemand, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    # plt.ylim(80000, 170000)
    ax.xaxis.set_ticks_position('none')
    ax.set_ylabel('Hours of Social Care')
    # ax.set_title('Total Unmet Social Care Need')
    fig.tight_layout()
    path = os.path.join(folder, 'publicSocialCareBarChart.pdf')
    pp = PdfPages(path)
    pp.savefig(fig)
    pp.close()
    
    
    # policyYears = int(p['endYear']-p['policyStartYear']) + 1
    # Fig. 9: Bar charts of total unmet care need by Policy
    fig, ax = plt.subplots()
    objects = ('Benchmark', 'P1')
    y_pos = np.arange(len(objects))
    shareUnmetCareDemand = []
    for i in range(numPolicies):
        c1 = output[i]['costTaxFreeChildCare']
        c2 = output[i]['costPublicChildCare']
        c3 = output[i]['costPublicSocialCare']
        c4 = output[i]['costTaxFreeSocialCare']
        policyCost = [sum(x) for x in zip(c1, c2, c3, c4)]
        shareUnmetCareDemand.append(np.sum(policyCost))
    ax.bar(y_pos, shareUnmetCareDemand, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    ax.xaxis.set_ticks_position('none')
    ax.set_ylabel('Pounds per week')
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
    
    # print 'doing mrg...'
    
    folder = simFolder + '/Graphs'
    if not os.path.exists(folder):
        os.makedirs(folder)
    

    # Add graphs across runs (for the same scenario/policy combinations)
    # For each policy scenario, take the average of year 2010-2020 for each run, and do a bar chart with error bars for each outcome of interest
    
    # Policy comparison: make charts by outcomes with bars representing the different policies.
    
    
    
    policies = ['Benchmark', 'Policy 1', 'Policy 2', 'Policy 3', 'Policy 4']
    
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

        

