from pathlib import Path
import pandas as pd

Folder_path = Path(__file__).parent  # .../code/data/raw/
parquet_path = Folder_path / ".cache" / "sp500" / "^GSPC_1997_2022.parquet"

df = pd.read_parquet(parquet_path)
df.to_csv(Folder_path / "GSPC_1997_2022.csv")   # keeps the date index
print(df.shape, "-> CSV written to", Folder_path / "GSPC_1997_2022.csv")