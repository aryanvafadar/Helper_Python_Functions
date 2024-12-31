"""
Takes a CSV File, converts it to a dataframe and converts it back to a csv file
"""
import pathlib
import pandas as pd



def main():
    # convert csv to frame
    frame = pd.read_csv(filepath_or_buffer=input_file, nrows=chunk_size)
    
    # convert back to csv
    frame.to_csv(output_file, index=False)


if __name__ == "__main__":
    
    current_directory = pathlib.Path(__file__).parent.parent
    
    try:
        input_file = input("File Path for Input File: ")
        chunk_size = int(input("Enter Number of Rows for New File: "))
        output_file = str(current_directory.joinpath('data_files', 'output_files')) + '/new_' + input_file.split(sep='/')[-1]
        
        main()
    
    except Exception as e:
        print(f'{e}')