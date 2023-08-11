import geopandas as gpd

# Define path to the un-zipped .gdb
gdb_path = "./National_Final_gdb/CSB1522.gdb"

# Define path to destination folder to land .parquet files
parquet_dest = "./some/folder/somewhere/"

row_start = 0
row_end = 1000000

for r in range(0, 20):
    print(f'Writing rows {row_start}:{row_end}')
    rows = slice(row_start, row_end)
    geo = gpd.read_file(gdb_path, rows=rows)
    # If there's no data in the data frame, exit the loop (don't write to .parquet)
    if len(geo) == 0:
        break
    else:
        path = parquet_dest + "csb_" + str(r) + ".parquet"
        geo.to_parquet(path=path)
        row_start = row_end + 1
        row_end = (r + 2) * 1000000
