# Finding Drivers of Zestimate Errors
![](https://github.com/ray-zapata/project_clustering_zillow/blob/main/assets/logo.png)

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

![](https://github.com/ray-zapata/project_clustering_zillow/blob/main/assets/divider.png)

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

WIP

### IV. Process
---

#### 1. Project Planning
🟢 **Plan** ➜ ☐ _Acquire_ ➜ ☐ _Prepare_ ➜ ☐ _Explore_ ➜ ☐ _Model_ ➜ ☐ _Deliver_

- [ ] Build this README containing:
    - Project overview
    - Initial thoughts and hypotheses
    - Project summary
    - Instructions to reproduce
- [ ] 

#### 2. Data Acquisition
✓ _Plan_ ➜ 🟢 **Acquire** ➜ ☐ _Prepare_ ➜ ☐ _Explore_ ➜ ☐ _Model_ ➜ ☐ _Deliver_

- [ ] Obtain initial data and understand its structure
    - Obtain data from Codeup database with appropriate SQL query
- [ ] Remedy any inconsistencies, duplicates, or structural problems within data
- [ ] Perform data summation

#### 3. Data Preparation
✓ _Plan_ ➜ ✓ _Acquire_ ➜ 🟢 **Prepare** ➜ ☐ _Explore_ ➜ ☐ _Model_ ➜ ☐ _Deliver_

- [ ] Address missing or inappropriate values, including outliers
- [ ] Plot distributions of variables
- [ ] Encode categorical variables
- [ ] Consider and create new features as needed
- [ ] Split data into `train`, `validate`, and `test`

#### 4. Data Exploration
✓ _Plan_ ➜ ✓ _Acquire_ ➜ ✓ _Prepare_ ➜ 🟢 **Explore** ➜ ☐ _Model_ ➜ ☐ _Deliver_

- [ ] Visualize relationships of variables
- [ ] Formulate hypotheses
- [ ] Use clustering methodology in exploration of data
    - Perform statistical testing and visualization
    - Use at least 3 combinations of features
    - Document takeaways of each clustering venture
    - Create new features with clusters if applicable
- [ ] Perform statistical tests
- [ ] Decide upon features and models to be used

#### 5. Modeling & Evaluation
✓ _Plan_ ➜ ✓ _Acquire_ ➜ ✓ _Prepare_ ➜ ✓ _Explore_ ➜ 🟢 **Model** ➜ ☐ _Deliver_

- [ ] Establish baseline prediction
- [ ] Create, fit, and predict with models
    - Create at least four different models
    - Use different configurations of algorithms, hyper parameters, and/or features
- [ ] Evaluate models with out-of-sample data
- [ ] Utilize best performing model on `test` data
- [ ] Summarize, visualize, and interpret findings

#### 6. Product Delivery
✓ _Plan_ ➜ ✓ _Acquire_ ➜ ✓ _Prepare_ ➜ ✓ _Explore_ ➜ ✓ _Model_ ➜ 🟢 **Deliver**
- [ ] Prepare Jupyter Notebook of project details through data science pipeline
    - Python code clearly commented when necessary
    - Sufficiently utilize markdown
    - Appropriately title notebook and sections
- [ ] With additional time, continue with exploration beyond MVP
- [ ] Proof read and complete README and project repository

### V. Modules
---

The created modules used in this project below contain full comments an docstrings to better understand their operation. Where applicable, all functions used `random_state=19` at all times. Use of functions requiring access to the Codeup database require an additional module named `env.py`. See project reproduction for more detail.

- [`acquire`](https://raw.githubusercontent.com/ray-zapata/project_clustering_zillow/main/acquire.py): contains functions used in initial data acquisition leading into the prepare phase
- [`prepare`](https://raw.githubusercontent.com/ray-zapata/project_clustering_zillow/main/prepare.py): contains functions used to prepare data for exploration and visualization
- [`explore`](https://raw.githubusercontent.com/ray-zapata/project_clustering_zillow/main/explore.py): contains functions to visualize the prepared data and estimate the best drivers of property value
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
