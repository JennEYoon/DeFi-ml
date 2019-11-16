#  Task list for SEC data Python machine learning repo.

Date:  8/24/2019  2:00 AM EST -- inspired by DREAM.    

 * Credit ratings transition matrix data from FINRA economist -- explore.
 * ML credit risk dataset from Kaggle, Udemy -- explore.
 * EIA.gov energ derivativesy trading data -- explore.
 * SEC Edgar company financial statements data -- explore.
 * SEC - FINRA Credut Risk data.
 * Stress Tests, FED, SEC, Treasury.
 * FED macro economic data -- explore.
 * Leverage ratios, and systemic risk calculations - from public data, other analysts.
 * DTC massive database -- explore.  
 
Date:  9/16/2019 - Projects datasciY.com  

 * Visualize Matplotlib 3D option implied vol surface  
 * Visualize Plotly and Dash, interactive graphics
 * Visualize Bokeh financial time series data
 * Visualize Tableau economics data
 
 * Amazon Lambda -- setting up Ubutu and Windows machines with Python + Libraries in layers.  
 * Currently writing questions for GARP FRM - Oct 15th due.
   * Go ahead and finish this week. Total of 6-8 questions.
  
 * 9/21/2019 - Updated meta keywords (search terms) on all html pages.  
 * Installed spell checker to VS Code.  Try it out later.  
 
 * 9/21/2019 Update 8:25 PM   
    * Next week get 3 plotting sutff done for "Projects.html" page on datasciY.com.  
    * Next week -- working on GARP FRM Question writing, finish 6 more.
    * Next week -- Confirm John Bogovic speaking at October 8th Meetup.  
    * Next week -- 3 to 5 more Stack Overflow Answers.  Shoot for 600 pts. Need 80 more pts, 522 now.  
 
    -------------------
    * Other Tasks -- Home garden, 4h per day 3-4 days next week AM.  
    * Other Goal -- Begin daily exercise, either 8:30 AM or 4:30 PM.  
                    7-9 PM is another good block for gym classes + yoga/swim.  

 * **9/24/2019 update** 
    * This week and next, finish Numpy chapter VanderPlas. pages 70-96.   
      VanderPlas Google Drive Link (https://drive.google.com/file/d/1_QUZKxzqp2ecdVxuzBW2URaKX_QAk9gW/view?usp=sharing)
    * Focus on reading and writing data objects to file, reduce memory cache/buffer 
      - SO 56GB buffer Questioner, SO NASA data object write questioner. 
    * Lookup SEC/FINRA TRACE corporate bond credit ratings database.  What state is it now?

### Update 9/28/2019  Eata - Economic Inequality, Map.  Update 10/5/2019.  

 * New report, USA greatest inequality in history, yet number of people in poverty is lower than ever before, absolute improvement.  Unemployment is also lower, but check total labor force participation.  % People in poverty only increased in 1 state, CT, from 2017 to 2018 in USA.  Improvements or statistically same in all other states.  So absolute poverty improved generally in US.  
  * Article hishgest inequality:  https://www.washingtonpost.com/business/2019/09/26/income-inequality-america-highest-its-been-since-census-started-tracking-it-data-show/  
   * Article on Virginia counties inequality:  https://patch.com/virginia/leesburg/poverty-income-trends-virginia  

### Update 10/1/1029  PySal/Inequality repo  

https://github.com/JennEYoon/inequality/blob/master/notebooks/gini.ipynb  

This seems to be nothing more than 1 notebook that uses geo package to create a sample document on how to use gini index mapping for Mexico in the year 1940.  Is there something more?  Can reproduce the notebook, or something similar, for USA, for different time periods.  Compare with UK, China, Hong Kong.  

PySAL is a larger package, python map database and visualization.  NumFocus sponsored.  Look into it more. 10/5/2019.  

#### Oct 3, 2019 Hactoberfest Started  

  * To do 4 pull requests by this weekend.  
  * Created "New Issue" for Inequality Docs -- SECdataPy repo.  
  * Created template in "comments".
  * To add data examples using "pull requests".
  * Re-read about creating pull request.
  * Done 1 pull-request & merge with template inequality.
  * To Do 2nd pull-request & merge with BLS data in Issue#1 inequality.  
  * Do 2 more for Hactoberfest by Sunday/Monday.  
  
#### Pull Request steps  

 * First, need to create something to add (a new inequality data doc)
 * Add changes to "inequality" branch local.
 * Create Pull Request with "branch inequality"
 * Upload new document to that branch - commit to brnach, pull request.  
 * Finalize draft pull request.  
 * Merge as owner, into branch.  Accept pull request.
 * Merge into master branch.  
 
Use "BLS-By-State-Inequality.png" image.  May 2019 data.  What is it now? 2019?  
Washington DC has 6x from top 10% to bottom 90%.  
South Dakoda has lowest inequality with 3.5X between top 10% to bottom 90%.  
https://github.com/JennEYoon/SECdataPy/blob/master/datasets/inequality/BLS-By-State-Inequality.png  


#### 10/4/2019 Tasks Update -- today to do.  

 * Moves github testing files to "tests" folder.  
 * Copy "Inequality Docs Template" to "data/inequality" folder in "branch inequality".
 * Commit to this branch, push, see what happens to Github commits count.
 * Optional -- add new commit to "inequality docs" pull request under Hactoberfest.
 * GeoPandas -- explore.  10/12/2019. 
 
#### 10/27/2019 Update  

 * GeoSnap -- still to do. 20 days.  PR finish on Monday.  
 * 6 PR done for Hactoberfest.  WCC and SECdataPy repo.  
 
#### 10/28/2019 Monday  

 * GeoSnap -- working on this today.  
 * Jupyter Notebooks 3d, 2d matplotlib -- WORKS! Renders today all notebooks.  
 
 
#### 11/8/2019  

 * from scipy2018 geospatial notebook  
   Trump gini in a bottle notebook: https://github.com/JennEYoon/scipy2018-geospatial-data/blob/master/_solved/case-gini-in-a-bottle-the-trump-vote.ipynb  
   Extend with 2018 and 2019 vote results.  
   Do higher country-level inequality lead to more Trump voters? 
   What else explains Trump voters?  Manufacturing job loss in reason per Yang, Relative economic poverty or recent decline in region?  See what changed in MSA areas and by State.  

 * Contact PyData - SEC Edgar repo person.  Look over his trading model.  Any thoughts?  
 * Connect with him on LinkedIn - done 11/16/2019.  
 * Ken Nicholaus.  Seems like a wild guy. Could be a risk.  Repo has interesting super-resolution DL repo, but take a look at the stock investing repo -- nothing original, but something to get started on...
 
 * Try to finishe Update to GeoSnap PR -- week of 11/16/2019.  
   1. Fix slice.  
   2. Then install and run example notebooks.  
   3. Write tests. 
   4. SUbmit revised PR.
   
--- end ---  
