
Run Locally 
------------

Run the Flask app locally.

Create a virtual environment, activate it and install all the dependencies.

C:/deployment> python -m venv venv
C:/deployment> venv/Scripts/activate
(venv)C:/deployment> pip install -r requirements.txt

Run the flask app locally. Make sure that the last two lines of the "app.py" file is uncommented.
(venv)C:/deployment> python app.py

This will invoke the app in localhost:5000
Open the link in an web browser and run the app.

----------------------------------------------------
Before you deploy the app, comment out the last two lines of the "app.py" file.


Deployment Steps
--------------------

[Development]
1. Train a ML/DL Model (e.g. CNN cats vs. dog image classifier). Save the trained model as a .keras file, e.g., "Cats_n_Dog_Classifier_CNN.keras"

Check the "Dev/Source Code/" for details of the CNN model.
"Dev/Test Images/" contains a few testing images.

Make sure that this .ketas file is available in the "Deploy" folder [already present there].

[Deployment]
2. Create a Web App using Flask

3. Create a github repository e.g., "RenderDemo" and Commit the code in the "Deploy" folder in this Github repo

4. Create an account on Render.com (cloud platform where the model will be deployed)

5. Create a Web app on Render

6. Link your Github repo RenderDemo with the Render wen app
Choose an appropriate plan (free plan or others, etc.)

7. Deploy the model on Render

8. After successful deployment your service will be up and the Web-App will be running, check the public URL.

9. Open the public URL in a web browser and interact with the app.


