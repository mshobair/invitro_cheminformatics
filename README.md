# invitro_cheminformatics
Workflow to perform cheminformatics analysis of a database instance on linux server containing in vitro toxicological data. This workflow queries the databases (invitrodb [prod_internal_invitrodb_v3_3], dsstox[], qsar[ro_rlougee_qsar] )


Workflow steps :
  1) Access invitrodb v3_3 database through R-package (tcpl) to get a list of "assay_component_endpoint_id" or "aeid" and obtain the DTXSID_hitc table for each aeid.
  2) Access DSSTOX database using python package "database"
  3) Reformat DTXSID_hitc (CSV) tables to DTXCID_hitc (tsv)
  4) Convert substance DTXSID to structure identifier DTXCID using python module DTXSIDtoDTXCID
  5) Clean DTXCID_hitc files using bash commands
  6) Access and query sbox_rlougee_qsar to add fingerprint(ToxPrint) columns to each DTXCID_hitc table
  7) Run the prepared files as input to the chemotype enrichment analysis workflow (repo: mshobair/cheminf ; branch= main) to generate enrichment table
  8) Combine the enrichment tables into one flat file. This is the baseline global enrichment table

Next steps:
  9) Modify the tcpl query to add filters using the "burst" functions, such as tcpl_cytopt, to change the DTXCID_hitc matrices.
  
  1) ACCESS - Within the EPA network, log to sc.epa.gov or other server with R installed, which can be accessed remotely from cu.epa.gov via ssh. 
  
Within shell terminal in a new directory:

```sh
R
```
Install tcpl if it is not installed using this command:

```r
install.packages("tcpl")
```
In R-prompt, load tcpl package, setup the database access parameters and query the assay_component_endpoint table. 
```r
 # load tcpl
library(tcpl)
# set database parameters (invitrodb v3_3); which is publically available
tcplConf(drvr="MySQL", user="_dataminer", pass="pass", db="prod_internal_invitrodb_v3_3", host="ccte-mysql-res.epa.gov")
# get list of aeids
aeid_table <- tcplLoadAeid()
# write table of aeids
write.csv(aeid_table, "aeid_table.csv", row.names = F)
```
- Obtain input files programmatically from invitrodb v3_3 
```r
# loop through each aeid and write the mc5 table
for(i in aeid_table$aeid[1:2]){ # substitute "2" in "[1:2]" with total number of aeids {total; 1:length(aeid_table$aeid)}
mc5 <- tcplSubsetChid(tcplPrepOtpt(tcplLoadData(lvl=5, fld ="aeid", val = i))) # getting level 5 data for binary hitcall (hitc)
mc5_sub <- mc5[, c("dsstox_substance_id", "hitc")] # selecting the relevant columns DTXSID(dsstox_substance_id) and hitcall (hitc)
mc5_sub_name <- paste0("mc5_", i, ".csv") # saving the DTXSID_hitc table for a specific aeid (i) and naming it by the aeid (mc5_1.csv)
write.csv(mc5_sub, mc5_sub_name, row.names = F) # writing the table to a CSV file (mc5_1.csv) in the current directory
}
```
Exit R :
ctrl + D
Y

2) ACCESS - Connect to the res1 databases and sandboxes.
Let's start a virtual environment, so that we can install python dependencies and modules to prepare the input files. We will make a virtual environment "test_env", activate it and install python modules in it to use as python scripts or Command-Line-Interface (CLI) tool. If virtualenv is not installed, consult with the IT team.

```sh
mkdir test_env
python3 -m virtualenv test_env
source test_env/bin/activate
pip install pandas
pip install mysql-connector
```

Go to database directory, and install

```sh
cd database
pip install -e .
cd ../
```

3) REFORMAT - Clean the files to be compatible with the chemotype enrichment analysis workflow. 

- remove lines with "NA" or "-1"
```sh
for file in mc*; do sed '/-/d'  $file | sed '/NA/d' >  clean/"$file.clean" ; done
```

- Convert CSV to TSV using csv2tsv.py
  - copy all the mc5* files into a new directory (csvtotsv)
```sh
mkdir csvtotsv
cp *clean csvtocsv
```
  
- run the CSV to TSV conversion and copy to TSV to new directory (TSV)
```sh
python csv2tsv.py
mkdir tsv
cp csvtotsv/*tsv tsv
```
4) Convert substance DTXSID to structure identifier DTXCID using python module Chemical_ID_Convert

install the Chemical_ID_Convert module
```sh
cd  Chemical_ID_Convert
pip install -e .
cd ..
```
run the chemid convert on the TSV

```sh
cd tsv
for file in *; do chemidconvert DTXSID DTXCID $file -e > "$file.dtxcid" ; done
```
copy converted files into a new directory (dtxcid)
```sh
mkdir dtxcid
cp tsv/*dtxcid dtxcid
```

5) skip if no errors
6) Query descriptor table to get the ToxPrint fingerprints. Install FillFingerprints module.
```sh
cd FillFingerprints
pip install -e .
cd ../
```
Generate fingerprint tables
```sh
cd dtxcid
for file in *; do fillfp $file -o "$file.fp" ; done
cd ../
```
copy fingerprint files to a new directory (fp)
```sh
mkdir fp
cp dtxcid/*fp fp
```
7) Generate Enrichment Table
install Enrichment_Table_Generator dependencies
```sh
cd Enrichment_Table_Generator
python setup.py install
cd ../
```
run enrichment for each file
```sh
cd fp
for file in *; do python Enrichment_Table_Generator/Enrichment_Table_Generator.py -i $file -o $file.enrich ; done
cd ../
```



