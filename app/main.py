#Find the right on duty crew memeber for assignment.
from datetime import datetime

import csv
import pytz
import pandas as pd

# Get and print current UTC time in MM-DD-YYYY HH:MM format string
current_time_str = datetime.now(tz=pytz.UTC).strftime("%Y-%m-%d %H:%M")

#User inputs a valid pairing length
pairingInvalid = True

while (pairingInvalid):
    # Get user to input pairing length.
    print("How long is the pairing you are looking to crew? (1-6 days)")
    pairingInput = int(input(">> "))

    # Validate the pairing length.
    if pairingInput > 6 or pairingInput < 1:
        pairingInvalid = True
        print("Pairing must be between 1 and 6 days.")
    else:
        pairingInvalid = False
        pairingSelect = int(pairingInput)
        break

#User input base
baseInvalid = True

while (baseInvalid):
    # Get a valid base.
    print("Please input a base.")
    baseInput = str(input(">> "))

    if baseInput == ("yyz" or "YYZ" or "toronto" or "Toronto"):
        baseInvalid = False,
        citySelect = str("YYZ")
        break
    elif baseInput == ("yyc" or "YYC" or "calgary" or "Calgary"):
        baseInvalid = False,
        citySelect = str("YYC")
        break
    elif baseInput == ("yvr" or "YVR" or "vancouver" or "Vancouver"):
        baseInvalid = False,
        citySelect = str("YVR")
        break
    else:
        print("Please select one of our main bases. (YYZ, YYC, or YVR)")
        continue

#Do you need a purser CCM?
purserInvalid = True

while (purserInvalid):
    # Input purser
    print("Do you need a Purser? Y/N")
    purserInput = str(input(">> "))

    if purserInput == ("y" or "Y" or "yes" or "Yes" or "YES"):
        purserInvalid = False,
        purserSelect = int(1)
        break
    elif purserInput == ("n" or "N" or "no" or "No" or "NO"):
        baseInvalid = False,
        purserSelect = int(0)
        break
    else:
        print("It's a yes or no question.")
        continue

#Do you need a 787 qualified FA? (All pursers are 787 qualified)
if purserSelect == (1):
    eightInvalid = False,
    eightSelect = int(1)
else:
    eightInvalid = True

    while (eightInvalid):
        # input 787 fa or not
        print("Do you need a 787 qualified FA? Y/N")
        eightInput = str(input(">> "))

        if eightInput == ("y" or "Y" or "yes" or "Yes" or "YES"):
            eightInvalid = False,
            eightSelect = int(1)
            break
        elif eightInput == ("n" or "N" or "no" or "No" or "NO"):
            eightInvalid = False,
            eightSelect = int(0)
            break
        else:
            print("It's a yes or no question.")
            continue

#dataframe read CrewList.csv
df = pd.read_csv('CrewList.csv', index_col=0)

#dfAll contains answers for Base, Purser, 787, and Days.
dfAll = df[(df['Base'] == (str(citySelect))) &
           (df['Purser'] == int(purserSelect)) &
           (df['787'] == int(eightSelect)) &
           (df['Days'] >= (int(pairingSelect)))]
#print(dfAll)

#Available crew members
print("Available " + (str(citySelect)) + " crew members as of " + (current_time_str), "\n")
print("Recommended crew callouts by days left on duty and reverse seniority:", "\n")

#Sort and print dataframe.
dfSort = dfAll.sort_values(by=["Days", "ID"], ascending=[True, False])
dfSort = dfSort.reset_index()
dfSort.index = pd.RangeIndex(start=1, stop=1+len(dfSort), step=1)
print(dfSort.head(10))