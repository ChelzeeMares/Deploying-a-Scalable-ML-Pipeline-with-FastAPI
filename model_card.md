# Model Card

## Model Details

#### Chelzee Mares
>
> Machine Learning Model with FastAPI
> 
> Programming Language: Python

## Intended Use

> To classify individuals based on the Census Bureau data that is publicly available

## Training Data

> Sourced from the Census Bureau
>
> 32,561 entries with 15 different categories as taken from census.csv
>
> Training data uses 80% or 0.8
>
> Function process_data preprocesses the data by using one hot encoding for the categorical information
> and label binarizeration for the labels
>
> Function apply_label converts the binary lable ina single inference sample into string output
>

## Evaluation Data

> Split into a training and test dataset using train_test_split
>
> 32,561 entries with 15 different categories as taken from census.csv
>
> Test data uses **20% or 0.2**
>
> Function process_data preprocesses the data by using one hot encoding for the categorical information
> and label binarizeration for the labels
>
> Function apply_label converts the binary lable ina single inference sample into string output
>
> 

## Metrics

> Precision: 0.7285
>
> Recall: 0.2699
>
> F1: 0.3939
>
> workclass: Private, Count: 4,578
>> Precision: 0.7051 | Recall: 0.2627 | F1: 0.3828
> 
> education: Bachelors, Count: 1,053
>> Precision: 0.8199 | Recall: 0.2933 | F1: 0.4321
>
> marital-status: Married-civ-spouse, Count: 2,950
>> Precision: 0.8538 | Recall: 0.2530 | F1: 0.3904
>
> occupation: Other-service, Count: 667
>> Precision: 0.2273 | Recall: 0.1923 | F1: 0.2083
>
> relationship: Wife, Count: 322
>> Precision: 0.8235 | Recall: 0.1958 | F1: 0.3164
>
> race: White, Count: 5,595
>> Precision: 0.7332 | Recall: 0.2675 | F1: 0.3920
>
> sex: Female, Count: 2,126
>> Precision: 0.5283 | Recall: 0.2403 | F1: 0.3304
>
> native-country: United-States, Count: 5,870
>> Precision: 0.7283 | Recall: 0.2690 | F1: 0.3929


## Ethical Considerations

> Disproportionate bias across education level, race, and marital status could lead to discrimination amongst certain groups.
>
> Make sure that none of the data includes any personal data.
>
> If bias is shown with certain groups, action might be taken that is unjust.

## Caveats and Recommendations

> The data should be high-quality and if it is not, the model performance may suffer.
>
> Incomplete data can show an imcomplete picture.
>
> Each scenario is different and bias created from the model might not take those scenarios into consideration.
>
> The model should use the most updated data in specified increments.
>
> Interpretation of the data should be clear.
>
> This particular model can be used to teach students on machine learning.
