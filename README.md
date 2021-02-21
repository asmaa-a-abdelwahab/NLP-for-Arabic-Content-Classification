# Supervised Learning for Arabic Text Classification to Organize the Content of UN Platforms

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
To install the required libraries run - `conda install --file requirements.txt`

### Main arguments
The following are the required arguments to predict the class of any new text:

- `-f <text_file>`: input txt file.
- `-m <model>`: input binary file of the model. binary files are available at the Artifacts directory.


### Classifying New Text
```bash
python3 Predict_new_text.py -f <text_file> -m <model>

Main arguments
  -f F        Input txt file (*.txt)
  -m M        Input binary file of the model
```
### TEST CASE

```bash
python3 Code/Predict_new_text.py -f Code/test.txt -m lr
```

#### output
<p align="center">
  <img src="https://github.com/asmaa-a-abdelwahab/NLP-for-Arabic-Content-Classification/blob/main/test-output.png"  width="96%" height="40%">
</p>

