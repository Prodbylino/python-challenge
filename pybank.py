import csv
import os
#set path
#import Financial as Financial

path_pybank = os.path.join(r'budget_data.csv')


# open csv file
with open(path_pybank, 'r') as pybank:
    # csv read
    pybank_reader = csv.reader(pybank, delimiter=',')
    next(pybank_reader)
    to_list = list(pybank_reader)
    # print(to_list)

    net_total = 0
    total_months = 0
    average_change = 0
    max_increase = 0
    max_increase_index = 0
    max_decrease = 0
    change = []
# total months
    total_months = len(to_list)


# # Get net total
    for list in to_list:
        net_total = net_total + float(list[1])

    #
# #get average_change
    total_change = 0
    for i in range(1, len(to_list)):

        total_change = (float(to_list[i][1]) - float(to_list[i-1][1])) + total_change
    average_change = total_change/(total_months-1)


    #greatest change alternative

    # for i in range(1,len(to_list)):
    #
    #     change.append(int(to_list[i][1]) - int(to_list[i-1][1]))
    #
    # max_change = max(change)
    # min_change = min(change)
    # for i in range(1,len(to_list)):
    #     if max_change == to_list[i][1]:
#greatest increase
    for i in range(1,len(to_list)):
        diff = int(to_list[i][1]) - int(to_list[i - 1][1])
        if diff > max_increase:
            max_increase = diff

            max_increase_index = i


    max_increase_month = to_list[max_increase_index][0]
    max_increase = int(to_list[max_increase_index][1])-int(to_list[max_increase_index-1][1])

#greatest decrease
    for i in range(1,len(to_list)):
        diff = int(to_list[i][1]) - int(to_list[i - 1][1])
        if diff < max_decrease:
            max_decrease = diff

            max_increase_index = i


    max_decrease_month = to_list[max_increase_index][0]
    max_decrease = int(to_list[max_increase_index][1])-int(to_list[max_increase_index-1][1])

#print em all
    print("Financial Analysis")
    print('----------------------------')
    print(f'Total Months: {total_months}')
    print(f'Total: $ {round(net_total)}')
    print(f'Average Change: ${round(average_change,2)}')

    print(f'Greatest Increase in Profits: {max_increase_month} $({max_increase})')
    print(f'Greatest Decrease in Profits: {max_decrease_month} $({max_decrease})')









