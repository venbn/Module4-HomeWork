
## Dev

I use Jupyter notebook to write the Python code, this code is built in Jupyter notebook on a Mac PC. 
The process must be pretty much same when executing from GitBash on WindowsPC except that you will need Visual Studio Code to install required extensions/moduled.
To ensure, a suitable environment is existing to execute this code, you will need to have python3 and pip3 installed already. 
Python versions older than 3 might not function effeciently.

## Dependencies

Apart from python3 and pip3, you will need to have jupyter, anaconda and matplotlib installed at the operating system level.
All the dependent librariries required to successfully use pandas and numpy modules must be installed as well as the code is heavily dependent on pandas, numpy and matplotlib modules.

## Pre-requisites

Ensure all the below csv files are existing on the OS from where you are executing the code. You will need to run "Jupyter notebook" from the same directory where all the files exist. Below is the list of files which need to exist for the successful execution of the code.

whales_analysis.csv
sp500_history.csv
algo_returns.csv
goog.csv
twtr.csv
nyse.csv
whale_analysis.ipynb

Git must be installed. If using Windows GitBash must be installed.

To execute the code from Windows - you will need Visual Studio Code installed as well to look at the code.

The file 'whale_analysis.ipynb' is the file to be executed from the 'Jupyter notebook' interface ONLY.

## Execution process

Clone the directory which contains all the .csv files and the .ipynb file to your system using the following commands

git clone https://github.com/venbn/Module4-HomeWork.git

Once the clone completes.. 

Go to the directory "Module4-HomeWork"

cd Module4-HomeWork

Execute 'Jupyter notebook' command

In the Jupyter notebook interface, open the file 'whale_analysis.ipynb'

You should be able to see the code
