import robin_stocks
import pandas as pd
import matplotlib.pyplot as plt

#
# DELETE PRIOR TO PUSH TO GITHUB
#
uName =
uPass =


def loggingIn(userName, passWord):
    robin_stocks.login(username=userName, password=passWord)


# for login info
# inputName = input('Username(email): ')
# inputPass = input('Password: ')

# unneeded while getting stock info
loggingIn(uName, uPass)

profile = robin_stocks.load_account_profile()
# print(profile)


# loop for getting stock ticker info for past week, and plotting a histogram/column info

kill = ''
while kill != 'kill':
    kill = input('Stock ticker: ')
    output = robin_stocks.get_historicals(kill, bounds='regular')
    dataFrame = pd.DataFrame(output)
    print(dataFrame)
    print(dataFrame.columns)
    volume = dataFrame['volume']
    plt.hist(volume, bins=30)
    plt.show()
