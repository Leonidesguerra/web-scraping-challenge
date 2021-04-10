### Mision to Mars - Web Srcaping challenge

Mision to mars is a web scraping project using the following tools:
  - Jupyter Notebook 
  - Pandas
  - Beautiful Soup
  - Splinter
  - Mongo Db
  - Flask
  - HTML
  - css
  - Boot Strap

# Working process

  For the working proces, first the web scraping proces started on Jupiter Notebook. Where code was writen and proven to work correctly. This step consisted on accesing 4 different urls, in order to find different contets for each.
  The contents included latest news title and paragraph, featured mars image url, facts list and a list of dictionaries containing titles and urls for high resolution images. 

  Once the code was working correctly I proceded to create a python script with a scraping function based on the code generated on jupyter notebook. This function is called from an app.py script that stores the data on mongo and renders the result to an html template which has been stiled witd css and bootstrap.

  The following screen shots show the final results:
  - [app_images.png](Images/app_images.png)
  - [result_page.png](Images/result_page.png)
