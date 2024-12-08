import intake

catalog = intake.open_catalog('data_catalog.yml')

# CSV
df = catalog['csv_example_data'].read()
print(df.head())
