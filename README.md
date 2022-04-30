# XNET: Deep Learning Based System for Radiologist.


For every radiologist to use this project i have created a web-application with simple interface so that everyone can understand and use it for their purpose.
this web-application can detect Various diseases like Covid-19, Pneumonia, Tuberculosis from Lungs X-Ray as well as CT-Scan Images by using deep learning and convolutional neural network.



# Dataset used:


1. Chest X-Ray (Pneumonia,Covid-19,Tuberculosis). => (https://www.kaggle.com/datasets/jtiptj/chest-xray-pneumoniacovid19tuberculosis)
![image](https://user-images.githubusercontent.com/93335175/166108488-f53839f7-deb5-422f-884b-c344d8d184b0.png)

3. Large COVID-19 CT scan slice dataset. => (https://www.kaggle.com/datasets/maedemaftouni/large-covid19-ct-slice-dataset)
![image](https://user-images.githubusercontent.com/93335175/166108502-e81f850a-74e6-4091-ae14-74d4c5b48e0e.png)


A. Chest X-Ray (Pneumonia,Covid-19,Tuberculosis):
This dataset is organized into 3 main folders (Test, Train, Val) and contains subfolders for each image category (Normal/Pneumonia/Covid-19/Tuberculosis). A total of 7135 x-ray images are present. of which 
in Train set there are 460-Covid, 1341-normal, 3875-pneumonia, 650- tuberculosis.
in Test Set 106-Covid, 234-normal, 390-pneumonia, 41- tuberculosis.
in Validation 10-Covid, 8-normal, 8-pneumonia, 12- tuberculosis.

Pneumonia Chest X-ray images (anterior-posterior) were selected from retrospective cohorts of pediatric patients of one to five years old from Guangzhou Women and Children’s Medical Center, Guangzhou is a City in China. All chest X-ray imaging was performed as part of patients’ routine clinical care.
For the analysis of chest x-ray images, all chest radiographs were initially screened for quality control by removing all low quality or unreadable scans. The diagnoses for the images were then graded by two expert physicians before being cleared for training the AI system. In order to account for any grading errors, the evaluation set was also checked by a third expert.
The normal chest X-ray (left panel) depicts clear lungs without any areas of abnormal opacification in the image. Bacterial pneumonia (middle) typically exhibits a focal lobar consolidation, in this case in the right upper lobe (white arrows), whereas viral pneumonia (right) manifests with a more diffuse ‘‘interstitial’’ pattern in both lungs.

Tuberculosis (TB) Chest X-ray Database: A team of researchers from Qatar University, Doha, Qatar, and the University of Dhaka, Bangladesh along with their collaborators from Malaysia in collaboration with medical doctors from Hamad Medical Corporation and Bangladesh have created a database of chest X-ray images for Tuberculosis (TB) positive cases along with Normal images

Covid-19: Data is collected from public sources as well as through indirect collection from hospitals and physicians.


B. Large COVID-19 CT scan slice dataset
in this Some of the datasets consist of categorized CT slices, and some include CT volumes with annotated lesion slices. 
Therefore, Author used the slice-level annotations to extract axial slices from CT volumes. then converted all the images to 8-bit to have a consistent depth.
we have gathered 7,593 COVID-19 images from 466 patients and 6,893 normal images from 604 patients


#Method used:
i have used multiclass classification of the X-Ray images since there are 4 classes in total which are Normal, Covid, Pneumonia and Tuberculosis
and for ct-scan images we have used Binary Classification beacuse there are only 2 classes which are Covid and Non-Covid

# Transfer Learning: Transfer learning is a research problem in machine learning that focuses on storing knowledge gained while solving one problem and applying it to a different but related problem.


# Model used:
At first i have selected 4 models mainly which are Inception, EfficientNetB0, ResNet50 and Xception.
Here are the accuracies i got

![image](https://user-images.githubusercontent.com/93335175/166108595-b1a7d209-ed2f-4f1c-abc6-b837ba5e7bed.png)


of which then i have used ResNet50 model for X-Ray images and xception model for ct-scan images along with the transfer learning method
to learn more about models you can visit these links ResNet50:https://keras.io/api/applications/resnet/  , xception:https://keras.io/api/applications/xception/


# Project Architecture:
![image](https://user-images.githubusercontent.com/93335175/166108696-627689d3-3fcd-478b-ac87-508de495953d.png)

# Web Application screenshots: 

Home Page
![image](https://user-images.githubusercontent.com/93335175/166108730-a1be62c0-a4f1-4822-a1ca-6fe9b583f441.png)


Result for the X-Ray images:
![image](https://user-images.githubusercontent.com/93335175/166108761-52641965-0567-4137-95d7-c5f0eaefe92e.png)


Result for the CT-Scan images:
![image](https://user-images.githubusercontent.com/93335175/166108776-b15b3d25-cba5-4f2e-99bb-cda9b79e384b.png)



