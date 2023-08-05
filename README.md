**Report Generator**

**Overview**

The Report Generator is a Python application that reads data from three input files (TeamMap.csv, ProductMaster.csv, and Sales.csv) and generates two output files (TeamReport.csv and ProductReport.csv). The application calculates total gross revenues for each sales team and summarizes sales of each product.

**Input Files**

Team Map

The TeamMap.csv file is a comma-separated text file containing information about sales teams. Each line consists of two values: an integer representing the team's unique identifier (TeamId) and a string representing the team's name (Name). The file includes a header with the field names.

Product Master

The ProductMaster.csv file is a comma-separated text file containing information about products. Each line consists of four values: an integer representing the product's unique identifier (ProductId), a string representing the product's name (Name), a floating-point value representing the product's price (Price per unit), and an integer representing the product's lot size (LotSize). The file does not contain a header.

Sales

The Sales.csv file is a comma-separated text file containing information about sales. Each line consists of five values: an integer representing the sale's unique identifier (SaleId), an integer representing the product's unique identifier (ProductId) from the Product Master, an integer representing the sales team's unique identifier (TeamId) from the Team Map, an integer representing the quantity sold (Quantity), and a floating-point value representing the discount percentage (Discount). The file does not contain a header.

**Output Files**

Team Report

The TeamReport.csv file is a comma-separated text file containing the sales team names and their total gross revenues. The file includes a header with the field names, and the teams are listed in descending order by their gross revenue.

Product Report

The ProductReport.csv file is a comma-separated text file summarizing the sales of each product. Each line consists of four values: the product's name, the gross revenue of sales, the total number of units sold, and the total cost of all discounts provided on sales of the product. The file includes a header with the field names, and the products are listed in descending order of their gross revenue.

**Usage**

To run the Report Generator, download all files in a single folder. Then, execute the following command in the command-line interface of the directory where you saved the files:

**python report.py -t TeamMap.csv -p ProductMaster.csv -s Sales.csv --team-report=TeamReport.csv --product-report=ProductReport.csv**

Make sure to provide the correct file paths for the input and output files. The application will read the data from the input files, perform the necessary calculations, and generate the team and product reports in the specified output files.
