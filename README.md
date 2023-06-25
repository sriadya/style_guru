# Style Guru

This app lets you visualize how you would look in a new hair style.
The app uses Openai's DALL-E model to edit an image based on a given prompt.

![App View]("style_guru_app.png")

Openai allows for image creation and editing an existing image. The prompt sketches for the different hairstyles and the test image of a mid 20's make office professional were generated using `openai.Image.create` api. 

The input image needs to be resized to 1024x1024, saved in `.png` format and should be less than 4MB. This code takes care of the resizing and the format. Only images that are not protected by copyrights and are owned by the user should be used for testing. Openai errors out if unauthorized images are used. 
 
`openai.Image.create_edit` api is used to generate new images of the chosen hair style superimposed on the input image. 

The interface for the app is generated using [Streamlit](https://streamlit.io/) and is hosted at [https://huggingface.co/spaces/adya/style_guru](https://huggingface.co/spaces/adya/style_guru)

Please share your comments and feedbacks to srikanthadya@gmail.com
