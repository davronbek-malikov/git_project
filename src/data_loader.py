import pandas as pd
import os
class DataLoader:
    """
    Class to load and merge CSV datasets from multiple league folders inside Data/Raw_Data.
    """

    def __init__(self, raw_data_path="Data/Raw_Data/"):
        self.raw_data_path = raw_data_path

    def load_league_files(self):
        """
        Loads all CSV files from each league folder and returns a list of DataFrames.
        """
        df_list = []
        # Loop over each league folder
        for league_folder in os.listdir(self.raw_data_path):
            league_path = os.path.join(self.raw_data_path, league_folder)
            if os.path.isdir(league_path):  # ensure it's a folder
                # Loop over CSV files in this folder
                for file in os.listdir(league_path):
                    if file.endswith(".csv"):
                        file_path = os.path.join(league_path, file)
                        df = pd.read_csv(file_path)
                        df_list.append(df)
        return df_list

    def merge_all_leagues(self):
        """
        Merge all league datasets into a single DataFrame.
        """
        df_list = self.load_league_files()
        merged_df = pd.concat(df_list, ignore_index=True)
        return merged_df