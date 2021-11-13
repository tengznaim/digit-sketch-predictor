# Digit Sketch Predictor

This is a simple sketch to digit predictor application built using Streamlit and a Resnet18 model trained on the MNIST dataset using PyTorch. This is mainly intended to showcase an end-to-end machine learning application from training a model, creating an application around it and finally deploying it. It is also intended as a personal working template for working with PyTorch and deploying using Docker.

![app-demo](https://user-images.githubusercontent.com/63803360/136689722-597af392-ce7e-4036-be89-9769ed851b6c.gif)

## What's In This Repository?

1. `digit-classifier.ipynb`
   - This is the model training script that showcases the use of both custom datasets and readily available datasets and turning them into DataLoaders. It also features custom training and test loops that I wrote to my preference with the inclusion of tqdm to show training progress.
   - This was initially built to be run locally but I later realised that using Colab was easier to leverage on their GPU capabilities.
2. `sketch-app`
   - This folder contains `app.py` and the best trained model I currently have.
   - `app.py` is a simple Streamlit application that has a drawable canvas to draw digits and predicts the digit using the trained model.
3. `Dockerfile`
   - This is the Dockerfile used to build the image which can later be used for deployment to Heroku.

## Working and Running on this Locally

To run and/or work on this app locally, run the following:

```
pip install -r requirements.txt
cd sketch-app
streamlit run app.py
```

The app can be viewed at `localhost:8501`

## Building a Docker Image

To build a Docker image of this application and run it, do the following:

> The Dockerfile is currently configured to work with a Heroku deployment and hence the $PORT environment variable. If you'd like to follow the remaining steps below, do change these to a desired port or port 8501 in order for the guide below to work

1. Install Docker
2. Build the image using the following:
   ```
   docker build -t <NAME> .
   ```
   - The t flag indicates the name for this image (an optional tag is also possible using the name:tag syntax)
   - The . at the end refers that the Dockerfile is in the current directory (ensure that the image is built when in this project directory)
3. Run the built image using the following:
   ```
   docker run -p 8501:8501 <NAME>
   ```
   - The p flag indicates publishing the exposed port to the host interface.
   - 8501:8501 refers to the binding of the host port to the exposed container port.
   - With this, once the container has started, the application can be viewed at `localhost:8501`.

## Deploying to Heroku

Under the References section below, there is an [option](https://www.youtube.com/watch?v=tTwGdUTR5h8) to deploy the image to Heroku locally using the Heroku CLI. However, I didn't want to build the image since it takes up space. Instead, I applied an alternative method of using GitHub actions to build and deploy the image through a workflow that can be triggered manually and can also theoretically be configured for a more extensive CI/CD. The GitHub actions I referenced here can be found [here](https://github.com/gonuit/heroku-docker-deploy).

Steps I took to get this workflow working are as follows:

1. Create the workflow yml under the folder `.github/workflows`
2. Create a Heroku app for the project.
3. Note down the app name, your Heroku email and get your Heroku API key from your Heroku settings.
4. Enter these values under `Settings > Secrets` with the following names:
   - HEROKU_API_KEY
   - HEROKU_APP_NAME
   - HEROKU_EMAIL
5. Push the deployment file and either let the workflow run if configured for push on master or manually trigger it.
   - Note that in order for committing workflows to work, you may need to generate a new Personal Access Token (PAT) with workflows checked.

Lastly, in order for this specific deployment to work, port references in the Dockerfile should be changed to the $PORT environment variable because Heroku assigns a port dynamically.

## References

1. Loading a pretrained model and modifying certain layers.
   - https://discuss.pytorch.org/t/load-only-a-part-of-the-network-with-pretrained-weights/88397/2
2. Using Colab with GitHub
   - https://bebi103a.github.io/lessons/02/git_with_colab.html
3. Expose and publish in Docker.
   - https://stackoverflow.com/questions/22111060/what-is-the-difference-between-expose-and-publish-in-docker
   - https://www.whitesourcesoftware.com/free-developer-tools/blog/docker-expose-port/
4. Debugging stopped containers.
   - https://www.thorsten-hans.com/how-to-run-commands-in-stopped-docker-containers/
   - I used this to inspect the file structure of the image because initially, the container wouldn't run properly due to an error in file copying.
5. Deploying Docker on Heroku
   - https://www.youtube.com/watch?v=tTwGdUTR5h8
6. GitHub Actions
   - [GitHub actions quickstart](https://docs.github.com/en/actions/quickstart)
   - [Creating a GitHub personal access token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token) (ensure workflows are checked)
   - [Adding secrets to use in workflows](https://docs.github.com/en/actions/security-guides/encrypted-secrets)
   - [What does Checkout actually mean?](https://github.community/t/what-is-actions-checkout-v2-in-github-action/191110)
