
import random
import numpy as np
import math
import networkx as nx

class Person:
    """The person class stores information about a person in the sim."""
    counter = 1
    def __init__ (self, mother, father, birthYear, age, sex, house, sec, cr, pcr, wage, 
                  inc, wlt, iw, fw, we, status, independence, healthStatus):
        self.mother = mother
        self.motherID = -1 # For pickle
        self.father = father
        self.fatherID = -1 # For pickle
        self.age = age
        self.ageClass = 0
        self.interactionAgeClass = 0
        self.mortalityAgeClass = 0
        self.status = status
        self.lifeExpectancy = 0
        self.independentStatus = independence
        self.maternityStatus = False
    
        # Pandemic variables
        self.healthStatus = healthStatus
        self.severityLevel = 0
        self.mildConditionIndex = 0
        self.daysFromInfection = 0
        self.incubationPeriod = -1
        self.symptomsLevel = None
        self.recoveryPeriod = -1
        self.workingShare = 1.0
        self.symptomatic = False
        self.hospitalized = False
        self.hasBeenExposed = False
        self.hasBeenInfectious = False
        self.haveBeenHospitalized = False
        self.inIntensiveCare = False
        self.networkInfectionFactor = 0
        self.placeOfDeath = None
        self.aiw = 0
        self.ciw = 0
        self.adw = 0
        self.cdw = 0
        self.gdw = 0
        self.numContacts = 0
        self.domesticRiskFactor = 0
        self.randomRiskFactor = 0
        self.communalRiskFactor = 0
        self.careRiskFactor = 0
        self.contagiousnessIndex = 0
        self.viralLoad = 0
        self.relativeRisk = 0
        self.contactReductionRate = 1.0
        self.testPositive = False
        self.dailyContacts = []
        self.randomContacts = []
        self.numContacts = 0
        self.networkContacts = 0
        self.numRandomContacts = 0
        self.socialContacts = nx.DiGraph()
        self.kinshipContacts = nx.DiGraph()
        self.socialContacIDs = []
        self.contactWeights = []
        self.genderWeight = 1.0
        self.nokCareContacts = []
        self.totalContacts = 0
        self.inHouseInformalCare = 0
        self.externalInformalCare = 0
        
        self.children = []
        self.childrenID = [] # For pickle
        self.yearMarried = []
        self.yearDivorced = []
        self.deadYear = 0
        self.yearInTown = 0
        self.outOfTownStudent = False
        self.birthdate = birthYear
        self.wage = wage
        self.income = inc
        self.lastIncome = inc
        self.workingPeriods = 0
        self.cumulativeIncome = 0
        self.potentialIncome = inc
        self.wealth = wlt
        self.incomeQuintile = -1
        self.financialWealth = 0
        self.wealthSpentOnCare = 0
        self.incomeExpenses = 0
        self.wealthPV = 0
        self.wealthForCare = 0
        self.initialIncome = iw
        self.finalIncome = fw
        self.workExperience = we
        self.careNeedLevel = 0
        self.socialWork = 0
        # Unmet Need variables 
        self.careNetwork = nx.DiGraph()
        self.careDemand = 0
        self.unmetCareNeed = 0
        self.cumulativeUnmetNeed = 0
        self.totalDiscountedShareUnmetNeed = 0
        self.averageShareUnmetNeed = 0
        self.totalDiscountedTime = 0
        
        self.classRank = cr
        self.parentsClassRank = pcr
        self.dead = False
        self.partner = None
        if sex == 'random':
            self.sex = random.choice(['male', 'female'])
        else:
            self.sex = sex
        self.house = house
        self.currentTown = None
        if self.house != None:
            self.currentTown = house.town
        self.houseID = -1 # For pickle
        self.sec = sec
        
        self.careAvailable = 0
        self.residualSupply = 0
        self.movedThisYear = False
        
        # Kinship network variables
        self.hoursChildCareDemand = 0
        self.netChildCareDemand = 0
        self.unmetChildCareNeed = 0
        self.hoursSocialCareDemand = 0
        self.unmetSocialCareNeed = 0
        self.informalChildCareReceived = 0
        self.formalChildCareReceived = 0
        self.publicChildCareContribution = 0
        self.informalSocialCareReceived = 0
        self.formalSocialCareReceived = 0
        self.childWork = 0
        self.socialWork = 0
        self.outOfWorkChildCare = 0
        self.outOfWorkSocialCare = 0
        self.residualWorkingHours = 0
        self.availableWorkingHours = 0
        self.residualInformalSupplies = [0.0, 0.0, 0.0, 0.0]
        self.residualInformalSupply = 0
        self.hoursInformalSupplies = [0.0, 0.0, 0.0, 0.0]
        self.maxFormalCareSupply = 0
        self.totalSupply = 0
        self.informalSupplyByKinship = [0.0, 0.0, 0.0, 0.0]
        self.formalSupplyByKinship = [0.0, 0.0, 0.0, 0.0]
        self.careForFamily = False
        self.networkSupply = 0
        self.networkTotalSupplies = []
        self.weightedTotalSupplies = []
        self.networkInformalSupplies = []
        self.networkFormalSocialCareSupplies = []
        self.careSupplyFromWealth = 0
        self.suppliers = []
        self.id = Person.counter
        Person.counter += 1

class ClassContact:
    def __init__ (self, age, quintile, num, totContacts, empContacts, totAgeContacts):
        self.age = age
        self.quintile = quintile
        self.number = num
        self.weight = 0
        self.totContactsByAge = totAgeContacts
        self.contacts = totContacts
        self.actualContacts = 0
        self.deltaContacts = totContacts
        self.meanContactsEmp = empContacts
        self.contactsByAge = [0]*len(self.meanContactsEmp)
        self.actualContactsByAge = [0]*len(self.meanContactsEmp)
        self.meanActContacts = [x/self.number for x in self.contactsByAge]
        self.deltaMeanContacts = [x-y for (x, y) in zip(self.meanContactsEmp, self.meanActContacts)]
        
class CareContact:
    def __init__ (self, contact, hoursOfCare):
        self.contact = contact
        self.contactDuration = hoursOfCare

class Population:
    """The population class stores a collection of persons."""
    def __init__ (self, initial, startYear, minStartAge, maxStartAge,
                  workingAge, incomeInitialLevels, incomeFinalLevels,
                  incomeGrowthRate, workDiscountingTime, wageVar, weeklyHours):
        self.allPeople = []
        self.livingPeople = []
        for i in range(int(initial)/2):
            ageMale = random.randint(minStartAge, maxStartAge)
            ageFemale = ageMale - random.randint(-2,5)
            if ( ageFemale < 24 ):
                ageFemale = 24
            birthYear = startYear - random.randint(minStartAge,maxStartAge)
            classes = [0, 1, 2, 3, 4]
            probClasses = [0.2, 0.35, 0.25, 0.15, 0.05]
            classRank = np.random.choice(classes, p = probClasses)
            
            workingTime = 0
            for i in range(int(ageMale)-int(workingAge[classRank])):
                workingTime *= workDiscountingTime
                workingTime += 1
            
            dKi = np.random.normal(0, wageVar)
            initialWage = incomeInitialLevels[classRank]*math.exp(dKi)
            dKf = np.random.normal(dKi, wageVar)
            finalWage = incomeFinalLevels[classRank]*math.exp(dKf)
            
            c = np.math.log(initialWage/finalWage)
            wage = finalWage*np.math.exp(c*np.math.exp(-1*incomeGrowthRate[classRank]*workingTime))
            income = wage*weeklyHours
            workExperience = workingTime
            healthStatus = 'susceptible'
            newMan = Person(None, None,
                            birthYear, ageMale, 'male', None, None, classRank, classRank, wage, income, 0, 
                            initialWage, finalWage, workExperience, 'worker', True, healthStatus)
            
            workingTime = 0
            for i in range(int(ageFemale)-int(workingAge[classRank])):
                workingTime *= workDiscountingTime
                workingTime += 1
                
            dKi = np.random.normal(0, wageVar)
            initialWage = incomeInitialLevels[classRank]*math.exp(dKi)
            dKf = np.random.normal(dKi, wageVar)
            finalWage = incomeFinalLevels[classRank]*math.exp(dKf)
            
            c = np.math.log(initialWage/finalWage)
            wage = finalWage*np.math.exp(c*np.math.exp(-1*incomeGrowthRate[classRank]*workingTime))
            income = wage*weeklyHours
            workExperience = workingTime
            newWoman = Person(None, None,
                              birthYear, ageFemale, 'female', None, None, classRank, classRank, wage, income, 0, 
                              initialWage, finalWage, workExperience, 'worker', True, healthStatus)

            # newMan.status = 'independent adult'
            # newWoman.status = 'independent adult'
            
            newMan.partner = newWoman
            newWoman.partner = newMan
            
            self.allPeople.append(newMan)
            self.livingPeople.append(newMan)
            self.allPeople.append(newWoman)
            self.livingPeople.append(newWoman)

            
