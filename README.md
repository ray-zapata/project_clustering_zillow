# Finding Drivers of Zestimate Errors
![](https://github.com/ray-zapata/project_clustering_zillow/blob/main/assets/logo.jpg)

### Table of Contents
---

I.   [Project Overview             ](#i-project-overview)
1.   [Description                  ](#1-description)
2.   [Deliverables                 ](#2-deliverables)

II.  [Project Summary              ](#ii-project-summary)
1.   [Goals                        ](#1-goals)
2.   [Initial Thoughts & Hypothesis](#2-initial-thoughts--hypothesis)
3.   [Findings & Next Phase        ](#3-findings--next-phase)

III. [Data Context                 ](#iii-data-context)
1.   [Database Relationships       ](#1-database-relationships)
2.   [Data Dictionary              ](#2-data-dictionary)

IV.  [Process                      ](#iv-process)
1.   [Project Planning             ](#1-project-planning)
2.   [Data Acquisition             ](#2-data-acquisition)
3.   [Data Preparation             ](#3-data-preparation)
4.   [Data Exploration             ](#4-data-exploration)
5.   [Modeling & Evaluation        ](#5-modeling--evaluation)
6.   [Product Delivery             ](#6-product-delivery)

V.   [Modules               ](#v-modules)

VI.  [Project Reproduction  ](#vi-project-reproduction)

<br>

![](https://github.com/ray-zapata/project_clustering_zillow/blob/main/assets/divider.png)

<br>

### I. Project Overview
---

#### 1. Description

WIP

#### 2. Deliverables

WIP


### II. Project Summary
---

#### 1. Goals

WIP

#### 2. Initial Thoughts & Hypothesis

WIP

#### 3. Findings & Next Phase

WIP

### III. Data Context
---

#### 1. Database Relationships

The Codeup `zillow` SQL database contains twelve tables, nine of which have foreign key links with our primary table `properties_2017`: `airconditioningtype`, `architecturalstyletype`, `buildingclasstype`, `heatingorsystemtype`, `predictions_2017`, `propertylandusetype`, `storytype`, `typeconstructiontype`, and `unique_properties`. Each table is connected by a pointed arrow with the corresponding foreign keys that link them. Many of these tables are unused in this project due to missing values, and this database map serves only to define the database.

![](https://github.com/ray-zapata/project_clustering_zillow/blob/main/assets/databasemap.png)

#### 2. Data Dictionary

Following acquisition and preparation of the initial SQL database, the DataFrames used in this project contain the following variables. Contained values are defined along with their respective data types.

| Variable               | Definition                                         | Data Type  |
|:----------------------:|:--------------------------------------------------:|:----------:|
| acreage                | conversion of lot_square_feet into acres           | float64    |
| age                    | age of propery as of 2017                          | int64      |
| bathrooms              | count of full- and half-bathrooms                  | float64    |
| bed_sqft_age_clstr_#   | boolean for five clusterings of bed_sqft_age       | int64      |
| bedrooms               | count of bedrooms                                  | int64      |
| bedrooms_per_sqft      | ratio of bedrooms to structure_square_feet         | float64    |
| census_tractcode       | US census tract codes for property location        | float64    |
| full_bathrooms         | count of only full-bathrooms                       | int64      |
| la_county              | boolean for if county is within Los Angeles County | int64      |
| land_value_usd         | value of land in U.S. dollars                      | float64    |
| lat_long_clstr_#       | boolean for five clusterings of lat_long           | int64      |
| latitude               | latitude geographic coordinate of property         | float64    |
| log_error *            | difference of log(Zestimate) and log(SalePrice)    | float64    |
| longitude              | longitude geographic coordinate of property        | float64    |
| lot_rooms_clstr_#      | boolean for five clusterings of lot_rooms          | int64      |
| lot_square_feet        | size of lot(land) in square feet                   | float64    |
| orange_county          | boolean for if county is within Orange County      | int64      |
| parcel_id              | unique identier of property                        | int64      |
| property_id            | unique identier of property                        | int64      |
| property_value_usd     | value of property in entirety in U.S. dollars      | float64    |
| room_count             | count of bedrooms and full- and half-bathrooms     | float64    |
| structure_square_feet  | dimensions of structure on property in square feet | float64    |
| structure_value_usd    | value of structure on propert in U.S. dollars      | float64    |
| tax_amount_usd         | most recent tax payment from property owner        | float64    |
| tract_size_age_clstr_# | boolean for five clusterings of tract_size_age     | int64      |
| transaction_date       | most recent date of property sale                  | datetime64 |
| year_built             | year structure was originally built                | int64      |

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  * Target variable

### IV. Process
---

#### 1. Project Planning
🟢 **Plan** ➜ ☐ _Acquire_ ➜ ☐ _Prepare_ ➜ ☐ _Explore_ ➜ ☐ _Model_ ➜ ☐ _Deliver_

- [ ] Build this README containing:
    - Project overview
    - Initial thoughts and hypotheses
    - Project summary
    - Instructions to reproduce
- [x] Plan stages of project and consider needs versus desires

#### 2. Data Acquisition
✓ _Plan_ ➜ 🟢 **Acquire** ➜ ☐ _Prepare_ ➜ ☐ _Explore_ ➜ ☐ _Model_ ➜ ☐ _Deliver_

- [x] Obtain initial data and understand its structure
    - Obtain data from Codeup database with appropriate SQL query
- [x] Remedy any inconsistencies, duplicates, or structural problems within data
- [x] Perform data summation

#### 3. Data Preparation
✓ _Plan_ ➜ ✓ _Acquire_ ➜ 🟢 **Prepare** ➜ ☐ _Explore_ ➜ ☐ _Model_ ➜ ☐ _Deliver_

- [x] Address missing or inappropriate values, including outliers
- [x] Plot distributions of variables
- [x] Encode categorical variables
- [x] Consider and create new features as needed
- [x] Split data into `train`, `validate`, and `test`

#### 4. Data Exploration
✓ _Plan_ ➜ ✓ _Acquire_ ➜ ✓ _Prepare_ ➜ 🟢 **Explore** ➜ ☐ _Model_ ➜ ☐ _Deliver_

- [x] Visualize relationships of variables
- [x] Formulate hypotheses
- [x] Use clustering methodology in exploration of data
    - Perform statistical testing and visualization
    - Use at least 3 combinations of features
    - Document takeaways of each clustering venture
    - Create new features with clusters if applicable
- [x] Perform statistical tests
- [x] Decide upon features and models to be used

#### 5. Modeling & Evaluation
✓ _Plan_ ➜ ✓ _Acquire_ ➜ ✓ _Prepare_ ➜ ✓ _Explore_ ➜ 🟢 **Model** ➜ ☐ _Deliver_

- [x] Establish baseline prediction
- [x] Create, fit, and predict with models
    - Create at least four different models
    - Use different configurations of algorithms, hyper parameters, and/or features
- [x] Evaluate models with out-of-sample data
- [x] Utilize best performing model on `test` data
- [x] Summarize, visualize, and interpret findings

#### 6. Product Delivery
✓ _Plan_ ➜ ✓ _Acquire_ ➜ ✓ _Prepare_ ➜ ✓ _Explore_ ➜ ✓ _Model_ ➜ 🟢 **Deliver**
- [ ] Prepare Jupyter Notebook of project details through data science pipeline
    - Python code clearly commented when necessary
    - Sufficiently utilize markdown
    - Appropriately title notebook and sections
- [x] With additional time, continue with exploration beyond MVP
- [ ] Proof read and complete README and project repository

### V. Modules
---

The created modules used in this project below contain full comments an docstrings to better understand their operation. Where applicable, all functions used `random_state=19` at all times. Use of functions requiring access to the Codeup database require an additional module named `env.py`. See project reproduction for more detail.

- [`acquire`](https://raw.githubusercontent.com/ray-zapata/project_clustering_zillow/main/acquire.py): contains functions used in initial data acquisition leading into the prepare phase
- [`prepare`](https://raw.githubusercontent.com/ray-zapata/project_clustering_zillow/main/prepare.py): contains functions used to prepare data for exploration and visualization
- [`explore`](https://raw.githubusercontent.com/ray-zapata/project_clustering_zillow/main/explore.py): contains functions to visualize the prepared data and estimate the best drivers of property value
- [`wrangle`  ](https://raw.githubusercontent.com/ray-zapata/project_clustering_zillow/main/wrangle.py  ): contains functions to prepare data in the manner needed for specific Zillow needs
- [`model`  ](https://raw.githubusercontent.com/ray-zapata/project_clustering_zillow/main/model.py  ): contains functions to create, test models and visualize their performance

### VI. Project Reproduction
---

To recreate and reproduce results of this project, you will need to create a module named `env.py`. This file will need to contain login credentials for the Codeup database server stored in their respective variables named `host`, `username`, and `password`. You will also need to create the following function within. This is used in all functions that acquire data from the SQL server to create the URL for connecting. `db_name` needs to be passed as a string that matches exactly with the name of a database on the server.

```py
def get_connection(db_name):
    return f'mysql+pymysql://{username}:{password}@{host}/{db_name}'
```

After its creation, ensure this file is not uploaded or leaked by ensuring git does not interact with it. When using any function housed in the created modules above, ensure full reading of comments and docstrings to understand its proper use and passed arguments or parameters.

[[Return to Top]](#finding-drivers-of-zestimate-errors)
