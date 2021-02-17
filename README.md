# NLP-for-Arabic-Content-Classification
Implemented while being a Technology Trainee at the ESCWA Technology Center

#### The main goal of this project is to provide a model that will be able to classify News and Articles for two UN projects, MSME micro, small, medium enterprises and entrepreneurship AND DIAR Driving Innovation in the Arab Region (Science, Technology & innovation). 


# There are three ctegories: 
- Entrepreneurship
- Science & Technology
- Other


# Data Collection:
- The Entrepreneurship Data was collected from eight websites: ryadibusiness, waya, youm7, jawlah, asharqbusiness, raedaamal, egyentrepreneur, and preneur-masr.
- The Science & Technology Data was collected from three websites: RT-Online, asharq, and sputniknews.
- The Data of the Other category was collected from three websites: UN News, birzeit university, and almashareq.


## Manual
This tools was built with Python and requires the installation of the 

### Main arguments
The following are the required arguments to predict the class of any new text:

- `-f <text_file>`: input txt file.
- `-m <model>`: input binary file of the model. binary files are available at the Artifacts directory.
