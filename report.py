#We can import "sys" as this is a built-in package
import sys
# Function to read data from the TeamMap file and return it stored as a dictionary
def import_teammap(file_path):
    teams = {}
    with open(file_path, 'r') as f:
        f.readline()  # this is used to skip the header
        for line in f:
            team_id, team_name = line.strip().split(',')
            teams[int(team_id)] = team_name
    return teams
# Function to read data from the Product Master file and it stored as a dictionary
def import_productmaster(file_path):
    products = {}
    with open(file_path, 'r') as f:
        for line in f:
            product_id, name, price, lot_size = line.strip().split(',')
            products[int(product_id)] = {
                'name': name,
                'price': float(price),
                'lot_size': int(lot_size)
            }
    return products
# Function to read data from the Sales file and return it stored as a list
def import_sales(file_path):
    sales = []
    with open(file_path, 'r') as f:
        for line in f:
            sale_id, product_id, team_id, quantity, discount = line.strip().split(',')
            sales.append({
                'product_id': int(product_id),
                'team_id': int(team_id),
                'quantity': int(quantity),
                'discount': float(discount)
            })
    return sales
# Function to calculate the total gross revenue for each sales team
def calculate_revenue(sales, products):
    team_revenue = {}
    for sale in sales:
        product_id = sale['product_id']
        team_id = sale['team_id']
        quantity = sale['quantity']
        price = products[product_id]['price']
        revenue = price * quantity * products[product_id]['lot_size']
        team_revenue[team_id] = team_revenue.get(team_id, 0) + revenue
    return team_revenue
# Function to do the calculations for the Product_Report
def calculate_products(sales, products):
    product_report = {}
    for sale in sales:
        product_id = sale['product_id']
        quantity = sale['quantity']
        price = products[product_id]['price']
        revenue = price * quantity * products[product_id]['lot_size']
        discount = revenue * (sale['discount'] / 100)
        if product_id not in product_report:
            product_report[product_id] = {
                'name': products[product_id]['name'],
                'revenue': revenue,
                'total_units': quantity * products[product_id]['lot_size'],
                'discount_cost': discount
            }
        else:
            product_report[product_id]['revenue'] += revenue
            product_report[product_id]['total_units'] += quantity * products[product_id]['lot_size']
            product_report[product_id]['discount_cost'] += discount
    return product_report
# Function to write the team report to the output file
def write_team_report(team_revenue, file_path, team_map):
    with open(file_path, 'w') as f:
        f.write('Team,GrossRevenue\n')
        for team_id, revenue in sorted(team_revenue.items(), key=lambda x: x[1], reverse=True):
            team_name = team_map.get(team_id, "Unknown Team")  # Get the team name from the team_map dictionary
            f.write(f'{team_name},{revenue:.2f}\n')
# Function to write the product report to the output file
def write_product_report(product_report, file_path):
    with open(file_path, 'w') as f:
        f.write('Name,GrossRevenue,TotalUnits,DiscountCost\n')
        for product_id, info in sorted(product_report.items(), key=lambda x: x[1]['revenue'], reverse=True):
            f.write(f"{info['name']},{info['revenue']:.2f},{info['total_units']},{info['discount_cost']:.2f}\n")
# Main function to handle the script execution
def main():
    #first let's make sure that we have the correct number of arguments
    if len(sys.argv) != 9:
        print("ERROR: Incorrect number of arguments. You need the following arguments: ['report.py', '-t', 'TeamMap.csv', '-p', 'ProductMaster.csv', '-s', 'Sales.csv', '--team-report=TeamReport.csv', '--product-report=ProductReport.csv']")
        sys.exit(1)
    #We will store the file names from the command line based on their positioning 
    team_map_file = sys.argv[sys.argv.index('-t') + 1]
    product_master_file = sys.argv[sys.argv.index('-p') + 1]
    sales_file = sys.argv[sys.argv.index('-s') + 1]
    team_report_arg = sys.argv[7]
    product_report_arg = sys.argv[8]

    # Extract the file names from the command-line arguments
    team_report_file = team_report_arg.split('=')[1]
    product_report_file = product_report_arg.split('=')[1]
    #Next we can use the functions we wrote above to read in the data from csvs without using Pandas.
    team_map = import_teammap(team_map_file)
    product_master = import_productmaster(product_master_file)
    sales = import_sales(sales_file)
    #Next we can perform the calculations needed for the output
    team_revenue = calculate_revenue(sales, product_master)
    product_report = calculate_products(sales, product_master)
    #And finally output the results in the requested format to 2 CSV files
    write_team_report(team_revenue, team_report_file, team_map)
    write_product_report(product_report, product_report_file)

if __name__ == '__main__':
    main()