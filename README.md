# invitro_cheminformatics
Workflow to perform cheminformatics analysis of a database instance on linux server containing in vitro toxicological data. This workflow queries the databases (invitrodb [prod_internal_invitrodb_v3_3], dsstox[], qsar[ro_rlougee_qsar] )
***
Something

***

Workflow steps :
  1) Access invitrodb v3_3 database through R-package (tcpl) to get a list of "assay_component_endpoint_id" or "aeid" and obtain the DTXSID_hitc table for each aeid.
  2) Access DSSTOX database using python package "database"
  3) Convert substance DTXSID to structure identifier DTXCID using python module DTXSIDtoDTXCID
  4) Clean DTXCID_hitc files using bash commands
  5) Access and query sbox_rlougee_qsar to add fingerprint(ToxPrint) columns to each DTXCID_hitc table
  6) Run the prepared files as input to the chemotype enrichment analysis workflow (repo: mshobair/cheminf ; branch= main) to generate enrichment table
  7) Combine the enrichment tables into one flat file. This is the baseline global enrichment table

Next steps:
  8) Modify the tcpl query to add filters using the "burst" functions, such as tcpl_cytopt, to change the DTXCID_hitc matrices.
  
  1)
  
  - Within the EPA network, log to sc.epa.gov or other server with R installed, which can be accessed remotely from cu.epa.gov via ssh. Within shell terminal in a new directory:

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
write.csv(aeid_table, "aeid_table.csv")
```
  - Obtain input files programmatically from invitrodb v3_3 
    - R-package tcpl query data from ccte-mysql-res.epa.gov  
  - Clean the files to be compatible with the chemotype enrichment analysis workflow
    - Python script to change identifier DTXSID to DTXCID
    - Bash scripts to clean and reforrmat the files
  - 
    - We used the provided data and stayed within the context of the Challenge.
    - Creating an easily reproducible way of collapsing large datasets
    - Begin exploring the identification of associations within the provided dataset between clinical factors and adaptive immunological features
    - Show examples of the explored associations using visualizations and showing the logic behind how these associations/visualizations were generated

***
Here is an overview of setting up the computing environment for chemotype enrichment analysis.

![](ETL.svg)

## Setting up dependencies and virtual environment
App development and testing was done primarily in Ubuntu 20.04/18.04.

<!-- GP - Edited to remove unneeded dependencies -->
### Install ubuntu dependencies:
```sh
sudo apt install -y curl sqlite3 pipenv jupyter-client r-base-core libgsl-dev libcurl4-openssl-dev git libxml2-dev

```
<!-- GP - Edited to add "R" and further show what to do when done with step-->
### Install R packages
```R
R (opens R environment)
install.packages(c("IRkernel", "data.table", "RSQLite", "sqldf", "BiocManager", "yaml")) 
(Answer "yes" twice)
library(IRkernel)
IRkernel::installspec()
library(BiocManager)
BiocManager::install("universalmotif")
BiocManager::install("MotifDb")

(Ctrl + D to Exit Environment)
(Answer "No" to saving workspace)
```

### Download, extract the zipped repo source 
Make certain you are not in "/" when running this.
```sh
git clone --branch datapipeline https://github.com/mshobair/precisionFDA_Covid19_repo.git 
cd precisionFDA_Covid19_repo
```
