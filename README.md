# ChatGPTLawCompare

 Comparing the output of ChatGPT and GPT-3 on various legal questions with search data. 
 
Streamlit app: https://houfu-chatgptlawcompare-main-jymt8s.streamlit.app/

*Blog post to come*

## Development

If you want to recreate the results in this repository or try more examples,
you have to perform these steps.

1. Fork this repository.

2. Scrape the Singapore Law website. 
You may want to refer to the About Singapore Law branch of ZeekerScraper 
[here](https://github.com/houfu/zeekerscrapers/tree/about_singapore_law).

3. The scraper, like the code in this repository, needs you to have your own Weaviate cluster
and your own OpenAI key. A [free Weaviate Cluster ](https://weaviate.io/)
is available for you to try, and you can get an OpenAI Key 
from [their website](https://platform.openai.com/account/api-keys).

4. Run the `prepare_data.py` script. This prepares `results.csv` which will be the source data 
for your streamlit app in `main.py`. 
To view this streamlit app, get an account at [streamlit](https://streamlit.io/) and deploy it there. 

If you would like to add more questions, you need to modify the dataset variable in `prepare_data.py`.
Add a question and an answer and then run the script. 
