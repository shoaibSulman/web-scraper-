import pandas
def saveFile(finalList):
    df=pandas.DataFrame(finalList)
    df.to_csv("Output.csv")
    
