# 6.00.2x Problem Set 4

import numpy
import random
import pylab
from ps3b import *

#
# PROBLEM 1
#        
def simulationDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 1.

    Runs numTrials simulations to show the relationship between delayed
    treatment and patient outcome using a histogram.

    Histograms of final total virus populations are displayed for delays of 300,
    150, 75, 0 timesteps (followed by an additional 150 timesteps of
    simulation).

    numTrials: number of simulation runs to execute (an integer)
    """
    numViruses = 100
    maxPop = 1000
    maxBirthProb = 0.1
    clearProb = 0.05
    resistances = {'guttagonol': False, 'grimpex': False}
    mutProb = 0.005
    delay = 0

    totalVirusNum = []
    for i in range(numTrials):
        viruses = []
        for j in range(numViruses):        
            viruses.append( ResistantVirus(maxBirthProb, clearProb, resistances, mutProb) )
        
        patient = TreatedPatient(viruses, maxPop)
        for k in range(150):           
            trialVirusNum = patient.update()    
        patient.addPrescription("guttagonol")
        for k in range(delay):           
            trialVirusNum = patient.update()
        patient.addPrescription("grimpex")
        for k in range(150):           
            trialVirusNum = patient.update()
        print trialVirusNum
        totalVirusNum.append(trialVirusNum)
        
    pylab.hist(totalVirusNum)
    pylab.show()

  
simulationDelayedTreatment(100)

    
    






#
# PROBLEM 2
#
#def simulationTwoDrugsDelayedTreatment(numTrials):
##    """
##    Runs simulations and make histograms for problem 2.
##
##    Runs numTrials simulations to show the relationship between administration
##    of multiple drugs and patient outcome.
##
##    Histograms of final total virus populations are displayed for lag times of
##    300, 150, 75, 0 timesteps between adding drugs (followed by an additional
##    150 timesteps of simulation).
##
##    numTrials: number of simulation runs to execute (an integer)
##    """
    # TODO
