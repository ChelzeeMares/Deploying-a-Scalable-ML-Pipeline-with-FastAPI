# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details

> Chelzee Mares
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
> 
>
>  Function process_data preprocesses the data by using one hot encoding for the categorical information
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
> education: Bachelors, Count: 1,053
>Precision: 0.7285 | Recall: 0.2699 | F1: 0.3939

## Ethical Considerations

> Disproportionate bias across education level, race, and marital status could lead to discrimination amongst certain groups.
>
> Make sure that none of the data includes any personal data.
>
> If bias is shown with certain groups, action might be taken that is unjust.
>

## Caveats and Recommendations

> The data should be high-quality and if it is not, the model performance may suffer.
>
> Each scenario is different and bias created from the model might not take those scenarios into consideration.
>
> The model should use the most updated data in specified increments.
>
> Interpretation of the data should be clear.
>
> This particular model can be used to teach students on machine learning.
