nf = open('new_file_probability.txt', 'w')

n_black = 40
n_brown = 26
n_red = 22
n_blue = 12

p1_c1 = n_red
p1_c2 = n_blue

nTotal1 = (n_black + n_brown + n_red + n_blue)
P1 = (p1_c1 + p1_c2) / nTotal1
nf.write(f'Task 1 \nP(c1 or c2) = {P1}')

# =====

nTotal2 = 10
n_consultant = 8
triesNumb2 = 2

P_consultant = n_consultant / nTotal2
P_notConsultant = 1 - P_consultant

P2 = 1 - P_notConsultant**triesNumb2
nf.write(f'\n\nTask 2 \nP(at least 1 consultant in {triesNumb2} tries // and) = {P2}')

# =====

nTotal3 = 10
n_cousin = 2
triesNumb3 = 3

P_cousin = n_cousin / nTotal3
P_notCousin = 1 - P_cousin

P3 = 1 - P_notCousin**triesNumb3

nf.write(f'\n\nTask 3 \nP(at least 1 cousin in {triesNumb3} tries // and) = {P3}')

# =====

nTotal4 = 5
P_firstDep = 0.15
P_secondDep = 0.25
P_thirdDep = 0.2
P_fourthDep = 0.1

P4 = 1 - (P_firstDep + P_secondDep + P_thirdDep + P_fourthDep)

nf.write(f'\n\nTask 4 \nP(from the fifth department) = {P4}')

# =====

nTotal5 = 120
n_trainDrop = 80
n_railsOnSameTime = 2

P_trainDrop = n_trainDrop / nTotal5
P_totalTrainsOnSameTime = (nTotal5 / n_railsOnSameTime) / nTotal5

P5 = P_trainDrop * P_totalTrainsOnSameTime

nf.write(f'\n\nTask 5 \nP(trainDrop and neighbor({n_railsOnSameTime})) = {P5}')

# =====

P_standart = 0.9
P_fcStandart = 0.8

P6 = P_standart * P_fcStandart

nf.write(f'\n\nTask 6 \nP(fromStandart and firstClass) = {P6}')

# =====

nTotal7 = 10
nTotal7_q = 20
n_excellent = 3
n_excellentKnow = 20
n_good = 4
n_goodKnow = 16
n_goodEnough = 2
n_goodEnoughKnow = 10
n_bad = 1
n_badKnow = 5
triesNumb7 = 3

P_excellentStudent = n_excellent / nTotal7
P_goodStudent = n_good / nTotal7
P_goodEnoughStudent = n_goodEnough / nTotal7
P_badStudent = n_bad / nTotal7

P_excellentPass = (n_excellentKnow / nTotal7_q)**triesNumb7
P_goodPass = (n_goodKnow / nTotal7_q)**triesNumb7
P_goodEnoughPass = (n_goodEnoughKnow / nTotal7_q)**triesNumb7
P_badPass = (n_badKnow / nTotal7_q)**triesNumb7

P7_1 = P_excellentPass * P_excellentStudent
P7_2 = P_badPass * P_badStudent

nf.write(f'\n\nTask 7 \nP(itWasExcellentStudent and excellentStudentPass{triesNumb7}Questions) = {P7_1}'
      f'\nP(itWasBadStudent and badStudentPass{3}Questions) = {P7_2}')

# =====

perc_p1 = 0.4
perc_p2 = 0.3
perc_p3 = 0.3
P_p1Standart = 0.9
P_p2Standart = 0.95
P_p3Standart = 0.95

P_p1_and_p1Standart = perc_p1 * P_p1Standart
P_p2_and_p2Standart = perc_p2 * P_p2Standart
P_p3_and_p3Standart = perc_p3 * P_p3Standart

P8 = P_p1_and_p1Standart + P_p2_and_p2Standart + P_p3_and_p3Standart

nf.write(f'\n\nTask 8 \nP(standartFromP1 or standartFromP2 or standartFromP3) = {P8}')

# =====

perc_pnev = 0.4
perc_per = 0.3
perc_ang = 0.3
P_healingPnev = 0.8
P_healingPer = 0.7
P_healingAng = 0.85

P_healingPnev_and_percPnev = P_healingPnev * perc_pnev
P_healingPer_and_percPer = P_healingPer * perc_per
P_healingAng_and_percAng = P_healingAng * perc_ang

nf.write(f'\n\nTask 9 \nP(helingFromPer and perPercProb) = {P_healingPer_and_percPer}')

# =====

perc_highQualified = 0.3
perc_mediumQualified = 0.7
P_highQualified_HQ = 0.9
P_mediumQualified_HQ = 0.8

P10 = perc_highQualified * P_highQualified_HQ

nf.write(f'\n\nTask 10 \nP(isHQ and byHighQualified) = {P10}')