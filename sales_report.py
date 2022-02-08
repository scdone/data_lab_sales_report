"""Generate sales report showing total melons each salesperson sold."""
#this creates empty lists to append the data 
salespeople = []
melons_sold = []
#opens the sales report file
f = open('sales-report.txt')
#loops through file and splits lines between the | character
for line in f:
    line = line.rstrip()
    entries = line.split('|')

    #defines the sales person at index 0 of the list and the melon count at index 2 of the list
    salesperson = entries[0]
    melons = int(entries[2])

    #if the sales person already exists in the list, this adds melons to their count instead of duplicating the data
    if salesperson in salespeople:
        position = salespeople.index(salesperson)

        melons_sold[position] += melons
    #if the sales person is not already listed, this appends their data to the list
    else:
        salespeople.append(salesperson)
        melons_sold.append(melons)

#here the information is printed out, showing the name of the sales person and how many melons they sold. 
for i in range(len(salespeople)):
    print(f'{salespeople[i]} sold {melons_sold[i]} melons')

### improvements to be made - would be useful to show the total revenue the sales person made. ex "Tom Jones sold 500 melons, generating $2,000.00 in sales."
### would also be useful to order the salespeople by most sold melons / highest revenue generated







##### BELOW IS MY OWN ATTEMPT. DOESN'T WORKING. STILL TROUBLESHOOTING. 

# def sales_report(sales_report_file):
#     """Returns sales data for each salesperson by amount of melons sold."""

#     salespeople = []
#     melons_sold = []
#     total_revenue_generated = []

#     sales_report = open('sales-report.txt')

#     for line in sales_report:
#         line = line.rstrip()
#         entries = line.split("|")

#     salesperson = entries[0]
#     revenue_generated = entries[1]
#     melons_count = entries[2]

#     if salesperson in salespeople:
#         position = salespeople.index(salesperson)
#         melons_sold[position] += melons_count
#         total_revenue_generated[position] += revenue_generated

#     else:
#         salespeople.append(salesperson)
#         melons_sold.append(melons_count)
#         total_revenue_generated.append(revenue_generated)
    
#     for i in range(len(salespeople)):
#         print('SALES REPORT')
#         print(f'{salesperson[i]} sold {melons_sold[i]}, generating ${total_revenue_generated[i]} in revenue.')



# sales_report('sales-report.txt')


    
