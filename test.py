from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from pylab import *
from scipy.cluster.hierarchy import dendrogram, fcluster, ward
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nltk.download('punkt')
warnings.filterwarnings('ignore')
