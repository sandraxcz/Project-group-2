# Datalogical Thinking: Project - Algorithm Design (group 2) 
Group members: 
Camille, Magdalena, and Sandra 

## About the Assignment
The general idea for this assignment is that you work together in a group to curate a dataset, and design an algorithm to process that dataset in a meaningful way. You will publish both your dataset and your algorithm design on GitHub, alongside a simple website with some basic information on the project, dataset and algorithm, that will be hosted with GitHub Pages.

### Step 1 of the Assignment: Conceptualisation
The first step for this project would be to brainstorm with your teammates to decide what kind of data you would be interested in, and what you would like to be able to do with that data. This includes:

Finding or conceptualising an interesting dataset
Defining a specific problem or need for the data, that can be resolved algorithmically
Modelling (or fine-tuning the pre-existing model of) your data in a way that it becomes relevant for your algorithm
This process involves discussing questions such as: Where would you find the data you want to work with? Or would you need to collect or fabricate the data yourself? In what format is the data available? Can we work with this format in our algorithm? Or do we need to translate the data to another format? Do we need to clean the data in any way (e.g.: delete irrelevant or duplicate information; structure the data differently; correct errors in the data; add additional information to the data that would be useful for the algorithm)? How do we intend to use the data, and do we need to make any changes to the (way the) data (is structured) to facilitate this?

It is important for this step that you know your data. This requires you to have a good understanding of how the data you want to work with is modelled. E.g. for XML data: Which tags and attributes contain which information? Or, in the case of a database: Which attributes do the tables use, and how are the relations between different tables linked? At the same time, it is important to try to anticipate the needs of your algorithm. What kind of information would our algorithm require, and how is this information recorded in the dataset? Is the dataset modelled in a way that makes it easy for my algorithm to obtain the relevant data?

For example: if you were designing an algorithm that maps out a citation network (as in: who is citing who?) based on a selection of academic papers, your data would have to be modelled in a way that makes it easy for your algorithm to find a) the author names of each of the papers in your database; and b) the author names of each of the references cited in each of those papers.

If you are starting from pre-existing data, this means: understanding what kind of information it contains, and how it is structured. If you are developing your own dataset, this means conceptualising your own model to map your data onto (as you did, for example, in Assignment 1). You may also want to do a little of both: use pre-existing data, but make some changes to the way it is structured (or the information it contains) that makes it easier for your algorithm to access the information you need.

### Step 2 of the Assignment: Curate Your Dataset
Once you know how your data should be modelled, you can put it into practice. If you are collecting your own data: map it onto your data model. If you are starting from a dataset developed by others: clean the dataset and make relevant changes to the way it is modelled. The result of this step is that you will have a dataset that your algorithm can work with.
 *TIP: You can use a validator (like this one by the World Wide Web Consortium.) to check whether or not your XML is well-formed. And you can open your .csv file in any spreadsheet software (e.g. MS Excel, or Numbers) to check if they visualise your tables (rows / columns) correctly (to make sure you did not miss any comma’s, etc.).*

### Step 3 of the Assignment: Design Your Algorithm
Now that you have your dataset, you can start to process it. This is where your algorithm comes in. Using pseudocode, write out the different steps that are necessary to accomplish the task you have set out.

Note: For students who would like more of a challenge, we also allow you to write your algorithm in a full-fledged Turing-complete programming language, like python. If successful, we would of course consider this a strong demonstration of your skills and understanding of the course materials — which would have a positive effect on our determination of your grade. That said, however, we feel the need to stress that this is in no way a requirement, and that it will be possible to obtain a perfect grade (A) for assignments where the algorithm is written in pseudocode.

### Step 4 of the Assignment: Design a Small Website for Your Project
Using HTML and CSS, design a small website, distributed over a few relevant hyperlinked web pages, to contextualise your algorithm. This website should contain some general information about the project/assignment, a description of the dataset, a description of the algorithm, and more information about your team, and the division of labor.

### Step 5 of the Assignment: Publish Your Dataset, Algorithm, and Website on GitHub**
Bundle all of the work you did for Steps 2 through 4 together in a single repository that you post on GitHub. A template for this repository will be provided during the class on GitHub. Make your website publicly accessible by publishing it using GitHub Pages. Information on how to do this will also be provided during the class on GitHub.

## About the Course
*Datalogical Thinking* is a course taught at the [University of Borås](https://www.hb.se) (Sweden), as part of the [MA in Information Science: Digital Environments](https://www.hb.se/en/international-student/program/programmes/masters-programme-in-information-science-digital-environments/). The course, in its current form, was designed by Wout Dillen, and taught for the first time in the autumn of 2023, with the help of his colleagues David Gunnarson Lorentzen, Kayvan Yousefi Mojir, Elisa Tattersall Wallin, and Anton Carlander Borgström.

