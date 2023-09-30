from setuptools import setup, find_packages

name = 'knowledge_search_engine'
version = '0.1'
author = 'Alex Krstich'
author_email = 'akrstich06@gmail.com'
description = 'n this ambitious project, our primary objective is to 
develop a cutting-edge knowledge search engine that harnesses the power 
of advanced technologies such as Apache Spark, Elasticsearch, machine 
learning, and chatbot integration. This comprehensive system will 
empower users to effortlessly and efficiently access information from 
two pivotal sources: Stack Overflow and YouTube. The project unfolds in 
a series of meticulously planned stages, each contributing to the 
realization of this innovative knowledge search engine.

**Data Collection and Ingestion:**
Our project initiates with the meticulous collection and ingestion of 
data, a foundational step in ensuring the accuracy and richness of our 
knowledge base. On a monthly basis, an AWS Lambda function is triggered 
by Amazon Event Bridge, orchestrating the launch of an Airflow EC2 
instance. Within this controlled environment, Airflow takes charge of 
the data collection process, orchestrating the retrieval of valuable 
Stack Overflow data in XML format directly from the official source. 
Ensuring data quality and integrity is a paramount concern; therefore, 
an initial data quality check is performed before proceeding.

This raw Stack Overflow data, once verified for completeness, is 
securely organized within AWS S3 buckets. Utilizing the formidable 
capabilities of Apache Spark, we process this raw data, converting it 
from XML to CSV format. As we delve further into data transformation, we 
apply specific logic, including label mapping, to enhance the usability 
of the data. The processed data finds its home in a well-structured S3 
folder, ready for the next stages of our project.

**Model Embedding and Indexing:**
With the processed data in hand, our project then delves into the realms 
of machine learning and model embedding. The CSV data is summoned to a 
SageMaker or Lambda model endpoint, where machine learning models 
perform their magic, generating embeddings that capture the essence of 
our knowledge data. These embeddings are the keys to unlocking efficient 
searches.

Elasticsearch, renowned for its powerful text search capabilities, steps 
onto the stage next. Indexing is performed on the generated embeddings, 
and these indexes are meticulously stored in another S3 folder, primed 
for further processing. Apache Spark, working in tandem with an EMR 
cluster, optimizes these embeddings and indexes, ensuring they are 
fine-tuned for precision.

**User Interaction through Chatbot:**
The crown jewel of our project lies in the user interaction, made 
seamless through a user-friendly chatbot. Whether built using Streamlit 
or Langchain, this chatbot becomes the gateway for users to tap into the 
vast knowledge reservoir we've meticulously cultivated.

User queries flow into the system, passing through a classification and 
embedding model. This model classifies and embeds the queries, setting 
the stage for a precise search. Elasticsearch springs into action, 
scouring through the indexed knowledge. Top results are retrieved, 
laying the groundwork for the final touch. Llama 2, a tool designed for 
summarization, processes the results, distilling them into concise and 
informative answers. These, along with relevant YouTube links, are then 
presented to the users, facilitating a smooth and enriching learning 
experience.

**Technology Stack:**
Our project leverages a formidable technology stack, including AWS 
Lambda, Airflow, EMR, Apache Spark, SageMaker, Lambda, PyTorch, Hugging 
Face Transformers, AWS S3, Elasticsearch, and user interface frameworks 
like Streamlit and Langchain. This diverse set of technologies 
collaborates seamlessly to achieve our ambitious goals.

**Project Goals:**
Our overarching mission is to revolutionize knowledge access. By 
seamlessly integrating data collection, machine learning, and user 
interaction, we aim to create an advanced knowledge search engine that 
significantly enhances the learning experience for students and all 
knowledge seekers. This project promises to break down barriers, making 
valuable information more accessible and user-friendly than ever before.' 
url = 'https://github.com/akrstich/knowledge_search_engine'

install_requires = [
aiohttp==3.8.5
aiosignal==1.3.1
alembic==1.12.0
annotated-types==0.5.0
anyio==4.0.0
apache-airflow==2.7.1
apache-airflow-providers-common-sql==1.7.1
apache-airflow-providers-ftp==3.5.1
apache-airflow-providers-http==4.5.1
apache-airflow-providers-imap==3.3.1
apache-airflow-providers-sqlite==3.4.3
apispec==6.3.0
argcomplete==3.1.1
asgiref==3.7.2
async-timeout==4.0.3
attrs==23.1.0
Babel==2.12.1
backoff==1.10.0
blinker==1.6.2
cachelib==0.9.0
cattrs==23.1.2
certifi==2023.7.22
cffi==1.15.1
charset-normalizer==3.2.0
click==8.1.7
clickclick==20.10.2
colorama==0.4.6
colorlog==4.8.0
ConfigUpdater==3.1.1
connexion==2.14.2
cron-descriptor==1.4.0
croniter==1.4.1
cryptography==41.0.3
Deprecated==1.2.14
dill==0.3.1.1
dnspython==2.4.2
docutils==0.20.1
email-validator==1.3.1
exceptiongroup==1.1.3
Flask==2.2.5
Flask-AppBuilder==4.3.6
Flask-Babel==2.0.0
Flask-Caching==2.0.2
Flask-JWT-Extended==4.5.2
Flask-Limiter==3.5.0
Flask-Login==0.6.2
Flask-Session==0.5.0
Flask-SQLAlchemy==2.5.1
Flask-WTF==1.1.1
frozenlist==1.4.0
google-re2==1.1
googleapis-common-protos==1.60.0
graphviz==0.20.1
grpcio==1.57.0
gunicorn==21.2.0
h11==0.14.0
httpcore==0.16.3
httpx==0.23.3
idna==3.4
importlib-metadata==6.8.0
importlib-resources==6.0.1
inflection==0.5.1
itsdangerous==2.1.2
Jinja2==3.1.2
jsonschema==4.19.0
jsonschema-specifications==2023.7.1
lazy-object-proxy==1.9.0
limits==3.6.0
linkify-it-py==2.0.2
lockfile==0.12.2
Mako==1.2.4
Markdown==3.4.4
markdown-it-py==3.0.0
MarkupSafe==2.1.3
marshmallow==3.20.1
marshmallow-oneofschema==3.0.1
marshmallow-sqlalchemy==0.26.1
mdit-py-plugins==0.4.0
mdurl==0.1.2
multidict==6.0.4
opentelemetry-api==1.20.0
opentelemetry-exporter-otlp==1.20.0
opentelemetry-exporter-otlp-proto-common==1.20.0
opentelemetry-exporter-otlp-proto-grpc==1.20.0
opentelemetry-exporter-otlp-proto-http==1.20.0
opentelemetry-proto==1.20.0
opentelemetry-sdk==1.20.0
opentelemetry-semantic-conventions==0.41b0
ordered-set==4.1.0
packaging==23.1
pathspec==0.11.2
pendulum==2.1.2
pluggy==1.3.0
prison==0.2.1
protobuf==4.21.12
psutil==5.9.5
pycparser==2.21
pydantic==2.3.0
pydantic_core==2.6.3
Pygments==2.16.1
PyJWT==2.8.0
python-daemon==3.0.1
python-dateutil==2.8.2
python-nvd3==0.15.0
python-slugify==8.0.1
pytz==2023.3
pytzdata==2020.1
PyYAML==6.0.1
referencing==0.30.2
requests==2.31.0
requests-toolbelt==1.0.0
rfc3339-validator==0.1.4
rfc3986==1.5.0
rich==13.5.2
rich-argparse==1.3.0
rpds-py==0.10.2
setproctitle==1.3.2
six==1.16.0
sniffio==1.3.0
SQLAlchemy==1.4.49
SQLAlchemy-JSONField==1.0.1.post0
SQLAlchemy-Utils==0.41.1
sqlparse==0.4.4
tabulate==0.9.0
tenacity==8.2.3
termcolor==2.3.0
text-unidecode==1.3
typing_extensions==4.7.1
uc-micro-py==1.0.2
unicodecsv==0.14.1
urllib3==1.26.16
Werkzeug==2.2.3
wrapt==1.15.0
WTForms==3.0.1
yarl==1.9.2
zipp==3.16.2

setup(
    name=name,
    version=version,
    author=author,
    author_email=author_email,
    description=description,
    long_description=description,  # You can provide a longer description 
here if needed.
    url=url,
    license='MIT',  # Use the appropriate license.
    packages=find_packages(),
    install_requires=install_requires,
   #entry_points=entry_points,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        # Add any other classifiers relevant to your project.
    ],
)

