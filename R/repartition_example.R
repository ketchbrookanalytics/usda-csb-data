library(arrow)

arrow::open_dataset(
  "/some/folder/somewhere/"
) |> 
  arrow::write_dataset(
    path = "/some/other_folder/somewhere/", 
    partitioning = "STATEFIPS",
    format = "parquet"
  )